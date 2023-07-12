import pygame as pg
import Connector as C
import SceneLoader as SL
import CodeGenerator 
import Bot
import UI
import os

#Gets the path to this file, and removes the last bit at the end
currentDirectory = __file__.replace("main.py", '')
#This makes sure that then current Directory is the folder to this file, and not anywhere else
os.chdir(currentDirectory)

#Innitializes Pygame
pg.init()
#Initializes Pygames font system or whatever
pg.font.init()
#Checks to make sure that pygame has initialized, Stops program if not
if (not pg.get_init()):

    print("Failed to initialize!")

    # EXIT PROGRAM


#The Screen's Hight
screenWidth = 900
#The Screen's Width
screenHeight = 650
mainSurface = pg.display.set_mode([ screenWidth, screenHeight ]) # Start up the screen

#The background of the Main Menu
mainSurface.fill((100, 0, 100))

pg.display.set_caption("Auton Maker V2 - UvuvLib") # Set title of app

# pg.display.toggle_fullscreen()
fieldPic = pg.image.load("overunderfield.png").convert() # Loads image, and then converts it to to have a 
# consistent pixel format (higher speed)
appIcon = pg.image.load("uvuv.png").convert()

#Sets the field 
fieldRec = fieldPic.get_rect()
fieldRec.center = screenWidth//2, screenHeight//2

#Continues the Main Loop
isInMainLoop = True

#Forms an instance of the Main Singleton
C.Main(mainSurface, None, None, None, None)
#Instantiates the UIHandler, and asssigns the UIHandler variable in Main
C.Main.UIHandler = UI.UIHandler()
#Instantiates the UIBot, and asssigns the UIBot variable in Main
C.Main.Bot = Bot.Bot(mainSurface, 13.5, 17.5, fieldRec, 0, False)
#Instantiates the SceneLoader, and asssigns the SceneLoader variable in Main
C.Main.SceneLoader = SL.SceneLoader()
#Instantiates the CodeGenerator, and asssigns the CodeGenerator variable in Main
C.Main.CodeGenerator = CodeGenerator.CodeGenerator(mainSurface, 13.5, 17.5, fieldRec, 0, False)
#Loads the Main Scene
C.Main.Inst.SceneLoader.LoadScene(SL.MainMenu())
#Sets the app Icon
pg.display.set_icon(appIcon)

#The Main Loop
while isInMainLoop:
    #The series of inputs that will be shared with the Current scene
    Inputs = []

    for event in pg.event.get():
        if event.type == pg.QUIT: 
           #Exits the program if you press X to quit  
           isInMainLoop = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                #Exits the program if you press Escape
                isInMainLoop = False
            if event.key == pg.K_s:
                #Saves the project
                C.Main.Inst.CodeGenerator.saveToProject()
            #Updates the UI for the KEy that was just pressed
            C.Main.Inst.UIHandler.Update(pg.mouse.get_pos()[0], pg.mouse.get_pos()[1], event)
            #Appends any input that has happened
            Inputs.append(event)
        if event.type == pg.MOUSEBUTTONUP:
            #Appends the Mouse click input
            Inputs.append(event)
            #Updates the UI
            C.Main.Inst.UIHandler.Update(pg.mouse.get_pos()[0], pg.mouse.get_pos()[1],"MOUSEBUTTONUP")
    #Updates the active scene with the inputs
    C.Main.Inst.SceneLoader.UpdateActiveScene(Inputs)  
    #Clears the inputs  
    Inputs.clear()
    #Updates the display
    pg.display.flip() # HAVE AFTER ALL GRAPHICS UPDATES HAVE FINISHED


