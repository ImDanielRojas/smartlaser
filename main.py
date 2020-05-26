# -*- coding: utf-8 -*-


# QUITAMOS INFERENCIA DE MODELO DEEP LEARNING PARA QUE NO TARDE TANTO EN EJECUTAR, ADEMÁS, TENDRIAMOS QUE TRAERNOS TODAS LAS FUNCIONES DEL NOTEBOOK.
# PARA TESTEAR EL MODELO RNN, MEJOR EJECUTAR EL NOTEBOOK.
'''
import tensorflow as tf
import json
from pprint import pprint


with open('/Deep Learning Approach/SmartLaser.ipynb', 'r') as content_file:
    content = content_file.read()

data=json.loads(content)
data["cells"][:]["source"][0]

checkpoint = tf.train.Checkpoint()


sentence = 'sara had 100.0 pennies and n1 quarters in her bank . her dad borrowed n2 quarters from sara . how many quarters does she have now ?'
#sentence = 'what is 100 plus 100'
checkpoint.restore(tf.train.latest_checkpoint('./Deep Learning Approach/training_checkpoints'))
result, sentence = val(sentence.split(' '))
print(' '.join(sentence))
print('Equation predicted: ', ''.join(seq2text(result, targ_lang_index2word)[:-1]))
'''


import os

exec(open("./CV/OCR/basicOCR.py", encoding='utf-8').read())
exec(open("./NLP/Parsing Approach/NLPMathWordProblemSolver.py", encoding='utf-8').read())

f = open("./outputs/answer.txt", "r")
answer=f.read()

os.system('python ./CV/localizeCorrectAnswer.py {}'.format(answer))

