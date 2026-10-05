import React, { useState, useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import { useLanguage } from '../context/LanguageContext';
import { useKiosk } from '../context/KioskContext';
import { Mic, MicOff, Send, X, Sparkles, Volume2 } from 'lucide-react';

export default function VoiceModal({ isOpen, onClose }) {
  const { lang, t, speakText } = useLanguage();
  const { sessionId, privacyMode, setActiveAnalysis, setActiveCategory } = useKiosk();
  const navigate = useNavigate();

  const [isRecording, setIsRecording] = useState(false);
  const [transcript, setTranscript] = useState('');
  const [loading, setLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState('');
  const recognitionRef = useRef(null);

  // Initialize Web Speech API Recognition
  useEffect(() => {
    if (!isOpen) return;

    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (SpeechRecognition) {
      const recognition = new SpeechRecognition();
      recognition.continuous = false;
      recognition.interimResults = true;

      if (lang === 'hi') recognition.lang = 'hi-IN';
      else if (lang === 'od') recognition.lang = 'hi-IN'; // Fallback for browsers without Odia acoustic model
      else recognition.lang = 'en-IN';

      recognition.onstart = () => {
        setIsRecording(true);
        setErrorMessage('');
      };

      recognition.onresult = (event) => {
        let currentTranscript = '';
        for (let i = 0; i < event.results.length; i++) {
          currentTranscript += event.results[i][0].transcript;
        }
        setTranscript(currentTranscript);
      };

      recognition.onerror = (event) => {
        console.warn("Speech recognition error:", event.error);
        setIsRecording(false);
        if (event.error === 'not-allowed') {
          setErrorMessage('Microphone access was denied. You can type or select a demo query below.');
        }
      };

      recognition.onend = () => {
        setIsRecording(false);
      };

      recognitionRef.current = recognition;
    } else {
      setErrorMessage('Browser native speech recognition not supported. Please type or use quick demo buttons.');
    }

    return () => {
      if (recognitionRef.current) {
        recognitionRef.current.abort();
      }
    };
  }, [isOpen, lang]);

  const toggleRecording = () => {
    if (!recognitionRef.current) {
      alert("Microphone not available on this browser. You can type your problem or use the sample buttons.");
      return;
    }

    if (isRecording) {
      recognitionRef.current.stop();
      setIsRecording(false);
    } else {
      setTranscript('');
      try {
        recognitionRef.current.start();
        setIsRecording(true);
      } catch (err) {
        console.warn("Recognition start failed", err);
      }
    }
  };

  const handleProcessQuery = async (queryText) => {
    const textToSubmit = queryText || transcript;
    if (!textToSubmit.trim()) return;

    setLoading(true);
    setErrorMessage('');

    try {
      const res = await fetch('/api/voice/process', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          text: textToSubmit,
          language: lang,
          privacy_mode: privacyMode,
          session_id: sessionId
        })
      });

      const data = await res.json();
      if (data.status === 'SUCCESS') {
        setActiveAnalysis(data.classification);
        setActiveCategory(data.classification.category);
        
        // Voice response
        const speechMsg = lang === 'hi' 
          ? `आपकी समस्या ${data.classification.title} के अंतर्गत वर्गीकृत की गई है।`
          : lang === 'od'
          ? `ଆପଣଙ୍କ ସମସ୍ୟା ${data.classification.title} ଅଧୀନରେ ଚିହ୍ନଟ ହୋଇଛି।`
          : `Your query has been classified under ${data.classification.title}.`;
        speakText(speechMsg);

        onClose();
        navigate('/voice');
      }
    } catch (e) {
      console.error(e);
      setErrorMessage('Error communicating with Legal AI engine. Please retry.');
    } finally {
      setLoading(false);
    }
  };

  if (!isOpen) return null;

  return (
    <div style={{
      position: 'fixed',
      top: 0,
      left: 0,
      right: 0,
      bottom: 0,
      backgroundColor: 'rgba(15, 23, 42, 0.75)',
      backdropFilter: 'blur(4px)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      zIndex: 100,
      padding: '20px'
    }}>
      <div style={{
        background: '#ffffff',
        borderRadius: '24px',
        width: '100%',
        maxWidth: '680px',
        padding: '32px',
        boxShadow: '0 25px 50px -12px rgba(0, 0, 0, 0.25)',
        position: 'relative'
      }}>
        {/* Close Button */}
        <button 
          onClick={onClose}
          style={{
            position: 'absolute',
            top: '20px',
            right: '20px',
            border: 'none',
            background: '#f1f5f9',
            borderRadius: '50%',
            width: '40px',
            height: '40px',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            cursor: 'pointer',
            color: '#64748b'
          }}
        >
          <X size={20} />
        </button>

        {/* Modal Title */}
        <div style={{ textAlign: 'center', marginBottom: '24px' }}>
          <div style={{
            display: 'inline-flex',
            alignItems: 'center',
            gap: '8px',
            background: '#eff6ff',
            color: '#1d4ed8',
            padding: '6px 14px',
            borderRadius: '9999px',
            fontSize: '13px',
            fontWeight: 700,
            marginBottom: '8px'
          }}>
            <Sparkles size={16} /> Web Speech API & NyayaSathi Engine
          </div>
          <h2 style={{ fontSize: '24px', fontWeight: 800, color: '#0f172a' }}>
            {t('voiceAssistant')}
          </h2>
          <p style={{ color: '#64748b', fontSize: '15px' }}>
            {isRecording ? t('listening') : t('speakIssuePrompt')}
          </p>
        </div>

        {/* Big Pulsing Mic Button */}
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
          <button 
            className={`big-mic-button ${isRecording ? 'recording' : ''}`}
            onClick={toggleRecording}
            title={isRecording ? "Stop recording" : "Start speaking"}
          >
            {isRecording ? <MicOff size={42} /> : <Mic size={42} />}
          </button>
          
          <span style={{ fontSize: '13px', fontWeight: 600, color: isRecording ? '#dc2626' : '#2563eb' }}>
            {isRecording ? t('listeningSub') : "Tap microphone to speak"}
          </span>
        </div>

        {/* Realtime Transcript or Text Input */}
        <div style={{ marginTop: '20px' }}>
          <div style={{ position: 'relative' }}>
            <textarea
              value={transcript}
              onChange={(e) => setTranscript(e.target.value)}
              placeholder="Your spoken words will appear here, or you can type directly..."
              style={{
                width: '100%',
                height: '80px',
                borderRadius: '12px',
                border: '2px solid #e2e8f0',
                padding: '12px 16px',
                fontSize: '15px',
                fontFamily: 'inherit',
                resize: 'none',
                outline: 'none',
                color: '#0f172a'
              }}
            />
            {transcript && (
              <button
                onClick={() => handleProcessQuery(transcript)}
                disabled={loading}
                style={{
                  position: 'absolute',
                  right: '12px',
                  bottom: '12px',
                  background: '#2563eb',
                  color: 'white',
                  border: 'none',
                  borderRadius: '8px',
                  padding: '8px 16px',
                  fontSize: '14px',
                  fontWeight: 600,
                  cursor: 'pointer',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '6px'
                }}
              >
                {loading ? 'Analyzing...' : <><Send size={16} /> Analyze</>}
              </button>
            )}
          </div>

          {errorMessage && (
            <p style={{ color: '#dc2626', fontSize: '13px', marginTop: '6px' }}>{errorMessage}</p>
          )}
        </div>

        {/* Pre-Loaded Quick Scenarios (Deterministic Demo) */}
        <div style={{ marginTop: '20px', borderTop: '1px solid #e2e8f0', paddingTop: '16px' }}>
          <div style={{ fontSize: '13px', fontWeight: 600, color: '#475569', marginBottom: '8px' }}>
            {t('quickDemos')}
          </div>
          <div className="quick-queries" style={{ justifyContent: 'flex-start' }}>
            <button 
              className="query-pill"
              onClick={() => handleProcessQuery(t('sampleCriminal'))}
            >
              ⚖️ {t('sampleCriminal').substring(0, 36)}...
            </button>
            <button 
              className="query-pill"
              onClick={() => handleProcessQuery(t('sampleLand'))}
            >
              🌾 {t('sampleLand').substring(0, 36)}...
            </button>
            <button 
              className="query-pill"
              onClick={() => handleProcessQuery(t('sampleCheque'))}
            >
              💰 {t('sampleCheque').substring(0, 36)}...
            </button>
            <button 
              className="query-pill"
              onClick={() => handleProcessQuery(t('sampleLabor'))}
            >
              🧱 {t('sampleLabor').substring(0, 36)}...
            </button>
            <button 
              className="query-pill"
              onClick={() => handleProcessQuery(t('sampleSuccession'))}
            >
              📜 {t('sampleSuccession').substring(0, 36)}...
            </button>
            <button 
              className="query-pill"
              onClick={() => handleProcessQuery(t('sampleSenior'))}
            >
              👴 {t('sampleSenior').substring(0, 36)}...
            </button>
            <button 
              className="query-pill"
              onClick={() => handleProcessQuery(t('sampleFamily'))}
            >
              🛡️ {t('sampleFamily').substring(0, 36)}...
            </button>
            <button 
              className="query-pill"
              onClick={() => handleProcessQuery(t('sampleCyber'))}
            >
              💳 {t('sampleCyber').substring(0, 36)}...
            </button>
            <button 
              className="query-pill"
              onClick={() => handleProcessQuery(t('sampleTenancy'))}
            >
              🏢 {t('sampleTenancy').substring(0, 36)}...
            </button>
            <button 
              className="query-pill"
              onClick={() => handleProcessQuery(t('sampleConsumer'))}
            >
              🚜 {t('sampleConsumer').substring(0, 36)}...
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
