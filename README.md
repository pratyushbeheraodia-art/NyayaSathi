# NyayaSathi (ନ୍ୟାୟସାଥୀ / न्यायसाथी)

**Citizen Legal Assistance & Fast-Track Redressal Kiosk**  
*Empowering rural citizens, migrant laborers, and underserved communities with AI-guided legal rights, vernacular voice assistance, and procedural navigation.*

---

## 🏛️ Architecture Overview

```
Frontend (React 19 + Vite)        ←→        Backend (FastAPI + Python 3.14)        ←→        SQLite Database
           ↕                                                  ↕
   Web Speech API (STT & TTS)                          Mock AI / RAG Engine
```

NyayaSathi is engineered for public rural kiosks (e.g., Gram Panchayat Common Service Centers, Tahasil offices, and District Courts in Odisha and across India). It features **zero external proprietary API dependencies**, running entirely on deterministic local mock AI and browser-native Web Speech recognition and synthesis.

---

## ✨ Features Implemented (All 14 Modules)

| # | Feature | Description | Key Statutory Ground |
|---|---|---|---|
| 1 | **Voice-to-Legal-Path** | Speak grievance in Odia, Hindi, or English; instant AI classification & roadmap | BNS 2023, BNSS 2023 |
| 2 | **Smart Clarification Flow** | Interactive dynamic questions that refine case facts and offer tailored advice | Procedural Analysis |
| 3 | **Legal Journey Map** | Visual timeline from initial grievance to mediation and court orders | Dispute Timelines |
| 4 | **Evidence Organizer** | Catalog boundary photos, wage records, receipts, and injury slips | Bharatiya Sakshya Adhiniyam 2023 |
| 5 | **Document Checklist** | Readiness tracker of mandatory papers and issuing authorities (Patta, RI maps, etc.) | Revenue & Court Rules |
| 6 | **Privacy & Panic Wipe Mode** | Public kiosk incognito session with one-touch data clearing (no PII persistence) | Digital Privacy Standard |
| 7 | **Legal Rights Guides** | Plain-language statutory search across BNS, BNSS, CPA 2019, and Labour codes | Citizen Law Digest |
| 8 | **Official Resource Connector** | Verified 24/7 helplines (NALSA 15100, Cyber 1930, Women 181, Police 112) | National Portals |
| 9 | **Free Legal Aid (NALSA)** | Section 12 Legal Services Authorities Act eligibility calculator | Sec 12 LSA Act 1987 |
| 10 | **Case Status Tracker** | 16-character CNR lookup with hearing calendar, order sheets, and 5 demo cases | e-Courts System |
| 11 | **Deadline Guardian** | Statutory limitation calculator with color-coded expiry warnings | Limitation Act 1963 |
| 12 | **Human Help Escalation** | Book in-person Paralegal Volunteers (PLV) or virtual Tele-Law advocates | PLV Kiosk Scheme |
| 13 | **Voice Output (TTS)** | Accessible read-aloud voice playback using Web Speech Synthesis API | Universal Accessibility |
| 14 | **Action Summary (Nyaya Patra)** | Printable and downloadable legal action slip with QR code tracking | Kiosk Receipt Mechanism |

---

## 5 Pre-Loaded Realistic Demo Scenarios

1. **🌾 Land Encroachment & Mutation Dispute** (`LAND/2026/089`, CNR: `ODGN01-004521-2026`): Boundary wall encroachment in Chatrapur, Ganjam; RI demarcation and Tahasildar proceeding.
2. **🧱 Unpaid Wages for Migrant Brick Kiln Workers** (`LAB/2026/142`, CNR: `ODKH02-001984-2026`): ₹48,000 unpaid wages; Assistant Labour Commissioner Form VI conciliation.
3. **🚜 Defective Paddy Thresher Machine Warranty** (`CONS/2026/304`, CNR: `ODCT03-009120-2026`): Farmer denied warranty; District Consumer Commission claim.
4. **🛡️ Domestic Protection & Maintenance** (`DV/2026/058`, CNR: `ODPU04-003418-2026`): Urgent residence protection and monthly sustenance under PWDVA 2005.
5. **💳 Cyber Bank Phishing & UPI Debit** (`CYB/2026/911`, CNR: `ODBB05-008762-2026`): ₹34,500 theft; 1930 Golden Hour freeze and BNSS 457 recovery petition.

---

## 🖥️ Hardware Architecture

- **Computing Unit**: Fanless Ruggedized Intel N100 Quad-Core @ 3.4GHz / Raspberry Pi 5
- **Touch Display**: 7" Waveshare 1024x600 IPS Capacitive Multi-touch (450 nits)
- **Audio**: Dual MEMS Directional Noise-Cancelling Microphone Array + Dual 3W Acoustic Voice Speakers
- **Thermal Printer**: Embedded 58mm Thermal Receipt Mechanism for instant Nyaya Patra printing
- **Connectivity**: 4G LTE GSM Modem (eSIM auto-failover) + Local SQLite offline cache
- **Power**: 12V LiFePO4 Battery with Solar Micro-Inverter (6-hour continuous backup)

---

## 🚀 Quickstart Guide

### 1. Backend Setup (FastAPI)

```bash
# Python 3.10+ required
cd backend
python -m pip install -r requirements.txt
python run.py
```
*Backend runs on `http://127.0.0.1:8000` (Interactive API docs at `http://127.0.0.1:8000/docs`).*

### 2. Frontend Setup (React + Vite)

```bash
cd frontend
npm install
npm run dev
```
*Frontend runs on `http://localhost:5173` with reverse proxy configured to FastAPI.*

---

## 🌐 Multilingual Support

- **English (EN)**
- **हिंदी (HI)** - Hindi
- **ଓଡ଼ିଆ (OD)** - Odia

Toggle languages instantly via the top navigation bar or through speech prompts.

---

## 📜 License
Developed for Open Public Citizen Justice & NALSA Legal Aid Initiatives.
