"""
SteelVision AI Configuration
"""

# -----------------------------
# App Information
# -----------------------------

APP_NAME = "SteelVision AI"
APP_TAGLINE = "Edge AI Industrial Inspection Platform"

# -----------------------------
# Colors
# -----------------------------

PRIMARY_COLOR = "#0B3C5D"
SUCCESS_COLOR = "#28A745"
WARNING_COLOR = "#FFC107"
DANGER_COLOR = "#DC3545"

# -----------------------------
# Machine Health Logic
# -----------------------------

def calculate_health(defect_count: int) -> int:
    """
    Calculate machine health score.
    """

    if defect_count == 0:
        return 100
    elif defect_count == 1:
        return 90
    elif defect_count == 2:
        return 75
    elif defect_count == 3:
        return 60
    elif defect_count == 4:
        return 40
    else:
        return 20


# -----------------------------
# Machine Status
# -----------------------------

def machine_status(score: int) -> str:

    if score >= 90:
        return "Excellent"

    elif score >= 75:
        return "Good"

    elif score >= 50:
        return "Moderate"

    return "Critical"


# -----------------------------
# Maintenance Priority
# -----------------------------

def maintenance_priority(score: int) -> str:

    if score >= 90:
        return "Low"

    elif score >= 75:
        return "Medium"

    elif score >= 50:
        return "High"

    return "Critical"


# -----------------------------
# Recommendation
# -----------------------------

def maintenance_recommendation(priority: str) -> str:

    recommendations = {
        "Low": "Routine inspection recommended.",
        "Medium": "Schedule preventive maintenance.",
        "High": "Maintenance required within 24 hours.",
        "Critical": "Immediate shutdown and inspection recommended."
    }

    return recommendations.get(priority, "No recommendation available.")