#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytesseract
import os
from matplotlib import pyplot as plt
import numpy as np
import cv2
from PIL import Image
from difflib import SequenceMatcher
import sys


def main():
    
    im = Image.open("CV/img/questionImage.png")
    
    img=cv2.imread("CV/img/questionImage.png")
    cv2.imshow("Question",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #print("Recognizing text...\n")
    texto = pytesseract.image_to_string(im)
    
    #print(texto)
    
    problema=""
    for i in range(len(texto)):
        if texto[i]=='a' and texto[i+1]==')':
            break
        else:
            if texto[i]=='\n':
                problema+=" "
            else:
                problema+=texto[i] 

    
    f = open("outputs/problem.txt", "w")
    f.write(problema)
    f.close()
    
if __name__ == '__main__':
	main()
    


