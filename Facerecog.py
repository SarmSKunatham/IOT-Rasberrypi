import face_recognition
import cv2

FileLocation = "3.jpg"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# img = face_recognition.load_image_file(FileLocation)
face_location = face_recognition.face_locations(img)
print(face_location)
print("There are " + str(len(face_location)) + " people in this image.")

# ROI to opencv format location
x0 = face_location[0][3] # Left
y0 = face_location[0][0] # Top
x1 = face_location[0][1] # Bottom
y1 = face_location[0][2] # Right

img2 = cv2.imread(FileLocation)
cv2.rectangle(img2,(x0,y0),(x1,y1),(255,0,0),3)
cv2.imshow("Face Location Draw rectangle",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
