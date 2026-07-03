import React, { useState } from 'react';
import { TriageConsole, TelemetryCard } from './components/Dashboard';

const App = () => {
  const [location, setLocation] = useState('Japan');
  const [hazard, setHazard] = useState('Earthquake');
  const [status, setStatus] = useState('IDLE');
  const [logs, setLogs] = useState(['System Initialized. Waiting for input...']);
  const [telemetry, setTelemetry] = useState(null);
  const [alert, setAlert] = useState(null);

  const runAnalysis = async () => {
    setStatus('RUNNING');
    setLogs(prev => [...prev, `Triggering autonomous pipeline for ${hazard} in ${location}...`]);

    // Simulated API call to sensi_workspace/api.py
    try {
      // In a real app, this would be: await fetch('/api/analyze', ...)
      const response = await simulateApiCall(location, hazard);
      setLogs(prev => [...prev, ...response.logs]);
      setTelemetry(response.telemetry);
      setStatus(response.status);
      if (response.alert) setAlert(response.alert);
    } catch (e) {
      setLogs(prev => [...prev, `CRITICAL_FAILURE: ${e.message}`]);
      setStatus('ERROR');
    }
  };

  return (
    <div className="min-h-screen bg-slate-950 text-white p-8 font-sans">
      <header className="max-w-6xl mx-auto flex justify-between items-center mb-12">
        <div>
          <h1 className="text-4xl font-black tracking-tighter flex items-center gap-3">
            <span className="text-red-500">🛰️</span> PROJECT SENSI
          </h1>
          <p className="text-slate-400">Global Life-Safety Hazard Monitor</p>
        </div>
        <div className="flex gap-4">
          <div className="bg-slate-900 border border-slate-800 rounded-full px-4 py-2 text-xs font-bold flex items-center gap-2">
            <span className="w-2 h-2 rounded-full bg-green-500 animate-pulse"></span> MCP_SECURE
          </div>
          <div className="bg-slate-900 border border-slate-800 rounded-full px-4 py-2 text-xs font-bold">
            GUARD_NODE: ACTIVE
          </div>
        </div>
      </header>

      <main className="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Sidebar Controls */}
        <div className="space-y-6">
          <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6">
            <h2 className="text-sm font-bold uppercase tracking-widest text-slate-500 mb-6">Mission Config</h2>
            <div className="space-y-4">
              <div>
                <label className="block text-xs font-bold text-slate-400 mb-2">Location</label>
                <input
                  value={location}
                  onChange={e => setLocation(e.target.value)}
                  className="w-full bg-slate-800 border-none rounded-lg p-3 text-sm focus:ring-2 focus:ring-red-500 transition-all"
                />
              </div>
              <div>
                <label className="block text-xs font-bold text-slate-400 mb-2">Hazard Type</label>
                <select
                  value={hazard}
                  onChange={e => setHazard(e.target.value)}
                  className="w-full bg-slate-800 border-none rounded-lg p-3 text-sm"
                >
                  <option>Earthquake</option>
                  <option>Heatwave</option>
                </select>
              </div>
              <button
                onClick={runAnalysis}
                disabled={status === 'RUNNING'}
                className="w-full bg-red-600 hover:bg-red-500 disabled:bg-slate-700 text-white font-bold py-4 rounded-xl transition-all shadow-lg shadow-red-900/20"
              >
                {status === 'RUNNING' ? 'INGESTING...' : 'TRIGGER PREDICTION'}
              </button>
            </div>
          </div>

          <div className="bg-red-900/10 border border-red-900/50 rounded-2xl p-6">
            <h3 className="text-red-500 text-xs font-bold uppercase mb-2">Security Guardrail</h3>
            <p className="text-xs text-slate-400 leading-relaxed">
              Self-healing runtime monitoring the execution streams. Real-time code repair enabled for mission-critical uptime.
            </p>
          </div>
        </div>

        {/* Main Content */}
        <div className="lg:col-span-2 space-y-8">
          <TriageConsole logs={logs} />

          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            <TelemetryCard data={telemetry} type={hazard} />

            {alert && (
              <div className="bg-red-600 rounded-xl p-6 flex flex-col justify-between animate-in fade-in zoom-in duration-500">
                <div>
                  <div className="text-xs font-bold uppercase text-red-200 mb-2">Life-Safety Dispatch</div>
                  <div className="text-lg font-bold leading-tight">{alert.alert_message}</div>
                </div>
                <div className="mt-4 pt-4 border-t border-red-500 flex justify-between items-center">
                   <span className="text-[10px] font-mono text-red-200">{alert.dispatch_id}</span>
                   <span className="bg-white text-red-600 text-[10px] font-black px-2 py-1 rounded">VEO_GENERATED</span>
                </div>
              </div>
            )}
          </div>
        </div>
      </main>
    </div>
  );
};

// Simulation Helper
const simulateApiCall = (loc, haz) => new Promise(resolve => {
  setTimeout(() => {
    resolve({
      status: 'DISPATCHED',
      logs: [
        `LOGISTICS: Telemetry ingested for ${loc}`,
        `COMMS: High-fidelity broadcast generated via Veo.`,
        `ORCHESTRATOR: Signed Alert Dispatched.`
      ],
      telemetry: haz === 'Earthquake'
        ? { magnitude: 7.2, depth_km: 15, tsunami_risk: 'LOW' }
        : { temperature: '42.5C', humidity: '15%', heat_index: 54.2 },
      alert: {
        alert_message: `CRITICAL: ${haz} alert issued for ${loc}. Follow evacuation visuals immediately.`,
        dispatch_id: 'sha256_0x112233'
      }
    });
  }, 1500);
});

export default App;
