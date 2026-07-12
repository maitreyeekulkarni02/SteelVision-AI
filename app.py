import streamlit as st
from PIL import Image
import os
from datetime import datetime
import pandas as pd

from utils.model import detect_defects

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
Computer Vision Powered Predictive Maintenance
</h3>

<p>
AI based defect detection and machine health monitoring
for Industry 4.0.
</p>

</div>

""",
unsafe_allow_html=True
)



# --------------------------------------------------
# EDGE WORKFLOW
# --------------------------------------------------

if page == "Edge AI Workflow":

    st.title(
        "⚡ Edge AI Inspection Workflow"
    )


    st.markdown(
"""
## Industrial Inspection Pipeline


📷 Smartphone / Industrial Camera

↓

⚡ Edge Device Processing

↓

🤖 YOLO Computer Vision Model

↓

🔍 Defect Detection

↓

📊 Machine Health Intelligence

↓

🔧 Predictive Maintenance Action


### Production Architecture

Frontend:
React + TypeScript


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

    st.title(
        "About SteelVision AI"
    )


    st.write(
"""
SteelVision AI is an Industry 4.0
inspection platform that helps manufacturers
detect machine defects early and reduce downtime.
"""
)

    st.stop()



# --------------------------------------------------
# MAIN DASHBOARD
# --------------------------------------------------

st.subheader(
"🔍 Machine Inspection Dashboard"
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
        "Running Edge AI inspection..."
    ):

        result = detect_defects(
            image
        )


    detected_image = result["image"]

    defects = result["defects"]



    with col2:

        st.subheader(
        "AI Detection Result"
        )

        st.image(
            detected_image,
            width="stretch"
        )



    # ----------------------------------------------
    # HEALTH ANALYTICS
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


    a,b,c,d = st.columns(4)


    a.metric(
    "Health Score",
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
    # SEVERITY ANALYSIS
    # ----------------------------------------------

    st.divider()

    st.subheader(
    "⚠️ Defect Severity Analysis"
    )


    if defects:


        severity_rows=[]


        for defect in defects:


            severity = calculate_defect_severity(
                defect
            )


            severity_rows.append(

            {

            "Defect":
            defect["name"],

            "Confidence":
            f"{round(defect['confidence']*100,2)}%",

            "Severity":
            severity

            }

            )


        df = pd.DataFrame(
            severity_rows
        )


        st.dataframe(
            df,
            use_container_width=True
        )


    else:


        st.success(
        "No defects detected."
        )



    # ----------------------------------------------
    # CONFIDENCE ANALYTICS
    # ----------------------------------------------

    st.divider()

    st.subheader(
    "📈 Confidence Analytics"
    )


    if defects:


        chart_data = pd.DataFrame(
            get_confidence_data(defects)
        )


        chart_data = chart_data.set_index(
            "Defect"
        )


        st.bar_chart(
            chart_data
        )



    # ----------------------------------------------
    # SUMMARY
    # ----------------------------------------------

    st.divider()

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



    # ----------------------------------------------
    # RECOMMENDATION
    # ----------------------------------------------

    st.divider()

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
    "📄 Generate Report"
    )


    pdf = generate_report(
        health_score,
        status,
        priority,
        defects,
        recommendation
    )


    st.download_button(
        "Download Inspection PDF",
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
    "Upload a machine image to begin AI inspection."
    )



st.markdown(
"""
<center>
SteelVision AI | Industry 4.0 Edge AI Platform
</center>
""",
unsafe_allow_html=True
)