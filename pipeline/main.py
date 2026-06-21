import easyocr
import cv2
import sqlite3
from ultralytics import YOLO
from datetime import datetime


#########################################
# Severity Engine
#########################################

def severity_score():

    speed = 50
    pedestrians = 5
    school_zone = True
    night_time = False

    score = 0

    score += speed * 0.4
    score += pedestrians * 8

    if school_zone:
        score += 30

    if night_time:
        score -= 10

    return min(score,100)



#########################################
# Helmet Detection
#########################################

helmet_model = YOLO(

r"runs/detect/train-3/weights/best.pt"

)


helmet_results = helmet_model.predict(

source="datasets/helmet_dataset/images/val/000006.jpg",

conf=0.4

)



helmet_count = 0
head_count = 0


for r in helmet_results:


    for cls in r.boxes.cls:


        cls = int(cls)


        if cls == 0:

            helmet_count += 1


        elif cls == 2:


            head_count += 1



print()

print("Helmet Analysis")

print("----------------")


print("Helmets :",helmet_count)

print("Heads :",head_count)



if head_count > helmet_count:


    violation = "No Helmet"



    print()

    print("🚨 No Helmet Violation")


else:


    violation = "Helmet Present"



    print()

    print("✅ Helmet Present")



#########################################
# OCR Initialization
#########################################

reader = easyocr.Reader(['en'])



#########################################
# Database Connection
#########################################

conn = sqlite3.connect(

"violations.db"

)

cur = conn.cursor()



#########################################
# Read Image
#########################################

image_path = "sample_images/car.jpg"


image = cv2.imread(

image_path

)


result = reader.readtext(

image_path

)



#########################################
# OCR Processing
#########################################

for item in result:


    bbox,text,conf = item


    severity = severity_score()


    timestamp = datetime.now()



    if severity > 80:

        action = "Immediate Enforcement"



    elif severity > 50:


        action = "Medium Priority"



    else:


        action = "Low Priority"




    print()


    print("Violation Explanation")


    print("-----------------------")


    print("Plate :",text)


    print("OCR Confidence :",conf)


    print("Severity :",severity)


    print("Action :",action)


    print("Helmet Status :",violation)


    print("Timestamp :",timestamp)




#########################################
# Database Insert
#########################################


    cur.execute(

'''

INSERT INTO violations(

plate,

severity,

confidence,

timestamp,

action,

image_path

)

VALUES(?,?,?,?,?,?)

'''

,


(

text,

severity,

float(conf),

str(timestamp),

action,

"output/final_evidence.jpg"

)

)


    conn.commit()



#########################################
# Draw Bounding Box
#########################################


    x1 = int(

bbox[0][0]

)

    y1 = int(

bbox[0][1]

)


    x2 = int(

bbox[2][0]

)

    y2 = int(

bbox[2][1]

)



    cv2.rectangle(

image,

(x1,y1),

(x2,y2),

(0,255,0),

2

)



    cv2.putText(

image,

text,

(x1,y1-10),

cv2.FONT_HERSHEY_SIMPLEX,

0.8,

(0,255,0),

2

)



#########################################
# Save Evidence
#########################################

cv2.imwrite(

"output/final_evidence.jpg",

image

)



print()

print("Evidence Generated Successfully")



#########################################
# Close Database
#########################################

conn.close()