import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useLanguage } from '../context/LanguageContext';
import { useKiosk } from '../context/KioskContext';
import AudioSpeaker from '../components/AudioSpeaker';
import { 
  FileCheck2, 
  Building, 
  CheckCircle, 
  AlertCircle, 
  Printer, 
  Sparkles,
  ArrowRight
} from 'lucide-react';

export default function ChecklistPage() {
  const { lang, t } = useLanguage();
  const { activeCategory, setActiveCategory } = useKiosk();
  const [checklist, setChecklist] = useState([]);
  const [checkedItems, setCheckedItems] = useState({});
  const [loading, setLoading] = useState(true);

  const categories = [
    { id: 'criminal_police', label_en: '⚖️ Criminal FIR & Bail', label_hi: '⚖️ पुलिस एफआईआर व जमानत', label_od: '⚖️ ଏଫଆଇଆର ଓ ଜାମିନ' },
    { id: 'land_property', label_en: '🌾 Land Dispute & RoR', label_hi: '🌾 भूमि विवाद एवं पट्टा', label_od: '🌾 ଜମି ବିବାଦ ଓ ପଟ୍ଟା' },
    { id: 'banking_debt_cheque', label_en: '💰 Cheque Bounce (Sec 138)', label_hi: '💰 चेक बाउंस व ऋण', label_od: '💰 ଚେକ୍ ବାଉନ୍ସ' },
    { id: 'labor_employment', label_en: '🧱 Unpaid Wages & Job', label_hi: '🧱 बकाया मजदूरी व नौकरी', label_od: '🧱 ବକେୟା ମଜୁରୀ ଓ ଚାକିରି' },
    { id: 'domestic_violence', label_en: '🛡️ Domestic Protection', label_hi: '🛡️ घरेलू हिंसा संरक्षण', label_od: '🛡️ ଘରୋଇ ସୁରକ୍ଷା' },
    { id: 'family_matrimonial', label_en: '💍 Divorce & Custody', label_hi: '💍 विवाह विच्छेद व कस्टडी', label_od: '💍 ଛାଡ଼ପତ୍ର ଓ ହେପାଜତ' },
    { id: 'property_succession', label_en: '📜 Ancestral Partition', label_hi: '📜 पैतृक बंटवारा व बेटियां', label_od: '📜 ପୈତୃକ ସମ୍ପତ୍ତି ଭାଗ' },
    { id: 'tenancy_realestate', label_en: '🏢 RERA & Tenancy', label_hi: '🏢 रेरा बिल्डर व किरायेदारी', label_od: '🏢 ରେରା ଓ ଘରଭଡ଼ା' },
    { id: 'cyber_fraud_privacy', label_en: '💳 Cyber UPI Fraud', label_hi: '💳 साइबर ठगी 1930', label_od: '💳 ସାଇବର ଠକେଇ' },
    { id: 'consumer_dispute', label_en: '🚜 Consumer Goods & Bill', label_hi: '🚜 उपभोक्ता फोरम व वारंटी', label_od: '🚜 ଗ୍ରାହକ ଅଧିକାର' },
    { id: 'motor_accidents_traffic', label_en: '🚗 Accident MACT Claims', label_hi: '🚗 दुर्घटना मुआवजा एमएसीटी', label_od: '🚗 MACT ଦୁର୍ଘଟଣା କ୍ଷତିପୂରଣ' },
    { id: 'senior_citizen_welfare', label_en: '👴 Senior Citizen Rights', label_hi: '👴 वरिष्ठ नागरिक भरण-पोषण', label_od: '👴 ବରିଷ୍ଠ ନାଗରିକ ଅଧିକାର' },
    { id: 'child_pocso_education', label_en: '👶 Child & POCSO Justice', label_hi: '👶 बाल संरक्षण व पॉक्सो', label_od: '👶 ଶିଶୁ ସୁରକ୍ଷା ଓ POCSO' },
    { id: 'constitutional_rti_grievance', label_en: '📄 RTI & Civil Writs', label_hi: '📄 आरटीआई व जन शिकायत', label_od: '📄 RTI ସୂଚନା ଅଧିକାର' },
    { id: 'business_msme_tax', label_en: '💼 MSME Delayed Dues', label_hi: '💼 एमएसएमई बकाया व व्यापार', label_od: '💼 MSME ବକେୟା ବିଲ୍' },
    { id: 'universal_legal_assistant', label_en: '🌐 Universal Citizen Proof', label_hi: '🌐 सामान्य दस्तावेज़ सूची', label_od: '🌐 ସାଧାରଣ କାଗଜପତ୍ର' }
  ];

  useEffect(() => {
    setLoading(true);
    fetch(`/api/documents/checklist/${activeCategory}`)
      .then(res => res.json())
      .then(data => {
        setChecklist(data.documents || []);
        setLoading(false);
      })
      .catch(err => setLoading(false));
  }, [activeCategory]);

  const toggleCheck = (id) => {
    setCheckedItems(prev => ({ ...prev, [id]: !prev[id] }));
  };

  const mandatoryCount = checklist.filter(d => d.mandatory).length;
  const checkedMandatoryCount = checklist.filter(d => d.mandatory && checkedItems[d.id]).length;
  const readinessPct = mandatoryCount > 0 ? Math.round((checkedMandatoryCount / mandatoryCount) * 100) : 0;

  return (
    <div className="kiosk-container">
      {/* Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px', flexWrap: 'wrap', gap: '12px' }}>
        <div>
          <Link to="/" style={{ color: '#64748b', textDecoration: 'none', fontSize: '14px', fontWeight: 600 }}>
            ← Back to Home
          </Link>
          <h2 style={{ fontSize: '26px', fontWeight: 800, color: '#0f172a', marginTop: '4px' }}>
            {t('cardChecklistTitle')}
          </h2>
          <p style={{ color: '#64748b', fontSize: '14px' }}>
            Ensure you carry these verified records to prevent adjournments and expedite hearing.
          </p>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
          <AudioSpeaker text={`Document checklist for legal filing. You have verified ${checkedMandatoryCount} of ${mandatoryCount} mandatory documents.`} />
          <Link to="/slip" className="btn-secondary" style={{ padding: '8px 16px', fontSize: '14px' }}>
            <Printer size={16} /> Print Checklist
          </Link>
        </div>
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
                whiteSpace: 'nowrap'
              }}
            >
              {tabLabel}
            </button>
          );
        })}
      </div>

      {/* Readiness Progress Bar */}
      <div style={{
        background: '#ffffff',
        borderRadius: '16px',
        border: '1px solid #e2e8f0',
        padding: '20px',
        marginBottom: '24px',
        boxShadow: '0 2px 4px rgba(0,0,0,0.03)'
      }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
          <span style={{ fontSize: '15px', fontWeight: 700, color: '#0f172a' }}>
            Document Filing Readiness: {readinessPct}%
          </span>
          <span style={{ fontSize: '13px', fontWeight: 600, color: readinessPct >= 75 ? '#16a34a' : '#d97706' }}>
            {checkedMandatoryCount} of {mandatoryCount} Mandatory Documents Ready
          </span>
        </div>

        <div style={{ width: '100%', height: '10px', background: '#f1f5f9', borderRadius: '9999px', overflow: 'hidden' }}>
          <div style={{
            width: `${readinessPct}%`,
            height: '100%',
            background: readinessPct === 100 ? '#16a34a' : readinessPct >= 50 ? '#2563eb' : '#d97706',
            transition: 'width 0.3s ease'
          }}></div>
        </div>
      </div>

      {/* Documents List */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: '14px' }}>
        {checklist.map((doc) => {
          const docTitle = doc[`item_${lang}`] || doc.item_en;
          const isDone = checkedItems[doc.id];

          return (
            <div
              key={doc.id}
              onClick={() => toggleCheck(doc.id)}
              style={{
                background: isDone ? '#f0fdf4' : '#ffffff',
                border: isDone ? '2px solid #86efac' : '1px solid #e2e8f0',
                borderRadius: '14px',
                padding: '18px 22px',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'space-between',
                cursor: 'pointer',
                transition: 'all 0.15s ease',
                flexWrap: 'wrap',
                gap: '12px'
              }}
            >
              <div style={{ display: 'flex', alignItems: 'flex-start', gap: '16px' }}>
                <input
                  type="checkbox"
                  checked={!!isDone}
                  onChange={() => {}}
                  style={{
                    width: '24px',
                    height: '24px',
                    marginTop: '2px',
                    accentColor: '#16a34a',
                    cursor: 'pointer'
                  }}
                />

                <div>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap' }}>
                    <h4 style={{ fontSize: '17px', fontWeight: 700, color: '#0f172a' }}>
                      {docTitle}
                    </h4>
                    {doc.mandatory ? (
                      <span style={{ fontSize: '11px', fontWeight: 700, background: '#fee2e2', color: '#b91c1c', padding: '2px 8px', borderRadius: '4px' }}>
                        MANDATORY
                      </span>
                    ) : (
                      <span style={{ fontSize: '11px', fontWeight: 600, background: '#f1f5f9', color: '#475569', padding: '2px 8px', borderRadius: '4px' }}>
                        RECOMMENDED
                      </span>
                    )}
                  </div>

                  <p style={{ fontSize: '14px', color: '#475569', marginTop: '4px', lineHeight: 1.4 }}>
                    <strong>Purpose:</strong> {doc.purpose}
                  </p>
                </div>
              </div>

              <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                <div style={{
                  fontSize: '13px',
                  fontWeight: 600,
                  color: '#1e40af',
                  background: '#eff6ff',
                  padding: '6px 12px',
                  borderRadius: '8px',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '6px'
                }}>
                  <Building size={14} /> {doc.issuing_authority}
                </div>
                <AudioSpeaker text={`${docTitle}. Purpose: ${doc.purpose}. Issuing authority: ${doc.issuing_authority}`} />
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
