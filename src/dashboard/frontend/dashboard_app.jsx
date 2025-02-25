import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './app.css';

function DashboardApp() {
  const [metrics, setMetrics] = useState({ scrapLoss: 0, carbonEmission: 0, equipmentEfficiency: 0 });

  useEffect(() => {
    // Fetch dashboard metrics on component mount
    axios.get('/api/v1/dashboard/metrics')
      .then(response => {
        setMetrics(response.data.metrics);
      })
      .catch(error => {
        console.error("Error fetching dashboard metrics:", error);
      });
  }, []);

  return (
    <div className="dashboard-container">
      <h1>AlumiCatalyst Dashboard</h1>
      <div className="metric-card">
        <h2>Scrap Loss</h2>
        <p>{metrics.scrapLoss}</p>
      </div>
      <div className="metric-card">
        <h2>Carbon Emission</h2>
        <p>{metrics.carbonEmission}</p>
      </div>
      <div className="metric-card">
        <h2>Equipment Efficiency</h2>
        <p>{metrics.equipmentEfficiency}</p>
      </div>
    </div>
  );
}

export default DashboardApp;
