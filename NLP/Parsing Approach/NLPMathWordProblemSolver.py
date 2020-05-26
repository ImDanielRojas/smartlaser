import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk.corpus import PlaintextCorpusReader
import random
from nltk import word_tokenize
import operator
import os

# make sure you have downloaded the next things
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')

ops = {'+': operator.add, '-': operator.sub, '*':operator.mul, '/':operator.truediv, '**':operator.pow}

bag_of_words = os.getcwd() + '/NLP/Parsing Approach/bag_of_words'
wordlists = PlaintextCorpusReader(bag_of_words, '.txt')

ignore_words = stopwords.words('english')
ignore_words.append('have')
ignore_words.append('had')
ignore_words.append('has')
ignore_words.append('owned')
ignore_words.append('owns')
ignore_words.append('was')
ignore_words.append('happen')
ignore_words.append('happened')
ignore_words.append('ask')
ignore_words.append('asked')
ignore_words.append('wonder')
ignore_words.append('wondering')




ignore_symbols = ['!', '.', ',', ';', ':', '?', '#']

number2word = {'0': 'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9': 'nine',
                '10':'ten', '11':'eleven', '12':'twelve', '13':'thirteen', '14':'fourteen', '15':'fifteen', '16':'sixteen',
                '17':'seventeen', '18':'eighteen', '19':'nineteen', '20':'twenty', '30':'thirty', '40':'fourty', '50':'fifty',
                '60':'sixty', '70':'seventy', '80':'eighty', '90':'ninety', '100':'hundred', '1000':'thousand'}




word2number = {value: key for (key, value) in number2word.items()}


def get_features(word):
    return {'first letter': word[0]}


def NaiveBayesClassifierModel():
    labeled_words = ([(word, 'addition')
                      for word in wordlists.words(os.getcwd() + '/NLP/Parsing Approach/bag_of_words/addition.txt')] +
                     [(word, 'subtraction')
                      for word in wordlists.words(os.getcwd() + '/NLP/Parsing Approach/bag_of_words/subtraction.txt')])
    random.shuffle(labeled_words)
    featuresets = [(get_features(n), operation)
                   for (n, operation) in labeled_words]

    classifier = nltk.NaiveBayesClassifier.train(featuresets)
    return classifier


def translate(sentence):
    equation = ''
    classifier = NaiveBayesClassifierModel()
    tokenized = word_tokenize(sentence)
    pos = nltk.pos_tag(tokenized)
    lastPos = ' '
    for i, (word, syntax) in enumerate(pos):
        
        # EXCEPTIONS
        if word == 'me' and (lastPos == 'give' or lastPos == 'gave') and equation[-1] == '-':
            equation = equation[:-1] + '+'
            
        if word == '(':
            equation += ' ' + '('
        if word == ')':
            equation += ' ' + ')'
            
            
        if word == 'half':
            if equation[-1] in ops.keys():
                equation = equation[:-1]
            equation += ' ' + '/' + ' ' + '2'
            
            
        # NUMBERS
        if (syntax == 'CD' or word in word2number.keys()):
            if(word in word2number.keys()):
                number = word2number[word]
            else:
                number = word
            
            if len(equation) > 0 and equation[-1] not in ops.keys(): # para que no haya 2 numeros juntos sin simbolo, puesto al haber quitado "and" de la bag of words
                equation += ' ' + '+'
            equation += ' ' + number
        # SYMBOLS
        elif word in wordlists.words(os.getcwd() + '/NLP/Parsing Approach/bag_of_words/addition.txt'):
            if len(equation) == 0 or equation[-1] not in ops.keys():
                equation += ' ' + '+'
        elif word in wordlists.words(os.getcwd() + '/NLP/Parsing Approach/bag_of_words/subtraction.txt'):
            if len(equation) == 0 or equation[-1] not in ops.keys():
                equation += ' ' + '-'
        elif word in wordlists.words(os.getcwd() + '/NLP/Parsing Approach/bag_of_words/product.txt'):
            if len(equation) == 0 or equation[-1] not in ops.keys():
                equation += ' ' + '*'
        elif word in wordlists.words(os.getcwd() + '/NLP/Parsing Approach/bag_of_words/division.txt'):
            if len(equation) == 0 or equation[-1] not in ops.keys():
                equation += ' ' + '/'
        elif word in wordlists.words(os.getcwd() + '/NLP/Parsing Approach/bag_of_words/exponentiation.txt'):
            if len(equation) == 0 or equation[-1] not in ops.keys():
                equation += ' ' + '**'
        elif ('V' in syntax and word not in ignore_words):
            if len(equation) == 0 or equation[-1] not in ops.keys():
                verb = word
                op = classifier.classify(get_features(verb))
                if (op == 'addition'):
                    equation += ' ' + '+'
                else:
                    equation += ' ' + '-'
        
        
        if word != ' ':
            lastPos = word
        
    if equation [-1] in ops.keys():
        equation = equation[:-1]
    
    
    
    return equation


def solve(equation):
    OPERATION = '+'
    equation_tokenized = word_tokenize(equation)
    answer = 0
    for part in equation_tokenized:
        try:
            if '/' in part:
                numerador = part.split('/')[0]
                denominador = part.split('/')[1]
                part = float(numerador) / float(denominador)
                
            num = float(part)
            answer = ops[OPERATION](answer, num)
            answer = round(answer, 2)
        except (ValueError):
            if (part == '**'):
                OPERATION = '**'
            elif (part == '/'):
                OPERATION = '/'
            elif (part == '*'):
                OPERATION = '*'
            elif (part == '-'):
                OPERATION = '-'
            else:
                OPERATION = '+'
            pass
    
    
    answer = round(eval(equation), 2)
    
    if str(answer)[-2:] == '.0':
        answer = int(answer)
        
        
    return answer




if __name__ == '__main__':
    
    smartLaserMODE = True
    
    if smartLaserMODE:
        f = open(os.getcwd() + "/outputs/problem.txt", "r")
        problem = f.read()
        print(problem)
    else:
        problem = input(
            "Math word problem: ")
        
    # MAIN CALLS
    equation = translate(problem)
    print(equation)
    answer = solve(equation)
    print('= {}'.format(answer))
    
    
    
    if smartLaserMODE:
        f = open(os.getcwd() + "/outputs/answer.txt","w+")
        f.write(str(answer))
        f.close()
    
    
    
    
    '''
    
     NORMAS PARA INTRODUCIR MATH PROBLEMS:
        - SOLAMENTE USAR UN VERBO CUANDO QUIERAS QUE ÉSTE SE UTILICE PARA PONER UN SÍMBOLO EN LA ECUACION
        - SI QUIERES QUE LAS OPERACIONES TENGAN CIERTO ORDEN, UTILIZA PARENTESIS EN EL PROBLEMA, SEPARADO POR ESPACIOS
    
     he quitado el "and" de la bag of words
     he quitado "more"
    
    
    '''
    
    