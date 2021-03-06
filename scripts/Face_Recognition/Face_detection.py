import cv2
import os

file = "haarcascade_frontalface_default.xml"
haar = cv2.CascadeClassifier(file)
cam = cv2.VideoCapture(0)
dataset = "datasets"
name = "avi"

path = os.path.join(dataset,name)
if not os.path.isdir(path):
    os.mkdir(path)

(width,height) = (130,100)
count = 1

while (count < 50):
    _,img = cam.read()
    print(count)
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = haar.detectMultiScale(grayImg,1.3,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        onlyface = grayImg[y:y+h,x:x+w]
        resizeImg = cv2.resize(onlyface,(width,height))
        cv2.imwrite("%s/%s.jpg"%(path,count),resizeImg)
        count+=1
    cv2.imshow("Face Detection",img)
    key = cv2.waitKey(10)
    if key == 27:
        break
print("Faces captured")
cam.release()
cv2.destroyAllWindows()
