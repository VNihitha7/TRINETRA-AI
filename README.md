Here's a professional, competition-ready **README.md** for your GitHub repository.

---

# TRINETRA AI

## Overview

TRINETRA AI is an AI-powered Traffic Intelligence and Violation Management System designed to automate traffic monitoring, violation detection, evidence generation, and decision support.

The system integrates Computer Vision, Optical Character Recognition (OCR), Explainable AI, Database Management, and Interactive Analytics to assist authorities in monitoring traffic violations and improving road safety.

TRINETRA AI aims to transform traditional traffic surveillance into a data-driven, intelligent, and scalable smart-city solution.

---

## Problem Statement

Traffic enforcement in many cities still relies heavily on manual monitoring, resulting in:

* Delayed violation detection
* Limited situational awareness
* Inefficient resource allocation
* Lack of centralized intelligence
* Difficulty in maintaining digital evidence

TRINETRA AI addresses these challenges by automating the complete violation management pipeline.

---

## Key Features

### Vehicle Number Plate Recognition

* Automatic extraction of vehicle registration numbers using EasyOCR
* Confidence score generation for OCR predictions
* Automated evidence generation

### Helmet Violation Detection

* Custom-trained YOLO model for helmet detection
* Detection of riders and safety compliance
* Real-time visual evidence generation

### Severity Assessment Engine

* Violation severity scoring
* Risk-based prioritization
* Action recommendation generation

### Digital Evidence Generation

* Bounding-box visualization
* Timestamp recording
* Automated evidence storage

### Database Management

* SQLite-based violation repository
* Persistent storage of:
  * Vehicle number
  * Severity score
  * Confidence score
  * Timestamp
  * Recommended action
  * Evidence image path

### Smart Dashboard

Interactive React dashboard providing:

* Live violation statistics
* Evidence gallery
* Severity monitoring
* Digital Twin monitoring
* AI Copilot insights
* Traffic radar visualization
* Predictive analytics

---

## System Architecture

```text
Input Image
      │
      ▼
Helmet Detection (YOLO)
      │
      ▼
Violation Analysis
      │
      ▼
Number Plate Recognition (EasyOCR)
      │
      ▼
Severity Assessment Engine
      │
      ▼
Evidence Generation
      │
      ▼
SQLite Database
      │
      ▼
Flask API
      │
      ▼
React Dashboard
```

---

## Technology Stack

### Artificial Intelligence

* YOLOv8
* EasyOCR
* OpenCV

### Backend

* Python
* Flask
* SQLite

### Frontend

* React
* Vite
* Framer Motion
* React Icons

### Data Processing

* NumPy
* OpenCV
* SQLite3

---

## Project Structure

```text
## Project Structure

```text
TRINETRA_AI
│
├── .streamlit/
│   └── config.toml
│
├── analytics/
│   ├── hotspots.py
│   └── time_analysis.py
│
├── api/
│   └── server.py
│
├── backend/
│   ├── api.py
│   └── explanation.py
│
├── dashboard/
│   └── app.py
│
├── database/
│   ├── db.py
│   └── check.py
│
├── datasets/
│   └── helmet_dataset/
│       ├── images/
│       ├── labels/
│       └── data.yaml
│
├── evidence/
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   ├── package.json
│   ├── package-lock.json
│   ├── vite.config.js
│   └── index.html
│
├── helmet/
│   ├── train.py
│   ├── detect.py
│   └── no_helmet.py
│
├── ocr/
│   └── plate_reader.py
│
├── parking/
│   └── detect.py
│
├── pipeline/
│   └── main.py
│
├── scripts/
│   └── detect.py
│
├── seatbelt/
│   └── detect.py
│
├── severity/
│   ├── score.py
│   └── context_score.py
│
├── tracking/
│   └── tracker.py
│
├── triple_riding/
│   └── detect.py
│
├── output/
│   ├── evidence.jpg
│   └── final_evidence.jpg
│
├── sample_images/
│   ├── car.jpg
│   ├── helmet_test.jpg
│   ├── evidence.jpg
│   └── evidence2.jpg
│
├── trained_models/
│
├── runs/
│   └── detect/
│
├── requirements.txt
├── violations.db
├── yolov8n.pt
├── README.md
└── .gitignore
```

```

```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/VNihitha7/TRINETRA-AI.git
cd TRINETRA-AI
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Backend

Execute the violation processing pipeline:

```bash
python main.py
```

Start the Flask API:

```bash
python api/server.py
```

API Endpoint:

```text
http://127.0.0.1:5000/
```

---

## Running the Frontend

Navigate to frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start development server:

```bash
npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

---

## Dashboard Modules

### Live Monitoring

Displays real-time traffic intelligence metrics.

### Violation Statistics

Visual overview of detected violations.

### Recent Violations Feed

Continuous stream of detected incidents.

### Live Incident Records

Structured display of violation logs.

### Evidence Gallery

AI-generated visual evidence repository.

### Severity Meter

Risk assessment and prioritization.

### Digital Twin Monitoring

Zone-based monitoring of city infrastructure.

### AI Copilot

Decision-support and patrol recommendations.

### Traffic Radar

Visual representation of monitoring activity.

### AI Forecast

Predictive analysis of future traffic violations.

---

## Future Enhancements

* Triple riding detection
* Illegal parking detection
* Real-time CCTV integration
* Cloud database deployment
* Mobile application
* GPS-based incident mapping
* Automated e-challan generation
* Multi-camera city surveillance

---

## Use Cases

* Smart City Traffic Management
* Law Enforcement Support
* Road Safety Monitoring
* Urban Mobility Analytics
* Intelligent Transportation Systems

---

## Results

The system successfully demonstrates:

* Automated helmet violation detection
* Number plate recognition
* Severity assessment
* Evidence generation
* Violation database management
* Interactive command-center dashboard

---

## Vision

TRINETRA AI envisions a future where traffic management is proactive rather than reactive, leveraging Artificial Intelligence, Computer Vision, and Predictive Analytics to create safer roads and smarter cities.

---

## License

This project is developed for academic, research, and innovation purposes.

---

*"Detect. Analyze. Predict. Protect."*
