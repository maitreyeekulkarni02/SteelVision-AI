"""
SteelVision AI
Predictive Maintenance Engine
"""


def predict_failure(health, defect_count):

    if health >= 90:
        probability = 5

    elif health >= 80:
        probability = 15

    elif health >= 70:
        probability = 30

    elif health >= 60:
        probability = 45

    elif health >= 50:
        probability = 60

    elif health >= 40:
        probability = 75

    else:
        probability = 90

    probability += defect_count * 2

    probability = min(probability, 99)

    if probability < 25:

        priority = "Low"

        risk = "LOW"

        cost = 2500

    elif probability < 50:

        priority = "Medium"

        risk = "MEDIUM"

        cost = 6500

    elif probability < 75:

        priority = "High"

        risk = "HIGH"

        cost = 12000

    else:

        priority = "Immediate"

        risk = "CRITICAL"

        cost = 18500

    return {
        "failure_probability": probability,
        "priority": priority,
        "risk": risk,
        "estimated_cost": cost,
        "remaining_life": 100 - probability,
    }
