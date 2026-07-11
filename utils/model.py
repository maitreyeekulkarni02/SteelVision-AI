from ultralytics import YOLO
from PIL import Image
import numpy as np
import cv2
import streamlit as st


# Load the model only once
@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")


def detect_objects(image):
    """
    Run YOLO detection on the uploaded image.
    Returns:
        annotated_image
        detections (list)
    """

    model = load_model()

    image_np = np.array(image)

    results = model(image_np)

    annotated = results[0].plot()

    annotated = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)

    detections = []

    for box in results[0].boxes:

        cls = int(box.cls[0])

        confidence = float(box.conf[0])

        class_name = model.names[cls]

        detections.append(
            {
                "class": class_name,
                "confidence": round(confidence * 100, 2),
            }
        )

    return Image.fromarray(annotated), detections