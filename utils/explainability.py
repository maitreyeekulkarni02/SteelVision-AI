"""
SteelVision AI
Explainable AI Engine
"""


def explain_prediction(health, defect_count, failure_probability):

    factors = []

    if health < 50:

        factors.append("Low machine health score (+35%)")

    elif health < 75:

        factors.append("Moderate health degradation (+20%)")

    if defect_count >= 3:

        factors.append("Multiple defects detected (+30%)")

    elif defect_count > 0:

        factors.append("Defect detected (+15%)")

    if failure_probability > 80:

        risk = "CRITICAL"

        reason = "Multiple mechanical degradation " "indicators detected."

    elif failure_probability > 50:

        risk = "WARNING"

        reason = "Early maintenance indicators detected."

    else:

        risk = "HEALTHY"

        reason = "Machine operating within safe limits."

    return {"factors": factors, "risk": risk, "reason": reason}
