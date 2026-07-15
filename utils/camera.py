import cv2
from PIL import Image


def get_camera_frame():

    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        return None

    ret, frame = camera.read()

    camera.release()

    if ret:

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        return Image.fromarray(frame)

    return None


def get_video_capture():

    camera = cv2.VideoCapture(0)

    return camera
