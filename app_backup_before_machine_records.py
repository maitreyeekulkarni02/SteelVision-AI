import streamlit as st
from PIL import Image
import os
from datetime import datetime
import pandas as pd


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

from utils.dashboard import (
    display_machine_metrics,
    display_status_panel,
    display_edge_status
)

from utils.history import (
    save_inspection,
    get_history,
    format_history
)



# ===============================
# PAGE CONFIG
# ===============================

st.set_page_config(
    page_title="SteelVision AI",
    page_icon="??",
    layout="wide"
)



# ===============================
# LOAD CSS
# ===============================

if os.path.exists("styles/style.css"):

    with open("styles/style.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )



# ===============================
# SIDEBAR
# ===============================

with st.sidebar:

    st.title("?? SteelVision AI")

    st.caption(
        "Edge AI Industrial Inspection Platform"
    )

    st.divider()


    page = st.radio(
        "Navigation",
        [
            "Inspection Dashboard",
            "Inspection History",
            "Edge AI Workflow",
            "About"
        ]
    )



# ===============================
# HEADER
# ===============================

st.markdown(
"""
<div class="header-card">

<h1>
?? SteelVision AI
</h1>

<h3>
AI Powered Predictive Maintenance
</h3>

<p>
Computer Vision + Edge AI for Industry 4.0
</p>

</div>
""",
unsafe_allow_html=True
)



# ===============================
# HISTORY PAGE
# ===============================

if page == "Inspection History":


    st.title(
        "?? Inspection History"
    )


    records = get_history()


    if records:

        data = format_history(
            records
        )


        st.dataframe(
            data,
            width="stretch"
        )


    else:

        st.info(
            "No inspection history available."
        )


    st.stop()



# ===============================
# EDGE AI WORKFLOW
# ===============================

if page == "Edge AI Workflow":


    st.title(
        "? Edge AI Architecture"
    )


    st.code(
"""
Industrial Camera

        ?

Edge Device

        ?

YOLO Vision Model

        ?

Industrial Defect Engine

        ?

Machine Health Intelligence

        ?

Maintenance Recommendation
"""
    )


    st.subheader(
        "Production Architecture"
    )


    st.write(
"""
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



# ===============================
# ABOUT
# ===============================

if page == "About":


    st.title(
        "About SteelVision AI"
    )


    st.write(
"""
SteelVision AI is an Edge AI powered
industrial inspection platform designed
for Industry 4.0 manufacturing environments.

It combines Computer Vision, AI analytics,
and predictive maintenance intelligence.
"""
    )


    st.stop()
# ===============================
# INSPECTION DASHBOARD
# ===============================


st.subheader(
    "?? Machine Inspection Dashboard"
)


mode = st.radio(
    "Inspection Mode",
    [
        "Upload Image",
        "Live Camera"
    ]
)


image = None



# ===============================
# INPUT
# ===============================

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



else:


    st.info(
        "?? Edge Camera Mode"
    )


    if st.button(
        "Capture Frame"
    ):

        image = get_camera_frame()



# ===============================
# AI INSPECTION PIPELINE
# ===============================

if image:


    col1, col2 = st.columns(2)



    with col1:


        st.subheader(
            "Input Image"
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


        defects = generate_industrial_defects(
            result["defects"]
        )



    with col2:


        st.subheader(
            "AI Detection Result"
        )


        st.image(
            result["image"],
            width="stretch"
        )



    # ===============================
    # INTELLIGENCE ENGINE
    # ===============================


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



    # ===============================
    # SAVE INSPECTION HISTORY
    # ===============================


    save_inspection(

        machine_name="Machine-01",

        defects=defects,

        health_score=health_score,

        status=status,

        priority=priority,

        recommendation=recommendation

    )



    # ===============================
    # DASHBOARD METRICS
    # ===============================


    st.divider()


    display_machine_metrics(
        health_score,
        status,
        priority,
        len(defects)
    )


    display_status_panel(
        health_score,
        status
    )


    display_edge_status()



    # ===============================
    # DEFECT ANALYTICS
    # ===============================


    st.divider()


    st.subheader(
        "?? Defect Analysis"
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


        df = pd.DataFrame(
            rows
        )


        st.dataframe(
            df,
            width="stretch"
        )



        st.subheader(
            "?? Confidence Analytics"
        )


        chart = pd.DataFrame(
            get_confidence_data(defects)
        )


        st.bar_chart(
            chart.set_index(
                "Defect"
            )
        )



    else:


        st.success(
            "No defects detected."
        )



    # ===============================
    # INSPECTION SUMMARY
    # ===============================


    st.divider()


    st.subheader(
        "?? Inspection Summary"
    )


    st.json(

        generate_inspection_summary(

            defects,

            health_score,

            status,

            priority

        )

    )



    # ===============================
    # MAINTENANCE
    # ===============================


    st.subheader(
        "?? Maintenance Recommendation"
    )


    st.info(
        recommendation
    )



    # ===============================
    # REPORT GENERATION
    # ===============================


    pdf = generate_report(

        health_score,

        status,

        priority,

        defects,

        recommendation

    )


    st.download_button(

        "?? Download Inspection Report",

        pdf,

        file_name=

        f"SteelVision_Report_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf",

        mime="application/pdf"

    )



    st.success(
        "? Inspection Completed Successfully"
    )



else:


    st.info(
        "Upload image or capture camera frame."
    )
