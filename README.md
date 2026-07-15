# 🏭 SteelVision AI

### Edge AI Powered Industrial Inspection & Predictive Maintenance Platform

> **An Industry 4.0 solution for real-time machine inspection, defect detection, predictive maintenance, digital twin monitoring, analytics, and AI-powered decision support.**

---

## 🚀 Overview

SteelVision AI is an intelligent industrial inspection platform that combines **Computer Vision**, **Edge AI**, and **Large Language Models (LLMs)** to help manufacturers monitor machine health, detect defects in real time, prioritize maintenance, and generate AI-powered inspection reports.

The platform enables factories to move from **reactive maintenance** to **predictive maintenance**, reducing downtime, improving safety, and increasing operational efficiency.

---

## 🎯 Key Highlights

- 🔍 Real-time AI Defect Detection
- 📷 Camera, Image & Video Inspection
- 🤖 AI Copilot powered by Ollama + Qwen
- 📊 Interactive Analytics Dashboard
- 🏭 Factory Digital Twin
- 🧠 Explainable AI Recommendations
- 🛠 AI Maintenance Planner
- 📄 PDF Inspection Reports
- 📚 Historical Inspection Records
- 📈 Machine Health Monitoring

---
# 📸 Application Preview

> Screenshots will be added after the UI is finalized.

## Dashboard

![Dashboard](assets/screenshots/dashboard.png)

---

## Inspection Result

![Inspection](assets/screenshots/inspection.png)

---

## Analytics Dashboard

![Analytics](assets/screenshots/analytics.png)

---

## Factory Digital Twin

![Digital Twin](assets/screenshots/digital_twin.png)

---

## AI Copilot

![Copilot](assets/screenshots/copilot.png)

---

## Maintenance Planner

![Maintenance](assets/screenshots/maintenance.png)

---

# ✨ Features

## 🤖 AI Inspection Engine

- Real-time object and defect detection using YOLO
- Image inspection
- Live camera inspection
- Video inspection
- Industrial defect classification
- Confidence score visualization
- Bounding box visualization

---

## 🏭 Machine Health Intelligence

- Automatic machine health score
- Machine status prediction
- Risk level estimation
- Maintenance priority calculation
- AI-generated recommendations
- Inspection summary generation

---

## 🛠 Predictive Maintenance

- AI maintenance planner
- Recommended spare parts
- Estimated downtime
- Maintenance schedule
- Severity-based repair suggestions
- Priority-based maintenance planning

---

## 📊 Analytics Dashboard

- Inspection analytics
- Machine health trends
- Defect frequency analysis
- Status distribution
- Historical performance
- Interactive charts

---

## 🏭 Factory Digital Twin

- Factory overview
- Machine monitoring
- Live operational status
- Visual machine representation
- Plant-level monitoring

---

## 📋 Machine Management

- Machine inventory
- Machine records
- Machine registration
- Location tracking
- Health monitoring
- Maintenance history

---

## 📂 Inspection History

- Historical inspection database
- Inspection search
- Machine-wise filtering
- Complete inspection records
- Inspection timeline

---

## 🤖 AI Copilot

- Local AI powered by Ollama
- Qwen LLM integration
- Machine health queries
- Inspection insights
- Maintenance guidance
- Factory summary
- Natural language interaction

---

## 📄 Reporting

- AI-generated inspection reports
- PDF report export
- Machine summaries
- Inspection recommendations
- Downloadable reports

---

## ⚡ Edge AI

- Local inference
- Offline AI capability
- Privacy-first architecture
- Fast inference
- Edge-ready deployment

---

# 🏗️ System Architecture

The following diagram illustrates the overall architecture of SteelVision AI.

```text
                   ┌─────────────────────────────┐
                   │     Input Sources           │
                   │─────────────────────────────│
                   │ • Image Upload             │
                   │ • Live Camera              │
                   │ • Video Inspection         │
                   └──────────────┬──────────────┘
                                  │
                                  ▼
                   ┌─────────────────────────────┐
                   │      YOLO Detection         │
                   │ Real-time Object Detection  │
                   └──────────────┬──────────────┘
                                  │
                                  ▼
                   ┌─────────────────────────────┐
                   │ Industrial Defect Engine    │
                   │ • Rust                      │
                   │ • Crack                     │
                   │ • Oil Leakage               │
                   │ • Corrosion                 │
                   │ • Missing Parts             │
                   └──────────────┬──────────────┘
                                  │
                                  ▼
                 ┌────────────────────────────────┐
                 │ Machine Intelligence Engine    │
                 │────────────────────────────────│
                 │ • Health Score                 │
                 │ • Risk Prediction              │
                 │ • Status Classification        │
                 │ • Recommendation Engine        │
                 └───────┬──────────────┬─────────┘
                         │              │
         ┌───────────────┘              └───────────────┐
         ▼                                              ▼
┌─────────────────────┐                     ┌─────────────────────┐
│ Maintenance Planner │                     │ SQLite Database     │
└──────────┬──────────┘                     └──────────┬──────────┘
           │                                           │
           └───────────────┬───────────────────────────┘
                           ▼
             ┌────────────────────────────────────┐
             │ Analytics & Visualization Layer    │
             │────────────────────────────────────│
             │ • Dashboard                        │
             │ • Digital Twin                     │
             │ • Machine Records                  │
             │ • Inspection History               │
             └───────────────┬────────────────────┘
                             │
            ┌────────────────┴────────────────┐
            ▼                                 ▼
   ┌────────────────────┐          ┌────────────────────┐
   │ AI Copilot         │          │ PDF Reports        │
   │ Ollama + Qwen      │          │ Report Generator   │
   └────────────────────┘          └────────────────────┘
```

