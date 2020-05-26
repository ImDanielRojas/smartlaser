#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 03:11:00 2020

@author: xange
"""

import os
from matplotlib import pyplot as plt
import numpy as np
import cv2
import checkout
import sys

def processing():
    
    print(sys.argv[1])
    lon=checkout.segmentation(str(sys.argv[1]))
    
    for i in range(lon):
        path="../data/images/segmented/segment{}.png".format(i)
        data=cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        cv2.imwrite('/data/images/input.png',data)
        
        print("Validating word-image with handwriting model...\n")
      
        os.system("python HTR.py")

if __name__ == '__main__':
	processing()



    
