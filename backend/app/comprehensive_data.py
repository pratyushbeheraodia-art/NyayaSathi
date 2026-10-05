from typing import Dict, Any, List

ALL_JOURNEYS: Dict[str, Any] = {
    "criminal_police": {
        "title_en": "Criminal FIR, Police Procedure & Bail Roadmap",
        "title_hi": "आपराधिक प्राथमिकी (FIR), पुलिस प्रक्रिया एवं जमानत यात्रा",
        "title_od": "ଅପରାଧିକ ଏଫଆଇଆର, ପୋଲିସ ପ୍ରକ୍ରିୟା ଓ ଜାମିନ ପଥ",
        "total_estimated_days": "1 - 30 Days",
        "stages": [
            {
                "step": 1,
                "title_en": "FIR Registration & Zero FIR (Sec 173 BNSS)",
                "title_hi": "प्राथमिकी (FIR) पंजीकरण एवं जीरो एफआईआर",
                "title_od": "ଏଫଆଇଆର ପଞ୍ଜୀକରଣ ଓ ଜିରୋ ଏଫଆଇଆର",
                "status": "IN_PROGRESS",
                "authority": "Police Station In-Charge (SHO)",
                "details": "Police are statutorily required to register an FIR for cognizable crimes regardless of jurisdiction.",
                "citizen_rights": "Right to receive a signed, stamped copy of the FIR immediately free of cost."
            },
            {
                "step": 2,
                "title_en": "Arrest Safeguards & 24-Hour Magistrate Rule",
                "title_hi": "गिरफ्तारी सुरक्षा नियम एवं 24 घंटे का अधिकार",
                "title_od": "ଗିରଫ ସୁରକ୍ଷା ନିୟମ ଓ ୨୪ ଘଣ୍ଟା ମଧ୍ୟରେ କୋର୍ଟ ହାଜର",
                "status": "UPCOMING",
                "authority": "Arresting Officer & Investigating Officer (IO)",
                "details": "Police must inform grounds of arrest, notify family, and conduct medical checkup.",
                "citizen_rights": "Under Article 22(2) & Sec 58 BNSS, arrested person must be produced before Magistrate within 24 hours."
            },
            {
                "step": 3,
                "title_en": "Bail Application / Anticipatory Bail (Sec 480/482 BNSS)",
                "title_hi": "जमानत याचिका / अग्रिम जमानत",
                "title_od": "ଜାମିନ ଆବେଦନ କିମ୍ବା ଅଗ୍ରୀମ ଜାମିନ",
                "status": "UPCOMING",
                "authority": "Judicial Magistrate / Sessions Court / High Court",
                "details": "Filing bail petition demonstrating roots in society and lack of flight risk.",
                "citizen_rights": "Bail is a statutory right for bailable offenses under Sec 478 BNSS."
            },
            {
                "step": 4,
                "title_en": "Investigation, Charge Sheet & Trial Discharge",
                "title_hi": "जांच, आरोप पत्र (चार्जशीट) एवं ट्रायल",
                "title_od": "ପୋଲିସ ତଦନ୍ତ, ଚାର୍ଜସିଟ୍ ଓ ମୋକଦ୍ଦମା ବିଚାର",
                "status": "UPCOMING",
                "authority": "Trial Court Magistrate / Sessions Judge",
                "details": "Police must file Final Report within 60-90 days; applicant can seek discharge if no prima facie evidence.",
                "citizen_rights": "Right to default statutory bail (Sec 187 BNSS) if charge sheet is delayed."
            }
        ]
    },
    "family_matrimonial": {
        "title_en": "Family Dispute, Mutual Divorce & Custody Path",
        "title_hi": "पारिवारिक विवाद, आपसी सहमति तलाक एवं कस्टडी यात्रा",
        "title_od": "ପାରିବାରିକ ବିବାଦ, ଛାଡ଼ପତ୍ର ଓ ସନ୍ତାନ ହେପାଜତ ପଥ",
        "total_estimated_days": "30 - 180 Days",
        "stages": [
            {
                "step": 1,
                "title_en": "Pre-Litigation Counseling & Settlement",
                "title_hi": "मुकदमे से पूर्व काउंसलिंग एवं आपसी समझौता",
                "title_od": "ମୋକଦ୍ଦମା ପୂର୍ବ କାଉନସେଲିଂ ଓ ଆପୋଷ ବୁଝାମଣା",
                "status": "COMPLETED",
                "authority": "Family Court Mediation Centre",
                "details": "Trained mediator assists parties in reaching an amicable Memorandum of Understanding (MoU).",
                "citizen_rights": "Confidential proceedings; statements in mediation cannot be used against you."
            },
            {
                "step": 2,
                "title_en": "Filing Petition (Sec 13B Mutual / Contested)",
                "title_hi": "याचिका दायर करना (धारा 13B आपसी / विवादित)",
                "title_od": "ଆବେଦନ ଦାଖଲ (ଧାରା ୧୩B ଆପୋଷ ବା ବିବାଦିତ)",
                "status": "IN_PROGRESS",
                "authority": "Principal Judge, Family Court",
                "details": "Submit joint affidavit for mutual consent or grounds of cruelty/desertion.",
                "citizen_rights": "Supreme Court permits waiver of 6-month statutory cooling period in irreparable breakdown."
            },
            {
                "step": 3,
                "title_en": "Interim Maintenance & Child Custody Orders",
                "title_hi": "अंतरिम गुजारा भत्ता एवं बच्चे की अभिरक्षा आदेश",
                "title_od": "ଅନ୍ତରୀଣ ଭରଣପୋଷଣ ଓ ପିଲାର ହେପାଜତ ନିର୍ଦ୍ଦେଶ",
                "status": "UPCOMING",
                "authority": "Family Court Bench",
                "details": "Court determines monthly child support and visitation rights as per Rajnesh v. Neha guidelines.",
                "citizen_rights": "Welfare of the child is the paramount statutory consideration."
            },
            {
                "step": 4,
                "title_en": "Final Decree & Permanent Alimony",
                "title_hi": "अंतिम डिक्री एवं स्थायी गुजारा भत्ता",
                "title_od": "ଚୂଡ଼ାନ୍ତ ରାୟ ଓ ସ୍ଥାୟୀ ଭରଣପୋଷଣ ଡିକ୍ରି",
                "status": "UPCOMING",
                "authority": "Family Court",
                "details": "Dissolution decree passed with settlement of matrimonial properties and stridhan.",
                "citizen_rights": "Both parties legally free to remarry after appeal period lapses."
            }
        ]
    },
    "domestic_violence": {
        "title_en": "Domestic Protection, Shelter & Maintenance Path",
        "title_hi": "घरेलू संरक्षण एवं भरण-पोषण न्याय यात्रा",
        "title_od": "ଘରୋଇ ସୁରକ୍ଷା ଓ ଭରଣପୋଷଣ ନ୍ୟାୟ ଯାତ୍ରା",
        "total_estimated_days": "15 - 45 Days",
        "stages": [
            {
                "step": 1,
                "title_en": "Crisis Assistance & Safe Shelter (Dial 181)",
                "title_hi": "संकटकालीन सहायता एवं सुरक्षित आश्रय",
                "title_od": "ଜରୁରୀ ସହାୟତା ଓ ସୁରକ୍ଷିତ ଆଶ୍ରୟ",
                "status": "COMPLETED",
                "authority": "One Stop Centre (OSC) / Women Helpline 181",
                "details": "Immediate medical checkup, emergency shelter, and psycho-social counseling.",
                "citizen_rights": "Absolute statutory right to food, shelter, and medical care at zero cost."
            },
            {
                "step": 2,
                "title_en": "Domestic Incident Report (DIR Form 1)",
                "title_hi": "घरेलू घटना रिपोर्ट (डीआईआर फॉर्म 1)",
                "title_od": "ଘଟଣା ରିପୋର୍ଟ (DIR ଫର୍ମ ୧)",
                "status": "IN_PROGRESS",
                "authority": "Protection Officer",
                "details": "Recording instances of emotional, physical, sexual, or economic abuse.",
                "citizen_rights": "Right to choose female officer and keep shelter location undisclosed."
            },
            {
                "step": 3,
                "title_en": "Ex-Parte Protection Order (Sec 18 PWDVA)",
                "title_hi": "एकपक्षीय सुरक्षा एवं निवास आदेश (धारा 18, 19)",
                "title_od": "ସୁରକ୍ଷା ଓ ଘରେ ରହିବା ଅଧିକାର ଆଦେଶ",
                "status": "UPCOMING",
                "authority": "Court of Judicial Magistrate (JMFC)",
                "details": "Within 3 days, judge issues injunction restraining eviction or harassment.",
                "citizen_rights": "Cannot be evicted from matrimonial home; police ordered to supervise."
            },
            {
                "step": 4,
                "title_en": "Interim Maintenance Order (Sec 20 PWDVA)",
                "title_hi": "अंतरिम मासिक गुजारा भत्ता आदेश",
                "title_od": "ମାସିକ ଭରଣପୋଷଣ ଆଦେଶ",
                "status": "UPCOMING",
                "authority": "JMFC Court & DLSA Panel Advocate",
                "details": "Court determines monthly sustenance allowance for applicant and minor children.",
                "citizen_rights": "Amount deducted directly from respondent's salary or bank account."
            }
        ]
    },
    "land_property": {
        "title_en": "Land Mutation & Boundary Demarcation Path",
        "title_hi": "भूमि नामांतरण एवं सीमांकन न्याय यात्रा",
        "title_od": "ଜମି ମ୍ୟୁଟେସନ ଏବଂ ସୀମା ନିର୍ଦ୍ଧାରଣ ପଥ",
        "total_estimated_days": "45 - 90 Days",
        "stages": [
            {
                "step": 1,
                "title_en": "Document Extraction & RoR Verification",
                "title_hi": "दस्तावेज़ निष्कर्षण एवं खतियान सत्यापन",
                "title_od": "ପଟ୍ଟା ସତ୍ୟାପନ ଓ କାଗଜପତ୍ର ସଂଗ୍ରହ",
                "status": "COMPLETED",
                "authority": "Bhulekh Portal / Mo Seva Kendra",
                "details": "Download digitally signed RoR (Record of Rights) and Plot map.",
                "citizen_rights": "Right to public land records within 3 days under ORTPSA Act."
            },
            {
                "step": 2,
                "title_en": "Field Demarcation Application (Form 10)",
                "title_hi": "सरकारी सीमांकन आवेदन (फॉर्म 10)",
                "title_od": "ସୀମା ମାପିବା ଆବେଦନ (ଫର୍ମ ୧୦)",
                "status": "IN_PROGRESS",
                "authority": "Tahasildar Office & Revenue Inspector (RI)",
                "details": "RI visits site with survey apparatus to measure coordinates with ₹100 fee.",
                "citizen_rights": "Notice must be served to all adjoining landowners 7 days in advance."
            },
            {
                "step": 3,
                "title_en": "Amicable Pre-Litigation Lok Adalat",
                "title_hi": "प्री-लिटिगेशन लोक अदालत समझौता",
                "title_od": "ପ୍ରି-ଲିଟିଗେସନ ଲୋକ ଅଦାଲତ ବୁଝାମଣା",
                "status": "UPCOMING",
                "authority": "Taluk Legal Services Committee (TLSC)",
                "details": "Retired judge and mediator facilitate peaceful boundary settlement.",
                "citizen_rights": "Zero court fees. Award has final decree status and cannot be appealed."
            },
            {
                "step": 4,
                "title_en": "Revenue Court / Sub-Collector Order (Sec 164 BNSS)",
                "title_hi": "राजस्व न्यायालय / एसडीएम अंतिम आदेश",
                "title_od": "ଉପ-ଜିଲ୍ଲାପାଳ କୋର୍ଟ ନିର୍ଦ୍ଦେଶ",
                "status": "UPCOMING",
                "authority": "Sub-Collector / SDM Court",
                "details": "Proceedings initiated if neighbor causes breach of peace.",
                "citizen_rights": "Right to state-assisted police protection during physical boundary erection."
            }
        ]
    },
    "property_succession": {
        "title_en": "Inheritance, Partition & Daughter Rights Roadmap",
        "title_hi": "पैतृक संपत्ति, बंटवारा एवं बेटियों के अधिकार की यात्रा",
        "title_od": "ପୈତୃକ ସମ୍ପତ୍ତି ଭାଗବଣ୍ଟା ଓ ଝିଅମାନଙ୍କ ଅଧିକାର ପଥ",
        "total_estimated_days": "60 - 180 Days",
        "stages": [
            {
                "step": 1,
                "title_en": "Family Genealogy & Legal Heir Certificate",
                "title_hi": "पारिवारिक वंशावली एवं कानूनी वारिस प्रमाण पत्र",
                "title_od": "ବଂଶାବଳୀ ଓ ଆଇନଗତ ଉତ୍ତରାଧିକାରୀ ପ୍ରମାଣପତ୍ର",
                "status": "COMPLETED",
                "authority": "Tahasildar / Revenue Inspector",
                "details": "Submitting family tree affidavit confirming all surviving Class-I legal heirs.",
                "citizen_rights": "All surviving sons and daughters must be named in the certificate."
            },
            {
                "step": 2,
                "title_en": "Equal Coparcenary Verification (Sec 6 HSA)",
                "title_hi": "समान सहदायिक (Coparcenary) अधिकार सत्यापन",
                "title_od": "ପୁଅ-ଝିଅଙ୍କ ସମାନ ଅଧିକାର ଯାଞ୍ଚ (ଧାରା ୬)",
                "status": "IN_PROGRESS",
                "authority": "Revenue Court / DLSA Panel Advocate",
                "details": "Applying 2005 Hindu Succession Amendment confirmed by Supreme Court (Vineeta Sharma).",
                "citizen_rights": "Daughters have an absolute equal birthright in ancestral property as sons."
            },
            {
                "step": 3,
                "title_en": "Partition Suit / Lok Adalat Family Settlement",
                "title_hi": "बंटवारा वाद / लोक अदालत पारिवारिक समझौता",
                "title_od": "ସମ୍ପତ୍ତି ଭାଗବଣ୍ଟା ମୋକଦ୍ଦମା ବା ଲୋକ ଅଦାଲତ",
                "status": "UPCOMING",
                "authority": "Civil Judge (Senior Division) / Taluk Lok Adalat",
                "details": "Drafting partition deed allocating metes and bounds shares.",
                "citizen_rights": "Compromise partition deed registered with concession in stamp duty."
            },
            {
                "step": 4,
                "title_en": "Separate Khata Mutation (Record of Rights)",
                "title_hi": "अलग खतियान एवं पट्टा नामांतरण",
                "title_od": "ପୃଥକ ପଟ୍ଟା ଓ ଖତିୟାନ ନାମାନ୍ତରଣ",
                "status": "UPCOMING",
                "authority": "Tahasildar Office",
                "details": "Creating individual Patta numbers for each legal heir's demarcated share.",
                "citizen_rights": "Independent right to sell, mortgage, or cultivate individual share."
            }
        ]
    },
    "tenancy_realestate": {
        "title_en": "RERA Builder Redressal & Tenancy Dispute Path",
        "title_hi": "रेरा (RERA) बिल्डर शिकायत एवं किरायेदारी न्याय यात्रा",
        "title_od": "ରେରା (RERA) ବିଲ୍ଡର ଠକେଇ ଓ ଘରଭଡ଼ା ବିବାଦ ପଥ",
        "total_estimated_days": "30 - 90 Days",
        "stages": [
            {
                "step": 1,
                "title_en": "Agreement Audit & Builder Demand Notice",
                "title_hi": "अनुबंध जांच एवं बिल्डर को कानूनी नोटिस",
                "title_od": "ଚୁକ୍ତିପତ୍ର ଯାଞ୍ଚ ଓ ବିଲ୍ଡରଙ୍କୁ ଲିଖିତ ନୋଟିସ୍",
                "status": "COMPLETED",
                "authority": "Buyer / Tenant & Opposite Party",
                "details": "Reviewing Builder-Buyer Agreement clauses and delivery date grace period.",
                "citizen_rights": "Buyer cannot be forced to pay unilateral one-sided penal interest."
            },
            {
                "step": 2,
                "title_en": "RERA Form M Electronic Filing",
                "title_hi": "रेरा (RERA) फॉर्म-M ऑनलाइन शिकायत",
                "title_od": "ରେରା (RERA) ପୋର୍ଟାଲରେ ଅନଲାଇନ ଅଭିଯୋଗ",
                "status": "IN_PROGRESS",
                "authority": "State Real Estate Regulatory Authority",
                "details": "Online complaint seeking flat possession or 100% refund plus interest.",
                "citizen_rights": "Under Sec 18 RERA, promoter must refund total amount with MCLR+2% interest."
            },
            {
                "step": 3,
                "title_en": "Adjudicating Officer Hearing / Rent Tribunal",
                "title_hi": "न्यायिक अधिकारी सुनवाई / किराया अधिकरण",
                "title_od": "ରେରା ବିଚାରପତିଙ୍କ ନିକଟରେ ଶୁଣାଣି",
                "status": "UPCOMING",
                "authority": "RERA Bench / Rent Controller",
                "details": "Hearing builder defence and verifying structural inspection report.",
                "citizen_rights": "Landlord cannot disconnect electricity or water during tenancy dispute."
            },
            {
                "step": 4,
                "title_en": "Recovery Warrant & Execution Order",
                "title_hi": "वसूली वारंट एवं कुर्की आदेश",
                "title_od": "ଟଙ୍କା ଆଦାୟ ୱାରେଣ୍ଟ ଓ ନିର୍ଦ୍ଦେଶନାମା",
                "status": "UPCOMING",
                "authority": "District Collector / Revenue Officer",
                "details": "Sum recovered as arrears of land revenue if builder defaults on refund.",
                "citizen_rights": "Attachment of builder company bank accounts and unsold inventory."
            }
        ]
    },
    "labor_employment": {
        "title_en": "Unpaid Wage Recovery & Labour Commission Path",
        "title_hi": "बकाया वेतन वसूली न्याय यात्रा",
        "title_od": "ବକେୟା ମଜୁରୀ ଆଦାୟ ନ୍ୟାୟ ଯାତ୍ରା",
        "total_estimated_days": "30 - 60 Days",
        "stages": [
            {
                "step": 1,
                "title_en": "Demand Notice & Attendance Compilation",
                "title_hi": "भुगतान मांग सूचना एवं उपस्थिति संकलन",
                "title_od": "ଦାବି ନୋଟିସ୍ ଓ ଦୈନିକ ଖାତା ପ୍ରମାଣ",
                "status": "COMPLETED",
                "authority": "Worker & Sub-contractor",
                "details": "Send recorded SMS/WhatsApp demand giving 7 days deadline.",
                "citizen_rights": "Payment of Wages Act prohibits wage deductions beyond statutory norms."
            },
            {
                "step": 2,
                "title_en": "Form VI Filing before Labour Commissioner",
                "title_hi": "श्रम आयुक्त के समक्ष प्रपत्र-VI आवेदन",
                "title_od": "ଶ୍ରମ କମିଶନରଙ୍କ ନିକଟରେ ଆବେଦନ",
                "status": "IN_PROGRESS",
                "authority": "Assistant Labour Commissioner (ALC)",
                "details": "ALC issues statutory summons to employer to produce wage register.",
                "citizen_rights": "Worker can claim unpaid wages plus up to 10 times compensation for delay."
            },
            {
                "step": 3,
                "title_en": "Mandatory Conciliation Conference",
                "title_hi": "अनिवार्य सुलह एवं समझौता बैठक",
                "title_od": "ବାଧ୍ୟତାମୂଳକ ଆପୋଷ ବୁଝାମଣା ବୈଠକ",
                "status": "UPCOMING",
                "authority": "District Labour Officer",
                "details": "Joint hearing where contractor is pressured to make direct bank transfer.",
                "citizen_rights": "Free legal aid representation arranged if employer brings a private advocate."
            },
            {
                "step": 4,
                "title_en": "Revenue Recovery Certificate (Distraint)",
                "title_hi": "राजस्व वसूली प्रमाण पत्र (कुर्की आदेश)",
                "title_od": "ଟଙ୍କା ଆଦାୟ ସାର୍ଟିଫିକେଟ୍",
                "status": "UPCOMING",
                "authority": "District Collector",
                "details": "Amount recovered as arrears of land revenue if employer defaults.",
                "citizen_rights": "Direct attachment of contractor bank accounts or equipment."
            }
        ]
    },
    "consumer_dispute": {
        "title_en": "Consumer Redressal & Refund Path",
        "title_hi": "उपभोक्ता क्षतिपूर्ति एवं समाधान यात्रा",
        "title_od": "ଗ୍ରାହକ କ୍ଷତିପୂରଣ ଓ ରିଫଣ୍ଡ ଯାତ୍ରା",
        "total_estimated_days": "60 - 120 Days",
        "stages": [
            {
                "step": 1,
                "title_en": "Docket Generation & 15-Day Legal Notice",
                "title_hi": "हेल्पलाइन डॉकेट व 15 दिवसीय विधिक नोटिस",
                "title_od": "୧୯୧୫ ଡକେଟ ଓ ୧୫ ଦିନର ଆଇନଗତ ନୋଟିସ୍",
                "status": "COMPLETED",
                "authority": "National Consumer Helpline (1915)",
                "details": "Formal communication offering seller last opportunity to replace or refund.",
                "citizen_rights": "Seller is obligated to respond within 15 days under CPA 2019."
            },
            {
                "step": 2,
                "title_en": "e-Daakhil Electronic Filing",
                "title_hi": "ई-दाखिल पोर्टल पर ऑनलाइन वाद दायर",
                "title_od": "ଇ-ଦାଖିଲ ପୋର୍ଟାଲରେ ଅଭିଯୋଗ ଦାୟର",
                "status": "IN_PROGRESS",
                "authority": "District Consumer Commission",
                "details": "Upload scanned bill, warranty card, photos; ₹0 court fee up to ₹5 Lakhs.",
                "citizen_rights": "No mandatory advocate required. Complainant can appear in person or online."
            },
            {
                "step": 3,
                "title_en": "Commission Mediation Cell",
                "title_hi": "आयोग मध्यस्थता केंद्र सुनवाई",
                "title_od": "କମିଶନ ମଧ୍ୟସ୍ଥତା କେନ୍ଦ୍ର",
                "status": "UPCOMING",
                "authority": "Consumer Mediation Cell",
                "details": "Parties referred for quick settlement before formal hearing.",
                "citizen_rights": "If settlement is reached, 100% of any paid court fees refunded."
            },
            {
                "step": 4,
                "title_en": "Final Judgment & Compensation Award",
                "title_hi": "अंतिम फैसला एवं मुआवजा आदेश",
                "title_od": "ଚୂଡ଼ାନ୍ତ ରାୟ ଓ କ୍ଷତିପୂରଣ ଆଦେଶ",
                "status": "UPCOMING",
                "authority": "District Commission Bench",
                "details": "Order to refund purchase sum plus interest and damages for harassment.",
                "citizen_rights": "Non-compliance punishable with imprisonment up to 3 years under Sec 72."
            }
        ]
    },
    "banking_debt_cheque": {
        "title_en": "Cheque Bounce (Sec 138) & Debt Redressal Path",
        "title_hi": "चेक बाउंस (धारा 138) एवं ऋण निवारण यात्रा",
        "title_od": "ଚେକ୍ ବାଉନ୍ସ (ଧାରା ୧୩୮) ଓ ଋଣ ସମାଧାନ ପଥ",
        "total_estimated_days": "30 - 90 Days",
        "stages": [
            {
                "step": 1,
                "title_en": "Bank Return Memo & 30-Day Statutory Notice",
                "title_hi": "बैंक रिटर्न मेमो एवं 30-दिवसीय वैधानिक नोटिस",
                "title_od": "ବ୍ୟାଙ୍କ ଫେରସ୍ତ ରସିଦ ଓ ୩୦ ଦିନର ଆଇନଗତ ନୋଟିସ୍",
                "status": "COMPLETED",
                "authority": "Bank & Drawer of Cheque",
                "details": "Notice sent via registered post giving drawer 15 days to pay the cheque amount.",
                "citizen_rights": "Statutory notice within 30 days of dishonour memo is mandatory."
            },
            {
                "step": 2,
                "title_en": "Filing Criminal Complaint before JMFC (Sec 138)",
                "title_hi": "मजिस्ट्रेट के समक्ष आपराधिक परिवाद दायर करना",
                "title_od": "ମାଜିଷ୍ଟ୍ରେଟଙ୍କ ନିକଟରେ ଅପରାଧିକ ମୋକଦ୍ଦମା ଦାୟର",
                "status": "IN_PROGRESS",
                "authority": "Judicial Magistrate First Class (JMFC)",
                "details": "If drawer defaults after 15 days, complaint filed within 30 days with verification affidavit.",
                "citizen_rights": "Offense carries imprisonment up to 2 years and fine up to double the cheque amount."
            },
            {
                "step": 3,
                "title_en": "Interim Compensation Order (Sec 143A NI Act)",
                "title_hi": "अंतरिम मुआवजा आदेश (20% राशि जमा)",
                "title_od": "ଅନ୍ତରୀଣ କ୍ଷତିପୂରଣ ନିର୍ଦ୍ଦେଶ (୨୦% ଟଙ୍କା ପୈଠ)",
                "status": "UPCOMING",
                "authority": "Magistrate Bench",
                "details": "Court directs accused drawer to deposit up to 20% of cheque amount as interim relief.",
                "citizen_rights": "Payable to complainant within 60 days of order."
            },
            {
                "step": 4,
                "title_en": "Lok Adalat Settlement / Final Conviction",
                "title_hi": "लोक अदालत समझौता / अंतिम सजा एवं वसूली",
                "title_od": "ଲୋକ ଅଦାଲତ ବୁଝାମଣା ବା ଚୂଡ଼ାନ୍ତ ରାୟ",
                "status": "UPCOMING",
                "authority": "National Lok Adalat / JMFC Court",
                "details": "Most cheque bounce matters compound amicably in Lok Adalat with full recovery.",
                "citizen_rights": "Compounded matter clears criminal record upon full payment."
            }
        ]
    },
    "cyber_fraud_privacy": {
        "title_en": "Cyber Fraud Golden Hour Recovery Path",
        "title_hi": "साइबर ठगी गोल्डन ऑवर रिकवरी यात्रा",
        "title_od": "ସାଇବର ଠକେଇ ଟଙ୍କା ଫେରସ୍ତ ଯାତ୍ରା",
        "total_estimated_days": "7 - 30 Days",
        "stages": [
            {
                "step": 1,
                "title_en": "Golden Hour Emergency Freeze (Dial 1930)",
                "title_hi": "गोल्डन ऑवर में तत्काल बैंक खाता फ्रीज",
                "title_od": "୧୯୩୦ ମାଧ୍ୟମରେ ତୁରନ୍ତ ଟଙ୍କା ଫ୍ରିଜ୍",
                "status": "COMPLETED",
                "authority": "National Cybercrime Reporting Portal (NCRP)",
                "details": "Automated system signals 14 major banks to block outflow on recipient wallet.",
                "citizen_rights": "Right to instant ACK token number for tracking lien status."
            },
            {
                "step": 2,
                "title_en": "Bank Liaison & ATM/UPI Invalidation",
                "title_hi": "बैंक शाखा सत्यापन एवं कार्ड ब्लॉक",
                "title_od": "ବ୍ୟାଙ୍କ ଷ୍ଟେଟମେଣ୍ଟ ଓ ସୁରକ୍ଷା ବ୍ଲକ",
                "status": "IN_PROGRESS",
                "authority": "Home Branch Bank Manager",
                "details": "Obtain stamped bank transaction statement showing UTR and timestamp.",
                "citizen_rights": "Zero-liability clause under RBI Master Circular if reported within 3 days."
            },
            {
                "step": 3,
                "title_en": "Police Station NCR / FIR Endorsement",
                "title_hi": "साइबर थाना पुष्टि एवं एफआईआर प्रति",
                "title_od": "ସାଇବର ଥାନାରେ ଏଫଆଇଆର ଦାୟର",
                "status": "UPCOMING",
                "authority": "District Cyber Police Station",
                "details": "Investigating officer verifies frozen recipient account balance.",
                "citizen_rights": "Copy of FIR must be provided immediately free of charge (BNSS Sec 173)."
            },
            {
                "step": 4,
                "title_en": "BNSS Sec 457 Restitution Order",
                "title_hi": "अदालत द्वारा धन वापसी आदेश (धारा 457)",
                "title_od": "କୋର୍ଟଙ୍କ ଦ୍ୱାରା ଟଙ୍କା ଫେରସ୍ତ ଆଦେଶ",
                "status": "UPCOMING",
                "authority": "Jurisdictional Chief Judicial Magistrate (CJM)",
                "details": "Magistrate directs bank nodal officer to credit frozen sum back to victim.",
                "citizen_rights": "No advocate commission or fee charged on recovered funds."
            }
        ]
    },
    "motor_accidents_traffic": {
        "title_en": "MACT Accident Claim & Compensation Path",
        "title_hi": "एमएसीटी सड़क दुर्घटना मुआवजा न्याय यात्रा",
        "title_od": "MACT ସଡ଼କ ଦୁର୍ଘଟଣା କ୍ଷତିପୂରଣ ଯାତ୍ରା",
        "total_estimated_days": "90 - 180 Days",
        "stages": [
            {
                "step": 1,
                "title_en": "Detailed Accident Report (DAR / Form 54)",
                "title_hi": "विस्तृत दुर्घटना रिपोर्ट (DAR) पंजीकरण",
                "title_od": "ଦୁର୍ଘଟଣା ତଦନ୍ତ ରିପୋର୍ଟ (DAR) ପଞ୍ଜୀକରଣ",
                "status": "COMPLETED",
                "authority": "Traffic Police / Investigating Officer",
                "details": "Police inspect offending vehicle, driver license, and third-party insurance policy.",
                "citizen_rights": "Police mandated to file DAR before Claims Tribunal within 90 days."
            },
            {
                "step": 2,
                "title_en": "Medical Disability & Income Verification",
                "title_hi": "चिकित्सा विकलांगता एवं आय सत्यापन",
                "title_od": "ଚିକିତ୍ସା କ୍ଷୟକ୍ଷତି ଓ ଆୟ ସତ୍ୟାପନ",
                "status": "IN_PROGRESS",
                "authority": "District Medical Board",
                "details": "Assessment of permanent functional disability and loss of future earning capacity.",
                "citizen_rights": "Interim no-fault liability relief payable under Sec 164 of Motor Vehicles Act."
            },
            {
                "step": 3,
                "title_en": "Claims Tribunal Evidence (Sec 166 MV Act)",
                "title_hi": "दावा अधिकरण साक्ष्य एवं सुनवाई",
                "title_od": "ଟ୍ରିବ୍ୟୁନାଲରେ ଶୁଣାଣି ଓ ପ୍ରମାଣ ଦାଖଲ",
                "status": "UPCOMING",
                "authority": "Motor Accident Claims Tribunal (District Judge)",
                "details": "Insurance company verification and settlement computation using standard multiplier.",
                "citizen_rights": "Victim entitled to medical cost, future loss, pain & suffering compensation."
            },
            {
                "step": 4,
                "title_en": "Award Deposit & Bank Transfer",
                "title_hi": "मुआवजा राशि बैंक अंतरण",
                "title_od": "କ୍ଷତିପୂରଣ ଟଙ୍କା ବ୍ୟାଙ୍କ ଖାତାକୁ ଜମା",
                "status": "UPCOMING",
                "authority": "MACT Tribunal & Insurance Company",
                "details": "Insurer must deposit compensation within 30 days of award.",
                "citizen_rights": "Amount placed in protected monthly annuity to safeguard victim's future."
            }
        ]
    },
    "senior_citizen_welfare": {
        "title_en": "Senior Citizen Protection & Maintenance Path",
        "title_hi": "वरिष्ठ नागरिक संरक्षण एवं भरण-पोषण यात्रा",
        "title_od": "ବରିଷ୍ଠ ନାଗରିକ ସୁରକ୍ଷା ଓ ଭରଣପୋଷଣ ପଥ",
        "total_estimated_days": "30 - 90 Days",
        "stages": [
            {
                "step": 1,
                "title_en": "Petition Filing before SDM Tribunal (Form A)",
                "title_hi": "एसडीएम ट्रिब्यूनल में आवेदन पत्र (फॉर्म A)",
                "title_od": "SDM ଟ୍ରିବ୍ୟୁନାଲରେ ଆବେଦନ ଫର୍ମ A",
                "status": "COMPLETED",
                "authority": "Sub-Divisional Magistrate (SDM)",
                "details": "Application stating neglect by children/relatives holding inherited property.",
                "citizen_rights": "No court fees. Lawyers prohibited to ensure simple, direct justice."
            },
            {
                "step": 2,
                "title_en": "Conciliation Officer Session",
                "title_hi": "सुलह अधिकारी के समक्ष परामर्श",
                "title_od": "ଆପୋଷ ବୁଝାମଣା ଅଧିକାରୀଙ୍କ ବୈଠକ",
                "status": "IN_PROGRESS",
                "authority": "Conciliation Officer",
                "details": "Direct counseling session attempting peaceful familial care settlement within 30 days.",
                "citizen_rights": "If conciliation fails, matter immediately proceeds to formal Tribunal adjudication."
            },
            {
                "step": 3,
                "title_en": "Statutory Maintenance Order (Max ₹10,000/mo)",
                "title_hi": "मासिक भरण-पोषण अनिवार्य आदेश",
                "title_od": "ବାଧ୍ୟତାମୂଳକ ମାସିକ ଖର୍ଚ୍ଚ ନିର୍ଦ୍ଦେଶ",
                "status": "UPCOMING",
                "authority": "Maintenance Tribunal Bench",
                "details": "Tribunal orders adult children to deposit monthly maintenance into parent's account.",
                "citizen_rights": "Non-payment results in warrants and imprisonment up to 1 month."
            },
            {
                "step": 4,
                "title_en": "Summary Eviction of Abusive Children (Sec 23)",
                "title_hi": "प्रताड़ित करने वाले बच्चों की बेदखली",
                "title_od": "ଅତ୍ୟାଚାରୀ ପିଲାଙ୍କୁ ଘରୁ ବାହାର କରିବା ଆଦେଶ",
                "status": "UPCOMING",
                "authority": "SDM Tribunal & Local Police",
                "details": "Order directing abusive children to vacate elderly parents' house within 30 days.",
                "citizen_rights": "Police mandated to physically enforce eviction and ensure parents' peaceful safety."
            }
        ]
    },
    "child_pocso_education": {
        "title_en": "Child Protection & Special POCSO Justice Path",
        "title_hi": "बाल संरक्षण एवं पॉक्सो त्वरित न्याय यात्रा",
        "title_od": "ଶିଶୁ ସୁରକ୍ଷା ଓ ପକ୍ସୋ (POCSO) ତ୍ୱରିତ ନ୍ୟାୟ ପଥ",
        "total_estimated_days": "1 - 60 Days",
        "stages": [
            {
                "step": 1,
                "title_en": "Emergency Reporting & Dial 1098 / 112",
                "title_hi": "आपातकालीन सूचना (1098 / 112)",
                "title_od": "ଜରୁରୀକାଳୀନ ସୂଚନା (୧୦୯୮ / ୧୧୨)",
                "status": "COMPLETED",
                "authority": "Special Juvenile Police Unit (SJPU) / Childline",
                "details": "Police officer in civilian clothes records information without subjecting child to trauma.",
                "citizen_rights": "Absolute statutory identity protection. Disclosing child victim's name is a criminal offense."
            },
            {
                "step": 2,
                "title_en": "Immediate Medical Examination & Care",
                "title_hi": "तत्काल चिकित्सा जांच एवं उपचार",
                "title_od": "ତୁରନ୍ତ ଡାକ୍ତରୀ ପରୀକ୍ଷା ଓ ମାଗଣା ଚିକିତ୍ସା",
                "status": "IN_PROGRESS",
                "authority": "Government Hospital Medical Officer",
                "details": "Free medical treatment conducted in the presence of parent or nominated woman.",
                "citizen_rights": "Zero fee hospital care; interim emergency compensation granted within 24 hours."
            },
            {
                "step": 3,
                "title_en": "Child Welfare Committee (CWC) Order",
                "title_hi": "बाल कल्याण समिति (CWC) सुरक्षा आदेश",
                "title_od": "ଶିଶୁ କଲ୍ୟାଣ କମିଟି (CWC) ସୁରକ୍ଷା ଆଦେଶ",
                "status": "UPCOMING",
                "authority": "Child Welfare Committee",
                "details": "CWC determines safe shelter, counseling, education continuance, and legal support.",
                "citizen_rights": "Free legal aid defense assigned automatically via DLSA."
            },
            {
                "step": 4,
                "title_en": "Special In-Camera Court Trial",
                "title_hi": "विशेष पॉक्सो अदालत में बंद कमरे में ट्रायल",
                "title_od": "ବନ୍ଦ କୋଠରୀରେ ବିଶେଷ ପକ୍ସୋ କୋର୍ଟ ଶୁଣାଣି",
                "status": "UPCOMING",
                "authority": "Special POCSO Judge",
                "details": "Child does not face the accused; testimony recorded via one-way screen or video link.",
                "citizen_rights": "Trial to be completed within 1 year; victim compensation awarded directly."
            }
        ]
    },
    "constitutional_rti_grievance": {
        "title_en": "RTI & Public Grievance Redressal Roadmap",
        "title_hi": "सूचना का अधिकार (RTI) एवं जन शिकायत समाधान यात्रा",
        "title_od": "ସୂଚନା ଅଧିକାର (RTI) ଓ ଜନ ଅଭିଯୋଗ ସମାଧାନ ପଥ",
        "total_estimated_days": "30 - 60 Days",
        "stages": [
            {
                "step": 1,
                "title_en": "RTI Form A Submission (Sec 6)",
                "title_hi": "आरटीआई आवेदन जमा करना (धारा 6)",
                "title_od": "RTI ଆବେଦନ ଦାଖଲ (ଧାରା ୬)",
                "status": "COMPLETED",
                "authority": "Public Information Officer (PIO)",
                "details": "Submit specific questions with ₹10 court fee stamp or online on RTI portal.",
                "citizen_rights": "Citizen is not required to give any reason for asking public information."
            },
            {
                "step": 2,
                "title_en": "30-Day Mandatory Disclosure Window",
                "title_hi": "30-दिवसीय अनिवार्य प्रकटीकरण अवधि",
                "title_od": "୩୦ ଦିନର ବାଧ୍ୟତାମୂଳକ ଉତ୍ତର ସମୟସୀମା",
                "status": "IN_PROGRESS",
                "authority": "PIO of Department",
                "details": "PIO must provide certified copies or reject with statutory section within 30 days (48 hours for life/liberty).",
                "citizen_rights": "If deadline is missed, information must be provided 100% free of charge."
            },
            {
                "step": 3,
                "title_en": "First Appeal before Senior Department Head",
                "title_hi": "प्रथम अपीलीय अधिकारी के समक्ष अपील",
                "title_od": "ବିଭାଗୀୟ ମୁଖ୍ୟଙ୍କ ନିକଟରେ ପ୍ରଥମ ଅପିଲ୍",
                "status": "UPCOMING",
                "authority": "First Appellate Authority (FAA)",
                "details": "Appeal filed within 30 days if information is delayed, misleading, or refused.",
                "citizen_rights": "FAA must pass speaking order within 30-45 days."
            },
            {
                "step": 4,
                "title_en": "Second Appeal & Penalty before Information Commission",
                "title_hi": "सूचना आयोग में द्वितीय अपील एवं जुर्माना",
                "title_od": "ରାଜ୍ୟ ସୂଚନା କମିଶନଙ୍କ ନିକଟରେ ଦ୍ୱିତୀୟ ଅପିଲ୍",
                "status": "UPCOMING",
                "authority": "State Information Commission (SIC)",
                "details": "Commission can impose ₹250/day penalty (up to ₹25,000) directly on defaulting PIO.",
                "citizen_rights": "Commission can award compensation to citizen for detriment suffered."
            }
        ]
    },
    "business_msme_tax": {
        "title_en": "MSME Delayed Payment & Business Recovery Path",
        "title_hi": "एमएसएमई विलंबित भुगतान एवं व्यापार समाधान यात्रा",
        "title_od": "MSME ବକେୟା ଟଙ୍କା ଓ ବ୍ୟାପାର ସମାଧାନ ପଥ",
        "total_estimated_days": "45 - 90 Days",
        "stages": [
            {
                "step": 1,
                "title_en": "45-Day Statutory Due Date Expiry",
                "title_hi": "45-दिवसीय भुगतान सीमा समाप्ति",
                "title_od": "୪୫ ଦିନର ବାଧ୍ୟତାମୂଳକ ସମୟସୀମା ଶେଷ",
                "status": "COMPLETED",
                "authority": "Buyer & Supplier (Udyam Registered)",
                "details": "Under Sec 15 of MSMED Act, payment cannot exceed 45 days from delivery of goods.",
                "citizen_rights": "Buyer is automatically liable to pay compound interest at 3 times RBI bank rate."
            },
            {
                "step": 2,
                "title_en": "Filing on MSME Samadhaan Portal",
                "title_hi": "एमएसएमई समाधान पोर्टल पर ऑनलाइन आवेदन",
                "title_od": "MSME ସମାଧାନ ପୋର୍ଟାଲରେ ଅନଲାଇନ ଆବେଦନ",
                "status": "IN_PROGRESS",
                "authority": "samadhaan.msme.gov.in",
                "details": "Upload tax invoices and delivery challans; automated notice served to defaulting buyer.",
                "citizen_rights": "Zero court fees for micro and small enterprises."
            },
            {
                "step": 3,
                "title_en": "MSME Facilitation Council Conciliation",
                "title_hi": "सुविधा परिषद के समक्ष सुलह सुनवाई",
                "title_od": "MSME ପରିଷଦଙ୍କ ନିକଟରେ ସମାଧାନ ବୈଠକ",
                "status": "UPCOMING",
                "authority": "State Micro & Small Enterprises Facilitation Council",
                "details": "Council conducts conciliation within 90 days; if unresolved, initiates arbitration.",
                "citizen_rights": "Council awards have the force of an arbitral decree."
            },
            {
                "step": 4,
                "title_en": "Arbitral Award Execution & Asset Attachment",
                "title_hi": "मध्यस्थता पंचाट क्रियान्वयन एवं कुर्की",
                "title_od": "କୋର୍ଟ ଆଦେଶ ଓ ଟଙ୍କା ଆଦାୟ ନିର୍ଦ୍ଦେଶ",
                "status": "UPCOMING",
                "authority": "Commercial Court / District Court",
                "details": "Buyer cannot challenge award without pre-depositing 75% of award amount (Sec 19).",
                "citizen_rights": "Compulsory recovery with compound monthly interest."
            }
        ]
    },
    "universal_legal_assistant": {
        "title_en": "Citizen Statutory Rights & Redressal Roadmap",
        "title_hi": "नागरिक वैधानिक अधिकार एवं त्वरित न्याय यात्रा",
        "title_od": "ନାଗରିକ ଆଇନଗତ ଅଧିକାର ଓ ସମାଧାନ ପଥ",
        "total_estimated_days": "30 - 90 Days",
        "stages": [
            {
                "step": 1,
                "title_en": "Fact Verification & Document Compilation",
                "title_hi": "तथ्य सत्यापन एवं दस्तावेज़ संकलन",
                "title_od": "ତଥ୍ୟ ଯାଞ୍ଚ ଓ କାଗଜପତ୍ର ସଂଗ୍ରହ",
                "status": "COMPLETED",
                "authority": "Citizen Self-Compilation",
                "details": "Collect all relevant written notices, identity cards, photos, and evidence.",
                "citizen_rights": "Right to state assistance under the Legal Services Authorities Act."
            },
            {
                "step": 2,
                "title_en": "Free DLSA Legal Aid Evaluation",
                "title_hi": "मुफ्त विधिक सहायता पात्रता जांच",
                "title_od": "ମାଗଣା ଆଇନ ସହାୟତା ଯୋଗ୍ୟତା ଯାଞ୍ଚ",
                "status": "IN_PROGRESS",
                "authority": "District Legal Services Authority (DLSA)",
                "details": "Evaluation under Section 12 for free panel advocate appointment.",
                "citizen_rights": "All court fees, typing, drafting, and process fees covered by government."
            },
            {
                "step": 3,
                "title_en": "Pre-Litigation Lok Adalat / Notice to Opponent",
                "title_hi": "प्री-लिटिगेशन लोक अदालत / विपक्षी को नोटिस",
                "title_od": "ପ୍ରି-ଲିଟିଗେସନ ଲୋକ ଅଦାଲତ ବୁଝାମଣା",
                "status": "UPCOMING",
                "authority": "Taluk Legal Services Committee",
                "details": "Attempting amicable compromise before filing contentious litigation.",
                "citizen_rights": "Amicable settlements are final with zero future appeal hurdles."
            },
            {
                "step": 4,
                "title_en": "Competent Court / Tribunal Hearing",
                "title_hi": "सक्षम न्यायालय / अधिकरण में सुनवाई",
                "title_od": "କୋର୍ଟ ବା ଟ୍ରିବ୍ୟୁନାଲରେ ଆଇନଗତ ଶୁଣାଣି",
                "status": "UPCOMING",
                "authority": "Jurisdictional Court",
                "details": "Adjudication of rights and issuance of binding decree or interim order.",
                "citizen_rights": "Right to speedy trial and certified judgment copies free of cost."
            }
        ]
    }
}
# Checklists for all 15 legal domains
ALL_CHECKLISTS = {
    "criminal_police": [
        {"item_en": "Written Complaint / FIR Draft with Date & Time", "item_hi": "दिनांक, समय व घटना विवरण सहित लिखित शिकायत", "item_od": "ତାରିଖ ଓ ସମୟ ସହ ଲିଖିତ ଅଭିଯୋଗ ପତ୍ର", "mandatory": 1, "purpose": "Basis for registration under Sec 173 BNSS", "issuing_authority": "Complainant / Advocate"},
        {"item_en": "Medical Legal Certificate (MLC) / Injury Slip", "item_hi": "चिकित्सा जांच पर्ची (एमएलसी / चोट रिपोर्ट)", "item_od": "ଡାକ୍ତରୀ ପରୀକ୍ଷା ରିପୋର୍ଟ (MLC)", "mandatory": 0, "purpose": "Corroborative bodily evidence", "issuing_authority": "Govt Hospital CMO"},
        {"item_en": "Aadhaar / Voter ID of Complainant", "item_hi": "शिकायतकर्ता का आधार / पहचान पत्र", "item_od": "ଅଭିଯୋଗକାରୀଙ୍କ ଆଧାର କାର୍ଡ", "mandatory": 1, "purpose": "Identity verification", "issuing_authority": "UIDAI / ECI"}
    ],
    "family_matrimonial": [
        {"item_en": "Original Marriage Registration Certificate / Wedding Card", "item_hi": "मूल विवाह प्रमाण पत्र / विवाह पत्रिका", "item_od": "ମୂଳ ବିବାହ ପ୍ରମାଣପତ୍ର ବା ନିମନ୍ତ୍ରଣ ପତ୍ର", "mandatory": 1, "purpose": "Proof of valid solemnized marriage", "issuing_authority": "Marriage Registrar / Panchayat"},
        {"item_en": "Affidavit of Income & Assets (Rajnesh v. Neha Format)", "item_hi": "आय एवं संपत्ति का विस्तृत शपथ पत्र", "item_od": "ଆୟ ଓ ସମ୍ପତ୍ତି ଘୋଷଣାନାମା ଶପଥପତ୍ର", "mandatory": 1, "purpose": "Mandatory for alimony / maintenance calculation", "issuing_authority": "Notary Public"},
        {"item_en": "Birth Certificates of Minor Children", "item_hi": "नाबालिग बच्चों का जन्म प्रमाण पत्र", "item_od": "ପିଲାମାନଙ୍କ ଜନ୍ମ ପ୍ରମାଣପତ୍ର", "mandatory": 0, "purpose": "Custody and child support adjudication", "issuing_authority": "Municipal Corporation"}
    ],
    "domestic_violence": [
        {"item_en": "Domestic Incident Report (DIR Form 1)", "item_hi": "घरेलू घटना रिपोर्ट (डीआईआर)", "item_od": "ଘରୋଇ ଘଟଣା ରିପୋର୍ଟ (DIR)", "mandatory": 1, "purpose": "Statutory basis for magistrate protection order", "issuing_authority": "Protection Officer / CDPO"},
        {"item_en": "Medical Examination / Injury Prescription", "item_hi": "चिकित्सा पर्ची (चोट लगने पर)", "item_od": "ଡାକ୍ତରୀ ପରୀକ୍ଷା ରିପୋର୍ଟ", "mandatory": 0, "purpose": "Physical abuse evidence", "issuing_authority": "Primary Health Centre"},
        {"item_en": "Ration Card / Proof of Shared Household", "item_hi": "राशन कार्ड / साझा निवास प्रमाण", "item_od": "ରାସନ କାର୍ଡ ବା ମିଳିତ ଘର ପ୍ରମାଣ", "mandatory": 1, "purpose": "Right to residence under Sec 19 PWDVA", "issuing_authority": "Civil Supplies Dept"}
    ],
    "land_property": [
        {"item_en": "RoR / Record of Rights (Patta)", "item_hi": "खतियान / जमाबंदी / पट्टा की प्रति", "item_od": "ଜମି ପଟ୍ଟା / ଖତିୟାନ ନକଲ", "mandatory": 1, "purpose": "Proof of ownership and recorded plot number", "issuing_authority": "Tahasildar / Bhulekh Portal"},
        {"item_en": "Latest Land Revenue Receipt (Khajna)", "item_hi": "नवीनतम लगान / खजाना रसीद", "item_od": "ଚଳିତ ବର୍ଷର ଖଜଣା ରସିଦ", "mandatory": 1, "purpose": "Proves continuous possession and tax compliance", "issuing_authority": "Revenue Inspector (RI) Office"},
        {"item_en": "Field Demarcation / Survey Map (Naksha)", "item_hi": "जमीन का प्रमाणित नक्शा", "item_od": "ସର୍ଭେ ନକ୍ସା କିମ୍ବା ମ୍ୟାପ୍", "mandatory": 0, "purpose": "Visual proof of boundaries and encroached area", "issuing_authority": "District Settlement Office"}
    ],
    "property_succession": [
        {"item_en": "Genealogy / Family Tree Affidavit (Vamshavali)", "item_hi": "पारिवारिक वंशावली शपथ पत्र", "item_od": "ବଂଶାବଳୀ ଶପଥପତ୍ର", "mandatory": 1, "purpose": "Proves Class-I legal heirs", "issuing_authority": "Tahasildar / Executive Magistrate"},
        {"item_en": "Death Certificate of Original Landholder", "item_hi": "मूल संपत्ति धारक का मृत्यु प्रमाण पत्र", "item_od": "ମୂଳ ଜମି ମାଲିକଙ୍କ ମୃତ୍ୟୁ ପ୍ରମାଣପତ୍ର", "mandatory": 1, "purpose": "Opens succession under Hindu Succession Act", "issuing_authority": "Registrar of Births & Deaths"},
        {"item_en": "Registered Will / Gift Deed (if any exists)", "item_hi": "पंजीकृत वसीयत / उपहार विलेख (यदि हो)", "item_od": "ପଞ୍ଜୀକୃତ ଉଇଲ୍ ବା ଦାନପତ୍ର", "mandatory": 0, "purpose": "Testamentary disposition proof", "issuing_authority": "Sub-Registrar Office"}
    ],
    "tenancy_realestate": [
        {"item_en": "Builder-Buyer Allotment Agreement (BBA)", "item_hi": "बिल्डर आवंटन समझौता विलेख", "item_od": "ବିଲ୍ଡର ଆବଣ୍ଟନ ଚୁକ୍ତିପତ୍ର", "mandatory": 1, "purpose": "Proves agreed date of possession & penalty terms", "issuing_authority": "Developer / Builder"},
        {"item_en": "Payment Receipts & Bank Transaction Slips", "item_hi": "भुगतान रसीदें एवं बैंक ट्रांजेक्शन विवरण", "item_od": "ଟଙ୍କା ପୈଠ ରସିଦ ଓ ବ୍ୟାଙ୍କ ଷ୍ଟେଟମେଣ୍ଟ", "mandatory": 1, "purpose": "Proof of total amount invested", "issuing_authority": "Bank / Builder Accounts"},
        {"item_en": "Registered Rent Agreement (for tenancy disputes)", "item_hi": "पंजीकृत किराया समझौता (किरायेदारी में)", "item_od": "ଘରଭଡ଼ା ଚୁକ୍ତିପତ୍ର", "mandatory": 1, "purpose": "Terms of rent, notice period & security deposit", "issuing_authority": "Notary / Sub-Registrar"}
    ],
    "labor_employment": [
        {"item_en": "Attendance Log / Work Diary / Job Card", "item_hi": "दैनिक उपस्थिति डायरी / कार्य पर्ची", "item_od": "ଦୈନିକ କାମ ଖାତା କିମ୍ବା ସ୍ଲିପ୍", "mandatory": 1, "purpose": "Proof of number of days and nature of labor", "issuing_authority": "Sub-contractor / Self Diary"},
        {"item_en": "Appointment Letter / Wage Slip / UPI History", "item_hi": "नियुक्ति पत्र / वेतन पर्ची / यूपीआई इतिहास", "item_od": "ନିଯୁକ୍ତି ପତ୍ର / ଦରମା ରସିଦ", "mandatory": 1, "purpose": "Proves employer-employee relationship", "issuing_authority": "Employer / Bank"},
        {"item_en": "e-Shram Card / Construction Worker Registration", "item_hi": "ई-श्रम कार्ड / निर्माण श्रमिक कार्ड", "item_od": "ଇ-ଶ୍ରମ କାର୍ଡ କିମ୍ବା ଶ୍ରମିକ କାର୍ଡ", "mandatory": 0, "purpose": "Entitles worker to state legal aid", "issuing_authority": "Ministry of Labour"}
    ],
    "consumer_dispute": [
        {"item_en": "Original Tax Invoice / GST Bill / Cash Memo", "item_hi": "मूल खरीद बिल / जीएसटी चालान", "item_od": "କିଣାଯାଇଥିବା ସାମଗ୍ରୀର ବିଲ୍", "mandatory": 1, "purpose": "Proof of transaction and consumer standing", "issuing_authority": "Seller / Merchant"},
        {"item_en": "Warranty Card with Dealer Stamp & Serial No", "item_hi": "वारंटी कार्ड (दुकानदार की मुहर सहित)", "item_od": "ସିଲ୍ ଥିବା ୱାରେଣ୍ଟି କାର୍ଡ", "mandatory": 1, "purpose": "Proves guarantee period validity", "issuing_authority": "Authorized Retailer"},
        {"item_en": "Service Centre Job Sheet / Denial Letter", "item_hi": "सर्विस सेंटर जॉब शीट / रिजेक्शन पर्ची", "item_od": "ସର୍ଭିସ ସେଣ୍ଟର ରିପୋର୍ଟ", "mandatory": 0, "purpose": "Proof of defect and refusal to repair", "issuing_authority": "Authorized Service Centre"}
    ],
    "banking_debt_cheque": [
        {"item_en": "Original Dishonored Cheque & Bank Return Memo", "item_hi": "मूल बाउंस चेक एवं बैंक रिटर्न मेमो", "item_od": "ବାଉନ୍ସ ଚେକ୍ ଓ ବ୍ୟାଙ୍କ ଫେରସ୍ତ ରସିଦ", "mandatory": 1, "purpose": "Statutory proof under Sec 138 NI Act", "issuing_authority": "Bank Branch"},
        {"item_en": "Statutory 30-Day Legal Demand Notice & Postal Receipt", "item_hi": "30-दिवसीय कानूनी नोटिस व स्पीड पोस्ट रसीद", "item_od": "୩୦ ଦିନର ଆଇନଗତ ନୋଟିସ୍ ଓ ଡାକ ରସିଦ", "mandatory": 1, "purpose": "Mandatory prerequisite before criminal complaint", "issuing_authority": "Advocate / India Post"},
        {"item_en": "Account Statement / Underlying Invoice or Agreement", "item_hi": "बैंक विवरण / अनुबंध विलेख", "item_od": "ଚୁକ୍ତିପତ୍ର ବା ବକେୟା ବିଲ୍", "mandatory": 1, "purpose": "Proof of legally enforceable debt", "issuing_authority": "Bank / Complainant"}
    ],
    "cyber_fraud_privacy": [
        {"item_en": "Stamped Bank Statement Highlighting Fraudulent Debits", "item_hi": "बैंक पासबुक / विवरण (अवैध लेन-देन रेखांकित)", "item_od": "ବ୍ୟାଙ୍କ ଷ୍ଟେଟମେଣ୍ଟ (ଅବୈଧ କାରବାର)", "mandatory": 1, "purpose": "Shows date, time, and UTR reference number", "issuing_authority": "Bank Branch / Netbanking"},
        {"item_en": "1930 Cyber Helpline Token Slip / NCRP Acknowledgment", "item_hi": "1930 साइबर कंप्लेंट पावती संख्या", "item_od": "୧୯୩୦ ସାଇବର ଅଭିଯୋଗ ଟୋକନ ସଂଖ୍ୟା", "mandatory": 1, "purpose": "Essential for bank freeze verification & magistrate refund", "issuing_authority": "National Cybercrime Portal"},
        {"item_en": "SMS Alerts, WhatsApp Chats & Fraudulent APK Screenshots", "item_hi": "धोखाधड़ी संदेश, व्हाट्सएप व एपीके स्क्रीनशॉट", "item_od": "ମେସେଜ୍ ଓ ହ୍ୱାଟ୍ସଆପ୍ ସ୍କ୍ରିନସଟ୍", "mandatory": 1, "purpose": "Digital footprint and phone numbers of fraudsters", "issuing_authority": "Victim Smartphone"}
    ],
    "motor_accidents_traffic": [
        {"item_en": "Detailed Accident Report (DAR) & Police FIR Copy", "item_hi": "विस्तृत दुर्घटना रिपोर्ट (DAR) व एफआईआर प्रति", "item_od": "ଦୁର୍ଘଟଣା ରିପୋର୍ଟ (DAR) ଓ ଏଫଆଇଆର ନକଲ", "mandatory": 1, "purpose": "Statutory basis for claim under Sec 166 MV Act", "issuing_authority": "Traffic Police Station"},
        {"item_en": "Hospital Injury Discharge Summary & Medical Bills", "item_hi": "अस्पताल डिस्चार्ज समरी एवं दवाइयों के बिल", "item_od": "ଡାକ୍ତରଖାନା ଡିସଚାର୍ଜ ସାର୍ଟିଫିକେଟ ଓ ମେଡିକାଲ ବିଲ୍", "mandatory": 1, "purpose": "Proves physical injury and actual medical expense", "issuing_authority": "Treating Hospital"},
        {"item_en": "Permanent Disability Certificate (if applicable)", "item_hi": "स्थायी विकलांगता प्रमाण पत्र", "item_od": "ସ୍ଥାୟୀ ଭିନ୍ନକ୍ଷମ ପ୍ରମାଣପତ୍ର", "mandatory": 0, "purpose": "Calculates loss of future income multiplier", "issuing_authority": "District Medical Board"}
    ],
    "senior_citizen_welfare": [
        {"item_en": "Age Proof (Aadhaar / Voter ID / Pension Passbook)", "item_hi": "आयु प्रमाण (आधार / मतदाता पहचान / पेंशन पर्ची)", "item_od": "ବୟସ ପ୍ରମାଣପତ୍ର (ଆଧାର / ପେନସନ ଖାତା)", "mandatory": 1, "purpose": "Must prove age 60 years or above", "issuing_authority": "UIDAI / Treasury"},
        {"item_en": "Property Ownership Document of Parent's House", "item_hi": "माता-पिता के मकान के स्वामित्व कागजात", "item_od": "ଘରର ମାଲିକାନା ପଟ୍ଟା ବା କାଗଜପତ୍ର", "mandatory": 1, "purpose": "Mandatory for evicting abusive children", "issuing_authority": "Tahasildar / Sub-Registrar"},
        {"item_en": "Medical Treatment Bills Showing Monthly Healthcare Need", "item_hi": "मासिक दवाई व इलाज के बिल", "item_od": "ଔଷଧ ଓ ଚିକିତ୍ସା ଖର୍ଚ୍ଚ ବିଲ୍", "mandatory": 0, "purpose": "Justifies higher monthly maintenance allowance", "issuing_authority": "Hospital / Pharmacy"}
    ],
    "child_pocso_education": [
        {"item_en": "Child Birth Certificate / School Bonafide Certificate", "item_hi": "बच्चे का जन्म प्रमाण पत्र / स्कूल प्रमाण", "item_od": "ଶିଶୁର ଜନ୍ମ ପ୍ରମାଣପତ୍ର ବା ସ୍କୁଲ ସାର୍ଟିଫିକେଟ", "mandatory": 1, "purpose": "Proves age below 18 years for minor protection", "issuing_authority": "Birth Registrar / School Principal"},
        {"item_en": "Income Certificate / BPL Card (for 25% Free RTE Admission)", "item_hi": "आय प्रमाण पत्र / बीपीएल कार्ड (मुफ्त दाखिला हेतु)", "item_od": "BPL କାର୍ଡ ବା ଆୟ ପ୍ରମାଣପତ୍ର (RTE ମାଗଣା ନାମଲେଖା)", "mandatory": 1, "purpose": "Right to Education EWS category admission", "issuing_authority": "Tahasildar Office"},
        {"item_en": "Special Medical Report / Counselor Report", "item_hi": "विशेष चिकित्सा या बाल परामर्श रिपोर्ट", "item_od": "ଡାକ୍ତରୀ ବା କାଉନସେଲିଂ ରିପୋର୍ଟ", "mandatory": 0, "purpose": "Confidential evaluation for POCSO court", "issuing_authority": "Govt Medical Officer"}
    ],
    "constitutional_rti_grievance": [
        {"item_en": "Form A RTI Application with ₹10 Court Fee Stamp", "item_hi": "₹10 शुल्क टिकट सहित प्रपत्र-A आरटीआई", "item_od": "₹୧୦ କୋର୍ଟ ଫି ଟିକେଟ ସହ RTI ଆବେଦନ ଫର୍ମ", "mandatory": 1, "purpose": "Statutory application under Sec 6 RTI Act 2005", "issuing_authority": "Applicant"},
        {"item_en": "Previous Application Receipt / Samadhan Grievance Docket", "item_hi": "पूर्व आवेदन पावती / समाधान पोर्टल शिकायत संख्या", "item_od": "ପୂର୍ବ ଆବେଦନ ରସିଦ ବା ଅଭିଯୋଗ ନମ୍ବର", "mandatory": 0, "purpose": "Proves government inaction or service delay", "issuing_authority": "Concerned Govt Dept"},
        {"item_en": "BPL Ration Card (if claiming fee exemption)", "item_hi": "बीपीएल राशन कार्ड (निःशुल्क आरटीआई हेतु)", "item_od": "BPL ରାସନ କାର୍ଡ (ମାଗଣା RTI ପାଇଁ)", "mandatory": 0, "purpose": "Exempts citizen from all RTI and copying fees", "issuing_authority": "Food & Civil Supplies"}
    ],
    "business_msme_tax": [
        {"item_en": "Udyam MSME Registration Certificate", "item_hi": "उद्यम एमएसएमई पंजीकरण प्रमाण पत्र", "item_od": "ଉଦ୍ୟମ MSME ପଞ୍ଜୀକରଣ ପ୍ରମାଣପତ୍ର", "mandatory": 1, "purpose": "Proof of micro/small enterprise standing", "issuing_authority": "Ministry of MSME"},
        {"item_en": "Tax Invoices & Signed Delivery Proof (Lorry Receipt / E-way bill)", "item_hi": "टैक्स इनवॉइस एवं डिलीवरी चालान (ई-वे बिल)", "item_od": "ଟ୍ୟାକ୍ସ ଇନଭଏସ ଓ ସାମଗ୍ରୀ ପହଞ୍ଚିବା ରସିଦ", "mandatory": 1, "purpose": "Proves delivery of goods and unpaid sum beyond 45 days", "issuing_authority": "Supplier & Transporter"},
        {"item_en": "Purchase Order (PO) / Commercial Contract", "item_hi": "खरीद आदेश (PO) / व्यापारिक अनुबंध", "item_od": "ଅର୍ଡର କପି ବା ଚୁକ୍ତିପତ୍ର", "mandatory": 1, "purpose": "Establishes agreed pricing and supply terms", "issuing_authority": "Buyer"}
    ],
    "universal_legal_assistant": [
        {"item_en": "Aadhaar Card / Government Identity Proof", "item_hi": "आधार कार्ड / सरकारी पहचान पत्र", "item_od": "ଆଧାର କାର୍ଡ ବା ସରକାରୀ ପରିଚୟପତ୍ର", "mandatory": 1, "purpose": "Identity verification for legal standing", "issuing_authority": "UIDAI / ECI"},
        {"item_en": "Written Chronology of Events & Notice Copies", "item_hi": "घटनाओं का लिखित क्रमवार विवरण व नोटिस", "item_od": "ଘଟଣାର ଲିଖିତ ବିବରଣୀ ଓ ନୋଟିସ୍ ନକଲ", "mandatory": 1, "purpose": "Forms factual basis for legal counseling", "issuing_authority": "Citizen Self-drafted"},
        {"item_en": "BPL Card / Income Certificate (if seeking free DLSA lawyer)", "item_hi": "बीपीएल कार्ड / आय प्रमाण पत्र (मुफ्त वकील हेतु)", "item_od": "BPL କାର୍ଡ ବା ଆୟ ପ୍ରମାଣପତ୍ର (ମାଗଣା ଓକିଲ ପାଇଁ)", "mandatory": 0, "purpose": "Sec 12 Legal Aid fee exemption", "issuing_authority": "Tahasildar Office"}
    ]
}
