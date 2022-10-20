import numpy as np
import cv2 
import matplotlib.pyplot as plt

# Original image
img = cv2.imread("ex3.jpg")
# plt.imshow(img); plt.title("Original"); plt.show()

# Blur image
blur = cv2.medianBlur(img, 11)
# plt.imshow(blur);plt.title("Blur");plt.show()

# Binarization -> Otsu
gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU) 
# plt.imshow(thresh, cmap="gray");plt.title("Thresholded"); plt.show()

# Opening to remove noise
kernel = np.ones((3,3), dtype="uint8")
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel,   iterations=2)
# plt.imshow(opening, cmap="gray");plt.title("Opening"); plt.show()

# Closing to fill the hole
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations= 2)
# plt.imshow(closing, cmap="gray"); plt.title("closing"); plt.show()

# Dilate -> sure background area
sure_bg = cv2.dilate(closing, kernel, iterations=2)
# plt.imshow(sure_bg, cmap="gray"); plt.title("sure bg"); plt.show()

# # Erosion -> sure foreground area
# sure_fg = cv2.erode(closing, kernel, iterations=2)
# plt.imshow(sure_fg, cmap="gray"); plt.title("sure fg"); plt.show()
# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
# plt.imshow(dist_transform, cmap="gray"); plt.title("Distance transform");plt.show()
_, sure_fg = cv2.threshold(dist_transform, 0.5*dist_transform.max(), 255, 0)
# plt.imshow(sure_fg, cmap="gray");plt.title("Distance transform threshold > 0.5 of max value");plt.show()
sure_fg = np.uint8(sure_fg)

# Unknown region -> boundary
unknown = cv2.subtract(sure_bg, sure_fg)
# plt.imshow(unknown, cmap="gray");plt.title("Unknown"); plt.show()

# Marker labelling
_, markers = cv2.connectedComponents(sure_fg)

# Add 1 to all labels so the bg is not 0 but 1
markers += 1

# Mark the region of unknown with zero
markers[unknown==255] = 0

# print(markers)
# plt.imshow(markers, cmap="jet"); plt.title("Markers Labelled"); plt.show()

# Apply watershed
markers = cv2.watershed(img, markers)
# boundary
img[markers==-1] = [255, 0, 0]

# plt.imshow(markers, cmap="jet"); plt.title("Markers"); plt.show()
# Total number of coins
print("Total number of coins: ", np.max(markers) - 1)
# plt.imshow(img); plt.title("result"); plt.show()
cv2.putText(img, "Total number of coins: " + str(np.max(markers) - 1), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
cv2.imshow("Result", img)
cv2.waitKey(0)
