"""
@author: gcanco

Takes line sketch (input.png from input folder) and outputs painterly rendering (output.png into output folder)
"""

from msa.predictor import Predictor

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import cv2
import numpy as np

#read input
def run_pix2pix():
    img_in = cv2.imread("input/input.png", 1)
    img_out = np.empty([])

    #convert input to black and white 256x256px
    width = 256
    height = 256
    dim = (width, height)
    (thresh, bwimg_in) = cv2.threshold(img_in, 127, 255, cv2.THRESH_BINARY)
    finimg_in = cv2.resize(bwimg_in, dim, interpolation = cv2.INTER_AREA)

    #run model
    predictor = Predictor(json_path = './models/gart_canny_256.json')
    img_predicted = predictor.predict(finimg_in)[0]
    img_out = img_predicted

    #output correct color mapping
    cv2.imwrite("output/output.png", cv2.cvtColor(img_out.astype('float32')*255, cv2.COLOR_RGB2BGR))

    predictor = None
