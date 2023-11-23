from ultralytics import YOLO
from PIL import Image
import cv2

model = YOLO("yolov8n.pt")

results = model.predict(source="0")
results = model.predict(source="folder", show=True)
results = model.predict(save=True)
results = model.predict(save=True, save_txt=True)
#results = model.predict(source=[im1, im2])