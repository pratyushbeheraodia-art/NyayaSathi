from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class VoiceProcessRequest(BaseModel):
    text: str
    language: str = "en"
    privacy_mode: bool = False
    session_id: Optional[str] = "session-guest"

class ClarificationSubmitRequest(BaseModel):
    category: str
    language: str = "en"
    answers: Dict[str, str] = {}
    session_id: Optional[str] = "session-guest"

class EvidenceUploadRequest(BaseModel):
    session_id: str = "session-guest"
    file_name: str
    file_type: str
    file_size: Optional[str] = "1.2 MB"
    category: str
    notes: Optional[str] = ""

class EscalationRequest(BaseModel):
    query_category: str
    citizen_name: Optional[str] = "Anonymous Citizen"
    phone_number: Optional[str] = None
    issue_summary: str
    language: str = "en"
    priority: str = "NORMAL"

class DeadlineCalculateRequest(BaseModel):
    dispute_category: str
    incident_date: str # YYYY-MM-DD

class LegalAidEligibilityRequest(BaseModel):
    gender: str = "other" # female, male, transgender
    category: str = "general" # sc_st, obc, general, disabled, disaster_victim, worker
    annual_income: float = 0.0
    state: str = "Odisha"

class PrivacyWipeRequest(BaseModel):
    session_id: str
