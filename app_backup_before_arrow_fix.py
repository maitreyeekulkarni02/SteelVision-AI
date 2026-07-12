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


from utils.machine_manager import (
    get_machines,
    update_machine_health
)



# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="SteelVision AI",
    page_icon="",
    layout="wide"
)



# =====================================
# LOAD STYLE
# =====================================

if os.path.exists("styles/style.css"):

    with open("styles/style.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )



# =====================================
# SIDEBAR
# =====================================

with st.sidebar:


    st.title(
        "STEELVISION AI"
    )


    st.caption(
        "Edge AI Industrial Inspection Platform"
    )


    st.divider()


    page = st.radio(

        "Navigation",

        [
            "Inspection Dashboard",
            "Inspection History",
            "Machine Records",
            "Edge AI Workflow",
            "About"
        ]

    )



# =====================================
# HEADER
# =====================================

st.markdown(

"""
<div class="header-card">

<h1>
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



# =====================================
# INSPECTION HISTORY PAGE
# =====================================

if page == "Inspection History":


    st.title(
        " Inspection History"
    )


    records = get_history()


    if records:


        history = format_history(
            records
        )


        st.dataframe(

            history,

            width="stretch"

        )


    else:


        st.info(
            "No inspection records found."
        )


    st.stop()



# =====================================
# MACHINE RECORDS PAGE
# =====================================

if page == "Machine Records":


    st.title(
        " Machine Records"
    )


    machines = get_machines()


    if machines:


        rows = []


        for machine in machines:


            rows.append(

            {

                "Machine ID":
                machine.machine_id,


                "Machine Name":
                machine.machine_name,


                "Type":
                machine.machine_type,


                "Location":
                machine.location,


                "Health":
                f"{machine.current_health}%",


                "Status":
                machine.status,


                "Last Inspection":
                str(machine.last_inspection)

            }

            )


        df = pd.DataFrame(
            rows
        )


        st.dataframe(

            df,

            width="stretch"

        )


    else:


        st.info(
            "No machines registered."
        )


    st.stop()



# =====================================
# EDGE AI WORKFLOW
# =====================================

if page == "Edge AI Workflow":


    st.title(
        "EDGE AI ARCHITECTURE"
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



# =====================================
# ABOUT
# =====================================

if page == "About":


    st.title(
        "About SteelVision AI"
    )


    st.write(

"""
SteelVision AI is an Industry 4.0
Edge AI inspection platform.

It combines Computer Vision,
Machine Health Intelligence,
and Predictive Maintenance.
"""

    )


    st.stop()
# =====================================
# INSPECTION DASHBOARD
# =====================================


st.subheader(
    "MACHINE INSPECTION DASHBOARD"
)



mode = st.radio(

    "Inspection Mode",

    [
        "Upload Image",
        "Live Camera"
    ]

)



image = None



# =====================================
# IMAGE INPUT
# =====================================


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
        " Edge Camera Mode"
    )


    if st.button(
        "Capture Frame"
    ):


        image = get_camera_frame()



# =====================================
# AI PIPELINE
# =====================================


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

        "Running YOLO Edge AI inspection..."

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



    # =====================================
    # INTELLIGENCE ENGINE
    # =====================================


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



    # =====================================
    # SAVE HISTORY
    # =====================================


    save_inspection(

        machine_name="Machine-01",

        defects=defects,

        health_score=health_score,

        status=status,

        priority=priority,

        recommendation=recommendation

    )



    # =====================================
    # UPDATE MACHINE HEALTH
    # =====================================


    update_machine_health(

        machine_id="M001",

        health=health_score,

        status=status

    )



    # =====================================
    # DASHBOARD METRICS
    # =====================================


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



    # =====================================
    # DEFECT ANALYSIS
    # =====================================


    st.divider()


    st.subheader(

        " Industrial Defect Analysis"

    )



    if defects:


        rows = []


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

            " Confidence Analytics"

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



    # =====================================
    # INSPECTION SUMMARY
    # =====================================


    st.divider()


    st.subheader(

        " Inspection Summary"

    )


    st.json(

        generate_inspection_summary(

            defects,

            health_score,

            status,

            priority

        )

    )



    # =====================================
    # MAINTENANCE
    # =====================================


    st.subheader(

        " Maintenance Recommendation"

    )


    st.info(

        recommendation

    )



    # =====================================
    # PDF REPORT
    # =====================================


    pdf = generate_report(

        health_score,

        status,

        priority,

        defects,

        recommendation

    )


    st.download_button(

        " Download Inspection Report",

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
