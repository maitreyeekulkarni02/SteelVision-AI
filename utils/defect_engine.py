"""
SteelVision AI
Industrial Defect Intelligence Engine

Converts computer vision detections
into manufacturing defect insights.
"""

import random

# --------------------------------------------------
# INDUSTRIAL DEFECT DATABASE
# --------------------------------------------------

DEFECT_TYPES = [
    {"name": "Rust", "severity": "Medium"},
    {"name": "Crack", "severity": "Critical"},
    {"name": "Oil Leakage", "severity": "High"},
    {"name": "Corrosion", "severity": "High"},
    {"name": "Loose Bolt", "severity": "Medium"},
    {"name": "Damaged Belt", "severity": "High"},
    {"name": "Missing Component", "severity": "Critical"},
    {"name": "Surface Damage", "severity": "Medium"},
]


# --------------------------------------------------
# INDUSTRIAL DEFECT SIMULATION
# --------------------------------------------------


def generate_industrial_defects(yolo_results):
    """
    Converts YOLO output into
    industrial inspection results.

    Future:
    Replace this with custom YOLO model.
    """

    defects = []

    # If YOLO detects something,
    # simulate industrial analysis

    if len(yolo_results) > 0:

        count = random.randint(1, 3)

        selected = random.sample(DEFECT_TYPES, count)

        for item in selected:

            defects.append(
                {
                    "name": item["name"],
                    "confidence": round(random.uniform(0.80, 0.98), 2),
                    "severity": item["severity"],
                }
            )

    return defects
