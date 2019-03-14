#!flask/bin/python
from flask import Flask
import numpy as np
import cv2
from PIL import ImageGrab
import time
from ctypes import windll
import datetime


app = Flask(__name__)

@app.route('/temp', methods=['GET'])
def index():
    start = datetime.datetime.now()
    user32 = windll.user32
    user32.SetProcessDPIAware()

    time.sleep(1)
    #takes screenshot
    img = ImageGrab.grab()

    #converts to np array for processing with opencv
    img_np = np.array(img)

    #display image
    cv2.imwrite("test.png", img_np)
    end = datetime.datetime.now()
    print(str(end-start))

    return "HI SEONG"


if __name__ == '__main__':
    app.run(debug=True)