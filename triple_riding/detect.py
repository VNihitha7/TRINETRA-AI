from ultralytics import YOLO


model = YOLO("yolov8n.pt")


results = model.predict(

source="datasets/helmet_dataset/images/val/evidence4.jpg",

save=True

)



for r in results:


    bike = 0

    person = 0


    for c in r.boxes.cls:


        cls = int(c)


        if cls == 3:

            bike += 1


        if cls == 0:

            person += 1



    print()


    print("Bikes :", bike)


    print("Persons :", person)



    if bike > 0 and person >= 3:


        print("Violation : Triple Riding")


    else:


        print("No Triple Riding")