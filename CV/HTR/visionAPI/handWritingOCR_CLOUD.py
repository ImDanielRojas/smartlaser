# -*- coding: utf-8 -*-
"""
Created on Fri May 22 01:38:43 2020

@author: xange
"""
import os, io
from google.cloud import vision
from google.cloud.vision import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'vision.json'

client = vision.ImageAnnotatorClient()


def detect_document(path):
        """Detects document features in an image."""
        client = vision.ImageAnnotatorClient()

        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = vision.types.Image(content=content)

        response = client.document_text_detection(image=image)

   

        if response.error.message:
            raise Exception(
                '{}\nFor more info on error messages, check: '
                'https://cloud.google.com/apis/design/errors'.format(
                    response.error.message))
            
        f = open("result_API.txt", "w")
        print(response.full_text_annotation.text)
        f.write(response.full_text_annotation.text)
        f.close()

detect_document("/img/p2.jpg")