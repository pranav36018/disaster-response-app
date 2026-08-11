const express = require('express');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 5000;

app.use(cors());
app.use(express.json());

// Mock Data
let incidents = [
  { id: 'mock1', type: 'FLOOD', lat: 12.9716, lng: 77.5946, severity: 'CRITICAL', title: 'Critical Flood Warning', desc: 'River water level rising rapidly.', time: new Date().toISOString() },
  { id: 'mock2', type: 'WILDFIRE', lat: 12.2958, lng: 76.6394, severity: 'WARNING', title: 'Wildfire Alert', desc: 'NASA FIRMS detected heat.', time: new Date().toISOString() },
];

const mockReports = [
  { id: 't1', lat: 12.98, lng: 77.60, user: '@citizen_john', text: "Water level rising rapidly near MG Road! Need help.", type: 'flood', time: 'Just now' },
  { id: 't2', lat: 12.95, lng: 77.62, user: '@sarah_tweets', text: "Smell of gas in the air downtown, lots of smoke.", type: 'fire', time: '1m ago' },
  { id: 't3', lat: 12.93, lng: 77.58, user: '@weather_bot', text: "WARNING: Flash flood alert issued for southern district.", type: 'alert', time: '2m ago' },
  { id: 't4', lat: 12.99, lng: 77.55, user: '@emergency_scanner', text: "Multiple calls reporting chemical spill on Highway 101.", type: 'spill', time: '4m ago' },
  { id: 't5', lat: 12.96, lng: 77.59, user: '@local_news', text: "Traffic at a standstill due to severe waterlogging.", type: 'flood', time: '5m ago' },
  { id: 't6', lat: 12.92, lng: 77.65, user: '@resident44', text: "Power is out across the entire neighborhood. Anyone else?", type: 'infrastructure', time: '8m ago' },
];

let socialFeed = [mockReports[5], mockReports[4]];
let reportIndex = 3;

// Simulate incoming feed periodically on the backend
setInterval(() => {
  if (reportIndex < 0) {
    reportIndex = mockReports.length - 1; // loop back to the start
  }
  
  // Clone the report and update its ID and time so it looks like a fresh live feed
  const newReport = { 
    ...mockReports[reportIndex], 
    time: 'Just now', 
    id: 't_' + Date.now() 
  };
  
  socialFeed = [newReport, ...socialFeed].slice(0, 50); // Keep the latest 50 items
  reportIndex--;
}, 4500);

// --- Routes ---

// Get all incidents
app.get('/api/incidents', (req, res) => {
  res.json(incidents);
});

// Create a new incident
app.post('/api/incidents', (req, res) => {
  const newIncident = {
    id: Date.now().toString(),
    time: new Date().toISOString(),
    ...req.body
  };
  incidents = [newIncident, ...incidents];
  res.status(201).json(newIncident);
});

// Get social feed
app.get('/api/social/feed', (req, res) => {
  res.json(socialFeed);
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
