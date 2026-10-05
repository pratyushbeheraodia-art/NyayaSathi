import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useLanguage } from '../context/LanguageContext';
import AudioSpeaker from '../components/AudioSpeaker';
import { 
  Clock, 
  AlertTriangle, 
  CheckCircle, 
  XCircle, 
  Calendar, 
  FileText,
  ShieldAlert
} from 'lucide-react';

export default function DeadlinePage() {
  const { lang, t, speakText } = useLanguage();
  const [deadlines, setDeadlines] = useState([]);
  const [category, setCategory] = useState('Cheque Dishonour');
  const [incidentDate, setIncidentDate] = useState(() => {
    const d = new Date();
    d.setDate(d.getDate() - 10);
    return d.toISOString().split('T')[0];
  });
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetch('/api/deadlines')
      .then(res => res.json())
      .then(data => {
        setDeadlines(data.deadlines || []);
        if (data.deadlines && data.deadlines.length > 0) {
          setCategory(data.deadlines[0].dispute_type_en);
        }
      });
  }, []);

  const handleCalculate = async () => {
    setLoading(true);
    try {
      const res = await fetch('/api/deadlines/calculate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          dispute_category: category,
          incident_date: incidentDate
        })
      });
      const data = await res.json();
      setResult(data);
      speakText(data.advice);
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
            {t('cardDeadlinesTitle')}
          </h2>
          <p style={{ color: '#64748b', fontSize: '14px' }}>
            Limitation Act calculator: Determine the absolute deadline to protect your case from statutory lapse.
          </p>
        </div>

        <AudioSpeaker text="Deadline Guardian. Under the Indian Limitation Act, failure to file within statutory limits can permanently bar your legal claim. Calculate your deadline now." />
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: '24px', marginBottom: '32px' }}>
        {/* Calculator Inputs */}
        <div style={{
          background: '#ffffff',
          borderRadius: '16px',
          border: '1px solid #cbd5e1',
          padding: '24px',
          boxShadow: '0 4px 6px -1px rgba(0,0,0,0.05)'
        }}>
          <h3 style={{ fontSize: '18px', fontWeight: 700, color: '#1e3a8a', marginBottom: '18px', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <Clock size={20} /> Limitation Period Calculator
          </h3>

          <div style={{ marginBottom: '16px' }}>
            <label style={{ display: 'block', fontSize: '14px', fontWeight: 700, color: '#334155', marginBottom: '6px' }}>
              Select Legal Matter / Cause of Action:
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
              {deadlines.map((d, i) => (
                <option key={i} value={d.dispute_type_en}>
                  {d[`dispute_type_${lang}`] || d.dispute_type_en}
                </option>
              ))}
            </select>
          </div>

          <div style={{ marginBottom: '22px' }}>
            <label style={{ display: 'block', fontSize: '14px', fontWeight: 700, color: '#334155', marginBottom: '6px' }}>
              Date Incident Occurred / Cheque Bounced / Notice Received:
            </label>
            <input
              type="date"
              value={incidentDate}
              onChange={(e) => setIncidentDate(e.target.value)}
              style={{
                width: '100%',
                padding: '12px 14px',
                borderRadius: '8px',
                border: '1px solid #cbd5e1',
                fontSize: '14px',
                color: '#0f172a'
              }}
            />
          </div>

          <button
            onClick={handleCalculate}
            disabled={loading}
            className="btn-primary"
            style={{ width: '100%' }}
          >
            {loading ? "Calculating Expiry..." : "Check Statutory Deadline"}
          </button>
        </div>

        {/* Calculation Result */}
        <div style={{
          background: '#ffffff',
          borderRadius: '16px',
          border: '1px solid #cbd5e1',
          padding: '24px',
          boxShadow: '0 4px 6px -1px rgba(0,0,0,0.05)'
        }}>
          {!result ? (
            <div style={{ textAlign: 'center', padding: '50px 20px', color: '#64748b' }}>
              <Clock size={44} style={{ opacity: 0.4, marginBottom: '10px' }} />
              <p>Select your dispute type and date on the left to verify your limitation timeline.</p>
            </div>
          ) : (
            <div>
              <div style={{
                background: result.status === 'SAFE' ? '#f0fdf4' : result.status === 'CRITICAL_WARNING' ? '#fffbeb' : '#fef2f2',
                border: `2px solid ${result.status === 'SAFE' ? '#86efac' : result.status === 'CRITICAL_WARNING' ? '#fde68a' : '#fca5a5'}`,
                borderRadius: '14px',
                padding: '18px',
                marginBottom: '18px'
              }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '8px' }}>
                  {result.status === 'SAFE' ? <CheckCircle size={24} color="#16a34a" /> : result.status === 'CRITICAL_WARNING' ? <AlertTriangle size={24} color="#d97706" /> : <XCircle size={24} color="#dc2626" />}
                  <h4 style={{ fontSize: '18px', fontWeight: 800, color: result.status === 'SAFE' ? '#166534' : result.status === 'CRITICAL_WARNING' ? '#92400e' : '#991b1b' }}>
                    {result.status === 'SAFE' ? "Within Limitation Period" : result.status === 'CRITICAL_WARNING' ? "Urgent Limitation Warning!" : "Statutory Period Expired"}
                  </h4>
                </div>

                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline', marginTop: '12px' }}>
                  <div>
                    <span style={{ fontSize: '12px', color: '#475569', fontWeight: 600 }}>Last Date to File:</span>
                    <div style={{ fontSize: '20px', fontWeight: 800, color: '#0f172a' }}>{result.expiry_date}</div>
                  </div>
                  <div style={{ textAlign: 'right' }}>
                    <span style={{ fontSize: '12px', color: '#475569', fontWeight: 600 }}>Days Remaining:</span>
                    <div style={{ fontSize: '22px', fontWeight: 800, color: result.days_remaining > 15 ? '#16a34a' : '#dc2626' }}>
                      {result.days_remaining} Days
                    </div>
                  </div>
                </div>
              </div>

              <div style={{ marginBottom: '16px' }}>
                <div style={{ fontSize: '12px', fontWeight: 700, color: '#64748b' }}>Statutory Rule:</div>
                <div style={{ fontSize: '14px', fontWeight: 700, color: '#1e3a8a', marginTop: '2px' }}>{result.act_reference}</div>
              </div>

              <div style={{ background: '#f8fafc', padding: '14px', borderRadius: '10px', fontSize: '14px', color: '#334155', lineHeight: 1.5, borderLeft: '4px solid #2563eb' }}>
                <strong>Advisory:</strong> {result.advice}
              </div>
            </div>
          )}
        </div>
      </div>

      {/* Statutory Rules Master Table */}
      <div style={{ background: '#ffffff', borderRadius: '16px', border: '1px solid #e2e8f0', padding: '24px' }}>
        <h3 style={{ fontSize: '18px', fontWeight: 700, color: '#0f172a', marginBottom: '14px' }}>
          Statutory Limitation Reference Chart (Indian Law)
        </h3>
        <div style={{ overflowX: 'auto' }}>
          <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '14px' }}>
            <thead>
              <tr style={{ background: '#f8fafc', borderBottom: '2px solid #e2e8f0', textAlign: 'left' }}>
                <th style={{ padding: '12px 16px' }}>Dispute Category</th>
                <th style={{ padding: '12px 16px' }}>Statutory Limitation</th>
                <th style={{ padding: '12px 16px' }}>Act Reference</th>
                <th style={{ padding: '12px 16px' }}>Trigger Event</th>
              </tr>
            </thead>
            <tbody>
              {deadlines.map((dl, idx) => (
                <tr key={idx} style={{ borderBottom: '1px solid #e2e8f0' }}>
                  <td style={{ padding: '12px 16px', fontWeight: 700, color: '#0f172a' }}>
                    {dl[`dispute_type_${lang}`] || dl.dispute_type_en}
                  </td>
                  <td style={{ padding: '12px 16px', color: '#dc2626', fontWeight: 600 }}>
                    {dl.limit_period_text}
                  </td>
                  <td style={{ padding: '12px 16px', color: '#475569' }}>
                    {dl.act_reference}
                  </td>
                  <td style={{ padding: '12px 16px', color: '#475569' }}>
                    {dl.trigger_event}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
