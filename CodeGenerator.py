
import math
import time
import pygame as pg
import tkinter as tk
from tkinter.filedialog import askopenfilename

tk.Tk().withdraw() # Says that you won't be using many tkinter functions

class CodeGenerator(): # In Constructor: File Path, Bot Starting X, Y, and Rotation

    isDriverRoute = False # False means

    x = 100
    y = 100

    lastLocations = [] # Array of last pixel X and pixel Y for rendering

    botWidth = 0
    botLength = 0

    fieldRectangle = pg.Rect(1,1,1,1)

    mainSurfaceArg = pg.Surface((0,0))

    botStartingRotation = 0

    lineWidth = 5

    lineDefaultColor = (72,209,204)
    reverseColor = (235, 252, 252)

    Action1 = (90, 34, 224)
    Action2 = (11, 127, 222)
    Action3 = (176, 11, 222)
    Action4 = (147, 191, 237)
    Action5 = (245, 226, 22)
    Action6 = (245, 122, 22)

    currentColor = lineDefaultColor

    projectPath = ""

    code = ""     # If Auton, write 0 at the start, if Driver write 1 at the start

    ##########   Format   ##########

    # { X, Y, Theta, Action Code } #

    ################################

    def __init__(self, mainSurfaceArg, width, length, fieldRect, startingRotRad, isDriverArg):

        self.mainSurfaceArg = mainSurfaceArg

        self.botWidth = width
        self.botLength = length

        self.botStartingRotation = startingRotRad

        self.isDriverRoute = isDriverArg

        self.fieldRectangle = fieldRect

        # Tells UvuvLib whether this is auton or driver
        if isDriverArg:
            self.code += '1' 
        else:
            self.code += '0'
        

        print("w")


    #######   Action Codes   #######

    # Inputted by the end user with 
    # function pointers. 6 possible.
    
    # 1 = 1st Opt: Scored Gamepiece
    # 2 = 2nd Opt: Descored Gamepiece
    # 3 = 3rd Opt: Action
    # 4 = 4th Opt: Action
    # 5 = 5th Opt: Action
    # 6 = 6th Opt: Action

    ################################


    def score():
        
        # Call to field and say that the bot scored, generate code for scoring mechanism.

        pass
        
    def switchAction(self, eventType):
        
        # A match-case statement to assign the colors based on key input. Used for both rendering and logic.
        match eventType:
            case pg.K_x:
                self.currentColor = self.lineDefaultColor
                print("Default")
            case pg.K_c:
                self.currentColor = self.reverseColor
                print("Reverse")
            case pg.K_1:
                self.currentColor = self.Action1
                print("Action1")
            case pg.K_2:
                self.currentColor = self.Action2
                print("Action2")
            case pg.K_3:
                self.currentColor = self.Action3
                print("Action3")
            case pg.K_4:
                self.currentColor = self.Action4
                print("Action4")
            case pg.K_5:
                self.currentColor = self.Action5
                print("Action5")
            case pg.K_6:         
                self.currentColor = self.Action6
                print("Action6")

    def displayHUD(self, mousex, mousey): 
            
        # sqrt( (x2 - x1)^2 + (y2 - y1)^2 )
        radius = math.sqrt( math.pow((self.x - mousex),2) + math.pow((self.y - mousey),2) )        

        pg.draw.circle(self.mainSurfaceArg, self.currentColor, ( self.x + self.botWidth/2, 
            self.y + self.botLength/2 ), radius, self.lineWidth)

        pg.draw.line(self.mainSurfaceArg, self.currentColor, (self.x+self.botWidth/2,self.y +
            self.botLength/2), (mousex, mousey), self.lineWidth) # NEED TO FIX, ADD END COORD

        theta = -math.atan2(( mousey - self.y) , ( mousex - self.x))

        # Forces the value to be between 0 - 6.1415
        while (theta < 0):
            theta += 2*math.pi

        # Draw Auton path
        autonLinePathColor = pg.Color(220, 255, 252)
        
        for coord in range(len(self.lastLocations)):
            if coord % 2 == 0 and len(self.lastLocations) - coord > 3:
                pg.draw.line(self.mainSurfaceArg, autonLinePathColor, (self.lastLocations[coord],self.lastLocations[coord+1]), 
                    (self.lastLocations[coord+2],self.lastLocations[coord+3]), abs(self.lineWidth - 2))
                
            elif coord % 2 == 0 and coord > 3:
                pg.draw.line(self.mainSurfaceArg, autonLinePathColor, (self.lastLocations[0],self.lastLocations[1]), 
                    (self.lastLocations[2],self.lastLocations[3]), abs(self.lineWidth - 2))

                
        
        #liney = math.tan(theta)*radius

        #perpliney = -math.cot(theta)*radius 

        #s = radius*.99

        #b = s*math.cos(theta)*math.cot(theta) + s*math.sin(theta) 
        
        #y = -math.cot(theta)*radius + b

        #x = math.sqrt(1-math.pow(y, 2))



        # 2 different circles, one with the radius arrow

        #pg.draw.polygon(self.mainSurfaceArg, self.lineColor, (coordinateLeftArrow, 
        #    coordinateRightArrow, coordinateMousePos), self.lineWidth)

        # Move to X Position and Y position. Including turn to angle. Find theta by doing trig. Angle between the current mouse pos 
            # and the robot default angle. Radius by how far the mouse is from the robot center. Radius is just for visual purposes.
            # Add an arrow as well pointing away from the bot towards the mouse. Append code to CODE variable. Add way to reverse drive

            

    def saveToProject(self):
        
        # Open the file inside the project path, appending it
        fileToSave = open(askopenfilename(), 'a')
        # Save the CODE variable to the User's C++ Project. 
        fileToSave.write(self.code)
        fileToSave.close()

        print("Saved!")

    
    def update(self):

        # Draws bot rectangle
        drew = pg.draw.rect(self.mainSurfaceArg, (255, 0, 0), (self.x, self.y,
            self.botWidth, self.botLength))

        return drew
    
    def dragStartingPos(self, x, y):
        # Just a rendering thing. Drags the bot around with the end of the mouse as the center of the bot
        self.x = x - self.botWidth / 2
        self.y = y - self.botLength / 2




    def moveTo(self, x, y, activated):

        # If clicked
        if activated:

            # Corrects X and Y to be in the end of the cursor
            self.x = x - self.botWidth / 2
            self.y = y - self.botLength / 2

            currentAction = 0 # Default action

            # Match case for the colors - actions, can be interpreted in UvuvLib
            match self.currentColor:
                case self.Action1:
                    currentAction = 1
                case self.Action2:
                    currentAction = 2
                case self.Action3:
                    currentAction = 3
                case self.Action4:
                    currentAction = 4
                case self.Action5:
                    currentAction = 5
                case self.Action6:
                    currentAction = 6
                case self.reverseColor:
                    currentAction = 7

            # Define native Pygame Pixel coords
            pixelX = self.x 
            pixelY = self.y

            print(pixelX - self.fieldRectangle.centerx + self.fieldRectangle.width / 2 )

            # (Pixel X - - recCenterX + recheight/2  ) divided by ( recheight / 12 feet) and feet to centimeters conversion
            centiX = (pixelX - self.fieldRectangle.centerx + self.fieldRectangle.width / 2 ) / (self.fieldRectangle.width / 12) * 30.48
            # (Pixel Y - recCenterY + recheight/2 ) divided by ( recheight / 12 feet) and feet to centimeters conversion
            centiY = (pixelY - self.fieldRectangle.centery + self.fieldRectangle.height / 2 ) / (self.fieldRectangle.height / 12) * 30.48

            self.code += f'[ {centiX},{centiY},{currentAction} ]'
            
            # Add Coords to formatted string
            self.lastLocations.append(pixelX) 
            self.lastLocations.append(pixelY)

            print(self.code)
            print("\n")

            # Returns color to default for ease of use
            self.currentColor = self.lineDefaultColor


    