---

This architecture represents the complete data flow from inspection to AI-assisted decision making.

## 📐 Architecture Diagrams

> High-resolution diagrams are included in the `assets/diagrams` folder.

- System Architecture
- AI Pipeline
- Database ER Diagram
- Inspection Workflow
# 🧠 AI Pipeline

SteelVision AI follows a modular AI pipeline for industrial inspection and predictive maintenance.

```text
          Image / Camera / Video
                     │
                     ▼
          YOLO Object Detection
                     │
                     ▼
       Industrial Defect Classification
                     │
                     ▼
         Machine Health Calculation
                     │
                     ▼
      Status & Risk Level Prediction
                     │
                     ▼
       AI Maintenance Recommendation
                     │
                     ▼
          Inspection History Storage
                     │
        ┌────────────┴────────────┐
        ▼                         ▼
 Analytics Dashboard       Factory Digital Twin
        │                         │
        └────────────┬────────────┘
                     ▼
             AI Copilot (Ollama)
                     │
                     ▼
             PDF Inspection Report
```

---

## Pipeline Stages

### 1️⃣ Data Acquisition

SteelVision AI accepts multiple inspection sources:

- Image Upload
- Live Camera Feed
- Video Inspection

---

### 2️⃣ AI Detection

The YOLO model performs:

- Object Detection
- Defect Localization
- Confidence Estimation

---

### 3️⃣ Industrial Intelligence

Detected objects are converted into industrial defects such as:

- Crack
- Rust
- Oil Leakage
- Corrosion
- Loose Bolt
- Surface Damage
- Missing Component
- Damaged Belt

---

### 4️⃣ Machine Intelligence

The platform computes:

- Machine Health Score
- Machine Status
- Maintenance Priority
- AI Recommendation

---

### 5️⃣ Data Persistence

Inspection results are stored in the local database, including:

- Machine Information
- Defects
- Health Score
- Status
- Timestamp
- Recommendations

---

### 6️⃣ Business Intelligence

Stored inspection data powers:

- Analytics Dashboard
- Factory Digital Twin
- Machine Records
- Inspection History

---

### 7️⃣ AI Decision Support

The integrated AI Copilot (Ollama + Qwen) enables users to query factory data using natural language and receive contextual maintenance insights.

---

### 8️⃣ Reporting

The final inspection report includes:

- Detected Defects
- Health Score
- Risk Level
- Maintenance Plan
- AI Recommendation
- PDF Export

## 📊 AI Pipeline Diagram

> A high-resolution AI pipeline diagram will be added in a future release.

![AI Pipeline](assets/diagrams/ai_pipeline.png)

# 📂 Project Structure

```text
SteelVision-AI/
│
├── ai/                        # AI Engine
│   ├── llm.py
│   ├── agent.py
│   ├── context.py
│   ├── prompts.py
│   └── report_writer.py
│
├── assets/
│   ├── screenshots/
│   ├── diagrams/
│   └── demo/
│
├── database/
│   ├── database.py
│   ├── models.py
│   └── machine_models.py
│
├── docs/
│
├── ui/
│   ├── analytics_dashboard.py
│   ├── command_center.py
│   ├── copilot_panel.py
│   ├── factory_twin.py
│   └── maintenance_panel.py
│
├── utils/
│   ├── analytics.py
│   ├── camera.py
│   ├── copilot.py
│   ├── dashboard.py
│   ├── defect_engine.py
│   ├── history.py
│   ├── inspection.py
│   ├── maintenance_planner.py
│   ├── model.py
│   ├── report.py
│   ├── video_inspection.py
│   └── ...
│
├── app.py                     # Main Streamlit Application
├── requirements.txt
├── README.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── Dockerfile                 # (Coming Soon)
└── docker-compose.yml         # (Coming Soon)
```
# 📦 Project Modules

