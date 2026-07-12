import os
from PIL import Image
from ultralytics import YOLO


# --------------------------------------------------
# MODEL PATH
# --------------------------------------------------

MODEL_PATH = "models/yolov8n.pt"


# --------------------------------------------------
# LOAD YOLO MODEL
# --------------------------------------------------

if not os.path.exists(MODEL_PATH):

    MODEL_PATH = "yolov8n.pt"


model = YOLO(MODEL_PATH)



# --------------------------------------------------
# DEFECT DETECTION FUNCTION
# --------------------------------------------------

def detect_defects(image):

    """
    Runs YOLO inference on uploaded machine image.

    Returns:

    {
        image: annotated image,
        defects: [
            {
                name:"",
                confidence:""
            }
        ]
    }

    """

    results = model(image)


    defects = []


    annotated_image = image.copy()



    for result in results:


        annotated_image = result.plot()


        boxes = result.boxes


        for box in boxes:


            confidence = float(
                box.conf[0]
            )


            class_id = int(
                box.cls[0]
            )


            class_name = model.names[class_id]


            defects.append(
                {
                    "name": class_name,
                    "confidence": confidence
                }
            )



    return {

        "image": annotated_image,

        "defects": defects

    }