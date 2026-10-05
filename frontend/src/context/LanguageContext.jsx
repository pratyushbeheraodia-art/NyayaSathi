import React, { createContext, useContext, useState, useEffect } from 'react';
import { translations } from '../translations/translations';

const LanguageContext = createContext();

export const LanguageProvider = ({ children }) => {
  const [lang, setLang] = useState(() => localStorage.getItem('nyayasathi_lang') || 'en');
  const [fontSize, setFontSize] = useState(() => localStorage.getItem('nyayasathi_font') || 'normal');
  const [highContrast, setHighContrast] = useState(() => localStorage.getItem('nyayasathi_contrast') === 'true');

  useEffect(() => {
    localStorage.setItem('nyayasathi_lang', lang);
  }, [lang]);

  useEffect(() => {
    localStorage.setItem('nyayasathi_font', fontSize);
    document.body.classList.remove('font-lg', 'font-xl');
    if (fontSize !== 'normal') {
      document.body.classList.add(fontSize);
    }
  }, [fontSize]);

  useEffect(() => {
    localStorage.setItem('nyayasathi_contrast', highContrast);
    if (highContrast) {
      document.body.classList.add('high-contrast');
    } else {
      document.body.classList.remove('high-contrast');
    }
  }, [highContrast]);

  const t = (key) => {
    const dict = translations[lang] || translations.en;
    return dict[key] || translations.en[key] || key;
  };

  const cycleFontSize = () => {
    if (fontSize === 'normal') setFontSize('font-lg');
    else if (fontSize === 'font-lg') setFontSize('font-xl');
    else setFontSize('normal');
  };

  // Browser Web Speech API text-to-speech
  const speakText = (text, customLang = null) => {
    if (!('speechSynthesis' in window)) return;
    window.speechSynthesis.cancel(); // Stop any ongoing speech
    const utterance = new SpeechSynthesisUtterance(text);
    const targetLang = customLang || lang;
    if (targetLang === 'hi') {
      utterance.lang = 'hi-IN';
    } else if (targetLang === 'od') {
      // Odia fallback to hi-IN or en-IN if Odia voice is not installed
      utterance.lang = 'hi-IN';
    } else {
      utterance.lang = 'en-IN';
    }
    utterance.rate = 0.95; // Slightly slower for clarity on kiosk
    window.speechSynthesis.speak(utterance);
  };

  const stopSpeech = () => {
    if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
    }
  };

  return (
    <LanguageContext.Provider value={{
      lang,
      setLang,
      t,
      fontSize,
      cycleFontSize,
      highContrast,
      setHighContrast,
      speakText,
      stopSpeech
    }}>
      {children}
    </LanguageContext.Provider>
  );
};

export const useLanguage = () => useContext(LanguageContext);
