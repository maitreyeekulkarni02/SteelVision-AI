"""
SteelVision AI
Analytics Intelligence Module

Responsible for:
- Defect severity analysis
- Inspection summary generation
- Confidence analytics
"""


from datetime import datetime



# --------------------------------------------------
# DEFECT SEVERITY ANALYSIS
# --------------------------------------------------

def calculate_defect_severity(defect):

    """
    Determines severity based on
    defect type and confidence.
    """


    name = defect["name"].lower()

    confidence = defect["confidence"]



    critical_defects = [

        "crack",
        "oil",
        "leak",
        "missing",
        "damage"

    ]



    high_risk_defects = [

        "corrosion",
        "rust"

    ]



    if any(
        item in name
        for item in critical_defects
    ):


        severity = "Critical"



    elif any(
        item in name
        for item in high_risk_defects
    ):


        severity = "High"



    elif confidence > 0.85:


        severity = "Medium"



    else:


        severity = "Low"



    return severity





# --------------------------------------------------
# CONFIDENCE ANALYTICS
# --------------------------------------------------

def get_confidence_data(defects):

    """
    Creates chart-ready data.
    """


    data = []


    for defect in defects:


        data.append(

            {
                "Defect":
                defect["name"],


                "Confidence":
                round(
                    defect["confidence"] * 100,
                    2
                )
            }

        )


    return data





# --------------------------------------------------
# INSPECTION SUMMARY
# --------------------------------------------------

def generate_inspection_summary(
        defects,
        health_score,
        status,
        priority
):


    """
    Generates industrial inspection summary.
    """



    summary = {


        "Inspection Time":
        datetime.now().strftime(
            "%d-%m-%Y %H:%M"
        ),


        "AI Model":
        "YOLOv8 Edge Vision Model",


        "Inspection Mode":
        "Computer Vision Analysis",


        "Detected Defects":
        len(defects),


        "Health Score":
        f"{health_score}%",


        "Machine Status":
        status,


        "Maintenance Priority":
        priority

    }



    return summary