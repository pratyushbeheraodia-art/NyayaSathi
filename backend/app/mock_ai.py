import re
from typing import Dict, Any, List

CATEGORIES_META = {
    "criminal_police": {
        "en": "Criminal Law, Police FIR & Bail",
        "hi": "आपराधिक कानून, पुलिस प्राथमिकी (FIR) एवं जमानत",
        "od": "ଅପରାଧିକ ଆଇନ, ପୋଲିସ ଏଫଆଇଆର ଓ ଜାମିନ",
        "icon": "ShieldAlert",
        "urgency": "Emergency",
        "default_law": "Bharatiya Nyaya Sanhita 2023 & BNSS 2023 Sec 173, 480",
        "forum": "Police Station / Judicial Magistrate Court / High Court",
        "cost": "₹0 - Free Zero FIR & Legal Aid Panel Defense",
        "questions": [
            {
                "id": "q1",
                "en": "Has the police refused to register your FIR or provided an acknowledgment copy?",
                "hi": "क्या पुलिस ने आपकी एफआईआर दर्ज करने से मना किया या पावती प्रति नहीं दी?",
                "od": "ପୋଲିସ ଆପଣଙ୍କ ଏଫଆଇଆର ପଞ୍ଜୀକରଣ କରିବାକୁ ମନା କରିଛି କି?",
                "options": [
                    {"value": "refused", "en": "Police refused to file FIR", "hi": "पुलिस ने एफआईआर लिखने से मना किया", "od": "ପୋଲିସ ଏଫଆଇଆର ଲେଖିବାକୁ ମନା କଲା"},
                    {"value": "received_copy", "en": "FIR registered, have signed copy", "hi": "एफआईआर दर्ज है, प्रतिलिपि है", "od": "ଏଫଆଇଆର ହୋଇଛି, ନକଲ ଅଛି"},
                    {"value": "fear_arrest", "en": "Fear of false arrest / Need anticipatory bail", "hi": "गिरफ्तारी का डर / अग्रिम जमानत चाहिए", "od": "ଗିରଫ ହେବାର ଭୟ / ଅଗ୍ରୀମ ଜାମିନ ଦରକାର"}
                ]
            },
            {
                "id": "q2",
                "en": "Is the offense cognizable (serious like theft, assault, bodily harm) or non-cognizable?",
                "hi": "क्या मामला गंभीर अपराध (चोरी, मारपीट, हमला) है या असंज्ञेय?",
                "od": "ଏହା କୌଣସି ଗମ୍ଭୀର ଅପରାଧ (ମାଡ଼ପିଟ, ଚୋରି, ଆକ୍ରମଣ) କି?",
                "options": [
                    {"value": "serious_cognizable", "en": "Cognizable / Physical violence / Theft", "hi": "गंभीर / शारीरिक हिंसा / चोरी", "od": "ଗମ୍ଭୀର / ଶାରୀରିକ ଆକ୍ରମଣ / ଚୋରି"},
                    {"value": "verbal_threat", "en": "Verbal abuse / Non-physical dispute", "hi": "गाली-गलौज / गैर-शारीरिक विवाद", "od": "ଗାଳିଗୁଲଜ / ମୌଖିକ ଧମକ"}
                ]
            }
        ]
    },
    "family_matrimonial": {
        "en": "Family Law, Divorce, Custody & Maintenance",
        "hi": "पारिवारिक कानून, विवाह विच्छेद, बाल अभिरक्षा एवं गुजारा",
        "od": "ପାରିବାରିକ ଆଇନ, ଛାଡ଼ପତ୍ର, ସନ୍ତାନ ହେପାଜତ ଓ ଭରଣପୋଷଣ",
        "icon": "HeartHandshake",
        "urgency": "High",
        "default_law": "Hindu Marriage Act 1955 Sec 13B & BNSS Sec 144",
        "forum": "Family Court / District Court Mediation Centre",
        "cost": "₹0 - Free Counseling & Mediation / Nominal Stamp Fee",
        "questions": [
            {
                "id": "q1",
                "en": "Are both spouses mutually agreeing to separate, or is it contested?",
                "hi": "क्या दोनों पक्ष आपसी सहमति से अलग होना चाहते हैं या विवादित है?",
                "od": "ଉଭୟ ପକ୍ଷ ଆପୋଷ ସହମତିରେ ଅଲଗା ହେବାକୁ ଚାହୁଁଛନ୍ତି କି ବିବାଦ ଅଛି?",
                "options": [
                    {"value": "mutual", "en": "Mutual Consent (Fast-track Sec 13B)", "hi": "पारस्परिक सहमति (त्वरित धारा 13B)", "od": "ଆପୋଷ ସହମତି (ଧାରା ୧୩B)"},
                    {"value": "contested", "en": "Contested (Cruelty, Desertion, Adultery)", "hi": "विवादित (प्रताड़ना, परित्याग)", "od": "ବିବାଦିତ (ନିର୍ଯାତନା, ପରିତ୍ୟାଗ)"},
                    {"value": "reconciliation", "en": "Want reconciliation / Restitution of rights", "hi": "साथ रहना चाहते हैं / सुलह चाहिए", "od": "ଏକାଠି ରହିବାକୁ ଚାହୁଁଛୁ / ବୁଝାମଣା ଦରକାର"}
                ]
            },
            {
                "id": "q2",
                "en": "Are there disputes regarding child custody or monthly child sustenance?",
                "hi": "क्या बच्चों की कस्टडी या मासिक खर्च को लेकर विवाद है?",
                "od": "ସନ୍ତାନର ହେପାଜତ କିମ୍ବା ମାସିକ ଖର୍ଚ୍ଚ ବିଷୟରେ ବିବାଦ ଅଛି କି?",
                "options": [
                    {"value": "custody_needed", "en": "Yes, seeking child custody & maintenance", "hi": "हाँ, कस्टडी व गुजारा भत्ता चाहिए", "od": "ହଁ, ପିଲାର ହେପାଜତ ଓ ଖର୍ଚ୍ଚ ଦରକାର"},
                    {"value": "no_children", "en": "No minor children involved", "hi": "नाबालिग बच्चे नहीं हैं", "od": "ନାବାଳକ ସନ୍ତାନ ନାହାଁନ୍ତି"}
                ]
            }
        ]
    },
    "domestic_violence": {
        "en": "Domestic Violence, Protection & Residence",
        "hi": "घरेलू हिंसा, महिला सुरक्षा एवं आवास अधिकार",
        "od": "ଘରୋଇ ହିଂସା, ମହିଳା ସୁରକ୍ଷା ଓ ବାସସ୍ଥାନ ଅଧିକାର",
        "icon": "Shield",
        "urgency": "Emergency",
        "default_law": "Protection of Women from Domestic Violence Act 2005",
        "forum": "JMFC Court & Women Protection Officer / OSC 181",
        "cost": "₹0 - 100% Free Legal Aid & Shelter Rights",
        "questions": [
            {
                "id": "q1",
                "en": "Are you facing physical danger, eviction from matrimonial home, or harassment?",
                "hi": "क्या आप शारीरिक खतरे, घर से निकाले जाने या प्रताड़ना का सामना कर रही हैं?",
                "od": "ଆପଣ ଶାରୀରିକ ବିପଦ, ଘରୁ ବାହାର କରିବା ବା ନିର୍ଯାତନାର ସମ୍ମୁଖୀନ କି?",
                "options": [
                    {"value": "immediate_danger", "en": "Urgent Physical Threat / Need Police (181/112)", "hi": "तात्कालिक खतरा / पुलिस चाहिए", "od": "ଜରୁରୀ ବିପଦ / ପୋଲିସ ଦରକାର (୧୮୧/୧୧୨)"},
                    {"value": "eviction_threat", "en": "Threat of eviction / Denied stridhan & shelter", "hi": "घर से निकालने की धमकी / स्त्रीधन रोका गया", "od": "ଘରୁ ବାହାର କରିବା ଧମକ / ସ୍ତ୍ରୀଧନ ବନ୍ଦ"},
                    {"value": "maintenance_needed", "en": "Need monthly maintenance for food & children", "hi": "भरण-पोषण गुजारा भत्ता चाहिए", "od": "ଭରଣପୋଷଣ ଖର୍ଚ୍ଚ ଆବଶ୍ୟକ"}
                ]
            }
        ]
    },
    "land_property": {
        "en": "Land Encroachment, Mutation & Boundaries",
        "hi": "भूमि विवाद, पट्टा, सीमांकन एवं नामांतरण",
        "od": "ଜମିବାଡ଼ି, ପଟ୍ଟା, ସୀମା ଓ ମ୍ୟୁଟେସନ ବିବାଦ",
        "icon": "MapPin",
        "urgency": "High",
        "default_law": "Odisha Land Reforms Act & BNSS Sec 164",
        "forum": "Revenue Court of Tahasildar & Taluk Lok Adalat",
        "cost": "₹0 - Free Lok Adalat / Nominal ₹100 Demarcation Fee",
        "questions": [
            {
                "id": "q1",
                "en": "Do you hold a government Record of Rights (RoR / Patta) in your name or ancestor's name?",
                "hi": "क्या आपके या पूर्वज के नाम सरकारी खतियान / पट्टा (RoR) उपलब्ध है?",
                "od": "ଆପଣଙ୍କ ନାମରେ ବା ପୂର୍ବପୁରୁଷଙ୍କ ନାମରେ ଜମି ପଟ୍ଟା (RoR) ଅଛି କି?",
                "options": [
                    {"value": "own_name", "en": "Yes, in my own name", "hi": "हाँ, मेरे नाम पर है", "od": "ହଁ, ନିଜ ନାମରେ ଅଛି"},
                    {"value": "ancestor", "en": "Yes, in father/grandfather's name", "hi": "हाँ, पूर्वज के नाम पर", "od": "ହଁ, ପୂର୍ବପୁରୁଷଙ୍କ ନାମରେ"},
                    {"value": "none", "en": "No papers available / Unrecorded", "hi": "कागजात नहीं हैं", "od": "କୌଣସି କାଗଜପତ୍ର ନାହିଁ"}
                ]
            }
        ]
    },
    "property_succession": {
        "en": "Inheritance, Partition, Will & Daughter Rights",
        "hi": "पैतृक संपत्ति, बंटवारा, वसीयत एवं बेटियों का अधिकार",
        "od": "ପୈତୃକ ସମ୍ପତ୍ତି, ବଣ୍ଟନ, ଉଇଲ୍ ଓ ଝିଅମାନଙ୍କ ଅଧିକାର",
        "icon": "FileText",
        "urgency": "Medium",
        "default_law": "Hindu Succession Act 1956 (Sec 6 Equal Coparcenary)",
        "forum": "Civil Court / Tahasildar Partition / Lok Adalat",
        "cost": "Fixed nominal court fee for partition suits",
        "questions": [
            {
                "id": "q1",
                "en": "Is the property ancestral (inherited) or self-acquired by parents?",
                "hi": "क्या संपत्ति पैतृक है या माता-पिता द्वारा स्व-अर्जित?",
                "od": "ସମ୍ପତ୍ତି ପୈତୃକ କିମ୍ବା ନିଜେ କିଣା ସମ୍ପତ୍ତି କି?",
                "options": [
                    {"value": "ancestral", "en": "Ancestral (daughters & sons have equal birthright)", "hi": "पैतृक (बेटा-बेटी का जन्मसिद्ध समान अधिकार)", "od": "ପୈତୃକ (ପୁଅ-ଝିଅଙ୍କ ସମାନ ଅଧିକାର)"},
                    {"value": "self_acquired_no_will", "en": "Self-acquired, but deceased left no registered Will", "hi": "स्व-अर्जित, बिना वसीयत निधन", "od": "ନିଜ ଅର୍ଜିତ, କୌଣସି ଉଇଲ୍ ନାହିଁ"},
                    {"value": "disputed_will", "en": "Someone is claiming a suspicious or forged Will", "hi": "फर्जी या संदिग्ध वसीयत का दावा", "od": "ଜାଲି ବା ସନ୍ଦେହଜନକ ଉଇଲ୍ ଦାବି"}
                ]
            }
        ]
    },
    "tenancy_realestate": {
        "en": "Tenant, Landlord & RERA Builder Disputes",
        "hi": "किरायेदारी विवाद एवं रेरा (RERA) बिल्डर धोखाधड़ी",
        "od": "ଭଡ଼ାଟିଆ, ଘରମାଲିକ ଓ ରେରା (RERA) ବିଲ୍ଡର ବିବାଦ",
        "icon": "Building",
        "urgency": "Medium",
        "default_law": "Real Estate (Regulation) Act 2016 & Model Tenancy Laws",
        "forum": "RERA Authority / Rent Tribunal / Civil Court",
        "cost": "Statutory online RERA complaint fee ₹1,000",
        "questions": [
            {
                "id": "q1",
                "en": "Are you dealing with builder flat delivery delay or a tenant eviction issue?",
                "hi": "क्या बिल्डर द्वारा फ्लैट देने में देरी है या किरायेदार विवाद?",
                "od": "ବିଲ୍ଡର ଫ୍ଲାଟ୍ ଦେବାରେ ବିଳମ୍ବ କରିଛି କିମ୍ବା ଘରଭଡ଼ା ବିବାଦ?",
                "options": [
                    {"value": "rera_delay", "en": "Builder delayed possession / Demanding full refund + interest", "hi": "बिल्डर ने कब्जा टाला / ब्याज सहित रिफंड चाहिए", "od": "ବିଲ୍ଡର କବଜା ଦେଇନି / ସୁଧ ସହ ଟଙ୍କା ଫେରସ୍ତ"},
                    {"value": "illegal_eviction", "en": "Landlord disconnecting electricity/water or illegal eviction", "hi": "मकान मालिक द्वारा बिजली-पानी काटना / अवैध बेदखली", "od": "ଘରମାଲିକ ଜବରଦସ୍ତ ବାହାର କରୁଛନ୍ତି"},
                    {"value": "security_deposit", "en": "Landlord refusing to return security advance deposit", "hi": "जमानत राशि (सिक्योरिटी) लौटाने से मना", "od": "ସିକ୍ୟୁରିଟି ଟଙ୍କା ଫେରାଉ ନାହାନ୍ତି"}
                ]
            }
        ]
    },
    "labor_employment": {
        "en": "Employment, Unpaid Wages, PF & Wrongful Termination",
        "hi": "रोजगार, बकाया वेतन, पीएफ एवं अनुचित बर्खास्तगी",
        "od": "ଚାକିରି, ବକେୟା ଦରମା, PF ଓ ଚାକିରିରୁ ବାହାର କରିବା",
        "icon": "Briefcase",
        "urgency": "High",
        "default_law": "Payment of Wages Act 1936 Sec 15 & Industrial Disputes Act",
        "forum": "Assistant Labour Commissioner (ALC) / Labour Court",
        "cost": "₹0 - 100% Free Government Legal Redressal",
        "questions": [
            {
                "id": "q1",
                "en": "What is the primary nature of employment grievance?",
                "hi": "रोजगार संबंधी मुख्य समस्या क्या है?",
                "od": "ଚାକିରି ସମ୍ପର୍କିତ ମୁଖ୍ୟ ସମସ୍ୟା କ'ଣ?",
                "options": [
                    {"value": "unpaid_wages", "en": "Unpaid salary / Delayed wages", "hi": "बकाया वेतन / मजदूरी नहीं मिली", "od": "ବକେୟା ଦରମା / ମଜୁରୀ ବନ୍ଦ"},
                    {"value": "wrongful_termination", "en": "Illegal termination without notice or severance", "hi": "बिना नोटिस अवैध बर्खास्तगी", "od": "ବିନା ନୋଟିସରେ ଚାକିରିରୁ ବିଦାୟ"},
                    {"value": "pf_gratuity", "en": "Non-payment of Gratuity or PF funds", "hi": "ग्रेच्युटी या पीएफ रोकने का मामला", "od": "ଗ୍ରାଚ୍ୟୁଟି ବା PF ଟଙ୍କା ଅଟକିଛି"},
                    {"value": "posh_harassment", "en": "Workplace harassment (POSH Act matter)", "hi": "कार्यस्थल पर यौन उत्पीड़न (POSH)", "od": "କାର୍ଯ୍ୟକ୍ଷେତ୍ରରେ ନିର୍ଯାତନା (POSH)"}
                ]
            }
        ]
    },
    "consumer_dispute": {
        "en": "Consumer Rights, Defective Goods & Fraudulent Services",
        "hi": "उपभोक्ता अधिकार, खराब उत्पाद, वारंटी एवं सेवा में कमी",
        "od": "ଗ୍ରାହକ ଅଧିକାର, ତ୍ରୁଟିପୂର୍ଣ୍ଣ ସାମଗ୍ରୀ ଓ ୱାରେଣ୍ଟି ସମସ୍ୟା",
        "icon": "ShoppingBag",
        "urgency": "Medium",
        "default_law": "Consumer Protection Act 2019 Sec 35",
        "forum": "District Consumer Disputes Commission / e-Daakhil",
        "cost": "₹0 court fee for claims up to ₹5 Lakhs",
        "questions": [
            {
                "id": "q1",
                "en": "Do you hold the purchase bill / invoice and warranty card?",
                "hi": "क्या आपके पास खरीद बिल व वारंटी कार्ड उपलब्ध है?",
                "od": "ଆପଣଙ୍କ ପାଖରେ କିଣା ବିଲ୍ ଓ ୱାରେଣ୍ଟି କାର୍ଡ ଅଛି କି?",
                "options": [
                    {"value": "have_bill", "en": "Yes, have tax invoice & warranty", "hi": "हाँ, बिल व वारंटी दोनों हैं", "od": "ହଁ, ବିଲ୍ ଓ ୱାରେଣ୍ଟି ଉଭୟ ଅଛି"},
                    {"value": "digital_proof", "en": "Digital UPI receipt / Online order record", "hi": "ऑनलाइन ऑर्डर या यूपीआई प्रमाण है", "od": "ଅନଲାଇନ ଅର୍ଡର ବା UPI ପ୍ରମାଣ ଅଛି"},
                    {"value": "no_bill", "en": "No formal bill, paid cash", "hi": "पक्का बिल नहीं, नकद दिया था", "od": "ନଗଦ ଦେଇଥିଲି, ବିଲ୍ ନାହିଁ"}
                ]
            }
        ]
    },
    "banking_debt_cheque": {
        "en": "Cheque Bounce (Sec 138), Loan Harassment & Debt",
        "hi": "चेक बाउंस (धारा 138), बैंक ऋण एवं वसूली उत्पीड़न",
        "od": "ଚେକ୍ ବାଉନ୍ସ (ଧାରା ୧୩୮), ବ୍ୟାଙ୍କ ଋଣ ଓ ରିକଭରି ଉତ୍ପୀଡ଼ନ",
        "icon": "CreditCard",
        "urgency": "High",
        "default_law": "Negotiable Instruments Act 1881 Sec 138 & RBI Fair Practices",
        "forum": "Judicial Magistrate Court / Banking Ombudsman",
        "cost": "Statutory court fee as per state schedule",
        "questions": [
            {
                "id": "q1",
                "en": "What type of banking or financial matter are you facing?",
                "hi": "आप किस प्रकार के बैंकिंग या वित्तीय मामले का सामना कर रहे हैं?",
                "od": "କେଉଁ ପ୍ରକାରର ବ୍ୟାଙ୍କିଙ୍ଗ ବା ଆର୍ଥିକ ସମସ୍ୟା ରହିଛି?",
                "options": [
                    {"value": "cheque_bounced", "en": "Cheque bounced / Dishonored due to insufficient funds", "hi": "चेक बाउंस हो गया (फंड अपर्याप्त)", "od": "ଚେକ୍ ବାଉନ୍ସ ହୋଇଛି (ଟଙ୍କା ନାହିଁ)"},
                    {"value": "recovery_agent_harassment", "en": "Harassment/Threats by loan recovery agents (RBI violation)", "hi": "रिकवरी एजेंट द्वारा प्रताड़ना व धमकी", "od": "ଋଣ ରିକଭରି ଏଜେଣ୍ଟଙ୍କ ଧମକ ଓ ଅସଦାଚରଣ"},
                    {"value": "cibil_dispute", "en": "Wrongful default reported to CIBIL / Credit bureau", "hi": "सिबिल (CIBIL) में गलत डिफॉल्ट दर्ज", "od": "CIBIL ରେ ଭୁଲ୍ ଡିଫଲ୍ଟ ରେକର୍ଡ"}
                ]
            }
        ]
    },
    "cyber_fraud_privacy": {
        "en": "Cyber Crime, UPI Fraud, Blackmail & Hacking",
        "hi": "साइबर अपराध, यूपीआई धोखाधड़ी, ब्लैकमेल एवं हैकिंग",
        "od": "ସାଇବର ଠକେଇ, UPI ଜାଲିଆତି, ବ୍ଲାକମେଲ ଓ ହ୍ୟାକିଙ୍ଗ",
        "icon": "AlertTriangle",
        "urgency": "Emergency",
        "default_law": "IT Act 2000 & BNS Sec 318, BNSS Sec 457",
        "forum": "National Cybercrime Portal 1930 & Jurisdictional Magistrate",
        "cost": "₹0 - Automated Banking Freeze via NCRP",
        "questions": [
            {
                "id": "q1",
                "en": "Is this financial money theft or digital blackmail / harassment?",
                "hi": "क्या यह पैसे कटने का मामला है या ऑनलाइन ब्लैकमेल/उत्पीड़न?",
                "od": "ଏହା ଟଙ୍କା କଟିବା ବିଷୟ କିମ୍ବା ଅନଲାଇନ ବ୍ଲାକମେଲ/ନିର୍ଯାତନା?",
                "options": [
                    {"value": "financial_under_2h", "en": "Money stolen via UPI/OTP within last 2 hours (Golden Hour)", "hi": "2 घंटे के भीतर यूपीआई से पैसे कटे (गोल्डन ऑवर)", "od": "୨ ଘଣ୍ଟା ଭିତରେ UPI ରୁ ଟଙ୍କା ଚୋରି (ଗୋଲ୍ଡେନ ସମୟ)"},
                    {"value": "financial_older", "en": "Money deducted more than 2 hours ago", "hi": "2 घंटे से अधिक पहले पैसे कटे", "od": "୨ ଘଣ୍ଟାରୁ ଅଧିକ ସମୟ ପୂର୍ବରୁ ଟଙ୍କା କଟିଛି"},
                    {"value": "blackmail_photo", "en": "Blackmail / Fake loan app / Deepfake or private photo misuse", "hi": "ब्लैकमेल / फर्जी लोन ऐप / फोटो का दुरुपयोग", "od": "ବ୍ଲାକମେଲ / ଫେକ୍ ଲୋନ୍ ଆପ୍ / ଫଟୋ ଅପବ୍ୟବହାର"}
                ]
            }
        ]
    },
    "motor_accidents_traffic": {
        "en": "Road Accidents, MACT Claims & Traffic Challans",
        "hi": "सड़क दुर्घटना मुआवजा, एमएसीटी एवं ट्रैफिक चालान",
        "od": "ସଡ଼କ ଦୁର୍ଘଟଣା କ୍ଷତିପୂରଣ MACT ଓ ଟ୍ରାଫିକ ଚାଲାଣ",
        "icon": "Car",
        "urgency": "High",
        "default_law": "Motor Vehicles Act 1988 (Sec 166 Compensation)",
        "forum": "Motor Accident Claims Tribunal (MACT) / Virtual Traffic Court",
        "cost": "₹0 - Legal Aid assigned for accident victims",
        "questions": [
            {
                "id": "q1",
                "en": "What is the primary nature of motor vehicle grievance?",
                "hi": "सड़क वाहन संबंधी मुख्य मामला क्या है?",
                "od": "ଗାଡ଼ି ମୋଟର ସମ୍ପର୍କିତ କେଉଁ ସମସ୍ୟା ରହିଛି?",
                "options": [
                    {"value": "accident_injury_claim", "en": "Accident injury / Disability compensation claim", "hi": "दुर्घटना में चोट / विकलांगता मुआवजा दावा", "od": "ଦୁର୍ଘଟଣା ଆଘାତ / କ୍ଷତିପୂରଣ ଦାବି"},
                    {"value": "fatal_accident", "en": "Death of breadwinner in accident / Dependency claim", "hi": "दुर्घटना में मृत्यु / आश्रितों का दावा", "od": "ଦୁର୍ଘଟଣାରେ ମୃତ୍ୟୁ / ଆଶ୍ରିତଙ୍କ କ୍ଷତିପୂରଣ"},
                    {"value": "wrong_challan", "en": "Disputing incorrect electronic traffic e-challan", "hi": "गलत ट्रैफिक चालान को चुनौती देना", "od": "ଭୁଲ୍ ଟ୍ରାଫିକ ଇ-ଚାଲାଣ ବିରୋଧରେ ଆବେଦନ"}
                ]
            }
        ]
    },
    "senior_citizen_welfare": {
        "en": "Senior Citizen Rights & Parental Maintenance",
        "hi": "वरिष्ठ नागरिक अधिकार एवं माता-पिता भरण-पोषण",
        "od": "ବରିଷ୍ଠ ନାଗରିକ ଅଧିକାର ଓ ପିତାମାତା ଭରଣପୋଷଣ",
        "icon": "Users",
        "urgency": "High",
        "default_law": "Maintenance & Welfare of Parents and Senior Citizens Act 2007",
        "forum": "Maintenance Tribunal (Sub-Divisional Magistrate SDM)",
        "cost": "₹0 - Zero fee fast-track procedure (90 days mandatory disposal)",
        "questions": [
            {
                "id": "q1",
                "en": "What specific relief do the senior citizens require?",
                "hi": "वरिष्ठ नागरिकों को किस प्रकार की राहत चाहिए?",
                "od": "ବରିଷ୍ଠ ନାଗରିକଙ୍କୁ କେଉଁ ସହାୟତା ଦରକାର?",
                "options": [
                    {"value": "monthly_maintenance", "en": "Children refusing food/medical care / Need monthly maintenance", "hi": "संतान द्वारा खर्चा न देना / मासिक भरण-पोषण चाहिए", "od": "ପିଲାମାନେ ଖର୍ଚ୍ଚ ଦେଉନାହାନ୍ତି / ମାସିକ ଭରଣପୋଷଣ"},
                    {"value": "evict_abusive_children", "en": "Evict abusive children from senior citizen's own home", "hi": "प्रताड़ित करने वाले बच्चों को घर से बेदखल करना", "od": "ଅତ୍ୟାଚାରୀ ପିଲାଙ୍କୁ ନିଜ ଘରୁ ବାହାର କରିବା"},
                    {"value": "cancel_gift_deed", "en": "Cancel gift deed transferred on broken condition of care", "hi": "देखभाल की शर्त पर दी गई संपत्ति उपहार रद्द करना", "od": "ସମ୍ପତ୍ତି ଦାନପତ୍ର ବାତିଲ୍ କରିବା"}
                ]
            }
        ]
    },
    "child_pocso_education": {
        "en": "Child Protection, POCSO, Custody & Education Rights",
        "hi": "बाल संरक्षण, पॉक्सो (POCSO) एवं शिक्षा का अधिकार",
        "od": "ଶିଶୁ ସୁରକ୍ଷା, ପକ୍ସୋ (POCSO) ଓ ମାଗଣା ଶିକ୍ଷା ଅଧିକାର",
        "icon": "ShieldCheck",
        "urgency": "Emergency",
        "default_law": "POCSO Act 2012, Juvenile Justice Act 2015 & RTE Act 2009",
        "forum": "Special POCSO Court / Child Welfare Committee (CWC) / Dial 1098",
        "cost": "₹0 - 100% Free State Protection & In-Camera Trial",
        "questions": [
            {
                "id": "q1",
                "en": "What child welfare matter requires legal assistance?",
                "hi": "किस प्रकार के बाल संरक्षण मामले में सहायता चाहिए?",
                "od": "କେଉଁ ପ୍ରକାରର ଶିଶୁ ସୁରକ୍ଷା ସହାୟତା ଆବଶ୍ୟକ?",
                "options": [
                    {"value": "pocso_abuse", "en": "Child abuse / Assault (Dial 1098 / Immediate FIR)", "hi": "बच्चे के साथ दुर्व्यवहार (1098 / तत्काल एफआईआर)", "od": "ଶିଶୁ ନିର୍ଯାତନା (୧୦୯୮ / ତୁରନ୍ତ ଏଫଆଇଆର)"},
                    {"value": "rte_admission", "en": "School refusing admission under 25% free RTE quota", "hi": "आरटीई के तहत 25% मुफ्त दाखिला न मिलना", "od": "ମାଗଣା ଶିକ୍ଷା (RTE 25%) ନାମଲେଖା ମନା"},
                    {"value": "child_labour", "en": "Rescue from illegal child labor / Bondage", "hi": "अवैध बाल श्रम से मुक्ति", "od": "ବେଆଇନ ଶିଶୁ ଶ୍ରମିକ ଉଦ୍ଧାର"}
                ]
            }
        ]
    },
    "constitutional_rti_grievance": {
        "en": "RTI, Civil Rights, Writs & Government Inaction",
        "hi": "सूचना का अधिकार (RTI), मौलिक अधिकार एवं जन शिकायत",
        "od": "ସୂଚନା ଅଧିକାର (RTI), ମୌଳିକ ଅଧିକାର ଓ ଜନ ଅଭିଯୋଗ",
        "icon": "HelpCircle",
        "urgency": "Medium",
        "default_law": "Right to Information Act 2005 & Constitution Art 226/32",
        "forum": "Public Information Officer (PIO) / Information Commission / High Court",
        "cost": "₹10 RTI application fee (Free for BPL card holders)",
        "questions": [
            {
                "id": "q1",
                "en": "What type of public grievance or administrative issue are you raising?",
                "hi": "आप किस प्रकार की जन शिकायत या प्रशासनिक मुद्दा उठा रहे हैं?",
                "od": "କେଉଁ ପ୍ରକାରର ସରକାରୀ ଅଭିଯୋଗ ବା RTI ଦାଖଲ କରିବାକୁ ଚାହୁଁଛନ୍ତି?",
                "options": [
                    {"value": "rti_filing", "en": "File new RTI or Appeal against refused government records", "hi": "नई आरटीआई या अपील (दस्तावेज़ छुपाने पर)", "od": "ନୂଆ RTI କିମ୍ବା ଅପିଲ୍ ଆବେଦନ"},
                    {"value": "service_delay_ortpsa", "en": "Undue delay in Caste/Income/Resident certificate (ORTPSA violation)", "hi": "जाति/आय प्रमाण पत्र में देरी (सेवा अधिकार उल्लंघन)", "od": "ଜାତି/ଆୟ ପ୍ରମାଣପତ୍ର ବିଳମ୍ବ (ORTPSA ଅଧିକାର)"},
                    {"value": "public_nuisance", "en": "Public nuisance, sewage overflow or illegal pollution (BNSS 152)", "hi": "सार्वजनिक उपद्रव, प्रदूषण या अतिक्रमण", "od": "ସର୍ବସାଧାରଣ ପ୍ରଦୂଷଣ ବା ଅସୁବିଧା (BNSS 152)"}
                ]
            }
        ]
    },
    "business_msme_tax": {
        "en": "Business Contracts, MSME Delayed Payments & Tax",
        "hi": "व्यापार अनुबंध, एमएसएमई बकाया भुगतान एवं कर विवाद",
        "od": "ବ୍ୟାପାର ଚୁକ୍ତିପତ୍ର, MSME ବକେୟା ଟଙ୍କା ଓ ଟିକସ ବିବାଦ",
        "icon": "FileCheck",
        "urgency": "Medium",
        "default_law": "MSMED Act 2006 Sec 16 (Compound Interest at 3x RBI Rate)",
        "forum": "MSME Facilitation Council / Commercial Court",
        "cost": "₹0 - Online filing on MSME Samadhaan portal",
        "questions": [
            {
                "id": "q1",
                "en": "What business matter requires legal intervention?",
                "hi": "व्यापार में किस कानूनी समाधान की आवश्यकता है?",
                "od": "ବ୍ୟବସାୟରେ କେଉଁ ଆଇନଗତ ସହାୟତା ଦରକାର?",
                "options": [
                    {"value": "msme_delayed_payment", "en": "Buyer defaulted on payment beyond 45 days (MSME Samadhaan)", "hi": "45 दिनों से अधिक भुगतान बकाया (MSME समाधान)", "od": "୪୫ ଦିନରୁ ଅଧିକ ବକେୟା ବିଲ୍ (MSME ସମାଧାନ)"},
                    {"value": "breach_of_contract", "en": "Breach of commercial contract / Non-delivery of goods", "hi": "व्यापारिक अनुबंध का उल्लंघन / माल न मिलना", "od": "ବ୍ୟବସାୟିକ ଚୁକ୍ତି ଉଲ୍ଲଂଘନ"},
                    {"value": "gst_tax_notice", "en": "GST mismatch notice or tax dispute", "hi": "जीएसटी या टैक्स नोटिस का जवाब", "od": "GST ବା ଟିକସ ନୋଟିସ୍ ଉତ୍ତର"}
                ]
            }
        ]
    },
    "universal_legal_assistant": {
        "en": "General Legal Consultation & Statutory Rights",
        "hi": "सामान्य कानूनी सलाह एवं वैधानिक अधिकार",
        "od": "ସାଧାରଣ ଆଇନ ପରାମର୍ଶ ଓ ଆଇନଗତ ଅଧିକାର",
        "icon": "Scale",
        "urgency": "Medium",
        "default_law": "Constitution of India, BNS 2023 & Legal Services Authorities Act",
        "forum": "District Legal Services Authority (DLSA) / Taluk Court",
        "cost": "₹0 - 100% Free Consultation under NALSA Scheme",
        "questions": [
            {
                "id": "q1",
                "en": "Do you need direct free legal aid representation or advice on legal procedure?",
                "hi": "क्या आपको मुफ्त सरकारी वकील चाहिए या प्रक्रियात्मक सलाह?",
                "od": "ଆପଣଙ୍କୁ ମାଗଣା ସରକାରୀ ଓକିଲ ଦରକାର କିମ୍ବା ଆଇନଗତ ପରାମର୍ଶ?",
                "options": [
                    {"value": "need_lawyer", "en": "Need Free Legal Aid Lawyer assigned by DLSA", "hi": "मुफ्त सरकारी वकील चाहिए", "od": "ମାଗଣା ସରକାରୀ ଓକିଲ ଆବଶ୍ୟକ"},
                    {"value": "procedural_guide", "en": "Need explanation of court procedure & forms", "hi": "अदालती प्रक्रिया व फॉर्म की जानकारी", "od": "କୋର୍ଟ ନିୟମ ଓ ଫର୍ମ ବୁଝିବା ଦରକାର"}
                ]
            }
        ]
    }
}

