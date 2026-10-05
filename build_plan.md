# NyayaSathi Build Plan

## Architecture Overview

```
Frontend (React + Vite)     ←→     Backend (Python FastAPI)     ←→     SQLite DB
     ↕                                    ↕
Web Speech API                     Mock AI / RAG Engine
```

## Phase 1: Project Scaffolding
1. Initialize Vite + React frontend
2. Initialize FastAPI backend
3. Set up SQLite database schema
4. Create project README

## Phase 2: Backend Core
1. FastAPI app with CORS
2. SQLite models (queries, knowledge base, documents)
3. Mock AI classification engine
4. RAG knowledge base with sample legal data
5. Demo scenarios (5 cases)
6. API endpoints for all 14 features

## Phase 3: Frontend Core
1. Design system (CSS variables, theme)
2. Multilingual i18n system (EN, HI, OD)
3. Home screen with all buttons
4. Language selector
5. Router setup

## Phase 4: Feature Implementation
1. Voice-to-Legal-Path (Web Speech API)
2. Smart Clarification flow
3. Legal Journey Map (visual timeline)
4. Evidence Organizer
5. Document Checklist
6. Privacy Mode
7. Legal Information display
8. Official Resource Connector
9. Legal Aid Information
10. Case Information (demo)
11. Deadline Guardian
12. Human Help Escalation
13. Voice Output (TTS)
14. Action Summary (download/print)

## Phase 5: Polish
1. Admin dashboard
2. Demo mode toggle
3. Hardware architecture diagram
4. Final styling & animations
5. Documentation

## Key Decisions
- **Mock AI**: All AI features use deterministic mock responses for demo reliability
- **Web Speech API**: Browser-native speech recognition (no external API needed)
- **Single-page app**: React Router for navigation
- **Responsive**: Works on 7" touchscreen to desktop
