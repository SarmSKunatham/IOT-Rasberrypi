# Lane Line Detection
'''
Pipeline: 
1. Gray scale
2. Blur with Gaussian filter
3. Canny edge detection
4. ROI masking
5. Hough transform to find lines
6. Draw Lines
'''
# Import libraries
import cv2 
import numpy as np
import matplotlib.pyplot as plt

# Functions 
# 1.
def grayscale(img):
    '''
    Convert BGR image to gray scale (1 channel)
    '''
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2.
def guassian_blur(img, kernel_size):
    '''
    Blur image with Gaussian filter
    '''
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

# 3.
def canny(img, low_threshold, high_threshold):
    '''
    Canny edge detection
    '''
    return cv2.Canny(img, low_threshold, high_threshold)

# 4.
def region_of_interest(img, vertices):
    '''
    ROI masking with a polygon shape formed from vertices
    '''
    # Create a mask with the same size as the image
    mask = np.zeros_like(img)

    # defining a 3 channel or 1 channel color to fill the mask with depending on the input image
    # 3 channels
    if len(img.shape) > 2:
        channel_count = img.shape[2] # 3 channels
        ignore_mask_color = (255, ) * channel_count # (255, 255, 255)
    # 1 channel
    else:
        ignore_mask_color = 255
    
    # Fill pixels inside the polygon defined by "vertices" with the fill color
    cv2.fillPoly(mask, vertices, ignore_mask_color)

    # Get the masked image -> returning masked pixels which are nonzero
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

# 5.
def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    '''
    Hough transform
    img should be the output of a canny transform
    '''
    # HT
    lines = cv2.HoughLinesP(img, rho, theta, threshold, minLineLength=min_line_len, maxLineGap=max_line_gap)
    draw_lines(img, lines)
    print("Drawed")
    # line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype="uint8") # canvas

# 6.
def draw_lines(img, lines, color=[255, 0, 0], thickness=10):
    '''
    Draw lines on the image
    '''
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), color, thickness)

def get_vertices(img):
    '''
    Get vertices for ROI masking
    '''
    rows, cols = img.shape[:2]
    bottom_left  = [cols*0.15, rows]
    top_left     = [cols*0.45, rows*0.6]
    bottom_right = [cols*0.95, rows]
    top_right    = [cols*0.55, rows*0.6] 
    
    ver = np.array([[bottom_left, top_left, top_right, bottom_right]], dtype=np.int32)
    return ver

# Main pipeline
def lane_finding_pipeline(img):
    '''
    Main pipeline
    '''
    # 1. Gray scale
    gray = grayscale(img)

    # 2. Blur with Gaussian filter
    kernel_size = 3
    blur_gray = guassian_blur(gray, kernel_size)

    # 3. Canny edge detection
    low_threshold = 50
    high_threshold = 150
    edges = canny(blur_gray, low_threshold, high_threshold)

    # 4. ROI masking
    vertices = get_vertices(edges)
    masked_img = region_of_interest(edges, vertices)

    # 5. Hough transform
    rho = 1
    theta = np.pi/180
    threshold = 15
    min_line_len = 40
    max_line_gap = 20
    hough_lines(masked_img, rho, theta, threshold, min_line_len, max_line_gap)
    
    return masked_img


# Test on images
fig = plt.figure(figsize=(20, 10))
image = cv2.imread('roadLane1.png')
ax = fig.add_subplot(1, 2, 1,xticks=[], yticks=[])
plt.imshow(image)
ax.set_title("Input Image")
ax = fig.add_subplot(1, 2, 2,xticks=[], yticks=[])
result = lane_finding_pipeline(image)
plt.imshow(result, cmap='gray')
ax.set_title("Output Image [Lane Line Detected]")
plt.show()
        



# def draw_lines(img, lines, color=[255, 0, 0], thickness=10):
#     '''
#     Draw lines on the image
#     '''
#     for line in lines:
#         for x1, y1, x2, y2 in line:
#             cv2.line(img, (x1, y1), (x2, y2), color, thickness)
