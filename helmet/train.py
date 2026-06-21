from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(

    data="datasets/helmet_dataset/images/val/evidence4.jpg",

    epochs=3,

    imgsz=320,

    batch=2,

    workers=0,

    device="cpu",

    cache=False

)