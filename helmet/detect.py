from ultralytics import YOLO

model = YOLO(

r"runs/detect/train-3/weights/best.pt"

)

results = model.predict(

source=r"datasets/helmet_dataset/images/val/evidence4.jpg",

save=True,

conf=0.4

)

print()

print("Helmet Detection Finished")