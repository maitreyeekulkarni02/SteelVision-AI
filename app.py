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
# LOAD CSS
# --------------------------------------------------

css_path = "styles/style.css"

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

    st.title("🏭 SteelVision AI")

    st.caption(
        "Edge AI Industrial Inspection Platform"
    )

    st.divider()


    page = st.radio(
        "Navigation",
        [
            "Inspection Dashboard",
            "System Architecture",
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
    AI Powered Machine Health Monitoring
    </h3>

    <p>
    Detect defects, analyze machine condition,
    and generate predictive maintenance insights.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)



# --------------------------------------------------
# ARCHITECTURE PAGE
# --------------------------------------------------

if page == "System Architecture":

    st.title("⚙️ Edge AI Architecture")


    st.write(
        """
        Camera / Smartphone Input

        ↓

        Edge Device

        ↓

        YOLO Computer Vision Model

        ↓

        Defect Detection

        ↓

        Machine Health Intelligence

        ↓

        Maintenance Recommendation


        Production Roadmap:

        Frontend:
        React


        Backend:
        FastAPI


        AI:
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

if page == "About":

    st.title("About SteelVision AI")


    st.write(
        """
        SteelVision AI is an Industry 4.0 solution
        that uses Computer Vision and Edge AI
        to detect machine defects and reduce downtime.
        """
    )


    st.stop()



# --------------------------------------------------
# INSPECTION DASHBOARD
# --------------------------------------------------

st.subheader(
    "🔍 Machine Inspection"
)



uploaded_file = st.file_uploader(
    "Upload machine image",
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

        st.subheader(
            "Original Image"
        )

        st.image(
            image,
            width="stretch"
        )



    with st.spinner(
        "AI analysing machine..."
    ):

        result = detect_defects(
            image
        )



    detected_image = result["image"]

    defects = result["defects"]



    with col2:

        st.subheader(
            "AI Detection"
        )

        st.image(
            detected_image,
            width="stretch"
        )



    # ----------------------------------------------
    # ANALYTICS
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
        "📊 Machine Health Analytics"
    )



    c1,c2,c3,c4 = st.columns(4)


    c1.metric(
        "Health Score",
        f"{health_score}%"
    )


    c2.metric(
        "Status",
        status
    )


    c3.metric(
        "Priority",
        priority
    )


    c4.metric(
        "Defects",
        len(defects)
    )



    st.progress(
        health_score/100
    )



    # ----------------------------------------------
    # DEFECT DETAILS
    # ----------------------------------------------

    st.subheader(
        "Detected Defects"
    )


    if defects:


        for defect in defects:

            st.warning(
                f"""
                {defect['name']}

                Confidence:
                {round(defect['confidence']*100,2)}%
                """
            )


    else:


        st.success(
            "No defects detected."
        )



    # ----------------------------------------------
    # RECOMMENDATION
    # ----------------------------------------------

    st.subheader(
        "🔧 AI Maintenance Recommendation"
    )


    st.info(
        recommendation
    )



    # ----------------------------------------------
    # PDF REPORT
    # ----------------------------------------------

    st.divider()


    st.subheader(
        "📄 Inspection Report"
    )


    pdf = generate_report(
        health_score,
        status,
        priority,
        defects,
        recommendation
    )



    st.download_button(

        label="Download PDF Report",

        data=pdf,

        file_name=
        f"SteelVision_Report_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf",

        mime="application/pdf"

    )



    st.success(
        "✅ Inspection Completed Successfully"
    )



else:


    st.info(
        "Upload machine image to start inspection."
    )



# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown(
    """
    <center>
    SteelVision AI | Industry 4.0 Edge AI Platform
    </center>
    """,
    unsafe_allow_html=True
)