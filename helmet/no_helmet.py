from ultralytics import YOLO


model=YOLO(

r"runs/detect/train-3/weights/best.pt"

)



results=model.predict(

source="datasets/helmet_dataset/images/val/evidence4.jpg",

conf=0.4

)




for r in results:


    helmet_count=0

    head_count=0



    for cls in r.boxes.cls:


        cls=int(cls)



        if cls==0:

            helmet_count+=1



        elif cls==2:


            head_count+=1




    print()


    print("Helmets :",helmet_count)

    print("Heads :",head_count)




    if head_count>helmet_count:


        print()


        print("🚨 NO HELMET VIOLATION")



    else:


        print()


        print()


        print("✅ HELMET PRESENT")