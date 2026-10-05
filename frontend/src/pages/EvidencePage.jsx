import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useLanguage } from '../context/LanguageContext';
import { useKiosk } from '../context/KioskContext';
import AudioSpeaker from '../components/AudioSpeaker';
import { 
  FolderCheck, 
  Upload, 
  Trash2, 
  FileText, 
  Image, 
  CheckCircle, 
  ShieldAlert,
  Sparkles,
  Camera,
  Plus
} from 'lucide-react';

export default function EvidencePage() {
  const { lang, t } = useLanguage();
  const { sessionId, activeCategory } = useKiosk();
  const [evidenceList, setEvidenceList] = useState([]);
  const [loading, setLoading] = useState(true);
  const [fileName, setFileName] = useState('');
  const [fileType, setFileType] = useState('PDF Document');
  const [notes, setNotes] = useState('');

  const fetchEvidence = () => {
    fetch(`/api/evidence/${sessionId}`)
      .then(res => res.json())
      .then(data => {
        setEvidenceList(data.evidence || []);
        setLoading(false);
      })
      .catch(err => setLoading(false));
  };

  useEffect(() => {
    fetchEvidence();
  }, [sessionId]);

  const handleUpload = async (customName = null, customType = null, customNotes = null) => {
    const fName = customName || fileName || `Evidence_${Date.now()}.pdf`;
    const fType = customType || fileType;
    const fNotes = customNotes || notes || "Submitted via Kiosk Document Scanner";

    try {
      const res = await fetch('/api/evidence/upload', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          session_id: sessionId,
          file_name: fName,
          file_type: fType,
          file_size: "1.4 MB",
          category: activeCategory,
          notes: fNotes
        })
      });
      const data = await res.json();
      if (data.status === 'SUCCESS') {
        setFileName('');
        setNotes('');
        fetchEvidence();
      }
    } catch (e) {
      console.error(e);
    }
  };

  const handleDelete = async (id) => {
    try {
      await fetch(`/api/evidence/${id}`, { method: 'DELETE' });
      fetchEvidence();
    } catch (e) {
      console.error(e);
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
            {t('cardEvidenceTitle')}
          </h2>
          <p style={{ color: '#64748b', fontSize: '14px' }}>
            Catalog receipts, boundary photos, witness diaries, and official notices for court submission.
          </p>
        </div>

        <AudioSpeaker text="Evidence Organizer. Securely catalog photographs, payment receipts, and witness records to strengthen your legal claim under the Bharatiya Sakshya Adhiniyam." />
      </div>

      {/* Quick Add Presets (Kiosk Friendly) */}
      <div style={{
        background: '#eff6ff',
        border: '1px solid #bfdbfe',
        borderRadius: '16px',
        padding: '20px',
        marginBottom: '24px'
      }}>
        <div style={{ fontSize: '14px', fontWeight: 700, color: '#1e40af', marginBottom: '12px', display: 'flex', alignItems: 'center', gap: '6px' }}>
          <Sparkles size={16} /> Quick Add Simulated Evidence (Kiosk Optical Scanner / Camera):
        </div>
        <div style={{ display: 'flex', gap: '10px', flexWrap: 'wrap' }}>
          <button 
            className="control-btn"
            style={{ background: '#ffffff', color: '#1e40af', borderColor: '#93c5fd' }}
            onClick={() => handleUpload("Survey_Plot_Boundary_Photo.jpg", "JPEG Image", "Clear photo of boundary pegs removed by encroacher")}
          >
            📸 Plot Boundary Photo
          </button>
          <button 
            className="control-btn"
            style={{ background: '#ffffff', color: '#1e40af', borderColor: '#93c5fd' }}
            onClick={() => handleUpload("Khajna_Tax_Receipt_2025-26.pdf", "PDF Receipt", "Official revenue tax receipt proving current possession")}
          >
            🧾 Land Revenue Khajna Receipt
          </button>
          <button 
            className="control-btn"
            style={{ background: '#ffffff', color: '#1e40af', borderColor: '#93c5fd' }}
            onClick={() => handleUpload("Unpaid_Wage_Passbook_Statement.pdf", "Bank PDF", "Bank passbook showing no salary credit for 4 months")}
          >
            💳 Bank Passbook Statement
          </button>
          <button 
            className="control-btn"
            style={{ background: '#ffffff', color: '#1e40af', borderColor: '#93c5fd' }}
            onClick={() => handleUpload("Machine_Warranty_GST_Invoice.jpg", "Invoice Image", "Retailer invoice and stamp for defective agricultural machinery")}
          >
            🚜 Machine Invoice & Warranty
          </button>
        </div>
      </div>

      {/* Manual Input Form */}
      <div style={{
        background: '#ffffff',
        borderRadius: '16px',
        border: '1px solid #e2e8f0',
        padding: '20px',
        marginBottom: '24px'
      }}>
        <h4 style={{ fontSize: '16px', fontWeight: 700, color: '#0f172a', marginBottom: '14px' }}>
          Add Custom Document or File Note:
        </h4>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '12px', marginBottom: '12px' }}>
          <input
            type="text"
            placeholder="Document Name (e.g. Village Panchayat Resolution)"
            value={fileName}
            onChange={(e) => setFileName(e.target.value)}
            style={{
              padding: '10px 14px',
              borderRadius: '8px',
              border: '1px solid #cbd5e1',
              fontSize: '14px'
            }}
          />
          <select
            value={fileType}
            onChange={(e) => setFileType(e.target.value)}
            style={{
              padding: '10px 14px',
              borderRadius: '8px',
              border: '1px solid #cbd5e1',
              fontSize: '14px'
            }}
          >
            <option>PDF Document</option>
            <option>JPEG / PNG Photo</option>
            <option>Audio Recording</option>
            <option>Handwritten Note</option>
          </select>
          <input
            type="text"
            placeholder="Relevance Note (Why is this important?)"
            value={notes}
            onChange={(e) => setNotes(e.target.value)}
            style={{
              padding: '10px 14px',
              borderRadius: '8px',
              border: '1px solid #cbd5e1',
              fontSize: '14px'
            }}
          />
        </div>
        <button
          onClick={() => handleUpload()}
          className="btn-primary"
          style={{ padding: '8px 20px', fontSize: '14px' }}
        >
          <Plus size={16} /> Save Document Record
        </button>
      </div>

      {/* Cataloged Evidence List */}
      <div>
        <h3 style={{ fontSize: '18px', fontWeight: 700, color: '#0f172a', marginBottom: '14px' }}>
          Cataloged Evidence Files ({evidenceList.length})
        </h3>

        {evidenceList.length === 0 ? (
          <div style={{
            background: '#ffffff',
            borderRadius: '12px',
            border: '2px dashed #cbd5e1',
            padding: '36px',
            textAlign: 'center',
            color: '#64748b'
          }}>
            <FolderCheck size={40} style={{ opacity: 0.5, marginBottom: '10px' }} />
            <p>No evidence files recorded yet. Use the quick presets above to scan or attach proof.</p>
          </div>
        ) : (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
            {evidenceList.map((item) => (
              <div
                key={item.id}
                style={{
                  background: '#ffffff',
                  border: '1px solid #e2e8f0',
                  borderRadius: '12px',
                  padding: '16px 20px',
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'center',
                  flexWrap: 'wrap',
                  gap: '12px'
                }}
              >
                <div style={{ display: 'flex', alignItems: 'center', gap: '14px' }}>
                  <div style={{
                    width: '42px',
                    height: '42px',
                    borderRadius: '10px',
                    background: '#eff6ff',
                    color: '#2563eb',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center'
                  }}>
                    {item.file_type.includes('Image') ? <Image size={22} /> : <FileText size={22} />}
                  </div>

                  <div>
                    <h4 style={{ fontSize: '16px', fontWeight: 700, color: '#0f172a' }}>
                      {item.file_name}
                    </h4>
                    <p style={{ fontSize: '13px', color: '#64748b', marginTop: '2px' }}>
                      {item.notes} | <span style={{ fontWeight: 600 }}>{item.file_size}</span>
                    </p>
                  </div>
                </div>

                <div style={{ display: 'flex', alignItems: 'center', gap: '16px' }}>
                  <div style={{ textAlign: 'right' }}>
                    <div style={{ fontSize: '11px', color: '#64748b', fontWeight: 600 }}>Legal Relevance</div>
                    <div style={{ fontSize: '15px', fontWeight: 800, color: '#059669', display: 'flex', alignItems: 'center', gap: '4px' }}>
                      <CheckCircle size={15} /> {item.relevance_score}% High
                    </div>
                  </div>

                  <button
                    onClick={() => handleDelete(item.id)}
                    style={{
                      border: 'none',
                      background: '#fee2e2',
                      color: '#dc2626',
                      borderRadius: '8px',
                      padding: '8px',
                      cursor: 'pointer'
                    }}
                    title="Remove item"
                  >
                    <Trash2 size={16} />
                  </button>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
