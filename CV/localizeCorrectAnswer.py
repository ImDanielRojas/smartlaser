#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:03:53 2020

@author: xange
"""

import pytesseract
import os
from matplotlib import pyplot as plt
import numpy as np
import cv2
from PIL import Image
from difflib import SequenceMatcher
import sys

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def localizeCorrectAnswer(target):
    
    
    # Text segmentation 
    rgb = cv2.imread("CV/img/questionImage.png")
    
    small = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
    
    #threshold the image
    _, bw = cv2.threshold(small, 0.0, 255.0, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    
    # get horizontal mask of large size since text are horizontal components
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 5))
    connected = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel)
    
    # find all the contours
    _, contours, hierarchy,=cv2.findContours(connected.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    
    #cv2.imshow("question",rgb)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    
    
    x1=0
    y1=0
    w1=0
    h1=0
    maximSimility=0
    respuesta=""
    
    print("\n-------------- Locating the correct answer in image --------------\n")
    
    text=""
    for i in range(len(contours)):
        x, y, w, h = cv2.boundingRect(contours[i])
    
        cv2.imwrite("CV/img/p.jpg",rgb[y-8:y+h+8,x-8:x+w+8])
    
        try:
            im = Image.open("CV/img/p.jpg")
            
            text = pytesseract.image_to_string(im)
        except:
            pass
        simility=similar(target,text)
        if  simility> maximSimility:
            x1,y1,w1,h1= x, y, w, h 
            maximSimility=simility
            respuesta=text
    
    colour2 = (0,0,255)
    cv2.rectangle(rgb, (x1, y1), (x1+w1, y1+h1), (colour2),3)
    cv2.imshow("Correct answer",rgb)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
	
    respuesta=[i for i in respuesta if i !=' ']
    print(''.join(respuesta))
    f = open("outputs/result.txt", "w")
    f.write(respuesta[0]+"\n")
    f.write(''.join(respuesta[2:])+"\n")
    f.write(str(x1+5)+" ")
    f.write(str(y1+5)+" ")
    
    f.close()
    
    print("\n---------------------------- Finished ----------------------------")
	
if __name__ == '__main__':
    
	localizeCorrectAnswer(str(sys.argv[1]))

