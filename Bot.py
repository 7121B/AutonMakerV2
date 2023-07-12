import pygame as pg
import Connector as C
import math
class Bot():

    x = 100
    y = 100
    lineDefaultColor = (72,209,204)
    reverseColor = (235, 252, 252)
    currentColor = lineDefaultColor
    botStartingRotation = 0
    lastLocations = [] # Array of last pixel X and pixel Y for rendering
    lineWidth = 5
    Action1 = (90, 34, 224)
    Action2 = (11, 127, 222)
    Action3 = (176, 11, 222)
    Action4 = (147, 191, 237)
    Action5 = (245, 226, 22)
    Action6 = (245, 122, 22)

    def __init__(self, mainSurfaceArg, width, length, startingRotRad, isDriverArg, fieldRect) -> None:
        self.mainSurfaceArg = mainSurfaceArg

        self.botWidth = width
        self.botLength = length

        self.botStartingRotation = startingRotRad

        self.isDriverRoute = isDriverArg

        self.fieldRectangle = fieldRect
        pass
    def displayHUD(self, mousex, mousey): 
            
        # sqrt( (x2 - x1)^2 + (y2 - y1)^2 )
        radius = math.sqrt( math.pow((self.x - mousex),2) + math.pow((self.y - mousey),2) )        

        pg.draw.circle(self.mainSurfaceArg, self.currentColor, ( self.x + self.botWidth/2, 
            self.y + self.botLength/2 ), radius, self.lineWidth)

        pg.draw.line(self.mainSurfaceArg, self.currentColor, (self.x+self.botWidth/2,self.y +
            self.botLength/2), (mousex, mousey), self.lineWidth) # NEED TO FIX, ADD END COORD
        
        Length = math.sqrt(math.pow((mousex - self.x),2) + math.pow((mousey - self.y),2))
        Length /= 100
        Length = math.ceil(Length * 100)/100

        #self.RenderText = self.GameFont.render(str(Length) + " meters", False,(0,0,0))

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
    pass
    def dragStartingPos(self, x, y):
        # Just a rendering thing. Drags the bot around with the end of the mouse as the center of the bot
        self.x = x - self.botWidth / 2
        self.y = y - self.botLength / 2

    def AppendLocation(self, X, Y):
        self.x = X - self.botWidth / 2
        self.y = Y - self.botLength / 2
        self.lastLocations.append(self.x)
        self.lastLocations.append(self.y)
        
        #print((self.x,self.y))
        pass
    def switchUIAction(self, eventType):
        
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

    def update(self):
        # Draws bot rectangle
        drew = pg.draw.rect(self.mainSurfaceArg, (255, 0, 0), (self.x, self.y,
            self.botWidth, self.botLength))

        return drew