KEYWORD_MAP = {
    "criminal_police": [
        "fir", "police", "arrest", "bail", "jail", "remand", "station", "than", "thana", "custody", "murder",
        "theft", "assault", "beating", "attack", "knife", "bns", "bnss", "crime", "criminal", "cognizable",
        "police complaint", "daroga", "sho", "magistrate", "zero fir", "fir copy", "false case", "extortion",
        "एफआईआर", "पुलिस", "थाना", "गिरफ्तारी", "जमानत", "जेल", "दरोगा", "हमला", "मारपीट", "चोरी", "अग्रिम जमानत",
        "ଏଫଆଇଆର", "ପୋଲିସ", "ଥାନା", "ଗିରଫ", "ଜାମିନ", "ଜେଲ", "ଚୋରି", "ମାଡ଼ପିଟ", "ଆକ୍ରମଣ"
    ],
    "family_matrimonial": [
        "divorce", "marriage", "custody", "child custody", "alimony", "husband", "wife", "separation",
        "mutual divorce", "talaq", "shaadi", "vivah", "matrimonial", "family court", "restitution",
        "तलाक", "विवाह", "शादी", "कस्टडी", "पति", "पत्नी", "अलग होना", "गुजारा", "पारिवारिक न्यायालय",
        "ଛାଡ଼ପତ୍ର", "ବିବାହ", "ସ୍ୱାମୀ", "ସ୍ତ୍ରୀ", "ସନ୍ତାନ ହେପାଜତ", "ପାରିବାରିକ ଅଦାଲତ"
    ],
    "domestic_violence": [
        "domestic violence", "pwdva", "abuse", "beating wife", "harassment by in-laws", "stridhan",
        "shelter", "protection order", "maintenance", "mahila", "dowry", "181", "one stop centre",
        "घरेलू हिंसा", "दहेज", "ससुराल", "मारपीट", "महिला प्रताड़ना", "निवास अधिकार", "181",
        "ଘରୋଇ ହିଂସା", "ଯୌତୁକ", "ମହିଳା ନିର୍ଯାତନା", "ବାସସ୍ଥାନ ଅଧିକାର", "୧୮୧"
    ],
    "land_property": [
        "land", "property", "patta", "ror", "encroach", "boundary", "mutation", "tehsildar", "tahasildar",
        "khatiyan", "khatian", "plot", "zamin", "jamin", "jameen", "kabja", "dakhil", "bhulekh", "demarcation",
        "जमीन", "भूमि", "पट्टा", "खतियान", "अतिक्रमण", "कब्जा", "नामांतरण", "तहसीलदार", "पटवारी", "मेढ़", "सीमांकन",
        "ଜମି", "ପଟ୍ଟା", "ଖତିୟାନ", "ବେଦଖଲ", "ସୀମା", "ତହସିଲ", "ମ୍ୟୁଟେସନ", "ଚାଷଜମି", "ଭୁଲେଖ"
    ],
    "property_succession": [
        "inheritance", "ancestral", "will", "vasiyat", "partition", "share", "daughter share", "coparcener",
        "legal heir", "succession", "property division", "father property", "grandfather",
        "पैतृक", "वसीयत", "बंटवारा", "उत्तराधिकार", "वारिस", "बेटी का हिस्सा", "संपत्ति विभाजन",
        "ପୈତୃକ ସମ୍ପତ୍ତି", "ଉଇଲ୍", "ବଣ୍ଟନ", "ଉତ୍ତରାଧିକାରୀ", "ଝିଅର ଭାଗ"
    ],
    "tenancy_realestate": [
        "tenant", "landlord", "rent", "eviction", "rera", "builder", "flat", "possession", "security deposit",
        "rent agreement", "kiraya", "makan malik", "kirayedar", "apartment",
        "किरायेदार", "मकान मालिक", "रेरा", "बिल्डर", "फ्लैट", "कब्जा", "सिक्योरिटी", "बेदखली",
        "ଭଡ଼ାଟିଆ", "ଘରମାଲିକ", "ରେରା", "ବିଲ୍ଡର", "ଫ୍ଲାଟ୍", "ଘରଭଡ଼ା"
    ],
    "labor_employment": [
        "salary", "wage", "wages", "contractor", "thekedar", "unpaid", "overtime", "factory", "worker", "labour",
        "labor", "e-shram", "shramik", "boss", "work", "majdoori", "majuri", "termination", "fired", "gratuity", "pf", "epfo", "posh",
        "मजदूरी", "वेतन", "ठेकेदार", "मालिक", "श्रमिक", "बकाया", "पगार", "कामगार", "श्रम", "ई-श्रम", "नौकरी से निकाला", "पीएफ",
        "ମଜୁରୀ", "ଦରମା", "କଣ୍ଟ୍ରାକ୍ଟର", "ଠିକାଦାର", "ଶ୍ରମିକ", "ବକେୟା", "ଇ-ଶ୍ରମ", "PF", "ଗ୍ରାଚ୍ୟୁଟି"
    ],
    "consumer_dispute": [
        "consumer", "defect", "defective", "warranty", "guarantee", "refund", "replace", "seed", "seeds",
        "fertilizer", "tractor", "machine", "shopkeeper", "dealer", "product", "purchase", "bill", "invoice", "e-daakhil", "insurance claim",
        "उपभोक्ता", "खराब", "वारंटी", "गारंटी", "दोषपूर्ण", "रिफंड", "बीज", "खाद", "ट्रैक्टर", "दुकानदार", "बिल", "बीमा दावा",
        "ଗ୍ରାହକ", "ଖରାପ", "ୱାରେଣ୍ଟି", "ଫେରସ୍ତ", "ନକଲି", "ବିହନ", "ଟ୍ରାକ୍ଟର", "ଦୋକାନୀ", "ମେସିନ", "ବିଲ୍"
    ],
    "banking_debt_cheque": [
        "cheque", "bounce", "dishonour", "sec 138", "loan", "recovery agent", "bank", "emi", "cibil", "debt",
        "overdue", "harassment", "drt", "sarfaesi", "default",
        "चेक", "बाउंस", "ऋण", "लोन", "रिकवरी एजेंट", "किस्त", "सिबिल", "बैंक नोटिस", "धारा 138",
        "ଚେକ୍", "ବାଉନ୍ସ", "ଋଣ", "ଲୋନ୍", "ବ୍ୟାଙ୍କ ନୋଟିସ୍", "CIBIL", "ଧାରା ୧୩୮"
    ],
    "cyber_fraud_privacy": [
        "cyber", "otp", "upi", "fraud", "phishing", "scam", "hacked", "phonepe", "gpay", "paytm",
        "debit", "withdrawal", "stolen", "1930", "link", "apk", "lottery", "blackmail", "deepfake", "photo leak", "loan app",
        "साइबर", "ओटीपी", "यूपीआई", "धोखाधड़ी", "बैंक", "खाता", "पैसे कट", "लिंक", "ठगी", "ब्लैकमेल", "1930",
        "ସାଇବର", "ଠକେଇ", "ଓଟିପି", "UPI", "ବ୍ୟାଙ୍କ", "ଟଙ୍କା", "କଟିଗଲା", "ପେଟିଏମ", "ଲିଙ୍କ", "ଠକାମି", "୧୯୩୦"
    ],
    "motor_accidents_traffic": [
        "accident", "mact", "vehicle", "car", "bike", "injury", "death", "compensation", "insurance", "challan",
        "traffic", "hit and run", "police report", "third party", "dar",
        "दुर्घटना", "सड़क हादसा", "मुआवजा", "गाड़ी", "चालान", "बीमा दावा", "एमएसीटी",
        "ଦୁର୍ଘଟଣା", "ଗାଡ଼ି", "କ୍ଷତିପୂରଣ", "ଇନସୁରାନ୍ସ", "ଚାଲାଣ", "MACT"
    ],
    "senior_citizen_welfare": [
        "senior citizen", "elderly", "parents", "maintenance of parents", "evict son", "old age", "pension",
        "father", "mother", "sdm tribunal", "care", "gift deed cancel",
        "वरिष्ठ नागरिक", "माता-पिता", "बुजुर्ग", "भरण पोषण", "बेटा घर से निकालना", "पेंशन", "एसडीएम",
        "ବରିଷ୍ଠ ନାଗରିକ", "ପିତାମାତା", "ବୃଦ୍ଧ", "ଭରଣପୋଷଣ", "ପୁଅକୁ ଘରୁ ବାହାର କରିବା"
    ],
    "child_pocso_education": [
        "child", "pocso", "minor", "abuse", "molestation", "cwc", "1098", "rte", "school admission",
        "child labour", "orphan", "juvenile",
        "बच्चा", "पॉक्सो", "नाबालिग", "बाल श्रम", "स्कूल दाखिला", "आरटीई", "1098",
        "ଶିଶୁ", "ପକ୍ସୋ", "ନାବାଳକ", "ଶିଶୁ ଶ୍ରମିକ", "ମାଗଣା ଶିକ୍ଷା", "RTE", "୧୦୯୮"
    ],
    "constitutional_rti_grievance": [
        "rti", "information", "right to information", "pio", "appeal", "certificate delay", "caste certificate",
        "public grievance", "pollution", "garbage", "nuisance", "collector", "samadhan", "jan sunwai", "writ",
        "आरटीआई", "सूचना का अधिकार", "अपील", "जाति प्रमाण पत्र", "जन शिकायत", "प्रदूषण", "कलेक्टर",
        "RTI", "ସୂଚନା ଅଧିକାର", "ଜାତି ପ୍ରମାଣପତ୍ର", "ଜନ ଅଭିଯୋଗ", "ଜିଲ୍ଲାପାଳ"
    ],
    "business_msme_tax": [
        "business", "msme", "samadhaan", "delayed payment", "buyer", "supplier", "contract", "breach", "gst",
        "invoice unpaid", "tax", "trademark",
        "व्यापार", "एमएसएमई", "बकाया बिल", "अनुबंध", "जीएसटी", "टैक्स",
        "ବ୍ୟବସାୟ", "MSME", "ଚୁକ୍ତିପତ୍ର", "GST", "ବକେୟା ବିଲ୍"
    ]
}

