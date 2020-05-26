# Smart Laser
A robot that points to the correct answer of a math word problem showed by a camera. The Computer Vision module will detect a paper hold by a person and will convert the frame to text using Optical Character Recognition. The text, including a math problem and four diffrent possible answers, will be sent to the Natural Language Processing module, which will translate the math word problem to a mathematical equation. This equation will then be solved and the result will be sent to the Robotics module that consists of a simulation of a laser pointer that will point to the correct answer out of the four.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need to install:
- Tensorflow
- Keras
- nltk (and some lines of code that are commented in NLPMathWordProblemSolver.py in the NLP Parsing approach folder)

## Architecture

This software is divided in three main modules.

![Software Achitecture diagram](smartlaserSoftwareArchitecture.jpeg)

### Natural Language Processing module

The NLP module consists of a hybrid model based on Deep Learning, Parsing and Naive Bayes techniques. We first started building a Recurrent Neural Network seq2seq model, built with a GRU Encoder, GRU Decoder and Bahdanau Attention. This model was tested with a broad number of datasets. However, the results were not as accurate as we desired. In order to support the lack of accuracy, we built another approach for the task. This approach consists in the parsing technique. The math word problem will be syntactically analyzed and will detect symbols and numbers from the text and build an equation to solve with the help of a Naive Bayes model classifier.

### Computer Vision module



### Laser Robotics Simulation module


## Testing

You can test this software with the math word problem set of examples in MathWordProblemsToTest.txt
If you want to test the NLP module by its own. You can do it by setting the smartLaserMODE variable to False in NLPMathWordProblemSolver.py and changing the access to the bag of words .txt to /{name_of_file}.txt
We invite you to test this software with some math word problem of your own!



## Authors

* **Daniel Rojas Pérez** - *NLP module* - [Github account](https://github.com/danielrojasperez)
* **Ange Xu** - *CV module* - [Github account](https://github.com/)
* **Marcos Muñoz González** - *Laser Robotics Simulation module* - [Github account](https://github.com/marcosmgz95)
* **Roger Piera** - *Laser Robotics Simulation module* - [Github account](https://github.com/RogerPiera)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


