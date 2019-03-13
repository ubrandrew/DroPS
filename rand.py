import cv2
import numpy as np
from ctypes import windll
import math

## currently unused
def pol_to_cart(pol):
    x = pol[0] * math.cos(math.degrees(pol[1]))
    y = pol[0] * math.sin(math.degrees(pol[1]))
    return (x,y)

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

# Remove contours that are too small
for cnt in contours:
    if cv2.contourArea(cnt) < 150:
        contours.remove(cnt)

print(len(contours))




cv2.drawContours(gray_copy, contours, -1, (0,255,0), 1) # Draw contour lines on grap_copy


cv2.imshow('Result', gray_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()
