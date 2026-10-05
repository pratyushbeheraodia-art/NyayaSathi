import React from 'react';
import { useLanguage } from '../context/LanguageContext';
import { PhoneCall, ShieldAlert, AlertTriangle } from 'lucide-react';

export default function EmergencyBanner() {
  const { t } = useLanguage();

  return (
    <div className="emergency-strip no-print">
      <div style={{ display: 'flex', alignItems: 'center', gap: '8px', fontWeight: 600, fontSize: '14px' }}>
        <ShieldAlert size={18} />
        <span>{t('emergencyStripText')}</span>
      </div>

      <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap' }}>
        <a href="tel:1930" title="National Cyber Crime Reporting Portal">
          <PhoneCall size={14} /> {t('cyberHelpline')}
        </a>
        <a href="tel:181" title="Women Emergency Crisis Helpline">
          <PhoneCall size={14} /> {t('womenHelpline')}
        </a>
        <a href="tel:112" title="National Emergency All-in-One">
          <PhoneCall size={14} /> {t('policeHelpline')}
        </a>
        <a href="tel:15100" title="NALSA Free Legal Aid Toll-free">
          <PhoneCall size={14} /> {t('legalAidHelpline')}
        </a>
      </div>
    </div>
  );
}
