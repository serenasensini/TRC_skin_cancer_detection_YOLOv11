from ultralytics import YOLO

from roboflow import Roboflow
rf = Roboflow(api_key="xyz")
project = rf.workspace("surawiwat-school-suranaree-university-of-technology").project("skin_cancer_detection-v2")
version = project.version(8)
dataset = version.download("yolov8")

# Load a model
model = YOLO("yolo11n.yaml")

# Train the model
results = model.train(data="SKIN_CANCER_DETECTION-V2-8/data.yaml",
                      epochs=100, imgsz=640,
                      optimizer="adam", lr0=0.01)