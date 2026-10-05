import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useLanguage } from '../context/LanguageContext';
import AudioSpeaker from '../components/AudioSpeaker';
import { 
  BookOpen, 
  Search, 
  Scale, 
  ShieldCheck, 
  FileText, 
  PhoneCall,
  Sparkles
} from 'lucide-react';

export default function LegalKnowledgePage() {
  const { lang, t } = useLanguage();
  const [articles, setArticles] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [loading, setLoading] = useState(true);

  const fetchArticles = (q = '') => {
    setLoading(true);
    fetch(`/api/legal/articles?q=${encodeURIComponent(q)}&lang=${lang}`)
      .then(res => res.json())
      .then(data => {
        setArticles(data.articles || []);
        setLoading(false);
      })
      .catch(err => setLoading(false));
  };

  useEffect(() => {
    fetchArticles(searchTerm);
  }, [lang]);

  const handleSearch = (e) => {
    e.preventDefault();
    fetchArticles(searchTerm);
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
            {t('cardArticlesTitle')}
          </h2>
          <p style={{ color: '#64748b', fontSize: '14px' }}>
            Simplified statutory guides on Indian Penal Codes (BNS, BNSS), land reforms, and consumer rights.
          </p>
        </div>

        <AudioSpeaker text="Legal Information Guide. Learn your basic rights, relevant sections, and court remedies explained in simple citizen language." />
      </div>

      {/* Search Bar */}
      <form onSubmit={handleSearch} style={{ display: 'flex', gap: '10px', marginBottom: '24px' }}>
        <div style={{ position: 'relative', flex: 1 }}>
          <Search size={18} style={{ position: 'absolute', left: '14px', top: '15px', color: '#64748b' }} />
          <input
            type="text"
            placeholder="Search by act, section, or issue (e.g. BNS, Sec 164, Land Patta, Wages)..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
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
          Search Guides
        </button>
      </form>

      {/* Articles List */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
        {articles.map((art) => {
          const title = art[`title_${lang}`] || art.title_en;
          const summary = art[`summary_${lang}`] || art.summary_en;

          return (
            <div
              key={art.id}
              style={{
                background: '#ffffff',
                borderRadius: '16px',
                border: '1px solid #e2e8f0',
                padding: '24px',
                boxShadow: '0 2px 4px rgba(0,0,0,0.03)'
              }}
            >
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '10px', marginBottom: '12px' }}>
                <div>
                  <span style={{ fontSize: '11px', fontWeight: 700, textTransform: 'uppercase', background: '#eff6ff', color: '#2563eb', padding: '3px 8px', borderRadius: '4px' }}>
                    {art.category.replace('_', ' ')}
                  </span>
                  <h3 style={{ fontSize: '20px', fontWeight: 800, color: '#1e3a8a', marginTop: '6px' }}>
                    {title}
                  </h3>
                </div>

                <AudioSpeaker text={`${title}. Summary: ${summary}. Legal sections: ${art.legal_sections}. Remedies: ${art.remedies}`} />
              </div>

              <p style={{ fontSize: '15px', color: '#334155', lineHeight: 1.6, marginBottom: '18px' }}>
                {summary}
              </p>

              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: '12px', background: '#f8fafc', padding: '16px', borderRadius: '12px', marginBottom: '14px' }}>
                <div>
                  <div style={{ fontSize: '12px', fontWeight: 700, color: '#64748b' }}>Statutory Sections:</div>
                  <div style={{ fontSize: '14px', fontWeight: 700, color: '#0f172a', marginTop: '2px' }}>{art.legal_sections}</div>
                </div>
                <div>
                  <div style={{ fontSize: '12px', fontWeight: 700, color: '#64748b' }}>Governing Act:</div>
                  <div style={{ fontSize: '14px', fontWeight: 700, color: '#0f172a', marginTop: '2px' }}>{art.relevant_acts}</div>
                </div>
                <div>
                  <div style={{ fontSize: '12px', fontWeight: 700, color: '#64748b' }}>Available Legal Remedies:</div>
                  <div style={{ fontSize: '14px', fontWeight: 700, color: '#059669', marginTop: '2px' }}>{art.remedies}</div>
                </div>
              </div>

              <div style={{ fontSize: '13px', color: '#475569', lineHeight: 1.5 }}>
                <strong>Procedure Summary:</strong> {art.procedure_steps}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
