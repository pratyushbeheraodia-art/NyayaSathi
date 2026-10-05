import sqlite3
import json
import os
from pathlib import Path
from datetime import datetime, date

DB_PATH = Path(__file__).resolve().parent.parent / "nyayasathi.db"

def get_connection():
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Table: queries (kiosk query logs)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS queries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_text TEXT NOT NULL,
        language TEXT DEFAULT 'en',
        detected_category TEXT,
        confidence REAL DEFAULT 0.0,
        urgency TEXT DEFAULT 'Medium',
        privacy_mode INTEGER DEFAULT 0,
        session_id TEXT,
        resolved INTEGER DEFAULT 0,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # Table: knowledge_base (statutory provisions & guides)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS knowledge_base (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL,
        title_en TEXT NOT NULL,
        title_hi TEXT NOT NULL,
        title_od TEXT NOT NULL,
        summary_en TEXT NOT NULL,
        summary_hi TEXT NOT NULL,
        summary_od TEXT NOT NULL,
        legal_sections TEXT,
        remedies TEXT,
        procedure_steps TEXT,
        relevant_acts TEXT,
        helpline TEXT
    );
    """)

    # Table: demo_cases (Realistic simulated cases for tracking)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS demo_cases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        case_number TEXT UNIQUE NOT NULL,
        cnr_number TEXT UNIQUE NOT NULL,
        title_en TEXT NOT NULL,
        title_hi TEXT NOT NULL,
        title_od TEXT NOT NULL,
        category TEXT NOT NULL,
        court_name TEXT NOT NULL,
        filing_date TEXT NOT NULL,
        next_hearing_date TEXT,
        status TEXT NOT NULL,
        petitioner TEXT NOT NULL,
        respondent TEXT NOT NULL,
        timeline_json TEXT,
        documents_json TEXT,
        order_summary TEXT
    );
    """)

    # Table: checklists (required documents)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS checklists (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL,
        item_en TEXT NOT NULL,
        item_hi TEXT NOT NULL,
        item_od TEXT NOT NULL,
        mandatory INTEGER DEFAULT 1,
        purpose TEXT,
        issuing_authority TEXT
    );
    """)

    # Table: resources (official portals & helplines)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resources (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name_en TEXT NOT NULL,
        name_hi TEXT NOT NULL,
        name_od TEXT NOT NULL,
        category TEXT NOT NULL,
        phone TEXT,
        portal_url TEXT,
        description_en TEXT,
        description_hi TEXT,
        description_od TEXT,
        is_helpline INTEGER DEFAULT 0
    );
    """)

    # Table: deadlines (limitation periods)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS deadlines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dispute_type_en TEXT NOT NULL,
        dispute_type_hi TEXT NOT NULL,
        dispute_type_od TEXT NOT NULL,
        limit_period_text TEXT NOT NULL,
        act_reference TEXT NOT NULL,
        trigger_event TEXT NOT NULL,
        penalty_if_missed TEXT,
        days_limit INTEGER
    );
    """)

    # Table: escalations (human assistance queue)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS escalations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        token_number TEXT UNIQUE NOT NULL,
        query_category TEXT NOT NULL,
        citizen_name TEXT DEFAULT 'Anonymous Citizen',
        phone_number TEXT,
        issue_summary TEXT NOT NULL,
        language TEXT DEFAULT 'en',
        status TEXT DEFAULT 'PENDING',
        priority TEXT DEFAULT 'NORMAL',
        kiosk_id TEXT DEFAULT 'KIOSK-OD-042',
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # Table: evidence_store (evidence files metadata)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS evidence_store (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id TEXT NOT NULL,
        file_name TEXT NOT NULL,
        file_type TEXT NOT NULL,
        file_size TEXT,
        category TEXT NOT NULL,
        notes TEXT,
        relevance_score INTEGER DEFAULT 85,
        uploaded_at TEXT DEFAULT CURRENT_TIMESTAMP
    );
    """)

    conn.commit()
    seed_initial_data(conn)
    conn.close()

