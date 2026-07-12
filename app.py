import streamlit as st
from PIL import Image
import os
from datetime import datetime

from utils.model import detect_defects
from utils.inspection import (
    calculate_health_score,
    get_machine_status,
    get_priority,
    get_recommendation
)

import config


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="SteelVision AI",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded"
)


# --------------------------------------------------
# LOAD CSS
# --------------------------------------------------

css_path = os.path.join("styles", "style.css")

if os.path.exists(css_path):
    with open(css_path) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/2920/2920277.png",
        width=100
    )

    st.title("SteelVision AI")

    st.caption(
        "Edge AI Powered Industrial Inspection Platform"
    )

    st.divider()

    menu = st.radio(
        "Navigation",
        [
            "Inspection Dashboard",
            "System Architecture",
            "About SteelVision AI"
        ]
    )

    st.divider()

    st.info(
        """
        Industry 4.0 Solution

        AI Computer Vision
        Predictive Maintenance
        Edge Intelligence
        """
    )


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    """
    <div class="header-card">

    <h1>🏭 SteelVision AI</h1>

    <h3>
    Intelligent Machine Inspection using Computer Vision
    </h3>

    <p>
    Detect industrial defects, calculate machine health,
    and generate maintenance recommendations using AI.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# SYSTEM ARCHITECTURE PAGE
# --------------------------------------------------

if menu == "System Architecture":

    st.title("⚙️ SteelVision AI Architecture")

    st.markdown(
        """
        ### Edge AI Inspection Workflow

        📷 Machine Camera / Smartphone Camera

        ↓

        🤖 YOLO Computer Vision Model

        ↓

        🔍 Defect Detection

        ↓

        📊 Health Score Calculation

        ↓

        🛠 Predictive Maintenance Recommendation


        ### Production Roadmap

        Frontend:
        React + TypeScript


        Backend:
        FastAPI


        AI Engine:
        Custom YOLO Model


        Database:
        PostgreSQL


        Deployment:
        Docker + Edge Device
        """
    )

    st.stop()



# --------------------------------------------------
# ABOUT PAGE
# --------------------------------------------------

if menu == "About SteelVision AI":

    st.title("About SteelVision AI")

    st.write(
        """
        SteelVision AI is an Industry 4.0 computer vision platform
        designed to reduce machine downtime by detecting defects
        early and providing actionable maintenance insights.
        """
    )

    st.stop()



# --------------------------------------------------
# INSPECTION DASHBOARD
# --------------------------------------------------

st.subheader("🔍 Machine Inspection Dashboard")


uploaded_file = st.file_uploader(
    "Upload Machine Image",
    type=[
        "jpg",
        "jpeg",
        "png"
    ]
)



if uploaded_file:


    image = Image.open(uploaded_file)


    col1, col2 = st.columns(2)



    with col1:

        st.markdown(
            "### Original Machine Image"
        )

        st.image(
            image,
            use_container_width=True
        )



    # ----------------------------------------------
    # AI INFERENCE
    # ----------------------------------------------

    with st.spinner(
        "Running AI defect detection..."
    ):

        result = detect_defects(image)


    detected_image = result["image"]

    defects = result["defects"]



    with col2:

        st.markdown(
            "### AI Detection Result"
        )

        st.image(
            detected_image,
            use_container_width=True
        )



    st.divider()



    # ----------------------------------------------
    # ANALYTICS
    # ----------------------------------------------

    defect_count = len(defects)


    health_score = calculate_health_score(
        defects
    )


    machine_status = get_machine_status(
        health_score
    )


    priority = get_priority(
        health_score
    )


    recommendation = get_recommendation(
        defects
    )



    st.subheader(
        "📊 Machine Health Analytics"
    )


    c1, c2, c3, c4 = st.columns(4)


    with c1:

        st.metric(
            "Machine Health",
            f"{health_score}%"
        )


    with c2:

        st.metric(
            "Status",
            machine_status
        )


    with c3:

        st.metric(
            "Maintenance Priority",
            priority
        )


    with c4:

        st.metric(
            "Defects Found",
            defect_count
        )



    # Health Progress

    st.progress(
        health_score / 100
    )


    st.divider()



    # ----------------------------------------------
    # DEFECT DETAILS
    # ----------------------------------------------

    st.subheader(
        "🛠 Detection Summary"
    )


    if defects:

        for defect in defects:

            st.warning(
                f"""
                Defect:
                {defect['name']}

                Confidence:
                {round(defect['confidence']*100,2)}%
                """
            )


    else:

        st.success(
            "No defects detected. Machine condition looks healthy."
        )



    # ----------------------------------------------
    # RECOMMENDATION
    # ----------------------------------------------

    st.subheader(
        "🔧 Maintenance Recommendation"
    )


    st.markdown(
        f"""
        <div class="recommendation-card">

        {recommendation}

        </div>
        """,
        unsafe_allow_html=True
    )



    st.success(
        "✅ Inspection Completed Successfully"
    )



    # ----------------------------------------------
    # REPORT PREVIEW
    # ----------------------------------------------

    st.divider()

    st.subheader(
        "📄 Inspection Report Preview"
    )


    st.write(
        {
            "Date":
            datetime.now().strftime(
                "%d-%m-%Y %H:%M"
            ),

            "Defects":
            defect_count,

            "Health Score":
            f"{health_score}%",

            "Status":
            machine_status,

            "Priority":
            priority
        }
    )



else:

    st.info(
        "Upload a machine image to start AI inspection."
    )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown(
    """
    <br>

    <center>

    SteelVision AI |
    Industry 4.0 Edge AI Inspection Platform

    </center>

    """,
    unsafe_allow_html=True
)