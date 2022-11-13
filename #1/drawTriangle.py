import numpy as np
import cv2

'''Pipeline:
1. Create canvas to draw on
2. Draw a triangle according to 3 points defined
3. Calculate the center point
4. Put text on the center point
'''

# Width and height of the background
W = 600
H = 600

# Black window of size W*H
img = np.zeros((H, W, 3), np.uint8)

# 3 vertices
p1 = (100, 300)
p2 = (500, 100)
p3 = (500, 500)

# Drawing triangle
cv2.line(img, p1, p2, (0, 0, 255), 2)
cv2.line(img, p2, p3, (0, 0, 255), 2)
cv2.line(img, p1, p3, (0, 0, 255), 2)

# Font
center = ((p1[0] + p2[0] + p3[0])//4, (p1[1] + p2[1] + p3[1])//3 )
font = cv2.FONT_HERSHEY_SIMPLEX
fontSize = 1
cv2.putText(img, "Homework 2", center , font, fontSize, (0, 0, 255), 2, cv2.LINE_AA)

# Show image
cv2.imshow("Triangle", img)
cv2.waitKey(0)
