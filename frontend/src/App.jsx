import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { LanguageProvider } from './context/LanguageContext';
import { KioskProvider } from './context/KioskContext';

import TopBar from './components/TopBar';
import EmergencyBanner from './components/EmergencyBanner';
import KioskFooter from './components/KioskFooter';

import HomePage from './pages/HomePage';
import VoicePathPage from './pages/VoicePathPage';
import ClarificationPage from './pages/ClarificationPage';
import JourneyPage from './pages/JourneyPage';
import EvidencePage from './pages/EvidencePage';
import ChecklistPage from './pages/ChecklistPage';
import LegalAidPage from './pages/LegalAidPage';
import CaseTrackerPage from './pages/CaseTrackerPage';
import DeadlinePage from './pages/DeadlinePage';
import ResourcesPage from './pages/ResourcesPage';
import LegalKnowledgePage from './pages/LegalKnowledgePage';
import EscalationPage from './pages/EscalationPage';
import ActionSlipPage from './pages/ActionSlipPage';
import AdminPage from './pages/AdminPage';

export default function App() {
  return (
    <LanguageProvider>
      <KioskProvider>
        <Router>
          <div style={{ display: 'flex', flexDirection: 'column', minHeight: '100vh' }}>
            <TopBar />
            <EmergencyBanner />
            <main style={{ flex: 1, display: 'flex', flexDirection: 'column' }}>
              <Routes>
                <Route path="/" element={<HomePage />} />
                <Route path="/voice" element={<VoicePathPage />} />
                <Route path="/clarification" element={<ClarificationPage />} />
                <Route path="/journey" element={<JourneyPage />} />
                <Route path="/evidence" element={<EvidencePage />} />
                <Route path="/checklist" element={<ChecklistPage />} />
                <Route path="/legal-aid" element={<LegalAidPage />} />
                <Route path="/cases" element={<CaseTrackerPage />} />
                <Route path="/deadlines" element={<DeadlinePage />} />
                <Route path="/resources" element={<ResourcesPage />} />
                <Route path="/legal-guides" element={<LegalKnowledgePage />} />
                <Route path="/escalate" element={<EscalationPage />} />
                <Route path="/slip" element={<ActionSlipPage />} />
                <Route path="/admin" element={<AdminPage />} />
              </Routes>
            </main>
            <KioskFooter />
          </div>
        </Router>
      </KioskProvider>
    </LanguageProvider>
  );
}
