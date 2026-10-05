import os
import random
import uuid
from datetime import datetime, timedelta
from typing import Optional, List, Dict, Any

from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from .database import get_connection, init_db
from .schemas import (
    VoiceProcessRequest,
    ClarificationSubmitRequest,
    EvidenceUploadRequest,
    EscalationRequest,
    DeadlineCalculateRequest,
    LegalAidEligibilityRequest,
    PrivacyWipeRequest
)
from .mock_ai import classify_query, refine_legal_path, CATEGORIES_META
from .rag_engine import search_legal_knowledge, get_category_knowledge
from .comprehensive_data import ALL_JOURNEYS, ALL_CHECKLISTS

# Initialize database on startup
init_db()

app = FastAPI(
    title="NyayaSathi Legal Assistance API",
    version="1.0.0",
    description="Multilingual Kiosk AI Legal Assistant for Rural and Citizen Empowerment"
)

# Enable CORS for local dev, Vite frontend, and Kiosk browsers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------------------------------------
# 1. Voice-to-Legal-Path
# -------------------------------------------------------------
@app.post("/api/voice/process")
def process_voice_query(req: VoiceProcessRequest):
    """Processes natural speech transcript or text input, classifies category, and returns instant legal path."""
    classification = classify_query(req.text, req.language)
    
    # If privacy mode is false, log to database for kiosk analytics
    if not req.privacy_mode:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO queries (user_text, language, detected_category, confidence, urgency, privacy_mode, session_id)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (req.text, req.language, classification["category"], classification["confidence"], classification["urgency"], 0, req.session_id))
        conn.commit()
        conn.close()

    return {
        "status": "SUCCESS",
        "input_text": req.text,
        "language": req.language,
        "classification": classification,
        "privacy_mode": req.privacy_mode,
        "session_id": req.session_id
    }

# -------------------------------------------------------------
# 2. Smart Clarification Flow
# -------------------------------------------------------------
@app.get("/api/clarification/questions/{category}")
def get_clarification_questions(category: str):
    """Returns targeted multiple-choice clarification questions for a legal domain."""
    alias_map = {
        "land_dispute": "land_property",
        "labor_dispute": "labor_employment",
        "family_dispute": "domestic_violence",
        "cyber_fraud": "cyber_fraud_privacy"
    }
    target = alias_map.get(category, category)
    meta = CATEGORIES_META.get(target, CATEGORIES_META["universal_legal_assistant"])
    return {
        "category": target,
        "questions": meta["questions"]
    }

@app.post("/api/clarification/submit")
def submit_clarification(req: ClarificationSubmitRequest):
    """Refines legal trajectory based on user's answers to clarification questions."""
    refined = refine_legal_path(req.category, req.answers, req.language)
    return refined

# -------------------------------------------------------------
# 3. Legal Journey Map (Visual Timeline)
# -------------------------------------------------------------
@app.get("/api/journey/{category}")
def get_legal_journey(category: str):
    """Returns interactive multi-stage legal roadmap with steps, timelines, and rights for ANY legal domain."""
    alias_map = {
        "land_dispute": "land_property",
        "labor_dispute": "labor_employment",
        "family_dispute": "domestic_violence",
        "cyber_fraud": "cyber_fraud_privacy"
    }
    target = alias_map.get(category, category)
    res = ALL_JOURNEYS.get(target, ALL_JOURNEYS["universal_legal_assistant"])
    return res

# -------------------------------------------------------------
# 4. Evidence Organizer
# -------------------------------------------------------------
@app.get("/api/evidence/{session_id}")
def list_evidence(session_id: str):
    """Retrieves uploaded evidence metadata for a given session."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM evidence_store WHERE session_id = ? ORDER BY id DESC", (session_id,))
    rows = cursor.fetchall()
    conn.close()
    return {"evidence": [dict(r) for r in rows]}

@app.post("/api/evidence/upload")
def upload_evidence(req: EvidenceUploadRequest):
    """Stores metadata and relevance score for citizen uploaded evidence (photos/slips/recordings)."""
    # Deterministic mock relevance score based on file type
    relevance = 92 if "pdf" in req.file_name.lower() or "receipt" in req.file_name.lower() else 85
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO evidence_store (session_id, file_name, file_type, file_size, category, notes, relevance_score)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (req.session_id, req.file_name, req.file_type, req.file_size, req.category, req.notes, relevance))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()

    return {
        "status": "SUCCESS",
        "evidence_id": new_id,
        "file_name": req.file_name,
        "relevance_score": relevance,
        "message": "Evidence securely cataloged for legal presentation."
    }

@app.delete("/api/evidence/{evidence_id}")
def delete_evidence(evidence_id: int):
    """Deletes an evidence record."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM evidence_store WHERE id = ?", (evidence_id,))
    conn.commit()
    conn.close()
    return {"status": "DELETED", "id": evidence_id}

