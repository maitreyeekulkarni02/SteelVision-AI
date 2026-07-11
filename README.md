# 🏭 SteelVision AI

> Edge AI-Powered Industrial Inspection & Predictive Maintenance Platform

SteelVision AI is an AI-powered industrial inspection system designed to detect visible machine defects using computer vision. It analyzes uploaded machine images, estimates machine health, prioritizes maintenance, and generates actionable recommendations.

This project is being developed as part of the **Tata Technologies InnoVent** innovation challenge.

---

## 🚀 Current MVP Features

- 📤 Upload machine images
- 📷 Webcam support (optional)
- 🤖 YOLO-based object detection
- 🟥 Bounding box visualization
- 📊 Detection confidence scores
- ❤️ Machine Health Score (0–100)
- 🚦 Machine Status
- ⚠️ Maintenance Priority
- 🛠️ Maintenance Recommendation Engine
- 📥 Download inspection report (CSV)

---

## 🧠 AI Workflow

```text
Machine Image
      │
      ▼
YOLO Detection
      │
      ▼
Defect Analysis
      │
      ▼
Machine Health Score
      │
      ▼
Maintenance Priority
      │
      ▼
AI Recommendation
```

---

## 🛠️ Tech Stack

- Python
- Streamlit
- OpenCV
- Ultralytics YOLO
- Pillow
- NumPy
- Pandas

---

## 📁 Project Structure

```text
SteelVision-AI/
│
├── app.py
├── requirements.txt
├── README.md
│
├── assets/
├── models/
├── sample_images/
└── utils/
    ├── inspection.py
    └── model.py
```

---

## 📸 Screenshots

Coming Soon

---

## 🎯 Future Roadmap

- Custom-trained industrial defect detection model
- Rust detection
- Crack detection
- Oil leakage detection
- Corrosion detection
- Loose bolt detection
- PDF inspection reports
- Live video inspection
- Edge AI deployment
- Industrial analytics dashboard

---

## 👩‍💻 Author

**Maitreyee Kulkarni**

Artificial Intelligence & Data Science Student

---

## ⭐ Project Status

🚧 MVP Under Active Development