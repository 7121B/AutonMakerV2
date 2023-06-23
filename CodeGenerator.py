
import Field
import math
import time
import pygame as pg

class CodeGenerator(): # In Constructor: File Path, Bot Starting X, Y, and Rotation

    isDriverRoute = False

    x = 100
    y = 100

    lastLocations = []

    botWidth = 0
    botLength = 0

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

    code = ""     # If Auton, write 0 at the start, if Driver write 1 at the start

    ##########   Format   ##########

    # { X, Y, Theta, Action Code } #

    ################################

    def __init__(self, mainSurfaceArg, width, length, startingRotRad, isDriverArg):

        self.mainSurfaceArg = mainSurfaceArg

        self.botWidth = width
        self.botLength = length

        self.botStartingRotation = startingRotRad

        self.isDriverRoute = isDriverArg

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

        print("filler")
        
    def switchAction(self, eventType):

        if (eventType == pg.K_c):
            self.currentColor = self.Action1
            print("Reverse")
            
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

        while (theta < 0):
            theta += 2*math.pi

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

            

    def saveToProject():

        # Save the CODE variable to the User's C++ Project. Tie to a button. Use sys for this.

        print("Saved!")

    
    def update(self):

        drew = pg.draw.rect(self.mainSurfaceArg, (255, 0, 0), (self.x, self.y,
            self.botWidth, self.botLength))

        return drew
    
    def dragStartingPos(self, x, y):
        self.x = x - self.botWidth / 2
        self.y = y - self.botLength / 2




    def moveTo(self, x, y, activated):

        if activated:

            self.x = x - self.botWidth / 2
            self.y = y - self.botLength / 2

            currentAction = 0

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

            self.code += f'[ {self.x},{self.y},{currentAction} ]'
            
            self.lastLocations.append(self.x)
            self.lastLocations.append(self.y)

            print(self.code)
            print("\n")

            self.currentColor = self.lineDefaultColor













