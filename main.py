#pip install ultralytics

from ultralytics import YOLO

# Load a dataset
model = YOLO("yolov8n.pt")

# train the model
results = model.train(data="config.yaml", epochs=1)