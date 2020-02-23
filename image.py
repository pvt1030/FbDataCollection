import cv2
import numpy as np

# Get user supplied values
# cascPath = Path('J:\UOM\Education\sample\xml\haarcascade_frontalface_default.xml')

# Create the haar cascade
print("kell")
faceCascade =cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
# faceCascade = cv2.CascadeClassifier(cascPath)
print(faceCascade)

# Read the image
image = cv2.imread('abba.png')
gray_new = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(type(gray_new))

info = np.iinfo(gray_new.dtype) # Get the information of the incoming image type
gray_new = gray_new.astype(np.float64) / info.max # normalize the data to 0 - 1
gray_new = 255 * gray_new # Now scale by 255
gray = gray_new.astype(np.uint8)
cv2.imshow("Window", gray)
print(type(gray))

# Detect faces in the image
faces = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml").detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, flags=0, minSize = (30, 30))
# gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
# flags=cv2.cv.CV_HAAR_SCALE_IMAGE}\


answer = "Found {0} faces!"
print(answer.format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(0)