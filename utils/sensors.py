"""
SteelVision AI
Industrial Sensor Simulator
"""

import random


def get_sensor_data():

    temperature = random.randint(45, 90)
    vibration = round(random.uniform(1.0, 8.0), 1)
    pressure = round(random.uniform(3.5, 5.5), 1)
    rpm = random.randint(1400, 1500)
    current = round(random.uniform(10.0, 20.0), 1)
    voltage = random.randint(410, 420)

    return {
        "temperature": temperature,
        "vibration": vibration,
        "pressure": pressure,
        "rpm": rpm,
        "current": current,
        "voltage": voltage,
    }
