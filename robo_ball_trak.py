# Before you run the Python code snippet below, run the following command:
# pip install roboflow autodistill autodistill_grounding_dino pip install scikit-learn

from autodistill_grounding_dino import GroundingDINO
from autodistill.detection import CaptionOntology
from autodistill.helpers import sync_with_roboflow
import cv2
import numpy as np
BOX_THRESHOLD = 0.3
CAPTION_ONTOLOGY = {
    "round ball of sports": "soccer_ball",
    "soccer player": "soccer_player"
}
TEXT_THRESHOLD = 0.70

model = GroundingDINO(
    ontology=CaptionOntology(CAPTION_ONTOLOGY),
    box_threshold=BOX_THRESHOLD,
    text_threshold=TEXT_THRESHOLD
)

sync_with_roboflow(
    workspace_id="VdcxoRO4eOTM9CmpgXKBCRimh403",
    workspace_url="train-the-yolo-with-my-own-dataset",
    project_id = "soccer_track",
    batch_id = "hBPv0KQzutoT9WdZkGny",
    model = model
)

input_image = cv2.imread(("output/80.jpg"))
# print(input_image.shape)
input_image_resize = cv2.resize(input_image, (1457, 517))
# cv2.imshow("resized", input_image_resize)
# cv2.imwrite("result.png", input_image_resize)
image = np.asarray(input_image_resize)
results = model.predict(image)

print(results)