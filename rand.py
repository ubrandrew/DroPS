import cv2
import numpy as np
from ctypes import windll
import math

## currently unused
def pol_to_cart(pol):
    x = pol[0] * math.cos(math.degrees(pol[1]))
    y = pol[0] * math.sin(math.degrees(pol[1]))
    return (x,y)

# 0. match contour with moment
# 1. Calculate centroid of contour
# 2. Find line splitting rectangle in half (bisect shorter side)
# 3. If centroid is on one side, direction is positive. If centroid is on the other, direction is negative.
def process_moments(moments, contours, img):
    # for mmt in moments:
    #     for cnt in contours:
             
        #map index of moments to index of contours


    for mmt in moments:
        cX = int(mmt["m10"] / mmt["m00"])
        cY = int(mmt["m01"] / mmt["m00"])
       
        cv2.circle(img, (cX, cY), 2, (0, 0, 255), -1)

    cv2.imshow('Result', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 

user32 = windll.user32
user32.SetProcessDPIAware()
img = cv2.imread('arrows.PNG')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


# hue sat value
lower = np.array([85,245,245])  #-- Lower range --
upper = np.array([95,255,255])  #-- Upper range --

mask = cv2.inRange(hsv, lower, upper)

res = cv2.bitwise_and(img, img, mask= mask)  #-- Contains pixels having the gray color--


gray = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY) # Convert to grayscle, single channel
gray_copy = gray.copy()
edges = cv2.Canny(gray,100,200,apertureSize = 3) # Edge detection--unused var
lines = cv2.HoughLines(edges, 1, np.pi/180, 13, 2) # Lines from edges--unused var

im2, contours, hierarchy = cv2.findContours(gray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
gray_copy = cv2.cvtColor(gray_copy,cv2.COLOR_GRAY2RGB) # Convert grayscale image to RGB to allow colored contour lines

# Contour Processing
moments = []

for cnt in contours:
    if cv2.contourArea(cnt) < 150: # Use symbolic constant
        contours.remove(cnt)
    else:
        rect = cv2.minAreaRect(cnt)
        print(f"Rect: {rect}")
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(gray_copy, [box], -1, (0,255,0), 1)
        print(box)
        moments.append(cv2.moments(cnt))

print(len(contours))
print(len(moments))

process_moments(moments, contours, gray_copy)

       

#cv2.drawContours(gray_copy, contours, -1, (0,255,0), 1) # Draw contour lines on grap_copy

# Fit rotated rectanlges around contours



# cv2.imshow('Result', gray_copy)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
