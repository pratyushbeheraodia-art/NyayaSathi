import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useLanguage } from '../context/LanguageContext';
import { useKiosk } from '../context/KioskContext';
import AudioSpeaker from '../components/AudioSpeaker';
import { 
  Printer, 
  Download, 
  QrCode, 
  Scale, 
  Building, 
  PhoneCall, 
  CheckCircle2, 
  MapPin, 
  ShieldCheck, 
  ArrowLeft 
} from 'lucide-react';

export default function ActionSlipPage() {
  const { lang, t, speakText } = useLanguage();
  const { activeCategory, activeAnalysis } = useKiosk();
  const [slip, setSlip] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/summary/generate-slip', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        category: activeCategory,
        language: lang,
        name: "Citizen Beneficiary"
      })
    })
    .then(res => res.json())
    .then(data => {
      setSlip(data);
      setLoading(false);
    })
    .catch(err => {
      console.error(err);
      setLoading(false);
    });
  }, [activeCategory, lang]);

  const handlePrint = () => {
    speakText("Printing your Nyaya Patra Action Slip.");
    window.print();
  };

  if (loading || !slip) {
    return <div className="kiosk-container" style={{ textAlign: 'center', padding: '60px' }}>Generating official action summary...</div>;
  }

  return (
    <div className="kiosk-container">
      {/* Header Controls */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px', flexWrap: 'wrap', gap: '12px' }} className="no-print">
        <div>
          <Link to="/" style={{ color: '#64748b', textDecoration: 'none', fontSize: '14px', fontWeight: 600 }}>
            ← Back to Home
          </Link>
          <h2 style={{ fontSize: '26px', fontWeight: 800, color: '#0f172a', marginTop: '4px' }}>
            {t('cardSummaryTitle')}
          </h2>
          <p style={{ color: '#64748b', fontSize: '14px' }}>
            Official Nyaya Patra: Carry this slip to the Tahasildar or Legal Services counter.
          </p>
        </div>

        <div style={{ display: 'flex', gap: '10px' }}>
          <button onClick={handlePrint} className="btn-primary">
            <Printer size={18} /> Print Action Slip (Nyaya Patra)
          </button>
        </div>
      </div>

      {/* Printable Slip Container */}
      <div 
        className="printable-slip"
        style={{
          background: '#ffffff',
          borderRadius: '16px',
          border: '2px solid #0f172a',
          padding: '36px',
          maxWidth: '720px',
          margin: '0 auto',
          boxShadow: '0 10px 25px -5px rgba(0,0,0,0.08)',
          fontFamily: 'serif'
        }}
      >
        {/* Slip Header with Ashoka Emblem / Justice Scale */}
        <div style={{ textAlign: 'center', borderBottom: '2px solid #0f172a', paddingBottom: '16px', marginBottom: '20px' }}>
          <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', gap: '8px', color: '#1e3a8a', marginBottom: '6px' }}>
            <Scale size={32} />
          </div>
          <h2 style={{ fontSize: '22px', fontWeight: 900, textTransform: 'uppercase', letterSpacing: '1px', color: '#0f172a', margin: 0 }}>
            NyayaSathi - Nyaya Patra (ନ୍ୟାୟ ପତ୍ର)
          </h2>
          <div style={{ fontSize: '13px', fontWeight: 600, color: '#475569', marginTop: '4px' }}>
            OFFICIAL KIOSK LEGAL ACTION SUMMARY | GOVT OF ODISHA & NALSA
          </div>
        </div>

        {/* Metadata Grid */}
        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(2, 1fr)',
          gap: '12px',
          fontSize: '13px',
          fontFamily: 'sans-serif',
          borderBottom: '1px solid #cbd5e1',
          paddingBottom: '16px',
          marginBottom: '20px'
        }}>
          <div>
            <span style={{ color: '#64748b' }}>Slip Token:</span>{' '}
            <strong style={{ color: '#1e3a8a', fontSize: '15px' }}>{slip.slip_token}</strong>
          </div>
          <div>
            <span style={{ color: '#64748b' }}>Issued On:</span>{' '}
            <strong>{slip.date_time}</strong>
          </div>
          <div>
            <span style={{ color: '#64748b' }}>Kiosk Origin:</span>{' '}
            <strong>{slip.kiosk_id}</strong>
          </div>
          <div>
            <span style={{ color: '#64748b' }}>Beneficiary:</span>{' '}
            <strong>{slip.citizen_name}</strong>
          </div>
        </div>

        {/* Case Categorization Box */}
        <div style={{
          background: '#f8fafc',
          border: '1px solid #cbd5e1',
          borderRadius: '8px',
          padding: '16px',
          marginBottom: '20px',
          fontFamily: 'sans-serif'
        }}>
          <div style={{ fontSize: '11px', fontWeight: 700, textTransform: 'uppercase', color: '#64748b' }}>Dispute Classification</div>
          <div style={{ fontSize: '18px', fontWeight: 800, color: '#0f172a', marginTop: '2px' }}>
            {slip.category_title}
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: '10px', marginTop: '12px', fontSize: '13px' }}>
            <div>
              <span style={{ color: '#64748b' }}>Applicable Law:</span>
              <div style={{ fontWeight: 600, color: '#1e3a8a' }}>{slip.applicable_law}</div>
            </div>
            <div>
              <span style={{ color: '#64748b' }}>Competent Forum:</span>
              <div style={{ fontWeight: 600, color: '#1e3a8a' }}>{slip.recommended_forum}</div>
            </div>
            <div>
              <span style={{ color: '#64748b' }}>Statutory Fee:</span>
              <div style={{ fontWeight: 700, color: '#059669' }}>{slip.statutory_cost}</div>
            </div>
            <div>
              <span style={{ color: '#64748b' }}>Free Legal Aid:</span>
              <div style={{ fontWeight: 700, color: '#059669' }}>100% Eligible under Sec 12</div>
            </div>
          </div>
        </div>

        {/* Next 3 Mandatory Steps */}
        <div style={{ marginBottom: '24px', fontFamily: 'sans-serif' }}>
          <h4 style={{ fontSize: '15px', fontWeight: 800, color: '#0f172a', textTransform: 'uppercase', marginBottom: '10px' }}>
            Citizen Action Checklist:
          </h4>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            {slip.next_3_actions.map((act, i) => (
              <div key={i} style={{ display: 'flex', alignItems: 'flex-start', gap: '10px', fontSize: '14px', color: '#1e293b' }}>
                <span style={{ width: '18px', height: '18px', border: '2px solid #0f172a', borderRadius: '4px', display: 'inline-block', flexShrink: 0, marginTop: '2px' }}></span>
                <span>{act}</span>
              </div>
            ))}
          </div>
        </div>

        {/* QR Code & Helpline Footer */}
        <div style={{
          borderTop: '2px solid #0f172a',
          paddingTop: '16px',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          fontFamily: 'sans-serif',
          gap: '20px'
        }}>
          <div>
            <div style={{ fontSize: '11px', fontWeight: 700, textTransform: 'uppercase', color: '#64748b', marginBottom: '4px' }}>
              Official 24/7 Helplines:
            </div>
            <div style={{ fontSize: '12px', color: '#0f172a', lineHeight: 1.5 }}>
              <div>• <strong>NALSA Legal Aid:</strong> 15100</div>
              <div>• <strong>Cyber Fraud Reporting:</strong> 1930</div>
              <div>• <strong>Women Crisis Helpline:</strong> 181</div>
              <div>• <strong>Police Emergency:</strong> 112</div>
            </div>
          </div>

          {/* Visual QR Code Representation */}
          <div style={{ textAlign: 'center' }}>
            <div style={{
              width: '90px',
              height: '90px',
              border: '2px solid #000000',
              padding: '6px',
              background: '#ffffff',
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              justifyContent: 'center'
            }}>
              <QrCode size={64} color="#000000" />
            </div>
            <span style={{ fontSize: '10px', fontWeight: 700, display: 'block', marginTop: '2px' }}>
              Scan to Track
            </span>
          </div>
        </div>

        <div style={{ textAlign: 'center', fontSize: '11px', color: '#64748b', marginTop: '16px', borderTop: '1px dashed #cbd5e1', paddingTop: '8px' }}>
          Valid without physical signature. Verified under Digital India e-Courts initiative.
        </div>
      </div>
    </div>
  );
}
