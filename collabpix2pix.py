import msa.utils
from msa.predictor import Predictor

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import cv2
import tensorflow as tf
import numpy as np
import params

img_in = cv2.imread("input/input.png", 1)
img_out = np.empty([])

width = 256
height = 256
dim = (width, height)
img_in = cv2.resize(img_in, dim, interpolation = cv2.INTER_AREA)

predictor = Predictor(json_path = './models/gart_canny_256.json')
img_predicted = predictor.predict(img_in)[0]
img_out = img_predicted

cv2.imwrite("output/output.png", cv2.cvtColor(img_out.astype('float32')*255, cv2.COLOR_RGB2BGR))

predictor = None