#pip install ultralytics

from ultralytics import YOLO

# Load a dataset
model = YOLO("yolov8n.yaml")  # build a new model from scratch

# train the model
results = model.train(data="config.yaml", epochs=1)