def seed_initial_data(conn):
    cursor = conn.cursor()

    # Check if already seeded
    cursor.execute("SELECT COUNT(*) FROM demo_cases")
    if cursor.fetchone()[0] > 0:
        return

    # 1. Seed Demo Cases (5 realistic Indian community cases)
    demo_cases_data = [
        (
            "LAND/2026/089",
            "ODGN01-004521-2026",
            "Gram Kanthi Land Encroachment & Mutation",
            "ग्राम कांठी भूमि अतिक्रमण एवं नामांतरण विवाद",
            "ଗ୍ରାମ କାଣ୍ଠି ଜମି ବେଦଖଲ ଏବଂ ମ୍ୟୁଟେସନ ବିବାଦ",
            "land_dispute",
            "Revenue Court of Tahasildar, Chatrapur, Ganjam",
            "2026-04-12",
            "2026-10-18",
            "HEARING_SCHEDULED",
            "Ramesh Chandra Nayak",
            "Bipin Behera & Revenue Inspector",
            json.dumps([
                {"stage": "Petition Filed", "date": "2026-04-12", "status": "COMPLETED", "note": "Section 23 of Odisha Land Reforms Act filed with RoR copy."},
                {"stage": "RI Field Demarcation", "date": "2026-06-05", "status": "COMPLETED", "note": "Revenue Inspector measured boundary survey plot 412/10."},
                {"stage": "Notice to Opponent", "date": "2026-08-20", "status": "COMPLETED", "note": "Summons delivered to respondent Bipin Behera."},
                {"stage": "Substantive Hearing", "date": "2026-10-18", "status": "UPCOMING", "note": "Arguments on possession document and settlement survey map."}
            ]),
            json.dumps([
                {"name": "RoR (Record of Rights / Patta)", "verified": True},
                {"name": "Field Demarcation Report by RI", "verified": True},
                {"name": "Land Revenue Khajna Receipt 2025-26", "verified": True}
            ]),
            "Interim boundary protection order maintained. Both parties instructed to maintain status quo until final demarcation order."
        ),
        (
            "LAB/2026/142",
            "ODKH02-001984-2026",
            "Brick Kiln Migrant Worker Unpaid Wages (₹48,000)",
            "ईंट भट्ठा प्रवासी मजदूर बकाया मजदूरी विवाद (₹48,000)",
            "ଇଟା ଭାଟି ପ୍ରବାସୀ ଶ୍ରମିକ ବକେୟା ମଜୁରୀ (₹୪୮,୦୦୦)",
            "labor_dispute",
            "Assistant Labour Commissioner, Bhubaneswar",
            "2026-07-03",
            "2026-10-09",
            "CONCILIATION_PENDING",
            "Savitri Majhi & 6 Workers",
            "Kalinga Bricks & Sub-contractor",
            json.dumps([
                {"stage": "Complaint Registered", "date": "2026-07-03", "status": "COMPLETED", "note": "Form VI under Section 15 of Payment of Wages Act."},
                {"stage": "Joint Verification Notice", "date": "2026-08-11", "status": "COMPLETED", "note": "Labour Officer inspection report confirmed 120 days work."},
                {"stage": "Conciliation Meeting", "date": "2026-10-09", "status": "UPCOMING", "note": "Mandatory settlement conference before prosecution referral."}
            ]),
            json.dumps([
                {"name": "Attendance notebook sign log", "verified": True},
                {"name": "Advance payment receipt slip", "verified": True},
                {"name": "Aadhaar e-Shram Card copies", "verified": True}
            ]),
            "Contractor directed to deposit ₹20,000 undisputed wage advance by next session or face distraint under Section 15(5)."
        ),
        (
            "CONS/2026/304",
            "ODCT03-009120-2026",
            "Defective Paddy Thresher Machine Warranty Denial",
            "दोषपूर्ण धान थ्रेशर मशीन वारंटी दावा अस्वीकृति",
            "ତ୍ରୁଟିପୂର୍ଣ୍ଣ ଧାନ ଅମଳ ମେସିନ ୱାରେଣ୍ଟି ଦାବି",
            "consumer_dispute",
            "District Consumer Disputes Redressal Commission, Cuttack",
            "2026-05-19",
            "2026-11-04",
            "EVIDENCE_STAGE",
            "Gopal Charan Das (Farmer)",
            "Krushi Udyog Machinery Pvt Ltd",
            json.dumps([
                {"stage": "Consumer Complaint Admitted", "date": "2026-05-19", "status": "COMPLETED", "note": "Under Section 35 of Consumer Protection Act 2019."},
                {"stage": "Written Version by Dealer", "date": "2026-07-28", "status": "COMPLETED", "note": "Opposite party alleged improper electrical voltage."},
                {"stage": "Expert Technical Report", "date": "2026-09-14", "status": "COMPLETED", "note": "Govt ITI engineer verified manufacturing motor defect."},
                {"stage": "Final Evidence & Arguments", "date": "2026-11-04", "status": "UPCOMING", "note": "Claim for ₹1,15,000 refund plus ₹25,000 compensation."}
            ]),
            json.dumps([
                {"name": "Tax Invoice & GST bill", "verified": True},
                {"name": "Warranty Card & Dealer Stamp", "verified": True},
                {"name": "Service call log recordings", "verified": True}
            ]),
            "Notice issued to manufacturer. Expert finding of inherent motor winding flaw taken on record."
        ),
        (
            "DV/2026/058",
            "ODPU04-003418-2026",
            "Urgent Maintenance & Residence Protection Order",
            "तत्काल भरण-पोषण एवं आवास संरक्षण आदेश (घरेलू हिंसा)",
            "ତ୍ୱରିତ ଭରଣପୋଷଣ ଓ ବାସସ୍ଥାନ ସୁରକ୍ଷା ଆଦେଶ",
            "family_dispute",
            "Court of Judicial Magistrate First Class (JMFC), Puri",
            "2026-08-02",
            "2026-10-12",
            "INTERIM_ORDER_PASSED",
            "Priyadarshini Sahoo (Applicant)",
            "Prashant Sahoo & In-laws",
            json.dumps([
                {"stage": "DIR Form I Submitted", "date": "2026-08-02", "status": "COMPLETED", "note": "Protection Officer DIR filed under Section 12 PWDVA 2005."},
                {"stage": "Ex-parte Interim Hearing", "date": "2026-08-16", "status": "COMPLETED", "note": "Interim protection under Sec 18 passed prohibiting harassment."},
                {"stage": "Financial Affidavit Exchange", "date": "2026-09-22", "status": "COMPLETED", "note": "Rajnesh v. Neha compliance disclosure filed."},
                {"stage": "Interim Maintenance Order Hearing", "date": "2026-10-12", "status": "UPCOMING", "note": "Fixing ₹7,500/month interim maintenance."}
            ]),
            json.dumps([
                {"name": "Domestic Incident Report (DIR) from Protection Officer", "verified": True},
                {"name": "Medical injury examination slip", "verified": True},
                {"name": "Marriage certificate & ration card", "verified": True}
            ]),
            "Interim injunction restraining respondent from entering shared household or alienating stridhan jewellery."
        ),
        (
            "CYB/2026/911",
            "ODBB05-008762-2026",
            "Unauthorized UPI Withdrawal & PM-Kisan Phishing Fraud",
            "अनाधिकृत यूपीआई निकासी एवं पीएम-किसान धोखाधड़ी",
            "ଅଣ-ଅନୁମୋଦିତ UPI ନେଣଦେଣ ଓ କିଷାନ ଯୋଜନା ଠକେଇ",
            "cyber_fraud",
            "Cyber & Financial Crime Police Station, Bhubaneswar",
            "2026-09-01",
            "2026-10-15",
            "FROZEN_ACCOUNT_RECOVERY",
            "Trilochan Mohanty",
            "Unknown Cyber Account Holder (ICICI Beneficiary)",
            json.dumps([
                {"stage": "1930 Portal Incident Log", "date": "2026-09-01", "status": "COMPLETED", "note": "Reported within golden hour of fraud (38 mins)."},
                {"stage": "Beneficiary Layer-1 Frozen", "date": "2026-09-02", "status": "COMPLETED", "note": "NCRP system froze ₹34,500 in beneficiary mule account."},
                {"stage": "Court De-freeze Petition", "date": "2026-10-15", "status": "UPCOMING", "note": "Sec 457 BNSS application for refund to victim's bank."}
            ]),
            json.dumps([
                {"name": "Bank transaction SMS & passbook update", "verified": True},
                {"name": "National Cyber Crime Portal Acknowledgment #23092601", "verified": True},
                {"name": "WhatsApp fake apk screenshot", "verified": True}
            ]),
            "Bank nodal officer confirms lien placed on recipient wallet. Police recommendation sent to magistrate for release order."
        )
    ]
    cursor.executemany("""
    INSERT INTO demo_cases (case_number, cnr_number, title_en, title_hi, title_od, category, court_name, filing_date, next_hearing_date, status, petitioner, respondent, timeline_json, documents_json, order_summary)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, demo_cases_data)

    # 2. Seed Knowledge Base
    kb_data = [
        (
            "land_dispute",
            "Land Mutation, Encroachment & Patta Rights",
            "भूमि नामांतरण, अतिक्रमण एवं पट्टा अधिकार",
            "ଜମି ମ୍ୟୁଟେସନ, ବେଦଖଲ ଏବଂ ପଟ୍ଟା ଅଧିକାର",
            "Clear guidelines on resolving rural land boundaries, resolving illegal encroachment, updating Khatiyan/Patta, and approaching the Tahasildar or Lok Adalat without expensive brokers.",
            "ग्रामीण भूमि सीमा विवाद, अवैध कब्जे से मुक्ति, खतियान/पट्टा अद्यतन और बिना दलाल तहसीलदार या लोक अदालत में आवेदन की प्रक्रिया।",
            "ଗ୍ରାମୀଣ ଜମି ସୀମା ବିବାଦ, ବେଆଇନ ବେଦଖଲ, ଖତିୟାନ/ପଟ୍ଟା ସଂଶୋଧନ ଏବଂ ତହସିଲଦାର ବା ଲୋକ ଅଦାଲତରେ ବିନା ଖର୍ଚ୍ଚରେ ନ୍ୟାୟ ପାଇବାର ନିୟମ।",
            "Odisha Land Reforms Act Sec 23, Revenue Laws, BNSS Sec 164 (Dispute concerning land/water)",
            "File Form 10 to Tahasildar for demarcation, Free Lok Adalat amicable settlement, Injunction in Civil Court",
            "1. Obtain certified RoR from Bhulekh portal. 2. File boundary demarcation petition with RI fee ₹100. 3. If neighbor resists, apply under Sec 164 BNSS before Sub-Divisional Magistrate. 4. Free mediation at Taluk Legal Services.",
            "Odisha Survey and Settlement Act 1958; Bharatiya Nagarik Suraksha Sanhita 2023",
            "Revenue Toll-Free: 1800-345-6770 / NALSA Legal Aid: 15100"
        ),
        (
            "labor_dispute",
            "Wage Theft, Minimum Wages & Migrant Worker Rights",
            "बकाया मजदूरी, न्यूनतम मजदूरी एवं प्रवासी श्रमिक अधिकार",
            "ବକେୟା ମଜୁରି, ସର୍ବନିମ୍ନ ମଜୁରୀ ଏବଂ ଶ୍ରମିକ ଅଧିକାର",
            "Workers have the legal right to receive timely wages without illegal cuts. Even without a written contract, oral testimony, attendance registers, and fellow worker statements are valid evidence.",
            "श्रमिकों को समय पर पूरी मजदूरी पाने का कानूनी अधिकार है। बिना लिखित समझौते के भी उपस्थिति प्रमाण व सहकर्मियों की गवाही मान्य साक्ष्य है।",
            "ସମସ୍ତ ଶ୍ରମିକଙ୍କର ସମୟ ଅନୁଯାୟୀ ସମ୍ପୂର୍ଣ୍ଣ ମଜୁରୀ ପାଇବାର ଆଇନଗତ ଅଧିକାର ରହିଛି। ଚୁକ୍ତିପତ୍ର ନଥିଲେ ମଧ୍ୟ ସାକ୍ଷୀ ଓ ଦୈନିକ ଖାତା ପ୍ରମାଣ ଭାବେ ଗ୍ରହଣୀୟ।",
            "Payment of Wages Act Sec 15, Code on Wages 2019, Inter-State Migrant Workmen Act",
            "Order for recovery of unpaid wage plus up to 10x compensation, Free assistance by Assistant Labour Commissioner",
            "1. Issue written wage demand slip to contractor. 2. File complaint before Assistant Labour Commissioner within 12 months. 3. If inter-state migrant, contact District Labour Helpline. 4. Case referred to Lok Adalat for quick release.",
            "Payment of Wages Act 1936; Minimum Wages Act 1948",
            "Labour Shramik Helpline: 1800-345-6703 / National Shramik 14434"
        ),
        (
            "consumer_dispute",
            "Defective Goods, Fake Seeds, Warranty Denial & Fair Refunds",
            "दोषपूर्ण उत्पाद, नकली बीज, वारंटी अस्वीकृति एवं उपभोक्ता अधिकार",
            "ତ୍ରୁଟିପୂର୍ଣ୍ଣ ସାମଗ୍ରୀ, ନକଲି ବିହନ ଓ ଗ୍ରାହକ ଅଧିକାର ସୁରକ୍ଷା",
            "Consumers can file complaints in District Consumer Commission without paying lawyer fees up to ₹50 Lakhs claim value. Electronic filing via e-Daakhil portal is available.",
            "दोषपूर्ण कृषि उपकरण, नकली खाद-बीज या इलेक्ट्रॉनिक सामान की वारंटी नकारने पर बिना वकील ₹50 लाख तक जिला उपभोक्ता आयोग में मुफ्त न्याय संभव है।",
            "ଖରାପ ମେସିନ, ନକଲି ବିହନ କିମ୍ବା ୱାରେଣ୍ଟି ଦେବାକୁ ମନା କଲେ ବିନା ଓକିଲରେ ଇ-ଦାଖିଲ ମାଧ୍ୟମରେ ୫୦ ଲକ୍ଷ ପର୍ଯ୍ୟନ୍ତ କ୍ଷତିପୂରଣ ଦାବି କରିପାରିବେ।",
            "Consumer Protection Act 2019 Sec 35, Sec 2(7) Deficiency in Service",
            "Full refund of purchase price, replacement of defective machinery, damages for crop loss & mental agony",
            "1. Send legal notice to seller/manufacturer giving 15 days to remedy. 2. Preserve tax invoice, warranty seal, photos. 3. File petition on e-Daakhil portal or submit 3 sets to District Commission. 4. Summons issued to dealer within 21 days.",
            "Consumer Protection Act 2019",
            "National Consumer Helpline: 1915 / SMS 'REPLY' to 8130009809"
        ),
        (
            "family_dispute",
            "Domestic Violence, Right to Residence & Free Legal Support",
            "घरेलू हिंसा से सुरक्षा, निवास का अधिकार एवं भरण-पोषण",
            "ଘରୋଇ ହିଂସାରୁ ସୁରକ୍ଷା, ଘରେ ରହିବା ଅଧିକାର ଏବଂ ଭରଣପୋଷଣ",
            "Women experiencing physical, verbal, emotional, or economic violence can obtain immediate protection, free residence rights, and monthly maintenance through Protection Officers or JMFC Court.",
            "किसी भी प्रकार की शारीरिक, मानसिक या आर्थिक प्रताड़ना पर महिलाओं को मुफ्त विधिक सहायता, घर से न निकाले जाने का अधिकार और गुजारा भत्ता तुरंत मिलता है।",
            "ଶାରୀରିକ କିମ୍ବା ମାନସିକ ନିର୍ଯାତନା କ୍ଷେତ୍ରରେ ମହିଳାମାନେ ତୁରନ୍ତ ସୁରକ୍ଷା ଅଧିକାରୀ ବା କୋର୍ଟରୁ ମାଗଣା ଆଇନ ସହାୟତା ଓ ଭରଣପୋଷଣ ପାଇପାରିବେ।",
            "Protection of Women from Domestic Violence Act (PWDVA) Sec 12, 18, 19, 20; BNSS Sec 144",
            "Immediate Protection Order (stopping abuse), Residence Order (cannot be evicted), Interim Maintenance within 60 days",
            "1. Contact nearest Women Protection Officer or dial 181. 2. Protection Officer prepares Domestic Incident Report (DIR Form 1). 3. Magistrate conducts hearing within 3 days. 4. Free lawyer assigned via DLSA.",
            "Protection of Women from Domestic Violence Act 2005",
            "Women Helpline: 181 / Emergency: 112 / NALSA Women Cell: 15100"
        ),
        (
            "cyber_fraud",
            "UPI Scams, OTP Phishing, Loan Apps & Account Lien Recovery",
            "साइबर धोखाधड़ी, यूपीआई फर्जीवाड़ा एवं खाता रिकवरी गाइड",
            "ସାଇବର ଠକେଇ, UPI ଠକାମି ଏବଂ ଟଙ୍କା ଫେରସ୍ତ ଆଇନ",
            "If victim of cyber theft or bank fraud, reporting within the 'Golden Hour' (first 2-3 hours) on helpline 1930 enables automated freeze of money in recipient mule bank accounts.",
            "ऑनलाइन ठगी होने पर 'गोल्डन ऑवर' (पहले दो-तीन घंटे) में 1930 पर कॉल करने से अपराधी के खाते में ट्रांसफर हुई राशि को तत्काल फ्रीज करवाया जा सकता है।",
            "ଅନଲାଇନ ଠକେଇ ହେବା କ୍ଷଣି ପ୍ରଥମ ୨ ଘଣ୍ଟା ମଧ୍ୟରେ ୧୯୩୦ ନମ୍ବରରେ କଲ୍ କଲେ ଠକର ବ୍ୟାଙ୍କ ଆକାଉଣ୍ଟକୁ ଫ୍ରିଜ୍ କରାଯାଇ ଟଙ୍କା ଫେରସ୍ତ କରାଯାଇପାରିବ।",
            "Bharatiya Nyaya Sanhita (BNS) Sec 318(4) Cheating, IT Act 2000 Sec 66D, BNSS Sec 457",
            "Immediate freeze on recipient bank accounts via NCRP portal, Court order for refund under BNSS 457",
            "1. Call 1930 immediately or log on to cybercrime.gov.in. 2. Note UTR number and recipient UPI ID. 3. Block ATM/UPI. 4. Visit Cyber Police station with bank statement for magistrate restitution certificate.",
            "Information Technology Act 2000; Bharatiya Nyaya Sanhita 2023",
            "National Cyber Crime Helpline: 1930 / WhatsApp Cyber Tip: +91-8750871111"
        )
    ]
    cursor.executemany("""
    INSERT INTO knowledge_base (category, title_en, title_hi, title_od, summary_en, summary_hi, summary_od, legal_sections, remedies, procedure_steps, relevant_acts, helpline)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, kb_data)

    # 3. Seed Checklists
    checklists_data = [
        # Land
        ("land_dispute", "RoR / Record of Rights (Patta)", "खतियान / जमाबंदी / पट्टा की प्रति", "ଜମି ପଟ୍ଟା / ଖତିୟାନ ନକଲ", 1, "Proof of ownership and recorded plot number", "Tahasildar / Bhulekh Portal"),
        ("land_dispute", "Latest Land Revenue Receipt (Khajna)", "नवीनतम लगान / खजाना रसीद", "ଚଳିତ ବର୍ଷର ଖଜଣା ରସିଦ", 1, "Proves continuous possession and tax compliance", "Revenue Inspector (RI) Office"),
        ("land_dispute", "Field Demarcation / Survey Map (Naksha)", "जमीन का प्रमाणित नक्शा", "ସର୍ଭେ ନକ୍ସା କିମ୍ବା ମ୍ୟାପ୍", 0, "Visual proof of boundaries and encroached area", "District Settlement Office"),
        ("land_dispute", "Aadhaar / Voter ID of Claimant", "दावेदार का आधार / पहचान पत्र", "ଦାବିଦାରଙ୍କ ଆଧାର କାର୍ଡ", 1, "Identity verification of legal claimant", "UIDAI / Election Commission"),

        # Labor
        ("labor_dispute", "Attendance Log / Work Diary", "दैनिक उपस्थिति डायरी / कार्य पर्ची", "ଦୈନିକ କାମ ଖାତା କିମ୍ବା ସ୍ଲିପ୍", 1, "Proof of number of days and nature of labor", "Sub-contractor / Self Diary"),
        ("labor_dispute", "Previous Wage Slip or UPI Payment Proof", "पिछली मजदूरी पर्ची या बैंक स्टेटमेंट", "ପୂର୍ବ ମଜୁରୀ ରସିଦ ବା ବ୍ୟାଙ୍କ ଟ୍ରାଞ୍ଜାକସନ", 1, "Demonstrates employer-employee wage agreement", "Bank / Employer"),
        ("labor_dispute", "e-Shram Card / Construction Worker Card", "ई-श्रम कार्ड / निर्माण श्रमिक कार्ड", "ଇ-ଶ୍ରମ କାର୍ଡ କିମ୍ବା ନିର୍ମାଣ ଶ୍ରମିକ କାର୍ଡ", 0, "Entitles worker to state legal defense fund", "Ministry of Labour"),

        # Consumer
        ("consumer_dispute", "Original Tax Invoice / Cash Memo", "मूल खरीद बिल / जीएसटी चालान", "କିଣାଯାଇଥିବା ସାମଗ୍ରୀର ବିଲ୍ / କ୍ୟାସ ମେମୋ", 1, "Proof of transaction and consumer standing", "Seller / Merchant"),
        ("consumer_dispute", "Warranty Card with Dealer Stamp", "वारंटी कार्ड (दुकानदार की मुहर सहित)", "ସିଲ୍ ଥିବା ୱାରେଣ୍ଟି କାର୍ଡ", 1, "Proves valid guarantee period", "Authorized Retailer"),
        ("consumer_dispute", "Photographs/Video of Defective Product", "खराब उपकरण की फोटो / वीडियो", "ଖରାପ ମେସିନର ଫଟୋ କିମ୍ବା ଭିଡିଓ", 1, "Evidence of physical defect or failure", "Consumer Self-recorded"),

        # Domestic / Family
        ("family_dispute", "Domestic Incident Report (DIR Form 1)", "घरेलू घटना रिपोर्ट (डीआईआर)", "ଘରୋଇ ଘଟଣା ରିପୋର୍ଟ (DIR)", 1, "Statutory basis for immediate protection order", "Protection Officer / CDPO"),
        ("family_dispute", "Medical Examination Slip (if physical injury)", "चिकित्सा जांच पर्ची (चोट लगने पर)", "ଡାକ୍ତରୀ ପରୀକ୍ଷା ରିପୋର୍ଟ (ଆଘାତ ଥିଲେ)", 0, "Corroborative physical evidence", "Govt Primary Health Centre / Hospital"),
        ("family_dispute", "Marriage Proof / Ration Card / Photographs", "विवाह प्रमाण / राशन कार्ड / फोटो", "ବିବାହ ପ୍ରମାଣପତ୍ର ବା ରାସନ କାର୍ଡ", 1, "Proof of domestic shared household relation", "Gram Panchayat / Registrar"),

        # Cyber
        ("cyber_fraud", "Bank Statement Highlighting Fraudulent Debits", "बैंक पासबुक / विवरण (अवैध लेन-देन रेखांकित)", "ବ୍ୟାଙ୍କ ଷ୍ଟେଟମେଣ୍ଟ (ଅବୈଧ କାରବାର)", 1, "Shows date, time, and UTR reference number", "Bank Branch / Netbanking"),
        ("cyber_fraud", "SMS Alerts & WhatsApp Chat Screenshots", "धोखाधड़ी संदेश व व्हाट्सएप स्क्रीनशॉट", "ମେସେଜ୍ ଓ ହ୍ୱାଟ୍ସଆପ୍ ସ୍କ୍ରିନସଟ୍", 1, "Digital footprint of fraudulent links or phishing", "Victim Phone"),
        ("cyber_fraud", "1930 Cyber Helpline Token Slip", "1930 साइबर कंप्लेंट पावती संख्या", "୧୯୩୦ ସାଇବର ଅଭିଯୋଗ ଟୋକନ ସଂଖ୍ୟା", 1, "Essential for bank freeze verification & court claim", "National Cybercrime Reporting Portal")
    ]
    cursor.executemany("""
    INSERT INTO checklists (category, item_en, item_hi, item_od, mandatory, purpose, issuing_authority)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, checklists_data)

    # 4. Seed Resources (Helplines & Portals)
    resources_data = [
        ("NALSA Legal Aid Helpline", "नालसा निःशुल्क विधिक सेवा", "ନାଲସା ମାଗଣା ଆଇନ ସେବା ହେଲ୍ପଲାଇନ୍", "legal_aid", "15100", "https://nalsa.gov.in", "24/7 Free legal advice and advocate assignment across India", "पूरे भारत में 24/7 मुफ्त कानूनी सलाह और सरकारी वकील की सुविधा", "ଭାରତ ସାରା ୨୪/୭ ମାଗଣା ଆଇନ ପରାମର୍ଶ ଏବଂ ସରକାରୀ ଓକିଲ ଯୋଗାଣ", 1),
        ("National Cyber Crime Reporting Helpline", "राष्ट्रीय साइबर अपराध हेल्पलाइन", "ଜାତୀୟ ସାଇବର ଅପରାଧ ହେଲ୍ପଲାଇନ୍", "emergency", "1930", "https://cybercrime.gov.in", "Toll-free emergency helpline to stop UPI / banking fraud within golden hour", "बैंक व यूपीआई ठगी को तत्काल फ्रीज कराने के लिए आपातकालीन नंबर", "ବ୍ୟାଙ୍କ ଓ UPI ଠକେଇ ଟଙ୍କା ଫ୍ରିଜ୍ କରିବା ପାଇଁ ଜରୁରୀ ନମ୍ବର", 1),
        ("National Emergency Unified Number", "राष्ट्रीय आपातकालीन एकीकृत सेवा", "ଜରୁରୀକାଳୀନ ସେବା (ପୋଲିସ/ଆମ୍ବୁଲାନ୍ସ)", "emergency", "112", "https://112.gov.in", "Emergency police, ambulance, and fire response in one single number", "पुलिस, एम्बुलेंस और अग्निशमन के लिए एकल आपातकालीन नंबर", "ପୋଲିସ, ଆମ୍ବୁଲାନ୍ସ ଓ ଅଗ୍ନିଶମ ସେବା ପାଇଁ ଏକକ ନମ୍ବର", 1),
        ("Women Helpline (Odisha & National)", "महिला हेल्पलाइन", "ମହିଳା ହେଲ୍ପଲାଇନ୍ ସେବା", "women", "181", "https://wcd.nic.in", "Crisis intervention, shelter, and medical support for women in distress", "संकटग्रस्त महिलाओं के लिए काउंसलिंग, आश्रय और तत्काल पुलिस सहायता", "ବିପଦରେ ଥିବା ମହିଳାମାନଙ୍କ ପାଇଁ କାଉନସେଲିଂ, ଆଶ୍ରୟ ଓ ସୁରକ୍ଷା", 1),
        ("National Consumer Toll-Free Helpline", "राष्ट्रीय उपभोक्ता हेल्पलाइन", "ଜାତୀୟ ଉପଭୋକ୍ତା ହେଲ୍ପଲାଇନ୍", "consumer", "1915", "https://consumerhelpline.gov.in", "File complaints against defective products, delayed delivery, and fraudulent sellers", "खराब उत्पाद, ठगी व वारंटी विवाद दर्ज कराने के लिए आधिकारिक मंच", "ଖରାପ ସାମଗ୍ରୀ ଓ ୱାରେଣ୍ଟି ବିବାଦ ଅଭିଯୋଗ ପଞ୍ଜୀକରଣ ପାଇଁ ମଞ୍ଚ", 1),
        ("Tele-Law Portal (Ministry of Law & Justice)", "टेली-लॉ योजना (विधि मंत्रालय)", "ଟେଲି-ଲ' ଯୋଜନା (ଭିଡିଓ ପରାମର୍ଶ)", "legal_aid", "14416", "https://tele-law.in", "Video-consultation with High Court panel lawyers via Gram Panchayat CSC", "ग्राम पंचायत स्तर पर उच्च न्यायालय के वकीलों से मुफ्त वीडियो परामर्श", "ଗ୍ରାମ ପଞ୍ଚାୟତ ସିଏସସି ଜରିଆରେ ବିଶେଷଜ୍ଞ ଓକିଲଙ୍କ ସହ ଭିଡିଓ ପରାମର୍ଶ", 1),
        ("e-Courts Services Portal", "ई-कोर्ट्स सेवाएं (केस ट्रैकर)", "ଇ-କୋର୍ଟ ସେବା (ମୋକଦ୍ଦମା ସ୍ଥିତି)", "portal", "1800-102-4040", "https://services.ecourts.gov.in", "Track CNR numbers, next court hearings, and order sheets from phone", "सीएनआर नंबर, अगली सुनवाई तारीख और अदालत के आदेश ऑनलाइन देखें", "କୋର୍ଟ ଶୁଣାଣି ତାରିଖ ଓ ନିର୍ଦ୍ଦେଶନାମା ଅନଲାଇନରେ ଦେଖନ୍ତୁ", 0),
        ("Odisha Jana Sunani (Samadhan)", "ओडिशा जन शुनाणी (समाधान पोर्टल)", "ଓଡ଼ିଶା ଜନ ଶୁଣାଣି (ସମାଧାନ ପୋର୍ଟାଲ)", "grievance", "1905", "https://janasunani.odisha.gov.in", "Direct public grievance redressal before District Collector and Chief Minister", "जिला कलेक्टर व मुख्यमंत्री के समक्ष जन शिकायत निवारण पोर्टल", "ଜିଲ୍ଲାପାଳ ଓ ମୁଖ୍ୟମନ୍ତ୍ରୀଙ୍କ ନିକଟରେ ସିଧାସଳଖ ଅଭିଯୋଗ ଦାଖଲ", 0)
    ]
    cursor.executemany("""
    INSERT INTO resources (name_en, name_hi, name_od, category, phone, portal_url, description_en, description_hi, description_od, is_helpline)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, resources_data)

    # 5. Seed Statutory Deadlines
    deadlines_data = [
        ("Cheque Dishonour / Bounce (Sec 138 NI Act)", "चेक बाउंस नोटिस एवं वाद सीमा", "ଚେକ୍ ବାଉନ୍ସ ନୋଟିସ୍ ସମୟସୀମା", "30 Days to send notice + 15 days cure + 30 days to file complaint", "Negotiable Instruments Act 1881 Sec 138(c)", "Bank return memo date", "Forfeiture of right to file criminal complaint under Sec 138", 75),
        ("Consumer Complaint Filing", "उपभोक्ता शिकायत दायर करने की मियाद", "ଗ୍ରାହକ ଅଭିଯୋଗ ଦାଖଲ ସମୟସୀମା", "2 Years from date cause of action arose", "Consumer Protection Act 2019 Sec 69", "Date of purchase or defect refusal", "Claim barred unless sufficient cause for delay condonation shown", 730),
        ("Payment of Wages Act Claim", "बकाया मजदूरी दावा दाखिल करने की समय सीमा", "ବକେୟା ମଜୁରୀ ଦାବି ସମୟସୀମା", "12 Months from date wages became payable", "Payment of Wages Act 1936 Sec 15(2)", "Date of non-payment", "Requires condonation of delay application before Labour Commissioner", 365),
        ("RTI First Appeal", "सूचना का अधिकार प्रथम अपील समय सीमा", "ସୂଚନା ଅଧିକାର (RTI) ପ୍ରଥମ ଅପିଲ", "30 Days from receipt of PIO rejection or expiry of 30 days period", "Right to Information Act 2005 Sec 19(1)", "Date of refusal or non-response", "Loss of statutory first appeal stage before Departmental Appellate Officer", 30),
        ("Civil Appeal against District Court Decree", "दीवानी अपील की समय सीमा", "ଦେୱାନୀ ମୋକଦ୍ଦମା ଅପିଲ ସମୟସୀମା", "90 Days to High Court / 30 Days to District Court", "Limitation Act 1963 Art 116", "Date of decree signature", "Decree attains finality; execution proceedings proceed", 90),
        ("Cyber Crime UPI Reversal Lien Claim", "साइबर ठगी बैंक खाता डी-फ्रीज दावा", "ସାଇବର ଠକେଇ ଟଙ୍କା ଫେରସ୍ତ ଆବେଦନ", "Immediately / Within 60 Days before charge sheet", "BNSS 2023 Sec 457", "NCRP freeze report date", "Money remains locked in interim banking suspension pool", 60)
    ]
    cursor.executemany("""
    INSERT INTO deadlines (dispute_type_en, dispute_type_hi, dispute_type_od, limit_period_text, act_reference, trigger_event, penalty_if_missed, days_limit)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, deadlines_data)

    # 6. Seed initial Escalations
    escalations_data = [
        ("NYA-2026-7801", "land_dispute", "Dharmendra Rout", "9861234501", "Demarcation delayed by RI for 4 months; seeking Taluk Legal Services mediator.", "od", "PENDING", "HIGH", "KIOSK-OD-042"),
        ("NYA-2026-7802", "labor_dispute", "Sunita Tudu", "9437112233", "Contractor absconded without paying 14 agricultural laborers ₹62,000.", "hi", "ASSIGNED", "HIGH", "KIOSK-OD-042"),
        ("NYA-2026-7803", "family_dispute", "Anonymous Citizen", None, "Requires confidential advice on Section 18 protection order from lady PLV.", "en", "IN_PROGRESS", "CRITICAL", "KIOSK-OD-042")
    ]
    cursor.executemany("""
    INSERT INTO escalations (token_number, query_category, citizen_name, phone_number, issue_summary, language, status, priority, kiosk_id)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, escalations_data)

    conn.commit()

if __name__ == "__main__":
    init_db()
    print("Database initialized and seeded successfully.")