# -------------------------------------------------------------
# 5. Document Checklist
# -------------------------------------------------------------
@app.get("/api/documents/checklist/{category}")
def get_document_checklist(category: str):
    """Returns statutory and recommended documents for any legal dispute."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM checklists WHERE category = ? ORDER BY mandatory DESC", (category,))
    rows = cursor.fetchall()
    conn.close()
    
    docs = [dict(r) for r in rows]
    if not docs:
        docs = ALL_CHECKLISTS.get(category, ALL_CHECKLISTS.get("universal_legal_assistant", []))
        # Add synthetic IDs if needed
        for i, d in enumerate(docs):
            if "id" not in d:
                d["id"] = i + 1
    return {"category": category, "documents": docs}

# -------------------------------------------------------------
# 6. Privacy Mode & Kiosk Wipe
# -------------------------------------------------------------
@app.post("/api/privacy/wipe-session")
def wipe_session(req: PrivacyWipeRequest):
    """Kiosk panic wipe: completely clears current session history, queries, and evidence metadata."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM evidence_store WHERE session_id = ?", (req.session_id,))
    cursor.execute("DELETE FROM queries WHERE session_id = ?", (req.session_id,))
    conn.commit()
    conn.close()

    return {
        "status": "WIPED",
        "session_id": req.session_id,
        "message": "All session data, voice queries, and files have been permanently cleared from kiosk memory."
    }

# -------------------------------------------------------------
# 7. Legal Information Display (RAG Articles)
# -------------------------------------------------------------
@app.get("/api/legal/articles")
def get_legal_articles(q: Optional[str] = "", lang: Optional[str] = "en", category: Optional[str] = None):
    """Retrieves plain-language legal articles across English, Hindi, and Odia."""
    results = search_legal_knowledge(q or "", lang or "en", category)
    return {"total": len(results), "articles": results}

@app.get("/api/legal/articles/{article_id}")
def get_single_article(article_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM knowledge_base WHERE id = ?", (article_id,))
    row = cursor.fetchone()
    conn.close()
    if not row:
        raise HTTPException(status_code=404, detail="Article not found")
    return dict(row)

# -------------------------------------------------------------
# 8. Official Resource Connector
# -------------------------------------------------------------
@app.get("/api/resources")
def get_resources():
    """Lists verified 24/7 helplines, government legal portals, and grievance systems."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM resources ORDER BY is_helpline DESC")
    rows = cursor.fetchall()
    conn.close()
    return {"resources": [dict(r) for r in rows]}

# -------------------------------------------------------------
# 9. Legal Aid Information & NALSA Eligibility Check
# -------------------------------------------------------------
@app.post("/api/legal-aid/check-eligibility")
def check_legal_aid_eligibility(req: LegalAidEligibilityRequest):
    """
    Evaluates free legal aid entitlement under Section 12 of Legal Services Authorities Act 1987.
    Eligible automatically:
    - Women and Children
    - SC / ST community members
    - Victims of human trafficking / beggar
    - Disabled individuals
    - Industrial workmen
    - Persons with annual income under ₹3,00,000 in Odisha (₹3,00,000 for High Court / Supreme Court ₹5,00,000)
    """
    is_eligible = False
    criteria_met = []

    if req.gender.lower() in ["female", "woman", "transgender", "other"]:
        is_eligible = True
        criteria_met.append("Entitled under Section 12(c): Women and Children get 100% Free Legal Aid irrespective of income.")

    if req.category.lower() in ["sc_st", "sc", "st"]:
        is_eligible = True
        criteria_met.append("Entitled under Section 12(a): Member of Scheduled Caste or Scheduled Tribe.")

    if req.category.lower() in ["worker", "workman", "labour"]:
        is_eligible = True
        criteria_met.append("Entitled under Section 12(e): Industrial workman / unorganized laborer.")

    if req.category.lower() in ["disabled", "divyang"]:
        is_eligible = True
        criteria_met.append("Entitled under Section 12(d): Person with disability.")

    if req.annual_income <= 300000.0:
        is_eligible = True
        criteria_met.append(f"Entitled under Section 12(h): Annual income (₹{req.annual_income:,.0f}) is within the statutory ₹3,00,000 limit for State Legal Services Authority.")

    nearest_office = {
        "name": "District Legal Services Authority (DLSA), Ganjam / Cuttack",
        "location": "District Court Complex, Ganjam / Cuttack, Odisha",
        "toll_free": "15100",
        "timings": "10:00 AM - 5:00 PM (Monday to Saturday)",
        "documents_needed": "Aadhaar Card, BPL Card / Income Certificate (if general category male)"
    }

    return {
        "eligible": is_eligible,
        "criteria_met": criteria_met,
        "nearest_office": nearest_office,
        "benefits": [
            "Free Senior Panel Advocate assigned to represent you in court",
            "All court fees, drafting charges, process fees, and typing paid by DLSA",
            "Certified copies of judgments provided free of cost",
            "Pre-litigation conciliation via Taluk Legal Services"
        ]
    }

# -------------------------------------------------------------
# 10. Case Information (Demo 5 Cases & CNR Lookup)
# -------------------------------------------------------------
@app.get("/api/cases")
def list_demo_cases():
    """Lists all pre-loaded demo cases."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM demo_cases")
    rows = cursor.fetchall()
    conn.close()

    cases = []
    for r in rows:
        c = dict(r)
        c["timeline"] = json.loads(c["timeline_json"]) if c["timeline_json"] else []
        c["documents"] = json.loads(c["documents_json"]) if c["documents_json"] else []
        cases.append(c)
    return {"cases": cases}

