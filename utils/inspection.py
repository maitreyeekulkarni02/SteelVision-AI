from collections import Counter

# Defect classes that your future custom YOLO model will use
CRITICAL_DEFECTS = {
    "crack",
    "oil_leakage",
    "missing_component",
}

MODERATE_DEFECTS = {
    "rust",
    "corrosion",
    "damaged_belt",
}

MINOR_DEFECTS = {
    "surface_damage",
    "loose_bolt",
}


def calculate_health(defects):
    """
    Calculate machine health score.
    """
    if len(defects) == 0:
        return 100

    critical = sum(1 for d in defects if d in CRITICAL_DEFECTS)

    if critical >= 2:
        return 20

    if critical == 1:
        return 40

    if len(defects) >= 3:
        return 60

    if len(defects) == 2:
        return 75

    return 90


def machine_status(score):
    if score >= 90:
        return "Excellent"

    if score >= 75:
        return "Good"

    if score >= 60:
        return "Moderate"

    return "Critical"


def maintenance_priority(score):
    if score >= 90:
        return "Low"

    if score >= 75:
        return "Medium"

    if score >= 60:
        return "High"

    return "Critical"


def recommendation(defects):
    if len(defects) == 0:
        return (
            "No visible defects detected. Continue routine preventive maintenance."
        )

    rec = []

    if "rust" in defects:
        rec.append("Remove rust and apply anti-corrosion coating.")

    if "corrosion" in defects:
        rec.append("Inspect affected components and replace if necessary.")

    if "crack" in defects:
        rec.append("Immediately inspect structural integrity.")

    if "oil_leakage" in defects:
        rec.append("Repair leakage and inspect seals.")

    if "loose_bolt" in defects:
        rec.append("Tighten all loose fasteners.")

    if "damaged_belt" in defects:
        rec.append("Replace damaged belt.")

    if "missing_component" in defects:
        rec.append("Install missing component before operation.")

    if "surface_damage" in defects:
        rec.append("Monitor damaged surface during next inspection.")

    if len(rec) == 0:
        rec.append("Perform manual inspection.")

    return "\n".join(f"• {r}" for r in rec)