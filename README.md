# 🚨 AI-Based Threat Detection System

This project implements a real-time object detection system designed to **classify vehicles as either civilian or potential threats** using YOLOv8 and custom-trained datasets. 

---

## 🧠 Project Overview

The core idea is to automate surveillance monitoring by identifying and distinguishing between **civilian vehicles** (e.g., cars, buses, tractors) and **threat vehicles** (e.g., enemy trucks, tanks, drones) in real-time video and image data.

The system helps address key challenges in surveillance such as human fatigue, slow manual detection, and oversight in high-pressure or high-traffic scenarios.

---

## 🎯 Key Features

- Real-time image and video detection using YOLOv8
- Clearly labeled bounding boxes for **civilian (green)** and **threat (red)** vehicles
- Beautiful GUI built using Tkinter for intuitive image/video uploads
- Trained on a **custom dataset created using Roboflow**

---

## 🗂 Dataset Details

- ✅ **Dataset Creation Tool**: [Roboflow](https://roboflow.com/)
- 🖼 **Classes**: 11 vehicle types categorized as either safe/civilian or threat
- 📦 **Note**: The dataset uploaded here on GitHub is **not the full version**. For demo or academic purposes, a limited subset is included.
- 📢 **Important**: The larger and more balanced your dataset is, the better your model will perform — especially when distinguishing rare threat-class vehicles.

---

## 🧪 Model

- 📌 Model: YOLOv8 (`yolov8n`)
- 🧾 Training Framework: Ultralytics YOLOv8
- 🏷 Classes:
  - Civilian: `civilian_auto`, `civilian_bus`, `civilian_tempo`, `civilian_tractor`, `civilian_truck`
  - Safe: `safe_av`, `safe_tanks`, `safe_truck`
  - Threat: `threat_av`, `threat_tank`, `threat_truck`
- ✅ Exported and integrated as a `.torchscript` model for GUI usage

---

## 💻 GUI Interface

Built a simple yet visually appealing GUI using `Tkinter` where the user can:

1. Upload an image or video.
2. Instantly see the detection output with labeled boxes.
3. Understand vehicle type through visual color coding.

> 🟩 Green Box = Civilian/Safe  
> 🟥 Red Box = Threat

---

## 🏁 How to Run

```bash
# Clone this repo
git clone https://github.com/your-username/threat-detection-yolov8.git
cd threat-detection-yolov8

# Create virtual environment (recommended)
python -m venv yolov8-gui-env
.\yolov8-gui-env\Scripts\activate   # Windows
source yolov8-gui-env/bin/activate # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run the GUI
python Code/gui_app.py
```
---
## 📊Evaluation_metrics:

- test_set:
  - mAP50: 98.72
  - mAP50-95: 84.03
  - precision: 96.55
  - recall: 95.88
  - f1_score: 96.20

---

## 🚧 Limitations

- This version does not include cybersecurity integration (e.g., spoofed feed detection).
- Threat-class images are comparatively fewer, which may affect performance unless the dataset is further balanced.
- It is a proof-of-concept, not deployed in production.

---

## 📌 Future Scope

- Integrating video integrity checks to detect manipulated/spoofed feeds
- Expanding dataset with more threat-class samples
- Deploying on edge devices like NVIDIA Jetson Nano for live surveillance

---

## 🙌 Acknowledgements

- Roboflow for seamless dataset annotation and augmentation
- Ultralytics for YOLOv8
- OpenCV and Tkinter for computer vision and GUI

---
⭐ Star this repo if you found it useful!