@app.get("/api/cases/{identifier}")
def get_case_by_identifier(identifier: str):
    """Looks up case by Case Number or 16-character CNR Number."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM demo_cases 
        WHERE case_number = ? OR cnr_number = ?
    """, (identifier, identifier))
    row = cursor.fetchone()
    conn.close()

    if not row:
        raise HTTPException(status_code=404, detail="Case number or CNR not found in registry.")

    c = dict(row)
    c["timeline"] = json.loads(c["timeline_json"]) if c["timeline_json"] else []
    c["documents"] = json.loads(c["documents_json"]) if c["documents_json"] else []
    return c

# -------------------------------------------------------------
# 11. Deadline Guardian (Limitation Calculator)
# -------------------------------------------------------------
@app.get("/api/deadlines")
def get_deadlines():
    """Returns statutory limitation rules for major dispute types."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM deadlines")
    rows = cursor.fetchall()
    conn.close()
    return {"deadlines": [dict(r) for r in rows]}

@app.post("/api/deadlines/calculate")
def calculate_deadline(req: DeadlineCalculateRequest):
    """Calculates limitation expiry date and remaining days based on incident date."""
    try:
        inc_date = datetime.strptime(req.incident_date, "%Y-%m-%d").date()
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD.")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM deadlines WHERE dispute_type_en LIKE ? LIMIT 1", (f"%{req.dispute_category}%",))
    row = cursor.fetchone()
    conn.close()

    limit_days = row["days_limit"] if row else 365
    act_ref = row["act_reference"] if row else "Limitation Act 1963"

    expiry_date = inc_date + timedelta(days=limit_days)
    today = date.today()
    days_remaining = (expiry_date - today).days

    if days_remaining < 0:
        status = "EXPIRED"
        badge_color = "red"
        advice = f"Limitation period expired {abs(days_remaining)} days ago. You must file a Condonation of Delay Application (Section 5 of Limitation Act) explaining valid cause."
    elif days_remaining <= 15:
        status = "CRITICAL_WARNING"
        badge_color = "amber"
        advice = f"URGENT: Only {days_remaining} days left to preserve statutory rights before court doors close!"
    else:
        status = "SAFE"
        badge_color = "green"
        advice = f"You have {days_remaining} days remaining to file your petition without penalty."

    return {
        "incident_date": str(inc_date),
        "expiry_date": str(expiry_date),
        "days_remaining": days_remaining,
        "limit_days": limit_days,
        "act_reference": act_ref,
        "status": status,
        "badge_color": badge_color,
        "advice": advice
    }

# -------------------------------------------------------------
# 12. Human Help Escalation
# -------------------------------------------------------------
@app.post("/api/escalation/request")
def request_human_help(req: EscalationRequest):
    """Registers citizen request for physical Paralegal Volunteer (PLV) / Tele-Law lawyer booking."""
    token = f"NYA-{datetime.now().year}-{random.randint(1000, 9999)}"
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO escalations (token_number, query_category, citizen_name, phone_number, issue_summary, language, status, priority)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (token, req.query_category, req.citizen_name or "Anonymous Citizen", req.phone_number, req.issue_summary, req.language, "PENDING", req.priority))
    conn.commit()
    conn.close()

    return {
        "status": "QUEUED",
        "token_number": token,
        "priority": req.priority,
        "kiosk_counter": "Counter #2 (Gram Panchayat Kiosk)",
        "plv_contact": "Paralegal Volunteer S. Mohapatra (+91 94370 00000)",
        "message": "Assistance request logged. Please present your token slip at the counter or wait for call."
    }

@app.get("/api/escalation/status/{token}")
def check_escalation_status(token: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM escalations WHERE token_number = ?", (token,))
    row = cursor.fetchone()
    conn.close()
    if not row:
        raise HTTPException(status_code=404, detail="Token not found.")
    return dict(row)

# -------------------------------------------------------------
# 13. Voice Output (TTS Phrases)
# -------------------------------------------------------------
@app.get("/api/voice/phrases")
def get_tts_phrases(lang: Optional[str] = "en"):
    """Returns audio prompt strings for Kiosk TTS synthesizer."""
    phrases = {
        "en": {
            "welcome": "Welcome to NyayaSathi, your digital legal companion. Please speak your problem or select a button.",
            "listening": "Listening... Please speak your legal issue clearly into the microphone.",
            "emergency_alert": "Emergency detected. Press the red button to call 112 or 181 immediately.",
            "print_ready": "Your Kiosk Action Slip is ready to print.",
            "privacy_wipe": "Privacy mode activated. All your conversation details have been wiped."
        },
        "hi": {
            "welcome": "न्यायसाथी में आपका स्वागत है। कृपया अपनी कानूनी समस्या बोलें या स्क्रीन पर विकल्प चुनें।",
            "listening": "सुन रहे हैं... कृपया माइक्रोफ़ोन में अपनी समस्या स्पष्ट रूप से बताएं।",
            "emergency_alert": "आपातकालीन स्थिति! तत्काल 112 या 181 पर कॉल करने के लिए लाल बटन दबाएं।",
            "print_ready": "आपकी कानूनी कार्य योजना पर्ची प्रिंट के लिए तैयार है।",
            "privacy_wipe": "गोपनीयता मोड सक्रिय। आपकी सभी बातचीत और डेटा मिटा दिया गया है।"
        },
        "od": {
            "welcome": "ନ୍ୟାୟସାଥୀକୁ ସ୍ୱାଗତ। ଦୟାକରି ଆପଣଙ୍କ ଆଇନଗତ ସମସ୍ୟା କୁହନ୍ତୁ କିମ୍ବା ବଟନ୍ ଚୟନ କରନ୍ତୁ।",
            "listening": "ଶୁଣୁଛୁ... ଦୟାକରି ମାଇକ୍ରୋଫୋନରେ ସ୍ପଷ୍ଟ ଭାବେ ଆପଣଙ୍କ ସମସ୍ୟା କୁହନ୍ତୁ।",
            "emergency_alert": "ଜରୁରୀକାଳୀନ ପରିସ୍ଥିତି! ତୁରନ୍ତ ୧୧୨ କିମ୍ବା ୧୮୧ କଲ୍ କରିବା ପାଇଁ ଲାଲ୍ ବଟନ୍ ଦବାନ୍ତୁ।",
            "print_ready": "ଆପଣଙ୍କ ନ୍ୟାୟ କାର୍ଯ୍ୟ ପତ୍ର ପ୍ରିଣ୍ଟ୍ ପାଇଁ ପ୍ରସ୍ତୁତ।",
            "privacy_wipe": "ଗୋପନୀୟତା ସୁରକ୍ଷିତ। ଆପଣଙ୍କ ସମସ୍ତ ତଥ୍ୟ କିଓସ୍କ ମେମୋରୀରୁ ଲିଭାଇ ଦିଆଯାଇଛି।"
        }
    }
    return phrases.get(lang, phrases["en"])

# -------------------------------------------------------------
# 14. Action Summary (Download / Print)
# -------------------------------------------------------------
@app.post("/api/summary/generate-slip")
def generate_action_slip(payload: Dict[str, Any]):
    """Generates structured printable Kiosk Action Slip / Nyaya Patra with QR tracking payload."""
    category = payload.get("category", "land_dispute")
    lang = payload.get("language", "en")
    user_name = payload.get("name", "Citizen Beneficiary")
    token = f"NYA-{datetime.now().strftime('%Y%m%d')}-{random.randint(100, 999)}"

    meta = CATEGORIES_META.get(category, CATEGORIES_META.get("land_property", CATEGORIES_META["universal_legal_assistant"]))
    
    slip_data = {
        "kiosk_id": "KIOSK-OD-042 (Ganjam Chatrapur Tahasil)",
        "slip_token": token,
        "date_time": datetime.now().strftime("%d-%m-%Y %I:%M %p"),
        "citizen_name": user_name,
        "category_title": meta.get(lang, meta["en"]),
        "applicable_law": meta["default_law"],
        "recommended_forum": meta["forum"],
        "statutory_cost": meta["cost"],
        "next_3_actions": [
            "1. Visit the nearest Taluk Legal Services Committee (TLSC) counter.",
            "2. Carry Aadhaar Card and stamped proof/bills listed in Document Checklist.",
            "3. Quote Token number at helpdesk for free panel lawyer allotment."
        ],
        "helplines": {
            "National Legal Aid": "15100",
            "Women Helpline": "181",
            "Cyber Fraud": "1930",
            "Emergency Police/Ambulance": "112"
        },
        "qr_verification_code": f"NYAYASATHI://VERIFY/{token}/{category}"
    }

    return slip_data

# -------------------------------------------------------------
# Admin Dashboard & Hardware Architecture Specs
# -------------------------------------------------------------
@app.get("/api/admin/metrics")
def get_admin_metrics():
    """Returns analytics telemetry for Kiosk monitoring."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM queries")
    total_queries = cursor.fetchone()[0]

    cursor.execute("SELECT detected_category, COUNT(*) as cnt FROM queries GROUP BY detected_category")
    by_category = {r[0]: r[1] for r in cursor.fetchall()}

    cursor.execute("SELECT language, COUNT(*) as cnt FROM queries GROUP BY language")
    by_language = {r[0]: r[1] for r in cursor.fetchall()}

    cursor.execute("SELECT COUNT(*) FROM escalations")
    total_escalations = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM evidence_store")
    total_evidence_files = cursor.fetchone()[0]

    conn.close()

    return {
        "kiosk_id": "KIOSK-OD-042",
        "location": "Ganjam District Collectorate Kiosk (Odisha)",
        "uptime": "99.8%",
        "total_queries": total_queries + 124, # Seed base for realistic dashboard
        "by_category": {
            "land_dispute": by_category.get("land_dispute", 0) + 54,
            "labor_dispute": by_category.get("labor_dispute", 0) + 32,
            "consumer_dispute": by_category.get("consumer_dispute", 0) + 18,
            "family_dispute": by_category.get("family_dispute", 0) + 12,
            "cyber_fraud": by_category.get("cyber_fraud", 0) + 8
        },
        "by_language": {
            "od": by_language.get("od", 0) + 68,
            "hi": by_language.get("hi", 0) + 38,
            "en": by_language.get("en", 0) + 18
        },
        "escalations_pending": total_escalations,
        "evidence_stored": total_evidence_files + 15,
        "kiosk_battery_backup": "100% (Solar UPS Connected)",
        "connectivity": "4G GSM Active (Primary) / Fiber (Standby)"
    }

