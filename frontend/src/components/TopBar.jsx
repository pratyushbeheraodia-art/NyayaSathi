import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useLanguage } from '../context/LanguageContext';
import { useKiosk } from '../context/KioskContext';
import { 
  Scale, 
  Shield, 
  ShieldAlert, 
  Trash2, 
  Type, 
  Eye, 
  Wifi, 
  BatteryCharging, 
  Home,
  Volume2
} from 'lucide-react';

export default function TopBar() {
  const { lang, setLang, t, cycleFontSize, highContrast, setHighContrast, speakText } = useLanguage();
  const { privacyMode, togglePrivacyMode, wipeAllSessionData } = useKiosk();
  const navigate = useNavigate();

  const handlePanicWipe = async () => {
    if (window.confirm("Quick Clear will permanently erase this session's history and audio data. Proceed?")) {
      await wipeAllSessionData();
      speakText("Session wiped. You are now safely at home screen.");
      navigate('/');
    }
  };

  return (
    <header className="kiosk-header">
      {/* Kiosk status bar */}
      <div className="kiosk-top-status">
        <div style={{ display: 'flex', alignItems: 'center', gap: '16px' }}>
          <span className="status-badge">
            <span className="status-dot"></span>
            KIOSK #OD-042 | Ganjam Collectorate
          </span>
          <span style={{ display: 'inline-flex', alignItems: 'center', gap: '4px' }}>
            <Wifi size={14} color="#22c55e" /> 4G Online
          </span>
          <span style={{ display: 'inline-flex', alignItems: 'center', gap: '4px' }}>
            <BatteryCharging size={14} color="#38bdf8" /> Solar UPS 100%
          </span>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '14px' }}>
          {privacyMode && (
            <span style={{ color: '#ef4444', fontWeight: 'bold', display: 'flex', alignItems: 'center', gap: '4px' }}>
              <ShieldAlert size={14} /> PRIVACY MODE ACTIVE (NO LOGS)
            </span>
          )}
          <span>Govt of Odisha & NALSA Legal Aid</span>
        </div>
      </div>

      {/* Main navigation header */}
      <div className="kiosk-nav-main">
        <Link to="/" className="brand-section">
          <div className="emblem-icon">
            <Scale size={28} />
          </div>
          <div className="brand-titles">
            <h1>{t('appTitle')}</h1>
            <div className="brand-sub">{t('kioskTagline')}</div>
          </div>
        </Link>

        {/* Controls */}
        <div className="header-controls">
          {/* Language selector */}
          <div className="lang-selector-group">
            <button 
              className={`lang-btn ${lang === 'od' ? 'active' : ''}`}
              onClick={() => { setLang('od'); speakText("ଓଡ଼ିଆ ଭାଷା ଚୟନ ହେଲା", 'od'); }}
            >
              ଓଡ଼ିଆ
            </button>
            <button 
              className={`lang-btn ${lang === 'hi' ? 'active' : ''}`}
              onClick={() => { setLang('hi'); speakText("हिंदी भाषा चुनी गई", 'hi'); }}
            >
              हिंदी
            </button>
            <button 
              className={`lang-btn ${lang === 'en' ? 'active' : ''}`}
              onClick={() => { setLang('en'); speakText("English language selected", 'en'); }}
            >
              English
            </button>
          </div>

          {/* Accessibility buttons */}
          <button 
            className="control-btn"
            onClick={cycleFontSize}
            title="Adjust text size for touchscreen readability"
          >
            <Type size={18} />
            <span>{t('fontScale')}</span>
          </button>

          <button 
            className={`control-btn ${highContrast ? 'active' : ''}`}
            onClick={() => setHighContrast(!highContrast)}
            title="High contrast mode"
          >
            <Eye size={18} />
            <span>{t('highContrast')}</span>
          </button>

          {/* Privacy mode toggle */}
          <button 
            className={`control-btn ${privacyMode ? 'privacy-active' : ''}`}
            onClick={togglePrivacyMode}
            title="Toggle incognito session without logging"
          >
            <Shield size={18} />
            <span>{t('privacyMode')}</span>
          </button>

          {/* Panic Clear button */}
          <button 
            className="control-btn panic-btn"
            onClick={handlePanicWipe}
            title="Emergency clear screen and wipe memory"
          >
            <Trash2 size={18} />
            <span>{t('panicClear')}</span>
          </button>
        </div>
      </div>
    </header>
  );
}
