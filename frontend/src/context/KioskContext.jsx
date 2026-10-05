import React, { createContext, useContext, useState, useEffect } from 'react';

const KioskContext = createContext();

export const KioskProvider = ({ children }) => {
  const [sessionId, setSessionId] = useState(() => {
    return 'kiosk-sess-' + Math.random().toString(36).substring(2, 9);
  });
  const [privacyMode, setPrivacyMode] = useState(false);
  const [demoMode, setDemoMode] = useState(true);
  const [activeCategory, setActiveCategory] = useState('land_dispute');
  const [activeAnalysis, setActiveAnalysis] = useState(null);
  const [clarificationAnswers, setClarificationAnswers] = useState({});

  const togglePrivacyMode = () => {
    setPrivacyMode(prev => !prev);
  };

  const wipeAllSessionData = async () => {
    try {
      await fetch('/api/privacy/wipe-session', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ session_id: sessionId })
      });
    } catch (e) {
      console.warn("Wipe API error", e);
    }
    // Generate new anonymous session ID
    setSessionId('kiosk-sess-' + Math.random().toString(36).substring(2, 9));
    setActiveAnalysis(null);
    setClarificationAnswers({});
    setActiveCategory('land_dispute');
  };

  return (
    <KioskContext.Provider value={{
      sessionId,
      privacyMode,
      togglePrivacyMode,
      demoMode,
      setDemoMode,
      activeCategory,
      setActiveCategory,
      activeAnalysis,
      setActiveAnalysis,
      clarificationAnswers,
      setClarificationAnswers,
      wipeAllSessionData
    }}>
      {children}
    </KioskContext.Provider>
  );
};

export const useKiosk = () => useContext(KioskContext);
