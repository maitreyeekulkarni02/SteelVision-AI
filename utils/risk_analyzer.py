"""
SteelVision AI
Machine Risk Analyzer
"""

from utils.history import get_history
from utils.machine_manager import get_machines


def get_highest_risk_machine():

    machines = get_machines()

    if not machines:

        return {"machine": "No machines", "health": 0, "defects": 0}

    # lowest health machine

    machine = sorted(machines, key=lambda x: x.current_health)[0]

    defect_count = 0

    history = get_history()

    if hasattr(history, "iterrows"):

        for _, row in history.iterrows():

            if str(row["machine_id"]) == str(machine.machine_id):

                defect_count += int(row["defect_count"])

    return {
        "machine": machine.machine_id,
        "health": machine.current_health,
        "defects": defect_count,
    }
