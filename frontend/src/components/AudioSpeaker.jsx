import React, { useState } from 'react';
import { Volume2, VolumeX } from 'lucide-react';
import { useLanguage } from '../context/LanguageContext';

export default function AudioSpeaker({ text, lang = null, label = null }) {
  const { speakText, stopSpeech } = useLanguage();
  const [isPlaying, setIsPlaying] = useState(false);

  const handleSpeak = (e) => {
    e.stopPropagation();
    if (isPlaying) {
      stopSpeech();
      setIsPlaying(false);
    } else {
      setIsPlaying(true);
      speakText(text, lang);
      // Auto reset playing indicator after estimated duration
      const wordCount = text.split(' ').length;
      const durationMs = Math.max(2000, (wordCount / 2.5) * 1000);
      setTimeout(() => setIsPlaying(false), durationMs);
    }
  };

  return (
    <button 
      onClick={handleSpeak}
      className="control-btn"
      style={{
        background: isPlaying ? '#dbeafe' : '#f8fafc',
        borderColor: isPlaying ? '#2563eb' : '#cbd5e1',
        color: isPlaying ? '#1e40af' : '#475569',
        height: '36px',
        padding: '0 10px',
        display: 'inline-flex',
        alignItems: 'center',
        gap: '6px',
        cursor: 'pointer'
      }}
      title="Listen to this explanation (TTS Voice Output)"
    >
      {isPlaying ? <VolumeX size={16} /> : <Volume2 size={16} />}
      {label && <span style={{ fontSize: '13px' }}>{label}</span>}
    </button>
  );
}