@app.get("/api/admin/queries")
def get_admin_queries():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM queries ORDER BY id DESC LIMIT 20")
    rows = cursor.fetchall()
    conn.close()
    return {"queries": [dict(r) for r in rows]}

@app.get("/api/admin/escalations")
def get_admin_escalations():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM escalations ORDER BY id DESC LIMIT 20")
    rows = cursor.fetchall()
    conn.close()
    return {"escalations": [dict(r) for r in rows]}

@app.get("/api/system/info")
def get_system_info():
    """Returns Kiosk hardware architecture and demo mode status."""
    return {
        "kiosk_model": "NyayaSathi Rural Kiosk V2.1",
        "processor": "Intel N100 Quad-Core @ 3.4GHz (Fanless Ruggedized)",
        "display": "7-inch Waveshare 1024x600 IPS Capacitive Touchscreen (High-Bright 450 nits)",
        "audio_input": "Dual MEMS Directional Noise-Cancelling Microphone Array",
        "audio_output": "3W Dual Sealed Stereo Speakers (Clear Voice Tuned)",
        "printer": "58mm Embedded Thermal Receipt Printer (Serial/USB)",
        "peripherals": "Integrated Optical Document Scanner (A4/Card)",
        "power_supply": "12V DC Solar/Battery Micro-Inverter with 6-Hour Fallback",
        "operating_system": "Custom Debian / Windows Kiosk Shell",
        "demo_mode": True,
        "mock_ai_engine": "Deterministic Low-Latency RAG Engine v1.0",
        "offline_support": "Local SQLite & Fallback Cache Enabled"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
