import numpy as np
import cv2
from PIL import ImageGrab

img = ImageGrab.grab()
img_np = np.array(img)

cv2.imshow("frame", img_np)
cv2.waitKey(0)
cv2.destroyAllWindows()
