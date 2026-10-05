import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useLanguage } from '../context/LanguageContext';
import { Home, HelpCircle, Cpu, Clock, Scale } from 'lucide-react';

export default function KioskFooter() {
  const { t } = useLanguage();
  const [timeStr, setTimeStr] = useState('');

  useEffect(() => {
    const update = () => {
      const now = new Date();
      setTimeStr(now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' }));
    };
    update();
    const interval = setInterval(update, 1000);
    return () => clearInterval(interval);
  }, []);

  return (
    <footer className="kiosk-footer no-print">
      <div style={{ display: 'flex', alignItems: 'center', gap: '16px' }}>
        <Link to="/" style={{ color: 'var(--primary)', textDecoration: 'none', display: 'flex', alignItems: 'center', gap: '6px', fontWeight: 600 }}>
          <Home size={16} /> {t('home')}
        </Link>
        <Link to="/resources" style={{ color: 'var(--text-secondary)', textDecoration: 'none', display: 'flex', alignItems: 'center', gap: '6px' }}>
          <HelpCircle size={16} /> {t('cardResourcesTitle')}
        </Link>
        <Link to="/admin" style={{ color: 'var(--text-secondary)', textDecoration: 'none', display: 'flex', alignItems: 'center', gap: '6px' }}>
          <Cpu size={16} /> {t('cardAdminTitle')}
        </Link>
      </div>

      <div style={{ display: 'flex', alignItems: 'center', gap: '16px' }}>
        <span style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
          <Clock size={14} /> {timeStr} IST
        </span>
        <span style={{ color: 'var(--text-muted)' }}>
          Powered by NALSA & Govt of Odisha Legal Services
        </span>
      </div>
    </footer>
  );
}