def classify_query(text: str, lang: str = "en") -> Dict[str, Any]:
    text_lower = text.lower()
    
    scores = {}
    for cat, keywords in KEYWORD_MAP.items():
        score = 0
        for kw in keywords:
            if kw in text_lower:
                score += 1
        scores[cat] = score

    best_category = max(scores, key=scores.get)
    best_score = scores[best_category]

    if best_score == 0:
        # Intelligently infer or use Universal Assistant
        best_category = "universal_legal_assistant"
        confidence = 0.85
    else:
        confidence = min(0.98, 0.78 + (best_score * 0.06))

    meta = CATEGORIES_META.get(best_category, CATEGORIES_META["universal_legal_assistant"])

    title = meta.get(lang, meta["en"])
    urgency = meta["urgency"]

    steps = {
        "criminal_police": [
            {"step": 1, "en": "Draft written complaint mentioning date, location, accused details & Sec 173 BNSS", "hi": "दिनांक, समय, स्थान एवं आरोपियों के विवरण सहित धारा 173 बीएनएसएस के तहत लिखित शिकायत दें", "od": "ତାରିଖ, ସ୍ଥାନ ଓ ଅଭିଯୁକ୍ତଙ୍କ ବିବରଣୀ ସହ BNSS ୧୭୩ ଅନୁସାରେ ଲିଖିତ ଏଫଆଇଆର ଦିଅନ୍ତୁ"},
            {"step": 2, "en": "Demanded signed stamped copy of FIR free of cost from Police Station In-charge", "hi": "थाना प्रभारी से बिना शुल्क हस्ताक्षरित एफआईआर की प्रति प्राप्त करें", "od": "ଥାନା ଅଧିକାରୀଙ୍କଠାରୁ ଦସ୍ତଖତ ଥିବା ମାଗଣା ଏଫଆଇଆର ନକଲ ସଂଗ୍ରହ କରନ୍ତୁ"},
            {"step": 3, "en": "If police refuses, send complaint to SP via registered post & apply before Magistrate under BNSS 175(3)", "hi": "इनकार पर पुलिस अधीक्षक (SP) को डाक भेजें और मजिस्ट्रेट के समक्ष धारा 175(3) में अर्जी दें", "od": "ମନା କଲେ ଏସପି (SP) ଙ୍କୁ ପଠାନ୍ତୁ ଏବଂ ମାଜିଷ୍ଟ୍ରେଟଙ୍କ ନିକଟରେ BNSS ୧୭୫(୩) ଆବେଦନ କରନ୍ତୁ"}
        ],
        "family_matrimonial": [
            {"step": 1, "en": "Gather marriage certificate, wedding photos, and income proof affidavits", "hi": "विवाह प्रमाण पत्र, विवाह फोटो और आय प्रमाण पत्र तैयार करें", "od": "ବିବାହ ପ୍ରମାଣପତ୍ର, ଫଟୋ ଓ ଆୟ ଘୋଷଣାନାମା ଏକତ୍ରିତ କରନ୍ତୁ"},
            {"step": 2, "en": "Opt for Family Court Pre-Litigation Mediation for amicable settlement", "hi": "पारस्परिक सुलह हेतु पारिवारिक अदालत के मध्यस्थता केंद्र में आवेदन करें", "od": "ଆପୋଷ ବୁଝାମଣା ପାଇଁ ପାରିବାରିକ ଅଦାଲତ ମଧ୍ୟସ୍ଥତା କେନ୍ଦ୍ରରେ ଆବେଦନ କରନ୍ତୁ"},
            {"step": 3, "en": "Apply for Sec 144 BNSS / Section 125 interim maintenance for sustenance", "hi": "खर्चे व बाल भरण-पोषण के लिए धारा 144 बीएनएसएस में अंतरिम गुजारा भत्ता मांगें", "od": "ଖର୍ଚ୍ଚ ଓ ପିଲାଙ୍କ ପାଇଁ BNSS ୧୪୪ ଅନୁଯାୟୀ ମାସିକ ଭରଣପୋଷଣ ଦାବି କରନ୍ତୁ"}
        ],
        "domestic_violence": [
            {"step": 1, "en": "Dial 181 / 112 immediately if under threat; connect to shelter home", "hi": "खतरे की स्थिति में तत्काल 181 या 112 मिलाएं; सुरक्षित आश्रय लें", "od": "ଜରୁରୀକାଳୀନ ପରିସ୍ଥିତିରେ ୧୮୧ ବା ୧୧୨ କୁ କଲ୍ କରନ୍ତୁ"},
            {"step": 2, "en": "Reach nearest Protection Officer to record Domestic Incident Report (DIR Form 1)", "hi": "महिला संरक्षण अधिकारी से मिलकर घटना रिपोर्ट (DIR Form 1) भरवाएं", "od": "ମହିଳା ସୁରକ୍ଷା ଅଧିକାରୀଙ୍କୁ ଭେଟି DIR ରିପୋର୍ଟ ଲେଖାନ୍ତୁ"},
            {"step": 3, "en": "Obtain free DLSA legal aid advocate for residence & protection order under Sec 18", "hi": "मुफ्त सरकारी वकील से घर में रहने का अधिकार व सुरक्षा आदेश पाएं", "od": "ମାଗଣା ସରକାରୀ ଓକିଲଙ୍କ ସହାୟତାରେ ବାସସ୍ଥାନ ଓ ସୁରକ୍ଷା ଆଦେଶ ପାଆନ୍ତୁ"}
        ],
        "land_property": [
            {"step": 1, "en": "Extract certified RoR Patta from Bhulekh portal or Tahasil kiosk", "hi": "तहसील या भूलेख पोर्टल से प्रमाणित खतियान निकालें", "od": "ଭୁଲେଖ ପୋର୍ଟାଲ ବା ତହସିଲରୁ ପଟ୍ଟାର ସତ୍ୟାପିତ ନକଲ ଆଣନ୍ତୁ"},
            {"step": 2, "en": "Submit Form 10 demarcation application with ₹100 government fee", "hi": "₹100 सरकारी शुल्क के साथ सीमांकन फॉर्म 10 जमा करें", "od": "₹୧୦୦ ସରକାରୀ ଫି ସହ ସୀମାଙ୍କନ ଆବେଦନ ଫର୍ମ ୧୦ ଦାଖଲ କରନ୍ତୁ"},
            {"step": 3, "en": "Seek amicable Lok Adalat settlement before Taluk Legal Services", "hi": "तालुक विधिक सेवा समिति में निःशुल्क लोक अदालत मध्यस्थता मांगें", "od": "ତାଲୁକ ଆଇନ ସେବା କମିଟିରେ ମାଗଣା ଲୋକ ଅଦାଲତ ପରାମର୍ଶ ଲୋଡ଼ନ୍ତୁ"}
        ],
        "property_succession": [
            {"step": 1, "en": "Obtain Family Tree / Legal Heir Certificate from Tahasildar", "hi": "तहसीलदार कार्यालय से प्रमाणित पारिवारिक वंशावली / कानूनी वारिस प्रमाण पत्र लें", "od": "ତହସିଲଦାରଙ୍କଠାରୁ ବଂଶାବଳୀ / ଆଇନଗତ ଉତ୍ତରାଧିକାରୀ ପ୍ରମାଣପତ୍ର ଆଣନ୍ତୁ"},
            {"step": 2, "en": "Under Hindu Succession Act Sec 6, daughters have equal birthright in ancestral coparcenary", "hi": "हिंदू उत्तराधिकार अधिनियम धारा 6 अनुसार बेटियों का बेटों के बराबर जन्मसिद्ध हक है", "od": "ହିନ୍ଦୁ ଉତ୍ତରାଧିକାର ଆଇନ ଧାରା ୬ ଅନୁସାରେ ଝିଅମାନଙ୍କର ପୁଅଙ୍କ ସହ ସମାନ ଅଧିକାର ଅଛି"},
            {"step": 3, "en": "File partition petition before Revenue Court or Civil Judge Senior Division", "hi": "सिविल जज या राजस्व न्यायालय में संपत्ति बंटवारा वाद दायर करें", "od": "ଦେୱାନୀ ଅଦାଲତରେ ସମ୍ପତ୍ତି ଭାଗବଣ୍ଟା ମୋକଦ୍ଦମା ଦାୟର କରନ୍ତୁ"}
        ],
        "tenancy_realestate": [
            {"step": 1, "en": "Compile Builder Buyer Agreement, payment receipts & communication logs", "hi": "बिल्डर खरीदार समझौता, भुगतान रसीदें एवं पत्राचार रिकॉर्ड तैयार करें", "od": "ବିଲ୍ଡର ଚୁକ୍ତିପତ୍ର, ଟଙ୍କା ପୈଠ ରସିଦ ଓ ମେସେଜ୍ ସଂଗ୍ରହ କରନ୍ତୁ"},
            {"step": 2, "en": "File formal complaint on State RERA portal claiming delivery or refund with interest", "hi": "राज्य रेरा (RERA) पोर्टल पर ब्याज सहित रिफंड का ऑनलाइन दावा करें", "od": "ରାଜ୍ୟ ରେରା (RERA) ପୋର୍ଟାଲରେ ସୁଧ ସହ ଟଙ୍କା ଫେରସ୍ତ ଆବେଦନ କରନ୍ତୁ"},
            {"step": 3, "en": "If tenancy dispute, approach local Rent Authority; landlord cannot disconnect basic amenities", "hi": "किरायेदारी विवाद में किराया प्राधिकरण जाएं; बिजली-पानी काटना अवैध है", "od": "ଭଡ଼ା ନିୟନ୍ତ୍ରକଙ୍କୁ ଜଣାନ୍ତୁ; ବିଜୁଳି ବା ପାଣି କାଟିବା ବେଆଇନ"}
        ],
        "labor_employment": [
            {"step": 1, "en": "Issue wage demand notice to contractor via WhatsApp/SMS record", "hi": "ठेकेदार को व्हाट्सएप/एसएमएस द्वारा बकाया भुगतान का संदेश दें", "od": "ଠିକାଦାରଙ୍କୁ ମଜୁରୀ ପାଇଁ ଲିଖିତ/ମେସେଜ୍ ସୂଚନା ଦିଅନ୍ତୁ"},
            {"step": 2, "en": "Collect fellow workers' witness signatures or attendance photos", "hi": "साथी श्रमिकों के हस्ताक्षर व हाजिरी के फोटो एकत्रित करें", "od": "ସାଥୀ ଶ୍ରମିକଙ୍କ ଦସ୍ତଖତ ବା କାମ ଡାଏରୀର ଫଟୋ ସଂଗ୍ରହ କରନ୍ତୁ"},
            {"step": 3, "en": "File Form VI before Assistant Labour Commissioner (ALC)", "hi": "सहायक श्रम आयुक्त के समक्ष प्रपत्र-VI शिकायत दर्ज करें", "od": "ସହକାରୀ ଶ୍ରମ କମିଶନରଙ୍କ ନିକଟରେ ଫର୍ମ-VI ଅଭିଯୋଗ ଦାୟର କରନ୍ତୁ"}
        ],
        "consumer_dispute": [
            {"step": 1, "en": "Call National Consumer Helpline 1915 to lodge official docket", "hi": "राष्ट्रीय उपभोक्ता हेल्पलाइन 1915 पर शिकायत संख्या दर्ज कराएं", "od": "ଜାତୀୟ ଗ୍ରାହକ ହେଲ୍ପଲାଇନ୍ ୧୯୧୫ ରେ ଡକେଟ ନମ୍ବର ପଞ୍ଜୀକରଣ କରନ୍ତୁ"},
            {"step": 2, "en": "Deliver 15-day formal rectification notice to the seller/dealer", "hi": "विक्रेता को 15 दिनों का कानूनी सुधार नोटिस भेजें", "od": "ଦୋକାନୀ ବା କମ୍ପାନୀକୁ ୧୫ ଦିନର ସମାଧାନ ନୋଟିସ୍ ପଠାନ୍ତୁ"},
            {"step": 3, "en": "Submit electronic claim on e-Daakhil.nic.in without lawyer fee", "hi": "बिना वकील खर्च e-Daakhil पोर्टल पर क्षतिपूर्ति दावा भरें", "od": "ଇ-ଦାଖିଲ ପୋର୍ଟାଲରେ ବିନା ଓକିଲରେ କ୍ଷତିପୂରଣ ଆବେଦନ କରନ୍ତୁ"}
        ],
        "banking_debt_cheque": [
            {"step": 1, "en": "Send statutory legal notice within 30 days of cheque return memo (Sec 138 NI Act)", "hi": "चेक रिटर्न मेमो मिलने के 30 दिनों के भीतर वैधानिक विधिक नोटिस भेजें", "od": "ଚେକ୍ ଫେରିବାର ୩୦ ଦିନ ମଧ୍ୟରେ ଧାରା ୧୩୮ ଆଇନଗତ ନୋଟିସ୍ ପଠାନ୍ତୁ"},
            {"step": 2, "en": "Give 15 days cure period; file criminal complaint before JMFC if unpaid within 30 days", "hi": "भुगतान हेतु 15 दिन दें; न मिलने पर 30 दिन में अदालत में परिवाद दायर करें", "od": "୧୫ ଦିନ ସମୟ ଦିଅନ୍ତୁ; ନଦେଲେ ମାଜିଷ୍ଟ୍ରେଟ ଅଦାଲତରେ ମୋକଦ୍ଦମା ଦାୟର କରନ୍ତୁ"},
            {"step": 3, "en": "If harassed by recovery agents, lodge complaint with Banking Ombudsman under RBI Fair Practices", "hi": "रिकवरी एजेंट प्रताड़ित करें तो आरबीआई बैंकिंग लोकपाल में शिकायत करें", "od": "ଋଣ ଏଜେଣ୍ଟ ଧମକ ଦେଲେ RBI ବ୍ୟାଙ୍କିଙ୍ଗ ଓମ୍ବୁଡସମ୍ୟାନଙ୍କ ନିକଟରେ ଅଭିଯୋଗ କରନ୍ତୁ"}
        ],
        "cyber_fraud_privacy": [
            {"step": 1, "en": "Immediately dial 1930 to freeze recipient bank accounts (Golden Hour)", "hi": "गोल्डन ऑवर में 1930 पर कॉल कर आरोपी का बैंक खाता तुरंत फ्रीज कराएं", "od": "ଗୋଲ୍ଡେନ ଆୱାର ଭିତରେ ୧୯୩୦ ରେ କଲ୍ କରି ଟଙ୍କା ଫ୍ରିଜ୍ କରାନ୍ତୁ"},
            {"step": 2, "en": "Block ATM/UPI and get stamped bank statement with UTR reference", "hi": "एटीएम/यूपीआई ब्लॉक कर बैंक से यूटीआर ट्रांजेक्शन पर्ची लें", "od": "ବ୍ୟାଙ୍କରୁ ଟ୍ରାଞ୍ଜାକସନ ୟୁଟିଆର (UTR) ବିବରଣୀ ସଂଗ୍ରହ କରନ୍ତୁ"},
            {"step": 3, "en": "Submit BNSS Sec 457 recovery petition before local Magistrate", "hi": "स्थानीय अदालत में धारा 457 बीएनएसएस के तहत धन वापसी अर्जी दें", "od": "ମାଜିଷ୍ଟ୍ରେଟ କୋର୍ଟରେ BNSS ୪୫୭ ଅନୁସାରେ ଟଙ୍କା ଫେରସ୍ତ ଆବେଦନ କରନ୍ତୁ"}
        ],
        "motor_accidents_traffic": [
            {"step": 1, "en": "Ensure Police records Detailed Accident Report (DAR) and Form 54", "hi": "पुलिस द्वारा विस्तृत दुर्घटना रिपोर्ट (DAR) एवं फॉर्म 54 दर्ज करवाएं", "od": "ପୋଲିସ ଦ୍ୱାରା ଦୁର୍ଘଟଣା ରିପୋର୍ଟ (DAR) ପଞ୍ଜୀକରଣ ନିଶ୍ଚିତ କରନ୍ତୁ"},
            {"step": 2, "en": "Collect hospital injury discharge summary and disability certificate", "hi": "अस्पताल मेडिकल डिस्चार्ज पर्ची एवं विकलांगता प्रमाण पत्र सुरक्षित रखें", "od": "ଡାକ୍ତରଖାନା ଚିକିତ୍ସା କାଗଜପତ୍ର ଓ ମେଡିକାଲ ବିଲ୍ ସଂଗ୍ରହ କରନ୍ତୁ"},
            {"step": 3, "en": "File claim petition before MACT Tribunal; insurer must deposit interim relief", "hi": "एमएसीटी ट्रिब्यूनल में दावा याचिका दायर करें; बीमा कंपनी मुआवजा देगी", "od": "MACT ଟ୍ରିବ୍ୟୁନାଲରେ କ୍ଷତିପୂରଣ ଆବେଦନ କରନ୍ତୁ; ବୀମା କମ୍ପାନୀ ଟଙ୍କା ଦେବ"}
        ],
        "senior_citizen_welfare": [
            {"step": 1, "en": "Approach Sub-Divisional Magistrate (SDM) Senior Citizen Maintenance Tribunal", "hi": "उप-मंडल मजिस्ट्रेट (एसडीएम) वरिष्ठ नागरिक भरण-पोषण ट्रिब्यूनल में अर्जी दें", "od": "ଉପ-ଜିଲ୍ଲାପାଳ (SDM) ବରିଷ୍ଠ ନାଗରିକ ଟ୍ରିବ୍ୟୁନାଲରେ ଆବେଦନ କରନ୍ତୁ"},
            {"step": 2, "en": "Tribunal has statutory power to order up to ₹10,000/month sustenance from adult children", "hi": "ट्रिब्यूनल संतानों को मासिक भरण-पोषण देने का अनिवार्य आदेश देगा", "od": "ଟ୍ରିବ୍ୟୁନାଲ ପିଲାମାନଙ୍କୁ ମାସିକ ଖର୍ଚ୍ଚ ଦେବାକୁ ବାଧ୍ୟତାମୂଳକ ନିର୍ଦ୍ଦେଶ ଦେବେ"},
            {"step": 3, "en": "If child abuses parent, Tribunal can summarily evict abusive child within 90 days", "hi": "यदि संतान प्रताड़ित करे तो 90 दिनों में उसे घर से बेदखल करने का अधिकार है", "od": "ଅତ୍ୟାଚାର କଲେ ୯୦ ଦିନ ଭିତରେ ପିଲାଙ୍କୁ ଘରୁ ବାହାର କରିବାର ନିର୍ଦ୍ଦେଶ ମିଳିବ"}
        ],
        "child_pocso_education": [
            {"step": 1, "en": "Dial 1098 (Childline) or 112 immediately for emergency child protection", "hi": "आपातकालीन बाल संरक्षण के लिए तत्काल 1098 या 112 डायल करें", "od": "ତୁରନ୍ତ ୧୦୯୮ (ଚାଇଲ୍ଡଲାଇନ୍) କିମ୍ବା ୧୧୨ ଡାୟାଲ୍ କରନ୍ତୁ"},
            {"step": 2, "en": "Child statement recorded in-camera by woman police officer without uniform", "hi": "महिला पुलिस अधिकारी द्वारा सादे कपड़ों में बंद कमरे में बयान दर्ज किया जाता है", "od": "ମହିଳା ପୋଲିସଙ୍କ ଦ୍ୱାରା ସାଦା ପୋଷାକରେ ଗୋପନୀୟ ବୟାନ ରେକର୍ଡ ହୁଏ"},
            {"step": 3, "en": "Free medical care, counseling & legal defense provided by Child Welfare Committee", "hi": "बाल कल्याण समिति द्वारा मुफ्त चिकित्सा, परामर्श व कानूनी सहायता मिलती है", "od": "ଶିଶୁ କଲ୍ୟାଣ କମିଟି ଦ୍ୱାରା ମାଗଣା ଚିକିତ୍ସା ଓ ସୁରକ୍ଷା ଯୋଗାଇ ଦିଆଯାଏ"}
        ],
        "constitutional_rti_grievance": [
            {"step": 1, "en": "Submit Form A RTI application with ₹10 fee to Public Information Officer (PIO)", "hi": "जन सूचना अधिकारी (PIO) को ₹10 शुल्क के साथ प्रपत्र-A आरटीआई जमा करें", "od": "ଜନ ସୂଚନା ଅଧିକାରୀ (PIO) ଙ୍କୁ ₹୧୦ ଫି ସହ RTI ଫର୍ମ ଦାଖଲ କରନ୍ତୁ"},
            {"step": 2, "en": "If no reply within 30 days, file First Appeal before Departmental Appellate Authority", "hi": "30 दिनों में उत्तर न मिलने पर प्रथम अपीलीय अधिकारी के समक्ष अपील करें", "od": "୩୦ ଦିନରେ ଉତ୍ତର ନମିଳିଲେ ପ୍ରଥମ ଅପିଲ୍ ଅଧିକାରୀଙ୍କ ନିକଟରେ ଅପିଲ୍ କରନ୍ତୁ"},
            {"step": 3, "en": "File Second Appeal before State Information Commission; PIO liable for ₹250/day penalty", "hi": "राज्य सूचना आयोग में द्वितीय अपील करें; अधिकारी पर ₹250/दिन जुर्माना लगेगा", "od": "ରାଜ୍ୟ ସୂଚନା କମିଶନଙ୍କ ନିକଟରେ ଅପିଲ୍ କରନ୍ତୁ; ଦୈନିକ ₹୨୫୦ ଜୋରିମାନା ହେବ"}
        ],
        "business_msme_tax": [
            {"step": 1, "en": "Issue formal invoice demand giving 15 days under MSMED Act 2006", "hi": "एमएसएमई अधिनियम 2006 के तहत 15 दिनों का औपचारिक भुगतान नोटिस भेजें", "od": "MSMED ଆଇନ ୨୦୦୬ ଅନୁସାରେ ୧୫ ଦିନର ବକେୟା ନୋଟିସ୍ ପଠାନ୍ତୁ"},
            {"step": 2, "en": "File petition online on MSME Samadhaan portal (samadhaan.msme.gov.in)", "hi": "एमएसएमई समाधान पोर्टल पर ऑनलाइन दावा दर्ज करें", "od": "MSME ସମାଧାନ ପୋର୍ଟାଲରେ ଅନଲାଇନ ଆବେଦନ କରନ୍ତୁ"},
            {"step": 3, "en": "Buyer is statutorily liable to pay compound interest at 3x RBI bank rate", "hi": "खरीदार आरबीआई बैंक दर के तीन गुना चक्रवृद्धि ब्याज देने के लिए बाध्य है", "od": "କ୍ରେତା RBI ସୁଧ ହାରର ୩ ଗୁଣ ଚକ୍ରବୃଦ୍ଧି ସୁଧ ଦେବାକୁ ବାଧ୍ୟ"}
        ],
        "universal_legal_assistant": [
            {"step": 1, "en": "Preserve all written notices, communications, receipts, and identity documents", "hi": "सभी लिखित नोटिस, रसीदें, संदेश और पहचान प्रमाण पत्र सुरक्षित रखें", "od": "ସମସ୍ତ ଲିଖିତ କାଗଜପତ୍ର, ରସିଦ ଓ ପରିଚୟପତ୍ର ସୁରକ୍ଷିତ ରଖନ୍ତୁ"},
            {"step": 2, "en": "Approach nearest District Legal Services Authority (DLSA) desk for free lawyer evaluation", "hi": "मुफ्त वकील पात्रता जांच हेतु निकटतम जिला विधिक सेवा प्राधिकरण (DLSA) जाएं", "od": "ମାଗଣା ଓକିଲ ସହାୟତା ପାଇଁ ନିକଟସ୍ଥ ଜିଲ୍ଲା ଆଇନ ସେବା କେନ୍ଦ୍ର (DLSA) କୁ ଯାଆନ୍ତୁ"},
            {"step": 3, "en": "Seek pre-litigation conciliation via Taluk Legal Services to resolve matter without fees", "hi": "बिना अदालती खर्च मामले के शांतिपूर्ण समाधान हेतु तालुक लोक अदालत में जाएं", "od": "ବିନା କୋର୍ଟ ଖର୍ଚ୍ଚରେ ସମାଧାନ ପାଇଁ ତାଲୁକ ଲୋକ ଅଦାଲତର ସାହାଯ୍ୟ ନିଅନ୍ତୁ"}
        ]
    }

    return {
        "category": best_category,
        "title": title,
        "category_titles": {
            "en": meta["en"],
            "hi": meta["hi"],
            "od": meta["od"]
        },
        "confidence": confidence,
        "urgency": urgency,
        "default_law": meta["default_law"],
        "forum": meta["forum"],
        "cost": meta["cost"],
        "clarification_questions": meta["questions"],
        "recommended_steps": steps.get(best_category, steps["universal_legal_assistant"]),
        "rights_summary": {
            "en": f"Under Indian law ({meta['default_law']}), citizens have statutory rights to seek redressal at {meta['forum']}. Free legal representation is guaranteed for eligible persons under the Legal Services Authorities Act.",
            "hi": f"भारतीय कानून ({meta['default_law']}) के तहत नागरिकों को {meta['forum']} में त्वरित न्याय का वैधानिक अधिकार प्राप्त है। विधिक सेवा प्राधिकरण अधिनियम के अंतर्गत पात्र नागरिकों को पूरी तरह निःशुल्क वकील मिलता है।",
            "od": f"ଭାରତୀୟ ଆଇନ ({meta['default_law']}) ଅନୁସାରେ ନାଗରିକଙ୍କୁ {meta['forum']} ରେ ନ୍ୟାୟ ପାଇବାର ଅଧିକାର ଅଛି। ନାଲସା ଅଧୀନରେ ଯୋଗ୍ୟ ବ୍ୟକ୍ତିଙ୍କୁ ସମ୍ପୂର୍ଣ୍ଣ ମାଗଣାରେ ଓକିଲ ପ୍ରଦାନ କରାଯାଏ।"
        }
    }

