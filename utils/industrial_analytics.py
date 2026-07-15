"""
SteelVision AI
Industrial Analytics Engine
"""

from utils.history import get_history


def defect_statistics():

    data = get_history()

    if data.empty:

        return {}

    stats = {}

    for defects in data["defects"]:

        for defect in str(defects).split(","):

            defect = defect.strip()

            if defect:

                stats[defect] = stats.get(defect, 0) + 1

    return stats


def health_history(machine_id=None):

    data = get_history()

    if data.empty:

        return data

    if machine_id:

        data = data[data["machine_id"] == machine_id]

    return data[["inspection_date", "health_score"]]


def recent_activity():

    data = get_history()

    if data.empty:

        return []

    activities = []

    for _, row in data.tail(5).iterrows():

        activities.append(f'{row["inspection_date"]} - ' f'{row["defects"]} detected')

    return activities
