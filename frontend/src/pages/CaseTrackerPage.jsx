import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useLanguage } from '../context/LanguageContext';
import AudioSpeaker from '../components/AudioSpeaker';
import { 
  Search, 
  Calendar, 
  Building, 
  User, 
  FileText, 
  CheckCircle2, 
  Clock, 
  ExternalLink,
  ChevronRight
} from 'lucide-react';

export default function CaseTrackerPage() {
  const { lang, t } = useLanguage();
  const [cases, setCases] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCase, setSelectedCase] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/cases')
      .then(res => res.json())
      .then(data => {
        setCases(data.cases || []);
        if (data.cases && data.cases.length > 0) {
          setSelectedCase(data.cases[0]);
        }
        setLoading(false);
      })
      .catch(err => setLoading(false));
  }, []);

  const handleSearch = (e) => {
    e.preventDefault();
    if (!searchQuery.trim()) return;
    fetch(`/api/cases/${searchQuery.trim()}`)
      .then(res => {
        if (!res.ok) throw new Error("Not found");
        return res.json();
      })
      .then(c => setSelectedCase(c))
      .catch(() => alert("No case found with that Case Number or CNR Number. Try selecting one of the demo cases below."));
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
            {t('cardCasesTitle')}
          </h2>
          <p style={{ color: '#64748b', fontSize: '14px' }}>
            e-Courts simulation: Track hearing dates, interim orders, and registered litigation.
          </p>
        </div>

        <AudioSpeaker text="e-Courts Case Status Tracker. Enter your 16-digit CNR number or select a case to view hearing dates and orders." />
      </div>

      {/* Search Input Bar */}
      <form onSubmit={handleSearch} style={{ display: 'flex', gap: '10px', marginBottom: '24px' }}>
        <div style={{ position: 'relative', flex: 1 }}>
          <Search size={18} style={{ position: 'absolute', left: '14px', top: '15px', color: '#64748b' }} />
          <input
            type="text"
            placeholder="Search by CNR Number (e.g., ODGN01-004521-2026) or Case No (LAND/2026/089)..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            style={{
              width: '100%',
              padding: '12px 16px 12px 42px',
              borderRadius: '12px',
              border: '2px solid #cbd5e1',
              fontSize: '15px',
              outline: 'none'
            }}
          />
        </div>
        <button type="submit" className="btn-primary" style={{ padding: '0 24px' }}>
          Track Case
        </button>
      </form>

      {/* Main Grid: Left Cases List, Right Selected Case Details */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: '20px' }}>
        {/* Left: 5 Demo Cases Selector */}
        <div>
          <h3 style={{ fontSize: '16px', fontWeight: 700, color: '#475569', marginBottom: '12px' }}>
            Pre-loaded Demo Cases ({cases.length})
          </h3>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
            {cases.map((c) => {
              const isSelected = selectedCase?.case_number === c.case_number;
              const caseTitle = c[`title_${lang}`] || c.title_en;
              return (
                <div
                  key={c.case_number}
                  onClick={() => setSelectedCase(c)}
                  style={{
                    background: isSelected ? '#eff6ff' : '#ffffff',
                    border: isSelected ? '2px solid #2563eb' : '1px solid #e2e8f0',
                    borderRadius: '12px',
                    padding: '14px 16px',
                    cursor: 'pointer',
                    transition: 'all 0.15s ease'
                  }}
                >
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '4px' }}>
                    <span style={{ fontSize: '12px', fontWeight: 700, color: '#2563eb' }}>
                      {c.case_number}
                    </span>
                    <span style={{ fontSize: '11px', fontWeight: 700, background: '#f1f5f9', color: '#475569', padding: '2px 6px', borderRadius: '4px' }}>
                      {c.status}
                    </span>
                  </div>

                  <h4 style={{ fontSize: '15px', fontWeight: 700, color: '#0f172a', marginBottom: '4px' }}>
                    {caseTitle}
                  </h4>

                  <div style={{ fontSize: '12px', color: '#64748b', display: 'flex', justifyContent: 'space-between' }}>
                    <span>CNR: {c.cnr_number}</span>
                    <span style={{ color: '#059669', fontWeight: 600 }}>Next: {c.next_hearing_date}</span>
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* Right: Detailed Case View */}
        {selectedCase && (
          <div style={{
            background: '#ffffff',
            borderRadius: '16px',
            border: '1px solid #cbd5e1',
            padding: '24px',
            boxShadow: '0 4px 6px -1px rgba(0,0,0,0.05)'
          }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '10px', borderBottom: '1px solid #e2e8f0', paddingBottom: '16px', marginBottom: '16px' }}>
              <div>
                <span style={{ fontSize: '12px', fontWeight: 700, color: '#2563eb', background: '#dbeafe', padding: '3px 8px', borderRadius: '4px' }}>
                  CNR: {selectedCase.cnr_number}
                </span>
                <h3 style={{ fontSize: '20px', fontWeight: 800, color: '#0f172a', marginTop: '6px' }}>
                  {selectedCase[`title_${lang}`] || selectedCase.title_en}
                </h3>
                <div style={{ fontSize: '13px', color: '#475569', display: 'flex', alignItems: 'center', gap: '6px', marginTop: '4px' }}>
                  <Building size={14} /> {selectedCase.court_name}
                </div>
              </div>

              <AudioSpeaker text={`Case ${selectedCase.case_number}. Next hearing date is scheduled on ${selectedCase.next_hearing_date}. Order: ${selectedCase.order_summary}`} />
            </div>

            {/* Key Hearing Banner */}
            <div style={{
              background: '#fef3c7',
              border: '1px solid #fde68a',
              borderRadius: '10px',
              padding: '12px 16px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
              marginBottom: '20px'
            }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                <Calendar size={20} color="#b45309" />
                <div>
                  <div style={{ fontSize: '11px', fontWeight: 700, color: '#b45309', textTransform: 'uppercase' }}>Upcoming Court Hearing</div>
                  <div style={{ fontSize: '17px', fontWeight: 800, color: '#92400e' }}>{selectedCase.next_hearing_date}</div>
                </div>
              </div>
              <span style={{ fontSize: '12px', fontWeight: 700, background: '#ffffff', color: '#b45309', padding: '4px 10px', borderRadius: '6px' }}>
                Status: {selectedCase.status}
              </span>
            </div>

            {/* Parties */}
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: '12px', marginBottom: '20px', background: '#f8fafc', padding: '14px', borderRadius: '10px' }}>
              <div>
                <span style={{ fontSize: '12px', fontWeight: 700, color: '#64748b' }}>Petitioner:</span>
                <div style={{ fontSize: '14px', fontWeight: 700, color: '#0f172a', marginTop: '2px' }}>{selectedCase.petitioner}</div>
              </div>
              <div>
                <span style={{ fontSize: '12px', fontWeight: 700, color: '#64748b' }}>Respondent:</span>
                <div style={{ fontSize: '14px', fontWeight: 700, color: '#0f172a', marginTop: '2px' }}>{selectedCase.respondent}</div>
              </div>
            </div>

            {/* Order Sheet Summary */}
            <div style={{ marginBottom: '20px' }}>
              <h4 style={{ fontSize: '14px', fontWeight: 700, color: '#0f172a', marginBottom: '6px' }}>
                Latest Interim Order Sheet:
              </h4>
              <p style={{ fontSize: '14px', color: '#334155', background: '#eff6ff', padding: '12px 14px', borderRadius: '8px', borderLeft: '4px solid #3b82f6', lineHeight: 1.5 }}>
                {selectedCase.order_summary}
              </p>
            </div>

            {/* Procedural Events Timeline */}
            <div>
              <h4 style={{ fontSize: '14px', fontWeight: 700, color: '#0f172a', marginBottom: '10px' }}>
                Case Milestones & Order History:
              </h4>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                {selectedCase.timeline && selectedCase.timeline.map((evt, idx) => (
                  <div key={idx} style={{ display: 'flex', alignItems: 'flex-start', gap: '10px', fontSize: '13px' }}>
                    <span style={{ minWidth: '85px', fontWeight: 700, color: '#2563eb' }}>{evt.date}</span>
                    <div style={{ flex: 1, background: '#f8fafc', padding: '6px 10px', borderRadius: '6px' }}>
                      <strong>{evt.stage}:</strong> {evt.note}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
