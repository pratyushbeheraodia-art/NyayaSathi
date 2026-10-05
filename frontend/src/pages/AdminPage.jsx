import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useLanguage } from '../context/LanguageContext';
import { useKiosk } from '../context/KioskContext';
import HardwareDiagram from '../components/HardwareDiagram';
import AudioSpeaker from '../components/AudioSpeaker';
import { 
  Cpu, 
  BarChart3, 
  ToggleLeft, 
  ToggleRight, 
  Activity, 
  Clock, 
  ShieldCheck, 
  Users, 
  Database,
  Radio,
  Battery
} from 'lucide-react';

export default function AdminPage() {
  const { lang, t } = useLanguage();
  const { demoMode, setDemoMode } = useKiosk();
  const [metrics, setMetrics] = useState(null);
  const [queriesLog, setQueriesLog] = useState([]);
  const [escalationsLog, setEscalationsLog] = useState([]);
  const [activeTab, setActiveTab] = useState('hardware');

  useEffect(() => {
    fetch('/api/admin/metrics')
      .then(res => res.json())
      .then(data => setMetrics(data));

    fetch('/api/admin/queries')
      .then(res => res.json())
      .then(data => setQueriesLog(data.queries || []));

    fetch('/api/admin/escalations')
      .then(res => res.json())
      .then(data => setEscalationsLog(data.escalations || []));
  }, []);

  return (
    <div className="kiosk-container">
      {/* Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px', flexWrap: 'wrap', gap: '12px' }}>
        <div>
          <Link to="/" style={{ color: '#64748b', textDecoration: 'none', fontSize: '14px', fontWeight: 600 }}>
            ← Back to Home
          </Link>
          <h2 style={{ fontSize: '26px', fontWeight: 800, color: '#0f172a', marginTop: '4px' }}>
            {t('cardAdminTitle')}
          </h2>
          <p style={{ color: '#64748b', fontSize: '14px' }}>
            Kiosk health telemetry, system metrics, hardware architecture, and audit logs.
          </p>
        </div>

        {/* Demo Mode Toggle */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '10px', background: '#ffffff', border: '1px solid #cbd5e1', padding: '8px 16px', borderRadius: '12px' }}>
          <span style={{ fontSize: '14px', fontWeight: 700, color: '#0f172a' }}>
            Demo Mode:
          </span>
          <button
            onClick={() => setDemoMode(!demoMode)}
            style={{ border: 'none', background: 'transparent', cursor: 'pointer', display: 'flex', alignItems: 'center' }}
          >
            {demoMode ? (
              <span style={{ display: 'flex', alignItems: 'center', gap: '6px', color: '#16a34a', fontWeight: 700 }}>
                <ToggleRight size={32} /> ACTIVE (MOCK AI)
              </span>
            ) : (
              <span style={{ display: 'flex', alignItems: 'center', gap: '6px', color: '#64748b', fontWeight: 600 }}>
                <ToggleLeft size={32} /> LIVE API
              </span>
            )}
          </button>
        </div>
      </div>

      {/* Top 4 Metrics Widgets */}
      {metrics && (
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '16px', marginBottom: '24px' }}>
          <div style={{ background: '#ffffff', borderRadius: '14px', border: '1px solid #e2e8f0', padding: '18px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', color: '#64748b', fontSize: '13px', fontWeight: 600 }}>
              <span>Total Kiosk Queries</span>
              <Activity size={18} color="#2563eb" />
            </div>
            <div style={{ fontSize: '28px', fontWeight: 900, color: '#0f172a', marginTop: '6px' }}>
              {metrics.total_queries}
            </div>
            <div style={{ fontSize: '12px', color: '#16a34a', fontWeight: 600, marginTop: '4px' }}>
              ↑ 18 today | Uptime {metrics.uptime}
            </div>
          </div>

          <div style={{ background: '#ffffff', borderRadius: '14px', border: '1px solid #e2e8f0', padding: '18px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', color: '#64748b', fontSize: '13px', fontWeight: 600 }}>
              <span>Language Distribution</span>
              <BarChart3 size={18} color="#059669" />
            </div>
            <div style={{ fontSize: '14px', fontWeight: 700, color: '#0f172a', marginTop: '8px' }}>
              Odia: {metrics.by_language.od} | Hindi: {metrics.by_language.hi} | English: {metrics.by_language.en}
            </div>
            <div style={{ fontSize: '12px', color: '#64748b', marginTop: '4px' }}>
              Primary: Odia (58% of interactions)
            </div>
          </div>

          <div style={{ background: '#ffffff', borderRadius: '14px', border: '1px solid #e2e8f0', padding: '18px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', color: '#64748b', fontSize: '13px', fontWeight: 600 }}>
              <span>Pending Escalations</span>
              <Users size={18} color="#ea580c" />
            </div>
            <div style={{ fontSize: '28px', fontWeight: 900, color: '#ea580c', marginTop: '6px' }}>
              {metrics.escalations_pending}
            </div>
            <div style={{ fontSize: '12px', color: '#64748b', marginTop: '4px' }}>
              Assigned to PLV S. Mohapatra
            </div>
          </div>

          <div style={{ background: '#ffffff', borderRadius: '14px', border: '1px solid #e2e8f0', padding: '18px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', color: '#64748b', fontSize: '13px', fontWeight: 600 }}>
              <span>Hardware Health</span>
              <Radio size={18} color="#0284c7" />
            </div>
            <div style={{ fontSize: '14px', fontWeight: 800, color: '#059669', marginTop: '8px' }}>
              {metrics.connectivity}
            </div>
            <div style={{ fontSize: '12px', color: '#475569', marginTop: '4px' }}>
              {metrics.kiosk_battery_backup}
            </div>
          </div>
        </div>
      )}

      {/* Tabs */}
      <div style={{ display: 'flex', gap: '10px', marginBottom: '20px' }}>
        <button
          onClick={() => setActiveTab('hardware')}
          style={{
            background: activeTab === 'hardware' ? '#1e3a8a' : '#ffffff',
            color: activeTab === 'hardware' ? '#ffffff' : '#334155',
            border: '1px solid #cbd5e1',
            borderRadius: '8px',
            padding: '10px 20px',
            fontWeight: 700,
            fontSize: '14px',
            cursor: 'pointer'
          }}
        >
          Hardware Architecture Blueprint
        </button>
        <button
          onClick={() => setActiveTab('logs')}
          style={{
            background: activeTab === 'logs' ? '#1e3a8a' : '#ffffff',
            color: activeTab === 'logs' ? '#ffffff' : '#334155',
            border: '1px solid #cbd5e1',
            borderRadius: '8px',
            padding: '10px 20px',
            fontWeight: 700,
            fontSize: '14px',
            cursor: 'pointer'
          }}
        >
          Kiosk Query Logs & Telemetry
        </button>
      </div>

      {activeTab === 'hardware' ? (
        <HardwareDiagram />
      ) : (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
          {/* Query Logs Table */}
          <div style={{ background: '#ffffff', borderRadius: '16px', border: '1px solid #e2e8f0', padding: '24px' }}>
            <h3 style={{ fontSize: '18px', fontWeight: 800, color: '#0f172a', marginBottom: '16px' }}>
              Recent Citizen Queries (Privacy Mode Wipes PII)
            </h3>
            <div style={{ overflowX: 'auto' }}>
              <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '13px' }}>
                <thead>
                  <tr style={{ background: '#f8fafc', borderBottom: '2px solid #e2e8f0', textAlign: 'left' }}>
                    <th style={{ padding: '10px' }}>ID</th>
                    <th style={{ padding: '10px' }}>Category</th>
                    <th style={{ padding: '10px' }}>Query Text</th>
                    <th style={{ padding: '10px' }}>Language</th>
                    <th style={{ padding: '10px' }}>Confidence</th>
                    <th style={{ padding: '10px' }}>Time</th>
                  </tr>
                </thead>
                <tbody>
                  {queriesLog.map(q => (
                    <tr key={q.id} style={{ borderBottom: '1px solid #e2e8f0' }}>
                      <td style={{ padding: '10px', fontWeight: 700 }}>#{q.id}</td>
                      <td style={{ padding: '10px', color: '#1e3a8a', fontWeight: 600 }}>{q.detected_category}</td>
                      <td style={{ padding: '10px', maxWidth: '300px', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
                        {q.user_text}
                      </td>
                      <td style={{ padding: '10px', textTransform: 'uppercase' }}>{q.language}</td>
                      <td style={{ padding: '10px', color: '#059669', fontWeight: 700 }}>{Math.round(q.confidence * 100)}%</td>
                      <td style={{ padding: '10px', color: '#64748b' }}>{q.created_at}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
