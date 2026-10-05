import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useLanguage } from '../context/LanguageContext';
import AudioSpeaker from '../components/AudioSpeaker';
import { 
  PhoneCall, 
  ExternalLink, 
  ShieldAlert, 
  HelpCircle, 
  Building2, 
  Scale, 
  Users 
} from 'lucide-react';

export default function ResourcesPage() {
  const { lang, t } = useLanguage();
  const [resources, setResources] = useState([]);
  const [filter, setFilter] = useState('all');

  useEffect(() => {
    fetch('/api/resources')
      .then(res => res.json())
      .then(data => setResources(data.resources || []));
  }, []);

  const filtered = resources.filter(r => {
    if (filter === 'all') return true;
    if (filter === 'helplines') return r.is_helpline === 1;
    if (filter === 'legal_aid') return r.category === 'legal_aid';
    if (filter === 'emergency') return r.category === 'emergency';
    return true;
  });

  return (
    <div className="kiosk-container">
      {/* Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px', flexWrap: 'wrap', gap: '12px' }}>
        <div>
          <Link to="/" style={{ color: '#64748b', textDecoration: 'none', fontSize: '14px', fontWeight: 600 }}>
            ← Back to Home
          </Link>
          <h2 style={{ fontSize: '26px', fontWeight: 800, color: '#0f172a', marginTop: '4px' }}>
            {t('cardResourcesTitle')}
          </h2>
          <p style={{ color: '#64748b', fontSize: '14px' }}>
            Direct toll-free hotlines, government grievance portals, and legal authorities.
          </p>
        </div>

        <AudioSpeaker text="Official government helplines and legal aid portals directory. Tap any card to dial or view details." />
      </div>

      {/* Filter Tabs */}
      <div style={{ display: 'flex', gap: '8px', marginBottom: '20px', overflowX: 'auto', paddingBottom: '6px' }}>
        {[
          { id: 'all', label: 'All Resources' },
          { id: 'helplines', label: '24/7 Toll-free Helplines' },
          { id: 'legal_aid', label: 'NALSA & Tele-Law' },
          { id: 'emergency', label: 'Emergency Response' }
        ].map(tab => (
          <button
            key={tab.id}
            onClick={() => setFilter(tab.id)}
            style={{
              background: filter === tab.id ? '#1e3a8a' : '#ffffff',
              color: filter === tab.id ? '#ffffff' : '#334155',
              border: filter === tab.id ? '1px solid #1e3a8a' : '1px solid #cbd5e1',
              borderRadius: '9999px',
              padding: '8px 18px',
              fontSize: '14px',
              fontWeight: 600,
              cursor: 'pointer'
            }}
          >
            {tab.label}
          </button>
        ))}
      </div>

      {/* Resource Cards Grid */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(290px, 1fr))', gap: '18px' }}>
        {filtered.map(r => {
          const resName = r[`name_${lang}`] || r.name_en;
          const resDesc = r[`description_${lang}`] || r.description_en;
          const isEmergency = r.category === 'emergency';

          return (
            <div
              key={r.id}
              style={{
                background: '#ffffff',
                border: isEmergency ? '2px solid #fca5a5' : '1px solid #e2e8f0',
                borderRadius: '16px',
                padding: '22px',
                display: 'flex',
                flexDirection: 'column',
                justifyContent: 'space-between',
                boxShadow: '0 2px 4px rgba(0,0,0,0.03)'
              }}
            >
              <div>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '8px' }}>
                  <span style={{
                    fontSize: '11px',
                    fontWeight: 700,
                    textTransform: 'uppercase',
                    padding: '3px 8px',
                    borderRadius: '4px',
                    background: isEmergency ? '#fee2e2' : '#eff6ff',
                    color: isEmergency ? '#dc2626' : '#2563eb'
                  }}>
                    {r.category.replace('_', ' ')}
                  </span>
                  <AudioSpeaker text={`${resName}. Helpline number: ${r.phone}. ${resDesc}`} />
                </div>

                <h3 style={{ fontSize: '18px', fontWeight: 800, color: '#0f172a', marginBottom: '8px' }}>
                  {resName}
                </h3>
                <p style={{ fontSize: '14px', color: '#475569', lineHeight: 1.4, marginBottom: '16px' }}>
                  {resDesc}
                </p>
              </div>

              <div>
                {r.phone && (
                  <a
                    href={`tel:${r.phone}`}
                    style={{
                      background: isEmergency ? '#dc2626' : '#2563eb',
                      color: '#ffffff',
                      textDecoration: 'none',
                      borderRadius: '10px',
                      padding: '12px 16px',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      gap: '8px',
                      fontWeight: 700,
                      fontSize: '16px',
                      marginBottom: '8px'
                    }}
                  >
                    <PhoneCall size={18} /> Dial Toll-Free: {r.phone}
                  </a>
                )}

                {r.portal_url && (
                  <a
                    href={r.portal_url}
                    target="_blank"
                    rel="noreferrer"
                    style={{
                      color: '#1e3a8a',
                      textDecoration: 'none',
                      fontSize: '13px',
                      fontWeight: 600,
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      gap: '4px'
                    }}
                  >
                    <span>Visit Official Portal</span> <ExternalLink size={13} />
                  </a>
                )}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
