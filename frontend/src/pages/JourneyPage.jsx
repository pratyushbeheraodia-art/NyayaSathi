import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useLanguage } from '../context/LanguageContext';
import { useKiosk } from '../context/KioskContext';
import AudioSpeaker from '../components/AudioSpeaker';
import { 
  Map, 
  CheckCircle2, 
  Clock, 
  Shield, 
  Building, 
  ArrowRight,
  FileCheck
} from 'lucide-react';

export default function JourneyPage() {
  const { lang, t } = useLanguage();
  const { activeCategory, setActiveCategory } = useKiosk();
  const [journeyData, setJourneyData] = useState(null);
  const [loading, setLoading] = useState(true);

  const categories = [
    { id: 'criminal_police', label_en: '⚖️ Criminal FIR & Bail', label_hi: '⚖️ पुलिस एफआईआर व जमानत', label_od: '⚖️ ଏଫଆଇଆର ଓ ଜାମିନ' },
    { id: 'land_property', label_en: '🌾 Land Encroachment', label_hi: '🌾 भूमि विवाद एवं पट्टा', label_od: '🌾 ଜମି ବିବାଦ ଓ ପଟ୍ଟା' },
    { id: 'banking_debt_cheque', label_en: '💰 Cheque Bounce (Sec 138)', label_hi: '💰 चेक बाउंस व ऋण', label_od: '💰 ଚେକ୍ ବାଉନ୍ସ' },
    { id: 'labor_employment', label_en: '🧱 Unpaid Wages & Job', label_hi: '🧱 बकाया मजदूरी व नौकरी', label_od: '🧱 ବକେୟା ମଜୁରୀ ଓ ଚାକିରି' },
    { id: 'domestic_violence', label_en: '🛡️ Domestic Protection', label_hi: '🛡️ घरेलू हिंसा संरक्षण', label_od: '🛡️ ଘରୋଇ ସୁରକ୍ଷା' },
    { id: 'family_matrimonial', label_en: '💍 Divorce & Custody', label_hi: '💍 विवाह विच्छेद व कस्टडी', label_od: '💍 ଛାଡ଼ପତ୍ର ଓ ହେପାଜତ' },
    { id: 'property_succession', label_en: '📜 Ancestral Partition', label_hi: '📜 पैतृक बंटवारा व बेटियां', label_od: '📜 ପୈତୃକ ସମ୍ପତ୍ତି ଭାଗ' },
    { id: 'tenancy_realestate', label_en: '🏢 RERA & Tenancy', label_hi: '🏢 रेरा बिल्डर व किरायेदारी', label_od: '🏢 ରେରା ଓ ଘରଭଡ଼ା' },
    { id: 'cyber_fraud_privacy', label_en: '💳 Cyber UPI Fraud', label_hi: '💳 साइबर ठगी 1930', label_od: '💳 ସାଇବର ଠକେଇ' },
    { id: 'consumer_dispute', label_en: '🚜 Consumer Defect & Bill', label_hi: '🚜 उपभोक्ता फोरम व वारंटी', label_od: '🚜 ଗ୍ରାହକ ଅଧିକାର' },
    { id: 'motor_accidents_traffic', label_en: '🚗 Accident MACT Claims', label_hi: '🚗 दुर्घटना मुआवजा एमएसीटी', label_od: '🚗 MACT ଦୁର୍ଘଟଣା କ୍ଷତିପୂରଣ' },
    { id: 'senior_citizen_welfare', label_en: '👴 Senior Citizen Rights', label_hi: '👴 वरिष्ठ नागरिक भरण-पोषण', label_od: '👴 ବରିଷ୍ଠ ନାଗରିକ ଅଧିକାର' },
    { id: 'child_pocso_education', label_en: '👶 Child & POCSO Justice', label_hi: '👶 बाल संरक्षण व पॉक्सो', label_od: '👶 ଶିଶୁ ସୁରକ୍ଷା ଓ POCSO' },
    { id: 'constitutional_rti_grievance', label_en: '📄 RTI & Civil Writs', label_hi: '📄 आरटीआई व जन शिकायत', label_od: '📄 RTI ସୂଚନା ଅଧିକାର' },
    { id: 'business_msme_tax', label_en: '💼 MSME Delayed Dues', label_hi: '💼 एमएसएमई बकाया व व्यापार', label_od: '💼 MSME ବକେୟା ବିଲ୍' },
    { id: 'universal_legal_assistant', label_en: '🌐 Universal Citizen Path', label_hi: '🌐 सामान्य विधिक यात्रा', label_od: '🌐 ସାଧାରଣ ଆଇନ ଯାତ୍ରା' }
  ];

  useEffect(() => {
    setLoading(true);
    fetch(`/api/journey/${activeCategory}`)
      .then(res => res.json())
      .then(data => {
        setJourneyData(data);
        setLoading(false);
      })
      .catch(err => {
        console.error(err);
        setLoading(false);
      });
  }, [activeCategory]);

  return (
    <div className="kiosk-container">
      {/* Page Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px', flexWrap: 'wrap', gap: '12px' }}>
        <div>
          <Link to="/" style={{ color: '#64748b', textDecoration: 'none', fontSize: '14px', fontWeight: 600 }}>
            ← Back to Home
          </Link>
          <h2 style={{ fontSize: '26px', fontWeight: 800, color: '#0f172a', marginTop: '4px' }}>
            {t('cardJourneyTitle')}
          </h2>
          <p style={{ color: '#64748b', fontSize: '14px' }}>
            Visual step-by-step statutory process from initial grievance to final legal resolution
          </p>
        </div>

        {journeyData && (
          <div style={{ background: '#eff6ff', color: '#1d4ed8', padding: '8px 16px', borderRadius: '12px', fontWeight: 700, fontSize: '14px', display: 'flex', alignItems: 'center', gap: '6px' }}>
            <Clock size={16} /> Est. Duration: {journeyData.total_estimated_days}
          </div>
        )}
      </div>

      {/* Category Tabs */}
      <div style={{ display: 'flex', gap: '8px', overflowX: 'auto', paddingBottom: '12px', marginBottom: '20px' }}>
        {categories.map(c => {
          const isSelected = activeCategory === c.id;
          const tabLabel = c[`label_${lang}`] || c.label_en;
          return (
            <button
              key={c.id}
              onClick={() => setActiveCategory(c.id)}
              style={{
                background: isSelected ? '#1e3a8a' : '#ffffff',
                color: isSelected ? '#ffffff' : '#334155',
                border: isSelected ? '1px solid #1e3a8a' : '1px solid #cbd5e1',
                padding: '10px 18px',
                borderRadius: '9999px',
                fontSize: '14px',
                fontWeight: 700,
                cursor: 'pointer',
                whiteSpace: 'nowrap',
                transition: 'all 0.15s ease'
              }}
            >
              {tabLabel}
            </button>
          );
        })}
      </div>

      {loading || !journeyData ? (
        <div style={{ textAlign: 'center', padding: '40px' }}>Loading legal trajectory...</div>
      ) : (
        <div>
          <div style={{
            background: '#ffffff',
            borderRadius: '16px',
            border: '1px solid #e2e8f0',
            padding: '24px',
            marginBottom: '24px'
          }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '16px' }}>
              <h3 style={{ fontSize: '20px', fontWeight: 800, color: '#1e3a8a' }}>
                {journeyData[`title_${lang}`] || journeyData.title_en}
              </h3>
              <AudioSpeaker text={journeyData[`title_${lang}`] || journeyData.title_en} />
            </div>

            {/* Stepper Timeline */}
            <div className="timeline-stepper">
              {journeyData.stages.map((stage, idx) => {
                const stageTitle = stage[`title_${lang}`] || stage.title_en;
                const isCompleted = stage.status === 'COMPLETED';
                const isInProgress = stage.status === 'IN_PROGRESS';

                return (
                  <div 
                    key={idx} 
                    className={`timeline-step ${isCompleted ? 'completed' : isInProgress ? 'active' : ''}`}
                  >
                    <div className="step-marker">
                      {isCompleted ? <CheckCircle2 size={18} /> : stage.step}
                    </div>

                    <div className="step-content-card">
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '8px', marginBottom: '8px' }}>
                        <div>
                          <span style={{
                            fontSize: '11px',
                            fontWeight: 700,
                            textTransform: 'uppercase',
                            padding: '3px 8px',
                            borderRadius: '4px',
                            background: isCompleted ? '#dcfce7' : isInProgress ? '#dbeafe' : '#f1f5f9',
                            color: isCompleted ? '#15803d' : isInProgress ? '#1d4ed8' : '#64748b'
                          }}>
                            {stage.status}
                          </span>
                          <h4 style={{ fontSize: '17px', fontWeight: 800, color: '#0f172a', marginTop: '6px' }}>
                            Stage {stage.step}: {stageTitle}
                          </h4>
                        </div>
                        <AudioSpeaker text={`${stageTitle}. Authority: ${stage.authority}. Details: ${stage.details}. Citizen Right: ${stage.citizen_rights}`} />
                      </div>

                      <div style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '13px', fontWeight: 600, color: '#475569', marginBottom: '10px' }}>
                        <Building size={14} color="#2563eb" /> Competent Authority: <span style={{ color: '#0f172a' }}>{stage.authority}</span>
                      </div>

                      <p style={{ fontSize: '14px', color: '#334155', lineHeight: 1.5, marginBottom: '12px' }}>
                        {stage.details}
                      </p>

                      <div style={{
                        background: '#eff6ff',
                        borderRadius: '8px',
                        padding: '10px 14px',
                        borderLeft: '4px solid #3b82f6',
                        fontSize: '13px',
                        color: '#1e40af',
                        display: 'flex',
                        alignItems: 'center',
                        gap: '8px'
                      }}>
                        <Shield size={16} flexShrink={0} />
                        <span><strong>Your Legal Right:</strong> {stage.citizen_rights}</span>
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>

          <div style={{ display: 'flex', gap: '14px', flexWrap: 'wrap' }}>
            <Link to="/checklist" className="btn-primary" style={{ flex: 1, minWidth: '220px' }}>
              <FileCheck size={18} /> View Required Document Checklist
            </Link>
            <Link to="/slip" className="btn-secondary" style={{ flex: 1, minWidth: '220px' }}>
              Print Legal Action Slip (Nyaya Patra)
            </Link>
          </div>
        </div>
      )}
    </div>
  );
}
