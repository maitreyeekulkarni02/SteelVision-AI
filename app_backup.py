import streamlit as st
from PIL import Image
import os
from datetime import datetime
import pandas as pd
import time

from utils.model import detect_defects

from utils.camera import get_camera_frame

from utils.defect_engine import (
    generate_industrial_defects
)

from utils.inspection import (
    calculate_health_score,
    get_machine_status,
    get_priority,
    get_recommendation
)

from utils.analytics import (
    calculate_defect_severity,
    get_confidence_data,
    generate_inspection_summary
)

from utils.report import generate_report



# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="SteelVision AI",
    page_icon="🏭",
    layout="wide"
)



# --------------------------------------------------
# CSS
# --------------------------------------------------

if os.path.exists("styles/style.css"):

    with open("styles/style.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )



# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.title("🏭 SteelVision AI")

    st.caption(
        "Edge AI Industrial Inspection Platform"
    )

    st.divider()

    page = st.radio(
        "Navigation",
        [
            "Inspection Dashboard",
            "Edge AI Workflow",
            "About"
        ]
    )



# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
"""
<div class="header-card">

<h1>
🏭 SteelVision AI
</h1>

<h3>
Real-Time Edge AI Machine Inspection
</h3>

<p>
Computer Vision powered predictive maintenance
for Industry 4.0.
</p>

</div>
""",
unsafe_allow_html=True
)



# --------------------------------------------------
# WORKFLOW PAGE
# --------------------------------------------------

if page == "Edge AI Workflow":

    st.title("⚡ Edge AI Architecture")


    st.markdown(
"""
Industrial Camera
|
↓
Edge Device
|
↓
YOLO Vision Engine
|
↓
Industrial Defect AI
|
↓
Machine Health Score
|
↓
Maintenance Action

Production Stack:

Frontend:
React


Backend:
FastAPI


AI:
Custom YOLO Model


Database:
PostgreSQL


Deployment:
Docker + Edge Hardware
"""
)


    st.stop()



# --------------------------------------------------
# ABOUT
# --------------------------------------------------

if page == "About":

    st.title("About SteelVision AI")

    st.write(
"""
SteelVision AI is an affordable Edge AI
inspection platform designed for factories
to detect defects and reduce machine downtime.
"""
)

    st.stop()



# --------------------------------------------------
# DASHBOARD
# --------------------------------------------------

st.subheader(
"🔍 Machine Inspection Dashboard"
)



mode = st.radio(
    "Inspection Mode",
    [
        "Upload Image",
        "Live Camera"
    ]
)



image = None



# --------------------------------------------------
# IMAGE MODE
# --------------------------------------------------

if mode == "Upload Image":


    uploaded_file = st.file_uploader(
        "Upload Machine Image",
        type=[
            "jpg",
            "jpeg",
            "png"
        ]
    )


    if uploaded_file:

        image = Image.open(
            uploaded_file
        )



# --------------------------------------------------
# CAMERA MODE
# --------------------------------------------------

else:


    st.info(
        "📷 Edge Camera Mode Activated"
    )


    if st.button(
        "Capture Inspection Frame"
    ):


        start = time.time()


        image = get_camera_frame()


        end = time.time()


        if image:


            fps = round(
                1/(end-start),
                2
            )


            st.success(
                f"Camera frame captured | FPS: {fps}"
            )


        else:

            st.error(
                "Camera not available"
            )



# --------------------------------------------------
# AI INSPECTION PIPELINE
# --------------------------------------------------

if image:


    col1,col2 = st.columns(2)



    with col1:

        st.subheader(
            "Input Image"
        )

        st.image(
            image,
            width="stretch"
        )



    with st.spinner(
        "⚡ Edge AI analysing..."
    ):


        yolo_result = detect_defects(
            image
        )


        defects = generate_industrial_defects(
            yolo_result["defects"]
        )



    with col2:

        st.subheader(
            "AI Detection Result"
        )


        st.image(
            yolo_result["image"],
            width="stretch"
        )



    # ----------------------------------------------
    # HEALTH
    # ----------------------------------------------

    health_score = calculate_health_score(
        defects
    )


    status = get_machine_status(
        health_score
    )


    priority = get_priority(
        health_score
    )


    recommendation = get_recommendation(
        defects
    )



    st.divider()


    st.subheader(
        "📊 Machine Health"
    )


    a,b,c,d = st.columns(4)


    a.metric(
        "Health",
        f"{health_score}%"
    )


    b.metric(
        "Status",
        status
    )


    c.metric(
        "Priority",
        priority
    )


    d.metric(
        "Defects",
        len(defects)
    )



    st.progress(
        health_score/100
    )



    # ----------------------------------------------
    # DEFECTS
    # ----------------------------------------------

    st.subheader(
        "🚨 Industrial Defect Analysis"
    )


    if defects:


        rows=[]


        for defect in defects:


            rows.append(
                {
                "Defect":
                defect["name"],

                "Confidence":
                f"{defect['confidence']*100:.2f}%",

                "Severity":
                calculate_defect_severity(defect)
                }
            )



        st.dataframe(
            pd.DataFrame(rows)
        )


        chart = pd.DataFrame(
            get_confidence_data(defects)
        )


        st.subheader(
            "📈 Confidence Analytics"
        )


        st.bar_chart(
            chart.set_index("Defect")
        )



    else:

        st.success(
            "No defects detected."
        )



    # ----------------------------------------------
    # SUMMARY
    # ----------------------------------------------

    st.subheader(
        "📋 Inspection Summary"
    )


    st.json(
        generate_inspection_summary(
            defects,
            health_score,
            status,
            priority
        )
    )



    # ----------------------------------------------
    # REPORT
    # ----------------------------------------------

    pdf = generate_report(
        health_score,
        status,
        priority,
        defects,
        recommendation
    )


    st.download_button(
        "📄 Download Inspection Report",
        pdf,
        file_name=
        f"SteelVision_Report_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf",
        mime="application/pdf"
    )



    st.success(
        "✅ Inspection Completed Successfully"
    )

else:

    st.info(
        "Select inspection mode and provide machine input."
    )