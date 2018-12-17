import numpy as np
import cv2
from PIL import ImageGrab

#takes screenshot
img = ImageGrab.grab()

#converts to np array for processing with opencv
img_np = np.array(img)

#display image
cv2.imshow("frame", img_np)
cv2.waitKey(0)
cv2.destroyAllWindows()