def refine_legal_path(category: str, answers: Dict[str, str], lang: str = "en") -> Dict[str, Any]:
    meta = CATEGORIES_META.get(category, CATEGORIES_META["universal_legal_assistant"])
    
    advice_en = "Based on your inputs, your matter is eligible for fast-track dispute settlement. You can file directly without hiring private intermediaries."
    advice_hi = "आपके उत्तरों के आधार पर आपका मामला त्वरित निपटारे के योग्य है। बिना किसी निजी बिचौलिए के सीधे आवेदन किया जा सकता है।"
    advice_od = "ଆପଣଙ୍କ ଉତ୍ତର ଅନୁସାରେ ଏହି ମାମଲା ଶୀଘ୍ର ସମାଧାନ ହୋଇପାରିବ। ବିନା କୌଣସି ଦଲାଲରେ ଆପଣ ନିଜେ ଆବେଦନ କରିପାରିବେ।"

    if category == "cyber_fraud_privacy" and answers.get("q1") == "financial_under_2h":
        advice_en = "CRITICAL ALERT: You are within the 2-Hour Golden Window! Nodal cyber officers can immediately freeze the funds in the receiver wallet. Dial 1930 right now."
        advice_hi = "अति महत्वपूर्ण: आप 2 घंटे के गोल्डन विंडो में हैं! तुरंत 1930 पर कॉल करें जिससे आरोपी का खाता फ्रीज हो सके।"
        advice_od = "ଅତ୍ୟନ୍ତ ଜରୁରୀ: ଆପଣ ୨ ଘଣ୍ଟାର ଗୋଲ୍ଡେନ ସମୟ ଭିତରେ ଅଛନ୍ତି! ତୁରନ୍ତ ୧୯୩୦ କୁ କଲ୍ କରି ଟଙ୍କା ଫ୍ରିଜ୍ କରାନ୍ତୁ।"
    elif category == "domestic_violence" and answers.get("q1") == "immediate_danger":
        advice_en = "EMERGENCY SAFETY PROTOCOL: Your safety is the highest priority. Dial 112 or 181 immediately. You are entitled to immediate state shelter and police protection."
        advice_hi = "आपातकालीन सुरक्षा: आपकी सुरक्षा सर्वोच्च प्राथमिकता है। तुरंत 112 या 181 पर कॉल करें। आपको तत्काल सरकारी आश्रय व पुलिस सुरक्षा का अधिकार है।"
        advice_od = "ଜରୁରୀକାଳୀନ ସୁରକ୍ଷା: ଆପଣଙ୍କ ସୁରକ୍ଷା ସବୁଠାରୁ ଗୁରୁତ୍ୱପୂର୍ଣ୍ଣ। ତୁରନ୍ତ ୧୧୨ କିମ୍ବା ୧୮୧ କଲ୍ କରନ୍ତୁ। ସରକାରୀ ଆଶ୍ରୟ ଓ ସୁରକ୍ଷା ଆପଣଙ୍କ ଅଧିକାର।"
    elif category == "criminal_police" and answers.get("q1") == "refused":
        advice_en = "POLICE INACTION REMEDY: Under Section 175(3) of BNSS 2023, you can send the complaint directly to the District Superintendent of Police (SP) by registered post, or file an application before the Judicial Magistrate to order an investigation."
        advice_hi = "पुलिस इनकार पर कानूनी उपाय: बीएनएसएस 2023 की धारा 175(3) के तहत पुलिस अधीक्षक (SP) को पंजीकृत डाक से शिकायत भेजें या मजिस्ट्रेट के समक्ष जांच आदेश हेतु अर्जी दें।"
        advice_od = "ପୋଲିସ ମନା କଲେ ଉପାୟ: BNSS ୧୭୫(୩) ଅନୁଯାୟୀ ଏସପି (SP) ଙ୍କୁ ଡାକ ଯୋଗେ ପଠାନ୍ତୁ କିମ୍ବା ମାଜିଷ୍ଟ୍ରେଟ କୋର୍ଟରେ ତଦନ୍ତ ଆଦେଶ ପାଇଁ ଆବେଦନ କରନ୍ତୁ।"
    elif category == "senior_citizen_welfare":
        advice_en = "SENIOR CITIZEN PROTECTION: The SDM Maintenance Tribunal has statutory powers under the 2007 Act to evict abusive children and order monthly maintenance within 90 days. No advocate is mandatory."
        advice_hi = "वरिष्ठ नागरिक सुरक्षा: 2007 कानून के तहत एसडीएम ट्रिब्यूनल को 90 दिनों में प्रताड़ित करने वाले बच्चों को घर से बेदखल करने और भरण-पोषण दिलाने का पूरा अधिकार है।"
        advice_od = "ବରିଷ୍ଠ ନାଗରିକ ସୁରକ୍ଷା: ୨୦୦୭ ଆଇନ ଅନୁସାରେ SDM ଟ୍ରିବ୍ୟୁନାଲ ୯୦ ଦିନ ଭିତରେ ଅତ୍ୟାଚାରୀ ପିଲାଙ୍କୁ ଘରୁ ବାହାର କରିବା ଓ ମାସିକ ଖର୍ଚ୍ଚ ଦେବାର ନିର୍ଦ୍ଦେଶ ଦେଇପାରିବେ।"

    return {
        "category": category,
        "status": "ANALYZED",
        "custom_advice": {
            "en": advice_en,
            "hi": advice_hi,
            "od": advice_od
        },
        "next_action": "Proceed to Legal Journey Map or Print Kiosk Action Slip."
    }
