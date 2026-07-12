import streamlit as st
from PIL import Image
import os
from datetime import datetime
import pandas as pd

from utils.model import detect_defects

from utils.defect_engine import (
    generate_industrial_defects
)

from utils.inspection import (
    calculate_health_score,
    get_machine_status,
    get_priority,
    get_recommendation
)

from utils.report import generate_report

from utils.analytics import (
    calculate_defect_severity,
    get_confidence_data,
    generate_inspection_summary
)



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
        "Edge AI Industrial Inspection"
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
AI Powered Predictive Maintenance Platform
</h3>

<p>
Industrial defect detection using Computer Vision and Edge AI.
</p>

</div>
""",
unsafe_allow_html=True
)



# --------------------------------------------------
# WORKFLOW PAGE
# --------------------------------------------------

if page == "Edge AI Workflow":

    st.title(
        "⚡ Edge AI Workflow"
    )

    st.markdown(
"""
Machine Camera
|
↓
Edge AI Device
|
↓
YOLO Vision Model
|
↓
Industrial Defect Engine
|
↓
Health Intelligence
|
↓
Maintenance Recommendation

### Production Roadmap

Frontend:
React


Backend:
FastAPI


AI:
Custom YOLO Industrial Model


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

    st.title(
        "About SteelVision AI"
    )

    st.write(
"""
SteelVision AI is an Industry 4.0 inspection platform
that enables manufacturers to identify defects,
monitor machine health and optimize maintenance.
"""
)

    st.stop()



# --------------------------------------------------
# DASHBOARD
# --------------------------------------------------

st.subheader(
"🔍 Machine Inspection Dashboard"
)



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


    col1,col2 = st.columns(2)



    with col1:

        st.subheader(
            "Original Image"
        )

        st.image(
            image,
            width="stretch"
        )



    with st.spinner(
        "Running AI inspection..."
    ):


        yolo_result = detect_defects(
            image
        )


        industrial_defects = generate_industrial_defects(
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



    defects = industrial_defects



    # --------------------------------------------------
    # HEALTH ANALYTICS
    # --------------------------------------------------

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
        "📊 Machine Health Intelligence"
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



    # --------------------------------------------------
    # DEFECT DETAILS
    # --------------------------------------------------

    st.divider()


    st.subheader(
        "🚨 Industrial Defects Detected"
    )


    if defects:


        rows=[]


        for defect in defects:


            severity = calculate_defect_severity(
                defect
            )


            rows.append(

                {

                "Defect":
                defect["name"],


                "Confidence":
                f"{defect['confidence']*100:.2f}%",


                "Severity":
                severity

                }

            )



        df = pd.DataFrame(
            rows
        )


        st.dataframe(
            df,
            use_container_width=True
        )


    else:


        st.success(
            "No industrial defects detected."
        )



    # --------------------------------------------------
    # CONFIDENCE
    # --------------------------------------------------

    st.subheader(
        "📈 Confidence Analytics"
    )


    if defects:


        chart = pd.DataFrame(
            get_confidence_data(defects)
        )


        chart = chart.set_index(
            "Defect"
        )


        st.bar_chart(
            chart
        )



    # --------------------------------------------------
    # SUMMARY
    # --------------------------------------------------

    st.subheader(
        "📋 Inspection Summary"
    )


    summary = generate_inspection_summary(
        defects,
        health_score,
        status,
        priority
    )


    st.json(
        summary
    )



    # --------------------------------------------------
    # RECOMMENDATION
    # --------------------------------------------------

    st.subheader(
        "🔧 AI Maintenance Recommendation"
    )


    st.info(
        recommendation
    )



    # --------------------------------------------------
    # REPORT
    # --------------------------------------------------

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
        "Upload machine image to begin inspection."
    )