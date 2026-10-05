import React, { useState } from 'react';
import { 
  Monitor, 
  Cpu, 
  Mic, 
  Volume2, 
  Printer, 
  BatteryCharging, 
  Radio, 
  Database,
  CheckCircle,
  HardDrive
} from 'lucide-react';

export default function HardwareDiagram() {
  const [activeComponent, setActiveComponent] = useState('display');

  const components = {
    display: {
      name: "7-Inch Touchscreen Display",
      spec: "Waveshare 1024x600 IPS Capacitive Multi-touch",
      details: "High brightness (450 nits) sunlight-readable display with toughened scratch-resistant glass, optimized for rural kiosk conditions and heavy fingertip interaction.",
      status: "CALIBRATED & ONLINE",
      icon: <Monitor size={28} color="#2563eb" />
    },
    compute: {
      name: "Ruggedized Computing Unit",
      spec: "Intel N100 Quad-Core @ 3.4GHz / Raspberry Pi 5 SBC",
      details: "Fanless aluminum heat-sink chassis, IP54 dust protection, running low-latency Linux/Windows Kiosk runtime with automatic watchdog self-reboot.",
      status: "CPU LOAD 12% | TEMP 41°C",
      icon: <Cpu size={28} color="#7c3aed" />
    },
    mic: {
      name: "Dual MEMS Microphone Array",
      spec: "Directional USB Sound Card with Hardware DSP Noise Suppression",
      details: "Filters ambient panchayat/bazaar noise and isolates voice from 1.5m distance. Native interface for browser Web Speech API in Hindi, Odia & English.",
      status: "MIC GAIN +18dB | NOISE REDUCTION ON",
      icon: <Mic size={28} color="#059669" />
    },
    speakers: {
      name: "Acoustic Voice Speakers",
      spec: "Dual 3W 8Ω Sealed Cavity Chambers",
      details: "Tuned for speech frequencies (300Hz-3.4kHz) to ensure clear comprehension of legal rights for elderly and visually impaired citizens.",
      status: "VOLUME 85% | STEREO BALANCED",
      icon: <Volume2 size={28} color="#d97706" />
    },
    printer: {
      name: "Thermal Receipt Printer",
      spec: "58mm Embedded Thermal Mechanism (Serial/USB)",
      details: "Instant printing of Nyaya Patra (Action Slips) with verification QR codes, checklist items, and DLSA helpline contacts without ink or ribbon.",
      status: "PAPER READY | CUTTER OK",
      icon: <Printer size={28} color="#db2777" />
    },
    power: {
      name: "Solar Micro-Inverter & UPS",
      spec: "12V LiFePO4 12Ah Battery Pack with MPPT Solar Controller",
      details: "Provides 6 hours of continuous operation during rural power outages with automatic surge suppression and brownout protection.",
      status: "100% CHARGED | SOLAR INPUT 18.2V",
      icon: <BatteryCharging size={28} color="#16a34a" />
    },
    network: {
      name: "Dual SIM 4G LTE Gateway",
      spec: "Industrial Quectel LTE Cat-4 Module",
      details: "Automatic carrier failover between Jio and Airtel with local SQLite caching for 100% offline fallback when towers are down.",
      status: "4G RSSI -68dBm (EXCELLENT)",
      icon: <Radio size={28} color="#0284c7" />
    },
    storage: {
      name: "Local Offline Storage & Cache",
      spec: "128GB High-Endurance NVMe / eMMC",
      details: "Houses local SQLite database, Indian legal statutes (BNS, BNSS, CPA), local dictionary, and cached legal aid directory for zero-latency operations.",
      status: "2.4GB USED / 120GB FREE",
      icon: <HardDrive size={28} color="#475569" />
    }
  };

  const selected = components[activeComponent];

  return (
    <div style={{ background: '#ffffff', borderRadius: '18px', border: '1px solid #e2e8f0', padding: '24px', boxShadow: '0 4px 6px -1px rgba(0,0,0,0.05)' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px', flexWrap: 'wrap', gap: '12px' }}>
        <div>
          <h3 style={{ fontSize: '20px', fontWeight: 800, color: '#0f172a' }}>
            NyayaSathi Rural Kiosk Hardware Architecture
          </h3>
          <p style={{ fontSize: '14px', color: '#64748b' }}>
            Interactive blueprint: Click any hardware block to inspect operational specifications.
          </p>
        </div>
        <div style={{ display: 'inline-flex', alignItems: 'center', gap: '6px', background: '#dcfce7', color: '#15803d', padding: '6px 12px', borderRadius: '9999px', fontSize: '13px', fontWeight: 700 }}>
          <CheckCircle size={16} /> All 8 Subsystems Verified
        </div>
      </div>

      {/* Grid of hardware subsystems */}
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(130px, 1fr))',
        gap: '12px',
        marginBottom: '24px'
      }}>
        {Object.entries(components).map(([key, item]) => {
          const isActive = activeComponent === key;
          return (
            <button
              key={key}
              onClick={() => setActiveComponent(key)}
              style={{
                background: isActive ? '#eff6ff' : '#f8fafc',
                border: isActive ? '2px solid #2563eb' : '1px solid #e2e8f0',
                borderRadius: '12px',
                padding: '14px 10px',
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                gap: '8px',
                cursor: 'pointer',
                transition: 'all 0.15s ease',
                textAlign: 'center'
              }}
            >
              <div>{item.icon}</div>
              <div style={{ fontSize: '13px', fontWeight: 700, color: isActive ? '#1e40af' : '#1e293b', lineHeight: 1.2 }}>
                {item.name.split(' ')[0]}
              </div>
            </button>
          );
        })}
      </div>

      {/* Selected Component Detail Box */}
      <div style={{
        background: '#f8fafc',
        borderRadius: '14px',
        border: '1px solid #cbd5e1',
        padding: '20px',
        display: 'flex',
        gap: '20px',
        alignItems: 'flex-start',
        flexWrap: 'wrap'
      }}>
        <div style={{
          width: '56px',
          height: '56px',
          borderRadius: '14px',
          background: '#ffffff',
          boxShadow: '0 2px 4px rgba(0,0,0,0.05)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center'
        }}>
          {selected.icon}
        </div>

        <div style={{ flex: 1, minWidth: '240px' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px', marginBottom: '6px' }}>
            <h4 style={{ fontSize: '18px', fontWeight: 800, color: '#0f172a' }}>{selected.name}</h4>
            <span style={{ fontSize: '12px', fontWeight: 700, background: '#e0f2fe', color: '#0369a1', padding: '3px 10px', borderRadius: '6px' }}>
              {selected.status}
            </span>
          </div>
          <div style={{ fontSize: '14px', fontWeight: 600, color: '#2563eb', marginBottom: '8px' }}>
            {selected.spec}
          </div>
          <p style={{ fontSize: '14px', color: '#475569', lineHeight: 1.5 }}>
            {selected.details}
          </p>
        </div>
      </div>
    </div>
  );
}
