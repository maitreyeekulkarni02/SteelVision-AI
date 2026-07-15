"""
SteelVision AI
AI Maintenance Planner
"""


def generate_maintenance_plan(machine, risk, defects, health):

    if risk == "CRITICAL":

        priority = "Immediate"
        hours = 2
        cost = 18500
        team = "Mechanical Maintenance"

    elif risk == "WARNING":

        priority = "Within 48 Hours"
        hours = 6
        cost = 8500
        team = "Maintenance Team"

    else:

        priority = "Scheduled"
        hours = 1
        cost = 2500
        team = "Inspection Team"

    parts = []

    for defect in defects:

        if isinstance(defect, dict):

            name = defect.get("name", "").lower()

        else:

            name = str(defect).lower()

        if "crack" in name:
            parts.append("Bearing")

        elif "rust" in name:
            parts.append("Anti-Corrosion Kit")

        elif "corrosion" in name:
            parts.append("Anti-Corrosion Kit")

        elif "belt" in name:
            parts.append("Drive Belt")

        elif "bolt" in name:
            parts.append("Fasteners")

        elif "oil" in name:
            parts.append("Seal Kit")

        elif "leak" in name:
            parts.append("Seal Kit")

        elif "damage" in name:
            parts.append("Replacement Assembly")

    if not parts:
        parts.append("General Inspection Kit")

    return {
        "machine": machine,
        "priority": priority,
        "hours": hours,
        "cost": cost,
        "team": team,
        "parts": sorted(set(parts)),
        "steps": [
            "Stop machine",
            "Disconnect power",
            "Inspect affected components",
            "Replace damaged parts",
            "Run AI inspection again",
            "Approve machine for production",
        ],
    }
