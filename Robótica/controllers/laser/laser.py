"""laser controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Supervisor
import numpy as np
import os

class Enumerate(object):
    def __init__(self, names):
        for number, name in enumerate(names.split()):
            setattr(self, name, number)



class Laser (Supervisor):
    timeStep = 128
    rotation = [-0.634826, -0.534825, -0.340446, 4]

    def boundSpeed(self, speed):
        return max(-self.maxSpeed, min(self.maxSpeed, speed))

    def __init__(self):
        super(Laser, self).__init__()
        self.robot = self.getFromDef('ROBOT1')
        self.board = self.getFromDef('BOARD')
        self.boardImageUrl = self.board.getField('imageUrl')
        self.translationField = self.robot.getField('rotation')
        self.coords = ''
        self.boardImageUrl.setMFString(0, "../textures/responses.jpg")
        
        
        self.keyboard.enable(Laser.timeStep)
        self.keyboard = self.getKeyboard()

    def run(self):
        self.displayHelp()
        f=open("../../../outputs/result.txt", "r")
        if f.mode == 'r':
            f1 = f.readlines()
            answer = f1[0].strip('\n')
            value = f1[1].strip('\n')
            coords = f1[2].strip('\n')
        if answer == "A" or answer=="a":
                print("The correct answer is A)", value)
                print("The coordinates of the answer are: ", coords)
                self.rotation = [-0.634826, -0.534825, -0.340446, 4]
                self.translationField.setSFRotation(self.rotation)
        if answer == "B" or answer=="b":
                print("The correct answer is B)", value)
                print("The coordinates of the answer are: ", coords)
                self.rotation = [-0.634826, -0.534825, -0.490446, 4]
                self.translationField.setSFRotation(self.rotation)
        if answer == "C" or answer=="c":
                print("The correct answer is C)", value)
                print("The coordinates of the answer are: ", coords)
                self.rotation = [-0.594826, -0.604825, -0.683446, 4]
                self.translationField.setSFRotation(self.rotation)
        if answer == "D" or answer=="d":
                print("The correct answer is D)", value)
                print("The coordinates of the answer are: ", coords)
                self.rotation = [-0.594826, -0.534825, -0.783446, 4]
                self.translationField.setSFRotation(self.rotation)
            
            
        # Main loop.
        while (Laser.timeStep != -1):
            k = self.keyboard.getKey()
            message = ''
            if k != -1:
                message = chr(k)
                if message.isnumeric() or message == '.' or message == ',':
                    self.coords += message
                    message = ''

            if k == ord('I'):
                message = ''
                self.displayHelp()
            """
            if k == ord('R'):
                message = 'Moving laser to the left top corner'
                self.rotation = [-0.634826, -0.324825, -0.840446, 4]
                self.translationField.setSFRotation(self.rotation)
            if k == ord('T'):
                message = 'Moving laser to the right top corner'
                self.rotation = [-0.634826, -0.324825, -0.840446, 4]
                self.translationField.setSFRotation(self.rotation)
            if k == ord('G'):
                message = 'Moving laser to the right bottom corner'
                self.rotation = [-1.104826, -0.414825, -0.840446, 4]
                self.translationField.setSFRotation(self.rotation)
            if k == ord('H'):
                message = 'Moving laser to the left bottom corner'
                self.rotation = [-1.254826, -0.534825, 0.150446, 4]
                self.translationField.setSFRotation(self.rotation)
            """
            if k == ord('A'):
                message = 'Moving laser to the left bottom corner'
                self.rotation = [-0.634826, -0.534825, -0.340446, 4]
                self.translationField.setSFRotation(self.rotation)
            if k == ord('B'):
                message = 'Moving laser to the left bottom corner'
                self.rotation = [-0.634826, -0.534825, -0.490446, 4]
                self.translationField.setSFRotation(self.rotation)
            if k == ord('C'):
                message = 'Moving laser to the left bottom corner'
                self.rotation = [-0.594826, -0.604825, -0.683446, 4]
                self.translationField.setSFRotation(self.rotation)
            if k == ord('D'):
                message = 'Moving laser to the left bottom corner'
                self.rotation = [-0.594826, -0.534825, -0.783446, 4]
                self.translationField.setSFRotation(self.rotation)
            
            # Erase last letter
            if k == 3:
                self.coords = self.coords[:-1]
                message = ''


            # If there are coordinates and enter key is pressed
            if self.coords != '' and k == 4:
                print('Going to coordinates: '+self.coords)
                targetCoords = self.coords.split(',')
                # If coordinates dont change just put the same old value
                x = float(targetCoords[0].strip()) if targetCoords[0] != '' else self.rotation[0] 
                y = float(targetCoords[1].strip()) if targetCoords[1] != '' else self.rotation[1] 
                z = float(targetCoords[2].strip()) if targetCoords[2] != '' else self.rotation[2] 
                self.rotation = [x, y, z, 4]
                self.translationField.setSFRotation(self.rotation)
                self.coords = ''
            elif message != '':
                print(message)
            elif self.coords != '' and k != -1:
                print('Coordinates: '+self.coords)
            
            # Step is required to update the robot state
            if self.step(self.timeStep) == -1:
                break

    def displayHelp(self):
        print(
            '\n'
            'Commands:\n'
            ' I for displaying the commands\n'
            ' A Point laser to answer A\n'  
            ' B Point laser to answer B\n'
            ' C Point laser to answer C\n'
            ' D Point laser to answer D\n'
            '-------------------------------------------------\n'     
            'HOW TO CHANGE COORDENATES IN THE FORMAT (X, Y, Z)\n'
            '-------------------------------------------------\n'
            'Press any number plus point comma separated, then press enter to change the coordinates.\n'    
            'You can press the backspace key in order to remove the last number, \',\' or \'.\'.'  
            '\n' 
        )

controller = Laser()
controller.run()