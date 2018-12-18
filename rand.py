import cv2
import numpy as np
from ctypes import windll
import math

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

gray = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,100,200,apertureSize = 3)

lines = cv2.HoughLines(edges, 1, np.pi/180, 13, 2)
print(len(lines))

for line in lines:
    line = line[0]# rho, theta = line[0]
    x1, y1 = pol_to_cart(line[0])
    x2, y2 = pol_to_cart(line[1])
    print(line[1])
    # cv2.line(img, (line[0],line[1]), (line[2], line[3]), [255,255,255], 3)

cv2.imshow('Result',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

#
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(gray,50,150,apertureSize = 3)
