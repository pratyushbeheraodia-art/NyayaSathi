import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useLanguage } from '../context/LanguageContext';
import { useKiosk } from '../context/KioskContext';
import AudioSpeaker from '../components/AudioSpeaker';
import { 
  Scale, 
  MapPin, 
  AlertCircle, 
  CheckCircle2, 
  ArrowRight, 
  HelpCircle, 
  FileText, 
  Printer,
  Sparkles,
  ExternalLink
} from 'lucide-react';

export default function VoicePathPage() {
  const { lang, t, speakText } = useLanguage();
  const { activeAnalysis, activeCategory, setActiveCategory } = useKiosk();
  const [analysis, setAnalysis] = useState(activeAnalysis);
  const navigate = useNavigate();

  // If no analysis is loaded in context, load default based on activeCategory
  useEffect(() => {
    if (!analysis) {
      fetch('/api/voice/process', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          text: "Land encroachment dispute boundary issue",
          language: lang,
          privacy_mode: false
        })
      })
      .then(res => res.json())
      .then(data => {
        if (data.status === 'SUCCESS') {
          setAnalysis(data.classification);
        }
      });
    }
  }, [analysis, lang]);

  if (!analysis) {
    return (
      <div className="kiosk-container" style={{ textAlign: 'center', padding: '60px 20px' }}>
        <Sparkles size={40} color="#2563eb" style={{ animation: 'spin 2s linear infinite' }} />
        <p style={{ marginTop: '16px', fontSize: '18px', fontWeight: 600 }}>Analyzing legal classification...</p>
      </div>
    );
  }

  const categoryTitle = analysis.category_titles 
    ? (analysis.category_titles[lang] || analysis.category_titles.en)
    : analysis.title;

  const rightsText = analysis.rights_summary 
    ? (analysis.rights_summary[lang] || analysis.rights_summary.en)
    : "You have statutory rights to legal redressal under Indian Law.";

  const badgeColor = analysis.urgency === 'Emergency' ? '#dc2626' : analysis.urgency === 'High' ? '#ea580c' : '#059669';
  const badgeBg = analysis.urgency === 'Emergency' ? '#fee2e2' : analysis.urgency === 'High' ? '#ffedd5' : '#d1fae5';

  return (
    <div className="kiosk-container">
      {/* Header Bar */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px', flexWrap: 'wrap', gap: '12px' }}>
        <div>
          <Link to="/" style={{ color: '#64748b', textDecoration: 'none', fontSize: '14px', fontWeight: 600, display: 'inline-flex', alignItems: 'center', gap: '4px', marginBottom: '6px' }}>
            ← {t('back')}
          </Link>
          <h2 style={{ fontSize: '26px', fontWeight: 800, color: '#0f172a' }}>
            {t('cardVoiceTitle')}
          </h2>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
          <AudioSpeaker text={`${categoryTitle}. ${rightsText}`} label="Listen to Advice" />
          <Link to="/slip" className="btn-secondary" style={{ padding: '8px 16px', fontSize: '14px' }}>
            <Printer size={16} /> {t('print')}
          </Link>
        </div>
      </div>

      {/* Main Classification Card */}
      <div style={{
        background: '#ffffff',
        borderRadius: '20px',
        border: '1px solid #cbd5e1',
        padding: '28px',
        boxShadow: '0 4px 6px -1px rgba(0,0,0,0.05)',
        marginBottom: '24px'
      }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '12px', borderBottom: '1px solid #e2e8f0', paddingBottom: '18px' }}>
          <div>
            <div style={{ display: 'inline-flex', alignItems: 'center', gap: '6px', background: badgeBg, color: badgeColor, padding: '4px 12px', borderRadius: '9999px', fontSize: '13px', fontWeight: 700, marginBottom: '8px' }}>
              <AlertCircle size={15} /> {t('urgency')}: {analysis.urgency}
            </div>
            <h1 style={{ fontSize: '26px', fontWeight: 800, color: '#1e3a8a', lineHeight: 1.2 }}>
              {categoryTitle}
            </h1>
          </div>

          <div style={{ textAlign: 'right' }}>
            <span style={{ fontSize: '12px', color: '#64748b', display: 'block', fontWeight: 600 }}>{t('confidence')}</span>
            <span style={{ fontSize: '20px', fontWeight: 800, color: '#059669' }}>
              {Math.round(analysis.confidence * 100)}% Match
            </span>
          </div>
        </div>

        {/* 3 Pillars: Law, Forum, Cost */}
        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))',
          gap: '16px',
          margin: '20px 0',
          padding: '16px',
          background: '#f8fafc',
          borderRadius: '12px'
        }}>
          <div>
            <div style={{ fontSize: '12px', fontWeight: 700, color: '#64748b', textTransform: 'uppercase' }}>{t('applicableLaw')}</div>
            <div style={{ fontSize: '15px', fontWeight: 700, color: '#0f172a', marginTop: '4px' }}>{analysis.default_law}</div>
          </div>
          <div>
            <div style={{ fontSize: '12px', fontWeight: 700, color: '#64748b', textTransform: 'uppercase' }}>{t('forum')}</div>
            <div style={{ fontSize: '15px', fontWeight: 700, color: '#0f172a', marginTop: '4px' }}>{analysis.forum}</div>
          </div>
          <div>
            <div style={{ fontSize: '12px', fontWeight: 700, color: '#64748b', textTransform: 'uppercase' }}>Official Expense</div>
            <div style={{ fontSize: '15px', fontWeight: 700, color: '#059669', marginTop: '4px' }}>{analysis.cost}</div>
          </div>
        </div>

        {/* Rights Summary */}
        <div style={{ background: '#eff6ff', borderRadius: '12px', padding: '18px', borderLeft: '5px solid #2563eb', marginBottom: '24px' }}>
          <h4 style={{ fontSize: '16px', fontWeight: 700, color: '#1e40af', marginBottom: '6px', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <Scale size={18} /> {t('rightsGranted')}
          </h4>
          <p style={{ fontSize: '15px', color: '#1e3a8a', lineHeight: 1.5 }}>
            {rightsText}
          </p>
        </div>

        {/* Immediate 3 Steps */}
        <div>
          <h3 style={{ fontSize: '18px', fontWeight: 700, color: '#0f172a', marginBottom: '14px' }}>
            Immediate Action Steps (Next 24-48 Hours):
          </h3>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
            {analysis.recommended_steps && analysis.recommended_steps.map((st, idx) => (
              <div key={idx} style={{ display: 'flex', alignItems: 'flex-start', gap: '14px', background: '#ffffff', border: '1px solid #e2e8f0', borderRadius: '12px', padding: '14px 18px' }}>
                <div style={{ width: '28px', height: '28px', borderRadius: '50%', background: '#2563eb', color: 'white', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: 700, fontSize: '14px', flexShrink: 0 }}>
                  {st.step}
                </div>
                <div style={{ fontSize: '15px', fontWeight: 600, color: '#1e293b', paddingTop: '3px' }}>
                  {st[lang] || st.en}
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Action Buttons */}
        <div style={{ display: 'flex', gap: '14px', marginTop: '28px', flexWrap: 'wrap' }}>
          <Link 
            to="/clarification" 
            className="btn-primary"
            style={{ flex: 1, minWidth: '220px' }}
          >
            <HelpCircle size={18} />
            <span>Answer Smart Clarification Questions</span>
          </Link>

          <Link 
            to="/journey" 
            className="btn-secondary"
            style={{ flex: 1, minWidth: '220px' }}
          >
            <MapPin size={18} />
            <span>View Full Legal Journey Map</span>
          </Link>

          <Link 
            to="/checklist" 
            className="btn-secondary"
            style={{ minWidth: '180px' }}
          >
            <FileText size={18} />
            <span>Required Documents</span>
          </Link>
        </div>
      </div>
    </div>
  );
}
