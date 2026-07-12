"""
SteelVision AI
Edge Camera Inspection Module

Simulates real-time industrial camera input.
"""

import cv2
from PIL import Image


def get_camera_frame():

    """
    Captures frame from local camera.

    Returns:
        PIL Image frame
    """


    camera = cv2.VideoCapture(0)


    if not camera.isOpened():

        return None



    success, frame = camera.read()


    camera.release()



    if not success:

        return None



    frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )


    return Image.fromarray(frame)