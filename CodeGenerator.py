
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

        self.GameFont = pg.font.SysFont('helvetica', 32, False, False)
        self.RenderText = self.GameFont.render("The Text", False, (0,0,0))
        self.mainSurfaceArg = mainSurfaceArg

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
        
    def switchCodeAction(self, eventType):
        
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


            

    def saveToProject(self):
        
        # Open the file inside the project path, appending it
        try:
            fileToSave = open(askopenfilename(), 'a')
            # Save the CODE variable to the User's C++ Project. 
            fileToSave.write(self.code)
            fileToSave.close()
            print("Saved!")
        except:
            print("Not Saved :(")


    def CheckActionButtons():
        pass

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

            print(self.code)
            print("\n")

            # Returns color to default for ease of use
            self.currentColor = self.lineDefaultColor
    def RenderMainMenu(self):
        #self.RenderText = self.GameFont.render("AUTON MAKER", True, (0,0,0), None)
        pass



    










