import cv2
import os
cam = cv2.VideoCapture(0) #switching on the camera
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height
#Classifier used to detect face is called
face_detector =
cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# For each person, enter one numeric face id
face_id = input('\n enter user id and press <return> ==> ')
print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
count = 0
while(True):
    ret, img = cam.read() #if frame is read correctly,True is returned
    #converts the given input image into a gray image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #detects objects of given scale factor and neighbors
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        #a rectangle is drawn around the detected face
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        count += 1 #incrementing the count value
        # Save the captured image into the datasets folder
        cv2.imwrite("C:/Users/R Rohith Reddy/Desktop/New folder/Captured
        Photos/face" + str(face_id)+ str(count) + ".jpg", gray[y:y+h,x:x+w])
        #to display the image
        cv2.imshow('image', img)
    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 30: # Take 30 face samples and stop video
        break
# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
