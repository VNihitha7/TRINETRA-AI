import "./App.css";
import { useState, useEffect } from "react";
import { motion } from "framer-motion";
import {
  FaMotorcycle,
  FaCar,
  FaDatabase,
  FaExclamationTriangle,
} from "react-icons/fa";

function Card({ icon, title, value }) {
  return (
    <motion.div whileHover={{ scale: 1.05 }} className="card">
      <div className="card-icon">{icon}</div>

      <h3>{title}</h3>

      <h1 className="card-value">{value}</h1>
    </motion.div>
  );
}

function App() {
  const [time, setTime] = useState("");
  const [violations, setViolations] = useState([]);
  const [totalCases, setTotalCases] = useState(0);
  const [maxSeverity, setMaxSeverity] = useState(0);

  useEffect(() => {
    const timer = setInterval(() => {
      setTime(new Date().toLocaleTimeString());
    }, 1000);

    return () => clearInterval(timer);
  }, []);
  useEffect(() => {

  fetch("http://127.0.0.1:5000/violations")

    .then((res) => res.json())

    .then((data) => {

  setViolations(data);

  setTotalCases(data.length);

  if (data.length > 0) {

    const highest = Math.max(
      ...data.map(v => v.severity)
    );

    setMaxSeverity(highest);

  }

})

    .catch((err) => {

      console.log(err);

    });

}, []);
<div className="sidebar">

  <h2>TRINETRA</h2>

  <ul>

    <li>🏠 Dashboard</li>

    <li>🚨 Violations</li>

    <li>📊 Analytics</li>

    <li>🧠 AI Intelligence</li>

    <li>📷 Evidence</li>

    <li>⚙ Settings</li>

  </ul>

</div>

  return (
    <div className="container">
      {/* Header */}

      <div className="header">
        <h1 className="title">TRINETRA AI</h1>
        <h2 className="clock">{time}</h2>
      </div>

      {/* Cards */}

      <div className="cards">
        <Card
          icon={<FaMotorcycle />}
          title="Helmet"
          value="18"
        />

        <Card
          icon={<FaCar />}
          title="Parking"
          value="9"
        />

        <Card
          icon={<FaExclamationTriangle />}
          title="Severity"
          value="92"
        />

        <Card
          icon={<FaDatabase />}
          title="Cases"
          value="31"
        />
      </div>

      {/* Main Layout */}

      <div className="main">
        {/* Left Side */}

        <div>
          {/* Statistics */}

          <div className="section">
            <h2>Violation Statistics</h2>

            <p>Helmet</p>

            <div className="bar-bg">
              <div className="bar helmet"></div>
            </div>

            <p>Parking</p>

            <div className="bar-bg">
              <div className="bar parking"></div>
            </div>

            <p>OCR</p>

            <div className="bar-bg">
              <div className="bar ocr"></div>
            </div>
          </div>

          {/* Ticker */}

          <div className="section">
            <h2>🚨 Recent Violations</h2>

            <div className="ticker">
              <span>
                🚨 MH20DV2363 Helmet Severity 92 &nbsp;&nbsp;&nbsp;
                🚨 AP39AB1234 Triple Riding Severity 81 &nbsp;&nbsp;&nbsp;
                🚨 TS09XY9876 Parking Severity 74
              </span>
            </div>
            <div className="table-box">

<h2>

Live Incident Records

</h2>

<table>

<thead>

<tr>

<th>Plate</th>

<th>Severity</th>

<th>Status</th>

</tr>

</thead>

<tbody>

<tr>

<td>MH20DV2363</td>

<td>92</td>

<td>Critical</td>

</tr>

<tr>

<td>AP39AB1234</td>

<td>81</td>

<td>Warning</td>

</tr>

<tr>

<td>TS09XY9876</td>

<td>74</td>

<td>Moderate</td>

</tr>

</tbody>

</table>

</div>
            
          </div>

          {/* Evidence */}

          <div className="section">

  <h2>Evidence Gallery</h2>

  <div className="evidence-grid">
    <img
      src="/evidence2.jpg"
      alt="evidence3"
      className="evidence"
    />
    <img
      src="/evidence3.jpg"
      alt="evidence4"
      className="evidence"
    />
    <img
      src="/evidence1.jpg"
      alt="evidence1"
      className="evidence"
    />
    <img
      src="/evidence.jpg"
      alt="evidence2"
      className="evidence"
    />

  </div>

</div>
          <div className="architecture">

  <h2>Live Violations</h2>
  <h>MH20 DV2363
Severity : 90
Confidence : 0.80</h>
  {violations.map((v, index) => (

    <div key={index} style={{marginBottom:"15px"}}>

      <strong>{v.plate}</strong>

      <br />

      Severity : {v.severity}

      <br />

      Confidence : {v.confidence}

      <br />

      {v.timestamp}

    </div>

  ))}

</div>
        </div>

        {/* Right Side */}

        <div>
          {/* Severity */}

          <h2>Severity Meter</h2>

          <div className="gauge">92</div>

          {/* Digital Twin */}

          <h2 className="section-title">
            Digital Twin City
          </h2>

         <div className="city">

<h2>Digital Twin Monitoring Grid</h2>

<div className="junction red-glow">

Junction A

</div>

<div className="junction yellow-glow">

Metro Station

</div>

<div className="junction green-glow">

School Zone

</div>

<div className="junction red-glow">

Stadium Event

</div>

</div>

          {/* AI Copilot */}

          <div className="copilot">
            <h2>🤖 AI Copilot</h2>

            <div className="city">
              <p>Highest Risk Area</p>

              <strong>Metro Junction A</strong>

              <p style={{ marginTop: "15px" }}>
                Predicted Violations
              </p>

              <p>Helmet : 12</p>

              <p>Parking : 5</p>

              <p>Triple Riding : 3</p>

              <p style={{ marginTop: "15px" }}>
                Suggested Patrol
              </p>

              <strong>Deploy Unit 3</strong>
            </div>
          </div>

          {/* Radar */}

          <h2 className="section-title">
            📡 Traffic Radar
          </h2>

          <div className="radar">
            <div className="scan"></div>
          </div>

          {/* Forecast */}

          <div className="forecast">
            <h3>🔮 AI Forecast</h3>

            <p>Expected Violations Tomorrow</p>

            <p>Helmet : 15</p>

            <p>Parking : 8</p>

            <p>Triple Riding : 4</p>

            <p>High Risk Zone : Junction A</p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;