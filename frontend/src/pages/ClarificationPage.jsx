import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useLanguage } from '../context/LanguageContext';
import { useKiosk } from '../context/KioskContext';
import AudioSpeaker from '../components/AudioSpeaker';
import { 
  HelpCircle, 
  CheckCircle, 
  ArrowRight, 
  AlertTriangle, 
  ShieldCheck, 
  Compass, 
  Printer 
} from 'lucide-react';

export default function ClarificationPage() {
  const { lang, t, speakText } = useLanguage();
  const { activeCategory, clarificationAnswers, setClarificationAnswers } = useKiosk();
  const [questions, setQuestions] = useState([]);
  const [answers, setAnswers] = useState(clarificationAnswers || {});
  const [refinedResult, setRefinedResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    fetch(`/api/clarification/questions/${activeCategory}`)
      .then(res => res.json())
      .then(data => {
        setQuestions(data.questions || []);
      })
      .catch(err => console.error(err));
  }, [activeCategory]);

  const handleSelectOption = (qId, optionVal) => {
    setAnswers(prev => ({ ...prev, [qId]: optionVal }));
  };

  const handleSubmit = async () => {
    setLoading(true);
    try {
      const res = await fetch('/api/clarification/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          category: activeCategory,
          language: lang,
          answers: answers
        })
      });
      const data = await res.json();
      setRefinedResult(data);
      setClarificationAnswers(answers);

      const adviceMsg = data.custom_advice[lang] || data.custom_advice.en;
      speakText(adviceMsg);
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="kiosk-container">
      {/* Top Breadcrumb */}
      <div style={{ marginBottom: '20px' }}>
        <Link to="/voice" style={{ color: '#64748b', textDecoration: 'none', fontSize: '14px', fontWeight: 600 }}>
          ← Back to Voice Path
        </Link>
        <h2 style={{ fontSize: '26px', fontWeight: 800, color: '#0f172a', marginTop: '6px' }}>
          Smart Clarification Flow
        </h2>
        <p style={{ color: '#64748b', fontSize: '15px' }}>
          {t('clarificationPrompt')}
        </p>
      </div>

      {!refinedResult ? (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
          {questions.map((q, idx) => {
            const questionTitle = q[lang] || q.en;
            return (
              <div 
                key={q.id}
                style={{
                  background: '#ffffff',
                  borderRadius: '16px',
                  border: '1px solid #e2e8f0',
                  padding: '24px',
                  boxShadow: '0 2px 4px rgba(0,0,0,0.03)'
                }}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '14px' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                    <span style={{
                      width: '28px',
                      height: '28px',
                      borderRadius: '50%',
                      background: '#eff6ff',
                      color: '#2563eb',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      fontWeight: 700,
                      fontSize: '14px'
                    }}>
                      {idx + 1}
                    </span>
                    <h3 style={{ fontSize: '17px', fontWeight: 700, color: '#0f172a' }}>
                      {questionTitle}
                    </h3>
                  </div>
                  <AudioSpeaker text={questionTitle} />
                </div>

                {/* Options List */}
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: '12px' }}>
                  {q.options.map((opt) => {
                    const isSelected = answers[q.id] === opt.value;
                    const optText = opt[lang] || opt.en;
                    return (
                      <button
                        key={opt.value}
                        type="button"
                        onClick={() => handleSelectOption(q.id, opt.value)}
                        style={{
                          background: isSelected ? '#eff6ff' : '#f8fafc',
                          border: isSelected ? '2px solid #2563eb' : '1px solid #cbd5e1',
                          borderRadius: '12px',
                          padding: '16px',
                          textAlign: 'left',
                          cursor: 'pointer',
                          display: 'flex',
                          alignItems: 'center',
                          gap: '12px',
                          transition: 'all 0.15s ease'
                        }}
                      >
                        <div style={{
                          width: '20px',
                          height: '20px',
                          borderRadius: '50%',
                          border: isSelected ? '6px solid #2563eb' : '2px solid #94a3b8',
                          background: '#ffffff',
                          flexShrink: 0
                        }}></div>
                        <span style={{ fontSize: '15px', fontWeight: isSelected ? 700 : 500, color: isSelected ? '#1e40af' : '#1e293b' }}>
                          {optText}
                        </span>
                      </button>
                    );
                  })}
                </div>
              </div>
            );
          })}

          <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '10px' }}>
            <button
              onClick={handleSubmit}
              disabled={loading || Object.keys(answers).length === 0}
              className="btn-primary"
              style={{ padding: '14px 32px', fontSize: '17px' }}
            >
              {loading ? "Analyzing Answers..." : <>Submit & Refine Legal Plan <ArrowRight size={18} /></>}
            </button>
          </div>
        </div>
      ) : (
        /* Result Screen */
        <div style={{
          background: '#ffffff',
          borderRadius: '20px',
          border: '1px solid #cbd5e1',
          padding: '32px',
          boxShadow: '0 4px 6px -1px rgba(0,0,0,0.05)'
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '12px', marginBottom: '16px' }}>
            <div style={{ width: '48px', height: '48px', borderRadius: '50%', background: '#dcfce7', color: '#16a34a', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
              <ShieldCheck size={28} />
            </div>
            <div>
              <h3 style={{ fontSize: '22px', fontWeight: 800, color: '#0f172a' }}>
                Case Strategy Refined
              </h3>
              <p style={{ color: '#64748b', fontSize: '14px' }}>
                Your tailored legal advisory based on submitted facts:
              </p>
            </div>
          </div>

          <div style={{
            background: '#f0fdf4',
            border: '2px solid #86efac',
            borderRadius: '14px',
            padding: '20px',
            fontSize: '17px',
            fontWeight: 600,
            color: '#166534',
            lineHeight: 1.6,
            marginBottom: '28px',
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'flex-start',
            gap: '16px'
          }}>
            <div>
              {refinedResult.custom_advice[lang] || refinedResult.custom_advice.en}
            </div>
            <AudioSpeaker text={refinedResult.custom_advice[lang] || refinedResult.custom_advice.en} />
          </div>

          <div style={{ display: 'flex', gap: '14px', flexWrap: 'wrap' }}>
            <Link to="/journey" className="btn-primary" style={{ flex: 1, minWidth: '220px' }}>
              <Compass size={18} /> Proceed to Legal Journey Map
            </Link>
            <Link to="/evidence" className="btn-secondary" style={{ flex: 1, minWidth: '220px' }}>
              Upload Supporting Evidence
            </Link>
            <Link to="/slip" className="btn-secondary" style={{ minWidth: '180px' }}>
              <Printer size={18} /> Print Action Slip
            </Link>
          </div>
        </div>
      )}
    </div>
  );
}
