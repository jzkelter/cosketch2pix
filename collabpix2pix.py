#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: memo

Main app
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np
import time

import params
import gui

import msa.utils
from msa.capturer import Capturer
from msa.predictor import Predictor
from msa.framestats import FrameStats

import cv2
import tensorflow as tf

import os

def run_pix2pix():
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

    img_in = cv2.imread("input/input.png", 1)

    width = 256
    height = 256
    dim = (width, height)
    img_in = cv2.resize(img_in, dim, interpolation=cv2.INTER_AREA)

    predictor = Predictor(json_path = './models/gart_canny_256.json')
    img_out = predictor.predict(img_in)[0]

    cv2.imwrite("output/output.png", 255*img_out)

    predictor = None