| Module | Description |
|---------|-------------|
| **app.py** | Main Streamlit application |
| **ai/** | Local LLM integration, prompts, report generation |
| **database/** | SQLAlchemy models and database configuration |
| **ui/** | Modular Streamlit interface components |
| **utils/** | Business logic, AI utilities and helper functions |
| **assets/** | Screenshots, architecture diagrams and demo media |
| **docs/** | Additional documentation |

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/maitreyeekulkarni02/SteelVision-AI.git

cd SteelVision-AI
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Install Ollama

Download and install Ollama from:

https://ollama.com

---

## 5. Download the AI Model

```bash
ollama pull qwen2.5:3b
```

---

## 6. Run the Application

```bash
streamlit run app.py
```

---

The application will be available at:

```
http://localhost:8501
```
# ▶️ Usage

SteelVision AI supports multiple inspection modes.

## 📷 Camera Inspection

- Open the Inspection Dashboard
- Select **Camera**
- Capture a frame
- View detected defects
- Review health score
- Generate maintenance plan

---

## 🖼️ Image Inspection

- Upload an image
- Run AI inspection
- Analyze detected defects
- Download PDF report

---

## 🎥 Video Inspection

- Upload a video
- Process each frame
- Review summarized inspection results

---

## 🤖 AI Copilot

Example questions:

- Which machines are critical?
- Show factory summary.
- Which machine has the lowest health?
- Show inspection history.
- What maintenance is recommended?

# 🛠️ Technology Stack

| Category | Technologies |
|-----------|--------------|
| **Frontend** | Streamlit |
| **Backend** | Python |
| **Computer Vision** | Ultralytics YOLO |
| **Artificial Intelligence** | Ollama, Qwen 2.5 |
| **Machine Learning** | YOLO-based Object Detection |
| **Image Processing** | OpenCV, Pillow |
| **Data Analysis** | Pandas |
| **Database** | SQLite, SQLAlchemy |
| **Report Generation** | PDF Report Generator |
| **Visualization** | Streamlit Charts |
| **Development** | VS Code, Git, GitHub |
| **Deployment** | Streamlit (Current), Docker (Planned) |

# 🔄 Project Workflow

```text
Image / Camera / Video
          │
          ▼
YOLO Object Detection
          │
          ▼
Industrial Defect Detection
          │
          ▼
Machine Health Calculation
          │
          ▼
Risk Prediction
          │
          ▼
Maintenance Planner
          │
          ▼
Database Storage
          │
          ▼
Analytics Dashboard
          │
          ▼
Digital Twin
          │
          ▼
AI Copilot
          │
          ▼
PDF Report Generation
```
# 📈 Project Highlights

- ✅ Real-time Edge AI Inspection
- ✅ Offline AI using Ollama
- ✅ YOLO-based Defect Detection
- ✅ Interactive Dashboard
- ✅ Predictive Maintenance
- ✅ Factory Digital Twin
- ✅ AI Copilot
- ✅ PDF Report Generation
- ✅ Machine Health Analytics
- ✅ Modular Architecture

# 🔮 Future Scope

SteelVision AI is designed to evolve into a complete Industry 4.0 platform.

## 🔹 Version 1.1

- Enhanced UI/UX
- Docker Support
- GitHub Actions (CI/CD)
- Improved AI Reports
- Performance Optimization
- Better Error Handling
- Logging Framework

---

## 🔹 Version 2.0

- Role-Based Access Control (RBAC)
- Retrieval-Augmented Generation (RAG)
- Equipment Manual Search
- Voice-enabled AI Copilot
- Multi-user Support
- Advanced Analytics
- Predictive Failure Forecasting

---

## 🔹 Version 3.0

- IoT Sensor Integration
- MQTT Communication
- OPC-UA Support
- Edge Device Deployment
- Multi-Factory Monitoring
- Mobile Application
- Cloud Dashboard
- AI-based Spare Parts Prediction

# 🗺️ Development Roadmap

| Version | Status |
|----------|--------|
| ✅ v1.0 | Industrial Inspection Platform |
| 🔄 v1.1 | Stability, Docker, CI/CD |
| 📋 v2.0 | Authentication + RAG + AI Enhancements |
| 🚀 v3.0 | IoT + Cloud + Mobile + Enterprise Features |

# 🎓 Learning Outcomes

Through this project, I gained hands-on experience with:

- Computer Vision using YOLO
- Edge AI deployment concepts
- Large Language Model (LLM) integration
- Local AI using Ollama
- Predictive Maintenance workflows
- SQLAlchemy ORM
- Database Design
- Streamlit Application Development
- Modular Software Architecture
- AI-powered Report Generation
- Industrial Analytics
- Git & GitHub
- Software Engineering Best Practices

# 🙏 Acknowledgements

Special thanks to the open-source community and the developers of:

- Ultralytics YOLO
- Streamlit
- Ollama
- Qwen
- SQLAlchemy
- OpenCV
- Pandas

Their tools and libraries made this project possible.