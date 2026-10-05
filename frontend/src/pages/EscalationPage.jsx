import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { useLanguage } from '../context/LanguageContext';
import { useKiosk } from '../context/KioskContext';
import AudioSpeaker from '../components/AudioSpeaker';
import { 
  Users, 
  Ticket, 
  Printer, 
  CheckCircle, 
  Phone, 
  MapPin, 
  ShieldAlert, 
  Clock 
} from 'lucide-react';

export default function EscalationPage() {
  const { lang, t, speakText } = useLanguage();
  const { activeCategory } = useKiosk();

  const [name, setName] = useState('');
  const [phone, setPhone] = useState('');
  const [category, setCategory] = useState(activeCategory);
  const [priority, setPriority] = useState('NORMAL');
  const [summary, setSummary] = useState('');
  const [tokenResult, setTokenResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!summary.trim()) {
      alert("Please provide a brief description of the issue.");
      return;
    }

    setLoading(true);
    try {
      const res = await fetch('/api/escalation/request', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          query_category: category,
          citizen_name: name || "Anonymous Citizen",
          phone_number: phone || null,
          issue_summary: summary,
          language: lang,
          priority: priority
        })
      });
      const data = await res.json();
      setTokenResult(data);
      speakText(`Your assistance token ${data.token_number} has been generated. Please proceed to ${data.kiosk_counter}.`);
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="kiosk-container">
      {/* Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px', flexWrap: 'wrap', gap: '12px' }}>
        <div>
          <Link to="/" style={{ color: '#64748b', textDecoration: 'none', fontSize: '14px', fontWeight: 600 }}>
            ← Back to Home
          </Link>
          <h2 style={{ fontSize: '26px', fontWeight: 800, color: '#0f172a', marginTop: '4px' }}>
            {t('cardEscalateTitle')}
          </h2>
          <p style={{ color: '#64748b', fontSize: '14px' }}>
            Connect with a local Paralegal Volunteer (PLV) or book a free Tele-Law advocate video call.
          </p>
        </div>

        <AudioSpeaker text="Human Help Escalation. If you need physical in-person assistance, request a token to meet our dedicated Paralegal Volunteer." />
      </div>

      {!tokenResult ? (
        <form onSubmit={handleSubmit} style={{
          background: '#ffffff',
          borderRadius: '18px',
          border: '1px solid #cbd5e1',
          padding: '28px',
          boxShadow: '0 4px 6px -1px rgba(0,0,0,0.05)',
          maxWidth: '720px',
          margin: '0 auto'
        }}>
          <h3 style={{ fontSize: '18px', fontWeight: 800, color: '#1e3a8a', marginBottom: '20px', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <Users size={22} /> Request On-Site / Virtual Paralegal Assistance
          </h3>

          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: '16px', marginBottom: '16px' }}>
            <div>
              <label style={{ display: 'block', fontSize: '14px', fontWeight: 700, color: '#334155', marginBottom: '6px' }}>
                Citizen Name (Optional / Can remain anonymous):
              </label>
              <input
                type="text"
                placeholder="e.g. Ramesh Nayak or Anonymous"
                value={name}
                onChange={(e) => setName(e.target.value)}
                style={{
                  width: '100%',
                  padding: '12px 14px',
                  borderRadius: '8px',
                  border: '1px solid #cbd5e1',
                  fontSize: '14px'
                }}
              />
            </div>

            <div>
              <label style={{ display: 'block', fontSize: '14px', fontWeight: 700, color: '#334155', marginBottom: '6px' }}>
                Mobile Number (For SMS token & callback):
              </label>
              <input
                type="tel"
                placeholder="10-digit mobile number"
                value={phone}
                onChange={(e) => setPhone(e.target.value)}
                style={{
                  width: '100%',
                  padding: '12px 14px',
                  borderRadius: '8px',
                  border: '1px solid #cbd5e1',
                  fontSize: '14px'
                }}
              />
            </div>
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: '16px', marginBottom: '16px' }}>
            <div>
              <label style={{ display: 'block', fontSize: '14px', fontWeight: 700, color: '#334155', marginBottom: '6px' }}>
                Dispute Classification:
              </label>
              <select
                value={category}
                onChange={(e) => setCategory(e.target.value)}
                style={{
                  width: '100%',
                  padding: '12px 14px',
                  borderRadius: '8px',
                  border: '1px solid #cbd5e1',
                  fontSize: '14px',
                  color: '#0f172a'
                }}
              >
                <option value="land_dispute">Land Encroachment & Mutation</option>
                <option value="labor_dispute">Unpaid Wage & Labor Dispute</option>
                <option value="consumer_dispute">Consumer Defect & Warranty</option>
                <option value="family_dispute">Domestic Violence & Protection</option>
                <option value="cyber_fraud">Cyber Fraud & Bank Lien</option>
              </select>
            </div>

            <div>
              <label style={{ display: 'block', fontSize: '14px', fontWeight: 700, color: '#334155', marginBottom: '6px' }}>
                Urgency Level:
              </label>
              <select
                value={priority}
                onChange={(e) => setPriority(e.target.value)}
                style={{
                  width: '100%',
                  padding: '12px 14px',
                  borderRadius: '8px',
                  border: '1px solid #cbd5e1',
                  fontSize: '14px',
                  color: '#0f172a'
                }}
              >
                <option value="NORMAL">Normal In-Person Queue</option>
                <option value="HIGH">High Priority (Elderly / Disabled / Worker)</option>
                <option value="CRITICAL">Critical Emergency (Immediate Threat / Active Fraud)</option>
              </select>
            </div>
          </div>

          <div style={{ marginBottom: '24px' }}>
            <label style={{ display: 'block', fontSize: '14px', fontWeight: 700, color: '#334155', marginBottom: '6px' }}>
              Summary of Issue / Specific Help Needed:
            </label>
            <textarea
              rows={3}
              placeholder="Describe the current status or what specific legal help you need from the volunteer..."
              value={summary}
              onChange={(e) => setSummary(e.target.value)}
              style={{
                width: '100%',
                padding: '12px 14px',
                borderRadius: '8px',
                border: '1px solid #cbd5e1',
                fontSize: '14px',
                fontFamily: 'inherit',
                resize: 'none'
              }}
            />
          </div>

          <button
            type="submit"
            disabled={loading}
            className="btn-primary"
            style={{ width: '100%', padding: '14px', fontSize: '16px' }}
          >
            {loading ? "Registering Token..." : "Generate Assistance Token Slip"}
          </button>
        </form>
      ) : (
        /* Printable Token Slip View */
        <div style={{
          background: '#ffffff',
          borderRadius: '20px',
          border: '2px dashed #2563eb',
          padding: '36px',
          maxWidth: '640px',
          margin: '0 auto',
          boxShadow: '0 10px 25px -5px rgba(0,0,0,0.1)',
          textAlign: 'center'
        }} className="printable-slip">
          <div style={{ display: 'inline-flex', alignItems: 'center', gap: '8px', background: '#dbeafe', color: '#1e40af', padding: '6px 16px', borderRadius: '9999px', fontSize: '14px', fontWeight: 700, marginBottom: '14px' }}>
            <Ticket size={18} /> Official Kiosk Assistance Token
          </div>

          <h1 style={{ fontSize: '38px', fontWeight: 900, color: '#1e3a8a', letterSpacing: '1px', margin: '8px 0' }}>
            {tokenResult.token_number}
          </h1>

          <div style={{ fontSize: '16px', fontWeight: 700, color: '#059669', marginBottom: '16px' }}>
            Status: {tokenResult.status} | Priority: {tokenResult.priority}
          </div>

          <div style={{ background: '#f8fafc', borderRadius: '12px', border: '1px solid #e2e8f0', padding: '16px', textAlign: 'left', marginBottom: '24px' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '8px', fontSize: '14px' }}>
              <MapPin size={16} color="#2563eb" /> Location: <strong>{tokenResult.kiosk_counter}</strong>
            </div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px', fontSize: '14px' }}>
              <Phone size={16} color="#2563eb" /> Assigned PLV: <strong>{tokenResult.plv_contact}</strong>
            </div>
          </div>

          <p style={{ color: '#475569', fontSize: '14px', marginBottom: '24px', lineHeight: 1.5 }}>
            {tokenResult.message}
          </p>

          <div style={{ display: 'flex', gap: '12px', justifyContent: 'center' }} className="no-print">
            <button
              onClick={() => window.print()}
              className="btn-primary"
              style={{ padding: '12px 28px' }}
            >
              <Printer size={18} /> Print Kiosk Slip
            </button>
            <button
              onClick={() => setTokenResult(null)}
              className="btn-secondary"
            >
              Book Another
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
