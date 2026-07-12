import cv2
import time
import streamlit as st

from PIL import Image

from utils.model import detect_defects
from utils.defect_engine import generate_industrial_defects


def start_video_inspection():

    st.subheader("REAL-TIME EDGE AI CAMERA INSPECTION")

    st.info(
        "Industrial camera simulation running on Edge AI pipeline"
    )

    run = st.checkbox(
        "Start Live Inspection"
    )


    frame_placeholder = st.empty()

    metrics_placeholder = st.empty()


    if run:

        camera = cv2.VideoCapture(0)

        previous_time = time.time()


        while run:

            ret, frame = camera.read()


            if not ret:
                st.error(
                    "Camera frame unavailable"
                )
                break


            rgb_frame = cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2RGB
            )


            image = Image.fromarray(
                rgb_frame
            )


            result = detect_defects(
                image
            )


            defects = generate_industrial_defects(
                result["defects"]
            )


            frame_placeholder.image(
                result["image"],
                width="stretch"
            )


            current_time = time.time()

            fps = 1 / (
                current_time - previous_time
            )

            previous_time = current_time


            metrics_placeholder.metric(
                "Inference FPS",
                f"{fps:.2f}"
            )


        camera.release()