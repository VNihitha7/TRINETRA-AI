import easyocr
import cv2
from datetime import datetime

reader = easyocr.Reader(['en'])

image_path = 'sample_images/car1.jpg'

image = cv2.imread(image_path)

result = reader.readtext(image_path)

for item in result:

    bbox,text,conf = item

    x1 = int(bbox[0][0])
    y1 = int(bbox[0][1])

    x2 = int(bbox[2][0])
    y2 = int(bbox[2][1])


    cv2.rectangle(image,
                  (x1,y1),
                  (x2,y2),
                  (0,255,0),
                  2)


    cv2.putText(image,
                text,
                (x1,y1-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0,255,0),
                2)


    print("Plate :",text)
    print("Confidence :",conf)


timestamp = datetime.now()


print("Timestamp :",timestamp)



cv2.imwrite("output/evidence.jpg",image)

print("Evidence Generated Successfully")