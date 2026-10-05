import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useLanguage } from '../context/LanguageContext';
import { useKiosk } from '../context/KioskContext';
import VoiceModal from '../components/VoiceModal';
import AudioSpeaker from '../components/AudioSpeaker';
import { 
  Mic, 
  Map, 
  FolderCheck, 
  FileCheck2, 
  Scale, 
  Search, 
  Clock, 
  Users, 
  PhoneCall, 
  BookOpen, 
  Printer, 
  Cpu, 
  Sparkles,
  ArrowRight,
  ShieldCheck
} from 'lucide-react';

export default function HomePage() {
  const { lang, t, speakText } = useLanguage();
  const { setActiveAnalysis, setActiveCategory, privacyMode, sessionId } = useKiosk();
  const [isVoiceOpen, setIsVoiceOpen] = useState(false);
  const navigate = useNavigate();

  const handleQuickDemo = async (queryText, category) => {
    setActiveCategory(category);
    try {
      const res = await fetch('/api/voice/process', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          text: queryText,
          language: lang,
          privacy_mode: privacyMode,
          session_id: sessionId
        })
      });
      const data = await res.json();
      if (data.status === 'SUCCESS') {
        setActiveAnalysis(data.classification);
        const speechMsg = lang === 'hi' 
          ? `आपकी समस्या ${data.classification.title} के अंतर्गत वर्गीकृत की गई है।`
          : lang === 'od'
          ? `ଆପଣଙ୍କ ସମସ୍ୟା ${data.classification.title} ଅଧୀନରେ ଚିହ୍ନଟ ହୋଇଛି।`
          : `Your query has been classified under ${data.classification.title}.`;
        speakText(speechMsg);
        navigate('/voice');
      }
    } catch (e) {
      navigate('/voice');
    }
  };

  return (
    <div className="kiosk-container">
      {/* Hero Section: Big Voice Prompt */}
      <section className="hero-voice-section">
        <div style={{ display: 'inline-flex', alignItems: 'center', gap: '8px', background: '#dbeafe', color: '#1e40af', padding: '6px 16px', borderRadius: '9999px', fontSize: '14px', fontWeight: 700, marginBottom: '8px' }}>
          <Sparkles size={16} /> {t('voiceAssistant')}
        </div>

        <h2 style={{ fontSize: '28px', fontWeight: 800, color: '#0f172a', marginBottom: '4px' }}>
          {t('speakIssuePrompt')}
        </h2>
        <p style={{ color: '#475569', fontSize: '16px', maxWidth: '640px' }}>
          {lang === 'hi' 
            ? "बिना किसी दलाल या वकील के अपनी भाषा में कानूनी अधिकार, आवश्यक दस्तावेज़ और निशुल्क सरकारी सहायता जानें।"
            : lang === 'od'
            ? "ବିନା କୌଣସି ଖର୍ଚ୍ଚ ବା ଦଲାଲରେ ଆପଣଙ୍କ ଭାଷାରେ ଆଇନଗତ ଅଧିକାର, ଦରକାରୀ କାଗଜପତ୍ର ଏବଂ ମାଗଣା ସରକାରୀ ସହାୟତା ଜାଣନ୍ତୁ।"
            : "Get instant statutory provisions, document checklists, limitation deadlines, and free NALSA legal aid guidance in your language."}
        </p>

        {/* Big Mic Button */}
        <button 
          className="big-mic-button"
          onClick={() => setIsVoiceOpen(true)}
          title="Click to speak your problem"
        >
          <Mic size={44} />
        </button>

        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <span style={{ fontSize: '14px', fontWeight: 700, color: '#2563eb' }}>
            {lang === 'hi' ? "माइक दबाकर बोलें" : lang === 'od' ? "ମାଇକ୍ ଦବାଇ କୁହନ୍ତୁ" : "Tap Microphone to Speak"}
          </span>
          <AudioSpeaker 
            text={lang === 'hi' ? "माइक बटन दबाएं और अपनी समस्या बताएं" : lang === 'od' ? "ମାଇକ୍ ବଟନ୍ ଦବାନ୍ତୁ ଏବଂ ଆପଣଙ୍କ ସମସ୍ୟା କୁହନ୍ତୁ" : "Tap the microphone to speak your legal issue"} 
            label="Audio Help" 
          />
        </div>

        {/* Quick Sample Situation Pills */}
        <div style={{ marginTop: '16px', width: '100%' }}>
          <div style={{ fontSize: '13px', fontWeight: 600, color: '#64748b', marginBottom: '8px' }}>
            {t('quickDemos')}
          </div>
          <div className="quick-queries">
            <button 
              className="query-pill"
              onClick={() => handleQuickDemo(t('sampleCriminal'), 'criminal_police')}
            >
              ⚖️ {lang === 'hi' ? "पुलिस एफआईआर / जमानत" : lang === 'od' ? "ପୋଲିସ ଏଫଆଇଆର / ଜାମିନ" : "Police FIR & Bail (BNSS)"}
            </button>
            <button 
              className="query-pill"
              onClick={() => handleQuickDemo(t('sampleLand'), 'land_property')}
            >
              🌾 {lang === 'hi' ? "जमीन मेढ़ / अवैध कब्जा" : lang === 'od' ? "ଜମି ସୀମା / ବେଦଖଲ" : "Land Encroachment"}
            </button>
            <button 
              className="query-pill"
              onClick={() => handleQuickDemo(t('sampleCheque'), 'banking_debt_cheque')}
            >
              💰 {lang === 'hi' ? "चेक बाउंस धारा 138" : lang === 'od' ? "ଚେକ୍ ବାଉନ୍ସ ଧାରା ୧୩୮" : "Cheque Bounce (Sec 138)"}
            </button>
            <button 
              className="query-pill"
              onClick={() => handleQuickDemo(t('sampleLabor'), 'labor_employment')}
            >
              🧱 {lang === 'hi' ? "बकाया मजदूरी / नौकरी" : lang === 'od' ? "ବକେୟା ମଜୁରୀ / ଚାକିରି" : "Unpaid Wages & Job"}
            </button>
            <button 
              className="query-pill"
              onClick={() => handleQuickDemo(t('sampleSuccession'), 'property_succession')}
            >
              📜 {lang === 'hi' ? "पैतृक संपत्ति / बेटियों का हक" : lang === 'od' ? "ପୈତୃକ ସମ୍ପତ୍ତି / ଝିଅର ଭାଗ" : "Inheritance & Daughter Share"}
            </button>
            <button 
              className="query-pill"
              onClick={() => handleQuickDemo(t('sampleSenior'), 'senior_citizen_welfare')}
            >
              👴 {lang === 'hi' ? "वरिष्ठ नागरिक / माता-पिता भरण" : lang === 'od' ? "ବରିଷ୍ଠ ନାଗରିକ / ଭରଣପୋଷଣ" : "Senior Citizen Maintenance"}
            </button>
            <button 
              className="query-pill"
              onClick={() => handleQuickDemo(t('sampleFamily'), 'domestic_violence')}
            >
              🛡️ {lang === 'hi' ? "घरेलू हिंसा / गुजारा भत्ता" : lang === 'od' ? "ଘରୋଇ ହିଂସା / ଭରଣପୋଷଣ" : "Domestic Protection & Alimony"}
            </button>
            <button 
              className="query-pill"
              onClick={() => handleQuickDemo(t('sampleCyber'), 'cyber_fraud_privacy')}
            >
              💳 {lang === 'hi' ? "साइबर / यूपीआई ठगी 1930" : lang === 'od' ? "ସାଇବର / UPI ଠକେଇ ୧୯୩୦" : "Cyber Fraud 1930"}
            </button>
            <button 
              className="query-pill"
              onClick={() => handleQuickDemo(t('sampleTenancy'), 'tenancy_realestate')}
            >
              🏢 {lang === 'hi' ? "रेरा बिल्डर / किरायेदारी" : lang === 'od' ? "ରେରା ବିଲ୍ଡର / ଘରଭଡ଼ା" : "RERA Builder & Tenancy"}
            </button>
            <button 
              className="query-pill"
              onClick={() => handleQuickDemo(t('sampleConsumer'), 'consumer_dispute')}
            >
              🚜 {lang === 'hi' ? "खराब उत्पाद / उपभोक्ता फोरम" : lang === 'od' ? "ତ୍ରୁଟିପୂର୍ଣ୍ଣ ମେସିନ / ୱାରେଣ୍ଟି" : "Consumer Rights & Warranty"}
            </button>
          </div>
        </div>
      </section>

      {/* Touch Kiosk Features Grid */}
      <div className="kiosk-grid">
        {/* 1. Voice-to-Legal-Path */}
        <div className="kiosk-card featured" onClick={() => setIsVoiceOpen(true)}>
          <span className="card-badge">AI Assistant</span>
          <div className="card-icon-wrapper white">
            <Mic size={26} />
          </div>
          <h3>{t('cardVoiceTitle')}</h3>
          <p>{t('cardVoiceDesc')}</p>
          <div style={{ marginTop: 'auto', display: 'flex', alignItems: 'center', gap: '6px', fontWeight: 700, fontSize: '14px', paddingTop: '12px' }}>
            <span>Start Speaking</span> <ArrowRight size={16} />
          </div>
        </div>

        {/* 2. Legal Journey Map */}
        <Link to="/journey" className="kiosk-card">
          <div className="card-icon-wrapper blue">
            <Map size={26} />
          </div>
          <h3>{t('cardJourneyTitle')}</h3>
          <p>{t('cardJourneyDesc')}</p>
        </Link>

        {/* 3. Evidence Organizer */}
        <Link to="/evidence" className="kiosk-card">
          <div className="card-icon-wrapper green">
            <FolderCheck size={26} />
          </div>
          <h3>{t('cardEvidenceTitle')}</h3>
          <p>{t('cardEvidenceDesc')}</p>
        </Link>

        {/* 4. Document Checklist */}
        <Link to="/checklist" className="kiosk-card">
          <div className="card-icon-wrapper orange">
            <FileCheck2 size={26} />
          </div>
          <h3>{t('cardChecklistTitle')}</h3>
          <p>{t('cardChecklistDesc')}</p>
        </Link>

        {/* 5. Free Legal Aid */}
        <Link to="/legal-aid" className="kiosk-card">
          <div className="card-icon-wrapper purple">
            <Scale size={26} />
          </div>
          <h3>{t('cardLegalAidTitle')}</h3>
          <p>{t('cardLegalAidDesc')}</p>
        </Link>

        {/* 6. Case Status Tracker */}
        <Link to="/cases" className="kiosk-card">
          <div className="card-icon-wrapper blue">
            <Search size={26} />
          </div>
          <h3>{t('cardCasesTitle')}</h3>
          <p>{t('cardCasesDesc')}</p>
        </Link>

        {/* 7. Deadline Guardian */}
        <Link to="/deadlines" className="kiosk-card">
          <div className="card-icon-wrapper red">
            <Clock size={26} />
          </div>
          <h3>{t('cardDeadlinesTitle')}</h3>
          <p>{t('cardDeadlinesDesc')}</p>
        </Link>

        {/* 8. Human Escalation */}
        <Link to="/escalate" className="kiosk-card">
          <div className="card-icon-wrapper green">
            <Users size={26} />
          </div>
          <h3>{t('cardEscalateTitle')}</h3>
          <p>{t('cardEscalateDesc')}</p>
        </Link>

        {/* 9. Official Resources */}
        <Link to="/resources" className="kiosk-card">
          <div className="card-icon-wrapper orange">
            <PhoneCall size={26} />
          </div>
          <h3>{t('cardResourcesTitle')}</h3>
          <p>{t('cardResourcesDesc')}</p>
        </Link>

        {/* 10. Legal Knowledge Guides */}
        <Link to="/legal-guides" className="kiosk-card">
          <div className="card-icon-wrapper purple">
            <BookOpen size={26} />
          </div>
          <h3>{t('cardArticlesTitle')}</h3>
          <p>{t('cardArticlesDesc')}</p>
        </Link>

        {/* 11. Action Summary (Print Slip) */}
        <Link to="/slip" className="kiosk-card">
          <div className="card-icon-wrapper blue">
            <Printer size={26} />
          </div>
          <h3>{t('cardSummaryTitle')}</h3>
          <p>{t('cardSummaryDesc')}</p>
        </Link>

        {/* 12. Admin & Hardware */}
        <Link to="/admin" className="kiosk-card">
          <div className="card-icon-wrapper green">
            <Cpu size={26} />
          </div>
          <h3>{t('cardAdminTitle')}</h3>
          <p>{t('cardAdminDesc')}</p>
        </Link>
      </div>

      {/* Voice Modal Dialog */}
      <VoiceModal isOpen={isVoiceOpen} onClose={() => setIsVoiceOpen(false)} />
    </div>
  );
}
