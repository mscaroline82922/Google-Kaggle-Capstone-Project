import React from 'react';

const TriageConsole = ({ logs }) => (
  <div className="bg-slate-900 border border-slate-700 rounded-lg p-4 font-mono text-sm h-64 overflow-y-auto">
    <div className="flex items-center gap-2 mb-2 border-b border-slate-700 pb-2 text-slate-400">
      <span className="w-3 h-3 rounded-full bg-red-500"></span>
      <span className="w-3 h-3 rounded-full bg-yellow-500"></span>
      <span className="w-3 h-3 rounded-full bg-green-500"></span>
      <span className="ml-2">SENSI_TRIAGE_CONSOLE</span>
    </div>
    {logs.map((log, i) => (
      <div key={i} className="mb-1">
        <span className="text-blue-400">[{new Date().toLocaleTimeString()}]</span> {log}
      </div>
    ))}
  </div>
);

const TelemetryCard = ({ data, type }) => (
  <div className="bg-slate-800 border border-slate-700 rounded-xl p-6 shadow-xl">
    <h3 className="text-slate-400 text-xs font-bold uppercase tracking-wider mb-4">
      {type} Real-Time Telemetry
    </h3>
    {data ? (
      <div className="grid grid-cols-2 gap-4">
        {Object.entries(data).map(([key, val]) => (
          <div key={key}>
            <div className="text-slate-500 text-xs capitalize">{key.replace('_', ' ')}</div>
            <div className="text-xl font-mono text-white">{val}</div>
          </div>
        ))}
      </div>
    ) : (
      <div className="text-slate-600 italic">Waiting for sensor ingestion...</div>
    )}
  </div>
);

export { TriageConsole, TelemetryCard };
