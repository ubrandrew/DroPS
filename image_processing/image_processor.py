import numpy as np
import cv2
from PIL import ImageGrab
from PIL import Image
import time
from ctypes import windll

def capture_img(res):
    user32 = windll.user32
    user32.SetProcessDPIAware()

    time.sleep(10)
    #takes screenshot
    img = ImageGrab.grab()

    #converts to np array for processing with opencv
    img_np = np.array(img)

    #display image
    # cv2.imshow("frame", img_np)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

def identify_edges():
    a = capture_img(None)
