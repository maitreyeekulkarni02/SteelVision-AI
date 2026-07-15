"""
SteelVision AI
Inspection Intelligence Engine

Handles:
- Machine health calculation
- Status classification
- Maintenance priority
- Recommendations
"""

# --------------------------------------------------
# HEALTH SCORE CALCULATION
# --------------------------------------------------


def calculate_health_score(defects):
    """
    Calculate machine health score
    based on detected defects.
    """

    if not defects:

        return 100

    defect_count = len(defects)

    critical_keywords = ["crack", "oil", "leak", "corrosion", "damage"]

    critical_count = 0

    for defect in defects:

        name = defect["name"].lower()

        for keyword in critical_keywords:

            if keyword in name:

                critical_count += 1

                break

    # Health rules

    if critical_count >= 3:

        return 20

    elif critical_count == 2:

        return 40

    elif defect_count >= 3:

        return 60

    elif defect_count == 2:

        return 75

    else:

        return 90


# --------------------------------------------------
# MACHINE STATUS
# --------------------------------------------------


def get_machine_status(score):

    if score >= 90:

        return "Excellent"

    elif score >= 75:

        return "Good"

    elif score >= 50:

        return "Moderate"

    else:

        return "Critical"


# --------------------------------------------------
# MAINTENANCE PRIORITY
# --------------------------------------------------


def get_priority(score):

    if score >= 90:

        return "Low"

    elif score >= 75:

        return "Medium"

    elif score >= 50:

        return "High"

    else:

        return "Critical"


# --------------------------------------------------
# RECOMMENDATION ENGINE
# --------------------------------------------------


def get_recommendation(defects):

    if not defects:

        return (
            "Machine condition is healthy. "
            "Continue regular preventive maintenance schedule."
        )

    defect_names = []

    for defect in defects:

        defect_names.append(defect["name"])

    defects_text = ", ".join(defect_names)

    return f"""
Detected issues:

{defects_text}


Recommended Actions:

• Schedule maintenance inspection
• Check affected machine components
• Perform detailed quality analysis
• Monitor machine health continuously
"""
