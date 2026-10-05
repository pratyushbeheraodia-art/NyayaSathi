import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { useLanguage } from '../context/LanguageContext';
import AudioSpeaker from '../components/AudioSpeaker';
import { 
  Scale, 
  CheckCircle, 
  MapPin, 
  PhoneCall, 
  FileText, 
  ShieldCheck, 
  UserCheck, 
  ArrowRight 
} from 'lucide-react';

export default function LegalAidPage() {
  const { lang, t, speakText } = useLanguage();

  const [gender, setGender] = useState('female');
  const [category, setCategory] = useState('general');
  const [income, setIncome] = useState(180000);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const checkEligibility = async (g = gender, c = category, inc = income) => {
    setLoading(true);
    try {
      const res = await fetch('/api/legal-aid/check-eligibility', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          gender: g,
          category: c,
          annual_income: parseFloat(inc),
          state: "Odisha"
        })
      });
      const data = await res.json();
      setResult(data);

      const msg = data.eligible 
        ? "Congratulations. You are entitled to 100% Free Legal Aid under Section 12 of the Legal Services Authorities Act."
        : "Evaluation complete. Please review the criteria.";
      speakText(msg);
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
            {t('cardLegalAidTitle')}
          </h2>
          <p style={{ color: '#64748b', fontSize: '14px' }}>
            Check your entitlement for a free state panel advocate under Legal Services Authorities Act 1987.
          </p>
        </div>

        <AudioSpeaker text="National Legal Services Authority (NALSA) Free Legal Aid Checker. Find out if you qualify for a government lawyer at zero cost." />
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: '24px' }}>
        {/* Form Calculator Card */}
        <div style={{
          background: '#ffffff',
          borderRadius: '18px',
          border: '1px solid #cbd5e1',
          padding: '24px',
          boxShadow: '0 4px 6px -1px rgba(0,0,0,0.05)'
        }}>
          <h3 style={{ fontSize: '18px', fontWeight: 700, color: '#1e3a8a', marginBottom: '18px', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <UserCheck size={20} /> Citizen Profile Evaluator
          </h3>

          {/* Gender */}
          <div style={{ marginBottom: '18px' }}>
            <label style={{ display: 'block', fontSize: '14px', fontWeight: 700, color: '#334155', marginBottom: '8px' }}>
              Gender:
            </label>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '8px' }}>
              {['female', 'male', 'transgender'].map(g => (
                <button
                  key={g}
                  type="button"
                  onClick={() => setGender(g)}
                  style={{
                    background: gender === g ? '#1e3a8a' : '#f8fafc',
                    color: gender === g ? '#ffffff' : '#334155',
                    border: gender === g ? '1px solid #1e3a8a' : '1px solid #cbd5e1',
                    borderRadius: '8px',
                    padding: '10px 6px',
                    fontSize: '13px',
                    fontWeight: 700,
                    cursor: 'pointer',
                    textTransform: 'capitalize'
                  }}
                >
                  {g}
                </button>
              ))}
            </div>
            {gender === 'female' && (
              <span style={{ fontSize: '12px', color: '#16a34a', fontWeight: 600, display: 'block', marginTop: '4px' }}>
                ✓ All women qualify for 100% Free Legal Aid under Sec 12(c) regardless of income.
              </span>
            )}
          </div>

          {/* Category */}
          <div style={{ marginBottom: '18px' }}>
            <label style={{ display: 'block', fontSize: '14px', fontWeight: 700, color: '#334155', marginBottom: '8px' }}>
              Social / Occupational Category:
            </label>
            <select
              value={category}
              onChange={(e) => setCategory(e.target.value)}
              style={{
                width: '100%',
                padding: '10px 14px',
                borderRadius: '8px',
                border: '1px solid #cbd5e1',
                fontSize: '14px',
                color: '#0f172a'
              }}
            >
              <option value="general">General / Other</option>
              <option value="sc_st">Scheduled Caste (SC) / Scheduled Tribe (ST)</option>
              <option value="worker">Industrial Workman / Unorganized Construction Labor</option>
              <option value="disabled">Divyang / Person with Physical Disability</option>
              <option value="disaster_victim">Victim of Mass Disaster / Flood / Violence</option>
            </select>
          </div>

          {/* Income Slider */}
          <div style={{ marginBottom: '24px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '6px' }}>
              <label style={{ fontSize: '14px', fontWeight: 700, color: '#334155' }}>
                Annual Household Income:
              </label>
              <span style={{ fontSize: '15px', fontWeight: 800, color: '#2563eb' }}>
                ₹{income.toLocaleString()} / year
              </span>
            </div>
            <input
              type="range"
              min="0"
              max="500000"
              step="10000"
              value={income}
              onChange={(e) => setIncome(Number(e.target.value))}
              style={{ width: '100%', accentColor: '#2563eb' }}
            />
            <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px', color: '#64748b', marginTop: '2px' }}>
              <span>₹0</span>
              <span>₹3,00,000 (Odisha Free Ceiling)</span>
              <span>₹5,00,000</span>
            </div>
          </div>

          <button
            onClick={() => checkEligibility()}
            disabled={loading}
            className="btn-primary"
            style={{ width: '100%' }}
          >
            {loading ? "Evaluating..." : <><ShieldCheck size={18} /> Check Free Legal Aid Eligibility</>}
          </button>
        </div>

        {/* Results Card */}
        <div style={{
          background: '#ffffff',
          borderRadius: '18px',
          border: '1px solid #cbd5e1',
          padding: '24px',
          boxShadow: '0 4px 6px -1px rgba(0,0,0,0.05)'
        }}>
          {!result ? (
            <div style={{ textAlign: 'center', padding: '50px 20px', color: '#64748b' }}>
              <Scale size={48} style={{ opacity: 0.4, marginBottom: '12px' }} />
              <p>Configure your details on the left and tap evaluate to see free lawyer eligibility.</p>
            </div>
          ) : (
            <div>
              <div style={{
                background: result.eligible ? '#f0fdf4' : '#fffbeb',
                border: result.eligible ? '2px solid #86efac' : '2px solid #fde68a',
                borderRadius: '14px',
                padding: '16px',
                marginBottom: '18px',
                display: 'flex',
                alignItems: 'center',
                gap: '12px'
              }}>
                <CheckCircle size={32} color={result.eligible ? "#16a34a" : "#d97706"} />
                <div>
                  <h4 style={{ fontSize: '18px', fontWeight: 800, color: result.eligible ? '#166534' : '#92400e' }}>
                    {result.eligible ? "100% Eligible for Free Legal Aid" : "Subject to Discretionary Review"}
                  </h4>
                  <p style={{ fontSize: '13px', color: '#475569' }}>
                    Under Section 12, Legal Services Authorities Act, 1987.
                  </p>
                </div>
              </div>

              {/* Criteria Met */}
              <div style={{ marginBottom: '18px' }}>
                <h5 style={{ fontSize: '14px', fontWeight: 700, color: '#0f172a', marginBottom: '8px' }}>
                  Statutory Grounds Met:
                </h5>
                <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                  {result.criteria_met.map((cm, idx) => (
                    <div key={idx} style={{ fontSize: '13px', color: '#166534', background: '#ecfdf5', padding: '8px 12px', borderRadius: '6px', fontWeight: 500 }}>
                      ✓ {cm}
                    </div>
                  ))}
                </div>
              </div>

              {/* Free Benefits */}
              <div style={{ marginBottom: '18px' }}>
                <h5 style={{ fontSize: '14px', fontWeight: 700, color: '#0f172a', marginBottom: '8px' }}>
                  What You Get at Zero Cost:
                </h5>
                <ul style={{ paddingLeft: '20px', fontSize: '13px', color: '#334155', display: 'flex', flexDirection: 'column', gap: '4px' }}>
                  {result.benefits.map((b, idx) => (
                    <li key={idx}>{b}</li>
                  ))}
                </ul>
              </div>

              {/* Nearest DLSA Center */}
              <div style={{ background: '#f8fafc', border: '1px solid #e2e8f0', borderRadius: '12px', padding: '14px', marginBottom: '18px' }}>
                <div style={{ fontSize: '12px', fontWeight: 700, color: '#2563eb', textTransform: 'uppercase', marginBottom: '4px' }}>
                  Nearest Authority Desk:
                </div>
                <div style={{ fontSize: '14px', fontWeight: 700, color: '#0f172a' }}>
                  {result.nearest_office.name}
                </div>
                <div style={{ fontSize: '13px', color: '#64748b', marginTop: '2px' }}>
                  {result.nearest_office.location} | Toll-free: <strong>15100</strong>
                </div>
              </div>

              <Link to="/escalate" className="btn-primary" style={{ width: '100%', textDecoration: 'none' }}>
                Book Appointment with Free Panel Lawyer <ArrowRight size={16} />
              </Link>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
