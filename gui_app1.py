import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import os
from ultralytics import YOLO
import torch

# Load TorchScript model
model = YOLO("C:/Users/Rajesh/OneDrive - JK LAKSHMIPAT UNIVERSITY/Desktop/SEM 6/Minor project/Code/yolov8_balanced.torchscript")

# Class names
CLASS_NAMES = {
    0: 'civilian_auto',
    1: 'civilian_bus',
    2: 'civilian_tempo',
    3: 'civilian_tractor',
    4: 'civilian_truck',
    5: 'safe_av',
    6: 'safe_tanks',
    7: 'safe_truck',
    8: 'threat_av',
    9: 'threat_tank',
    10: 'threat_truck'
}

# Class color
class_colors = {
    'civilian_auto': 'green',
    'civilian_bus': 'green',
    'civilian_tempo': 'green',
    'civilian_tractor': 'green',
    'civilian_truck': 'green',
    'safe_av': 'green',
    'safe_tanks': 'green',
    'safe_truck': 'green',
    'threat_av': 'red',
    'threat_tank': 'red',
    'threat_truck': 'red'
}

# Detection Function
def detect_and_display(file_path, is_video=False):
    if is_video:
        cap = cv2.VideoCapture(file_path)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            results = model(frame)[0]
            if results.boxes is not None:
                for box in results.boxes:
                    cls_id = int(box.cls[0])
                    label = CLASS_NAMES.get(cls_id, f"class_{cls_id}")
                    color = (0, 255, 0) if class_colors[label] == 'green' else (0, 0, 255)
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                    cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(rgb_frame)
            img.thumbnail((800, 600))
            imgtk = ImageTk.PhotoImage(img)
            panel.config(image=imgtk)
            panel.image = imgtk
            window.update()
        cap.release()
    else:
        img = cv2.imread(file_path)
        results = model(img)[0]
        if results.boxes is not None:
            for box in results.boxes:
                cls_id = int(box.cls[0])
                label = CLASS_NAMES.get(cls_id, f"class_{cls_id}")
                color = (0, 255, 0) if class_colors[label] == 'green' else (0, 0, 255)
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
                cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_rgb)
        img_pil.thumbnail((800, 600))
        imgtk = ImageTk.PhotoImage(img_pil)
        panel.config(image=imgtk)
        panel.image = imgtk

# Upload Button Handler
def upload_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image or Video files", "*.jpg *.jpeg *.png *.mp4 *.avi")]
    )
    if file_path.lower().endswith(('.mp4', '.avi')):
        detect_and_display(file_path, is_video=True)
    else:
        detect_and_display(file_path, is_video=False)

# ==== GUI STARTS HERE ====
window = tk.Tk()
window.title("🚨 AI-Based Threat Detection System")
window.geometry("1000x700")
window.configure(bg="#f0f2f5")

# Title Label
title_frame = tk.Frame(window, bg="#004080", pady=10)
title_frame.pack(fill="x")

title_label = tk.Label(title_frame, text="AI-Powered Threat Detection System", font=("Segoe UI", 18, "bold"), fg="white", bg="#004080")
title_label.pack()

# Upload Button
button_frame = tk.Frame(window, bg="#f0f2f5")
button_frame.pack(pady=30)

upload_button = tk.Button(
    button_frame,
    text="📁 Upload Image or Video",
    command=upload_file,
    font=("Segoe UI", 14),
    bg="#1e90ff",
    fg="white",
    padx=20,
    pady=10
)
upload_button.pack()

# Image Panel
panel_frame = tk.Frame(window, bg="#f0f2f5")
panel_frame.pack(expand=True, fill="both", padx=20, pady=(0, 10))

panel = tk.Label(panel_frame, bg="#dfe6e9", relief="ridge", bd=3)
panel.pack(expand=True, fill="both")
window.geometry("1000x750")


# Footer
footer = tk.Label(window, text="Developed for Minor Project | JKLU", font=("Segoe UI", 10), bg="#f0f2f5", fg="gray")
footer.pack(side="bottom", pady=10)

window.mainloop()
