import os
from datetime import datetime
from pathlib import Path

import pandas as pd
import streamlit as st
from PIL import Image

from app_pages.about import show_about
from app_pages.history import show_history
from ui.analytics_dashboard import show_analytics_dashboard
from ui.command_center import show_command_center
from ui.copilot_panel import show_copilot
from ui.factory_twin import show_factory_twin
from ui.maintenance_panel import show_maintenance_plan
from utils.analytics import (
    calculate_defect_severity,
    generate_inspection_summary,
    get_confidence_data,
)
from utils.camera import get_camera_frame
from utils.dashboard import (
    display_edge_status,
    display_machine_metrics,
    display_status_panel,
)
from utils.defect_engine import generate_industrial_defects
from utils.history import save_inspection
from utils.inspection import (
    calculate_health_score,
    get_machine_status,
    get_priority,
    get_recommendation,
)
from utils.machine_manager import get_machines, update_machine_health
from utils.maintenance_planner import generate_maintenance_plan
from utils.model import detect_defects
from utils.report import generate_report
from utils.video_inspection import start_video_inspection

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(page_title="SteelVision AI", page_icon="", layout="wide")


# =====================================
# LOAD STYLE
# =====================================

if os.path.exists("styles/style.css"):

    with open("styles/style.css") as f:

        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# =====================================


# Load Industrial Theme

css_path = Path("styles/style.css")

if css_path.exists():

    st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)


# SIDEBAR
# =====================================

with st.sidebar:

    st.title("STEELVISION AI")

    st.caption("Edge AI Industrial Inspection Platform")

    st.divider()

    page = st.radio(
        "Navigation",
        [
            "Command Center",
            "Inspection Dashboard",
            "Analytics Dashboard",
            "Factory Digital Twin",
            "Inspection History",
            "Machine Records",
            "Edge AI Workflow",
            "About",
        ],
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
    unsafe_allow_html=True,
)


# =====================================


# =====================================
# COMMAND CENTER
# =====================================

if page == "Command Center":

    show_command_center()

    st.stop()


# =====================================
# FACTORY DIGITAL TWIN PAGE
# =====================================

if page == "Factory Digital Twin":

    show_factory_twin()

    st.stop()


# =====================================
# ANALYTICS DASHBOARD PAGE
# =====================================


if page == "Analytics Dashboard":

    show_analytics_dashboard()

    st.stop()


# INSPECTION HISTORY PAGE
# =====================================

if page == "Inspection History":

    show_history()

    st.stop()


# =====================================
# MACHINE RECORDS PAGE
# =====================================

if page == "Machine Records":

    st.title(" Machine Records")

    machines = get_machines()

    if machines:

        rows = []

        for machine in machines:

            rows.append(
                {
                    "Machine ID": machine.machine_id,
                    "Machine Name": machine.machine_name,
                    "Type": machine.machine_type,
                    "Location": machine.location,
                    "Health": f"{machine.current_health}%",
                    "Status": machine.status,
                    "Last Inspection": str(machine.last_inspection),
                }
            )

        df = pd.DataFrame(rows)

        st.dataframe(df, width="stretch")

    else:

        st.info("No machines registered.")

    st.stop()


# =====================================
# EDGE AI WORKFLOW
# =====================================

if page == "Edge AI Workflow":

    st.title("EDGE AI ARCHITECTURE")

    st.code(
        """
Industrial Camera

        |

Edge Device

        |

YOLO Vision Model

        |

Industrial Defect Engine

        |

Machine Health Intelligence

        |

Maintenance Recommendation
"""
    )

    st.subheader("Production Architecture")

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

    show_about()

    st.stop()
# =====================================
# INSPECTION DASHBOARD
# =====================================


st.subheader("MACHINE INSPECTION DASHBOARD")


mode = st.radio(
    "Inspection Mode", ["Upload Image", "Live Camera", "Real-Time Video Inspection"]
)


image = None


# =====================================
# IMAGE INPUT
# =====================================


if mode == "Upload Image":

    uploaded_file = st.file_uploader(
        "Upload Machine Image", type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:

        image = Image.open(uploaded_file)


elif mode == "Real-Time Video Inspection":

    start_video_inspection()

    st.stop()

else:

    st.info(" Edge Camera Mode")

    if st.button("Capture Frame"):

        image = get_camera_frame()


# =====================================
# AI PIPELINE
# =====================================


machine_id = st.text_input("Machine ID", "MACHINE_001")


if image:

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Input Image")

        st.image(image, width="stretch")

    with st.spinner("Running YOLO Edge AI inspection..."):

        result = detect_defects(image)

        defects = generate_industrial_defects(result["defects"])

    with col2:

        st.subheader("AI Detection Result")

        st.image(result["image"], width="stretch")

    # =====================================
    # INTELLIGENCE ENGINE
    # =====================================

    health_score = calculate_health_score(defects)

    status = get_machine_status(health_score)

    priority = get_priority(health_score)

    recommendation = get_recommendation(defects)

    # =====================================
    # AI MAINTENANCE PLANNER
    # =====================================

    plan = generate_maintenance_plan(
        machine=machine_id, risk=priority, defects=defects, health=health_score
    )

    show_maintenance_plan(plan)

    # =====================================
    # SAVE HISTORY
    # =====================================

    save_inspection(
        machine_name=machine_id,
        defects=defects,
        health_score=health_score,
        status=status,
        priority=priority,
        recommendation=recommendation,
    )

    # =====================================
    # UPDATE MACHINE HEALTH
    # =====================================

    update_machine_health(machine_id="M001", health=health_score, status=status)

    # =====================================
    # DASHBOARD METRICS
    # =====================================

    st.divider()

    display_machine_metrics(health_score, status, priority, len(defects))

    display_status_panel(health_score, status)

    display_edge_status()

    # =====================================
    # DEFECT ANALYSIS
    # =====================================

    st.divider()

    st.subheader(" Industrial Defect Analysis")

    if defects:

        rows = []

        for defect in defects:

            rows.append(
                {
                    "Defect": defect["name"],
                    "Confidence": f"{defect['confidence']*100:.2f}%",
                    "Severity": calculate_defect_severity(defect),
                }
            )

        df = pd.DataFrame(rows)

        st.dataframe(df, width="stretch")

        st.subheader(" Confidence Analytics")

        chart = pd.DataFrame(get_confidence_data(defects))

        st.bar_chart(chart.set_index("Defect"))

    else:

        st.success("No defects detected.")

    # =====================================
    # INSPECTION SUMMARY
    # =====================================

    st.divider()

    st.subheader(" Inspection Summary")

    st.json(generate_inspection_summary(defects, health_score, status, priority))

    # =====================================
    # MAINTENANCE
    # =====================================

    st.subheader(" Maintenance Recommendation")

    st.info(recommendation)

    # =====================================
    # PDF REPORT
    # =====================================

    pdf = generate_report(health_score, status, priority, defects, recommendation)

    st.divider()

    show_copilot(
        machine=machine_id,
        defects=defects,
        health=health_score,
        priority=priority,
        recommendation=recommendation,
    )

    st.download_button(
        " Download Inspection Report",
        pdf,
        file_name=f"SteelVision_Report_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf",
        mime="application/pdf",
    )

    save_inspection(machine_id, defects, health_score, status, priority)

    st.success("INSPECTION COMPLETED SUCCESSFULLY")


else:

    st.info("Upload image or capture camera frame.")
