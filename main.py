
import pygame as pg
import CodeGenerator 

pg.init()

if (not pg.get_init()):

    print("Failed to initialize!")

    # EXIT PROGRAM

screenWidth = 900
screenHeight = 650
mainSurface = pg.display.set_mode([ screenWidth, screenHeight ]) # Start up the screen

mainSurface.fill((100, 0, 100))

pg.display.set_caption("Auton Maker V2 - UvuvLib") # Set title of app

pg.display.flip()

# pg.display.toggle_fullscreen()

fieldPic = pg.image.load("overunderfield.png").convert() # Loads image, and then converts it to to have a 
    # consistent pixel format (higher speed)
appIcon = pg.image.load("uvuv.png").convert()

fieldRec = fieldPic.get_rect()
fieldRec.center = screenWidth//2, screenHeight//2

cg = CodeGenerator.CodeGenerator(mainSurface, 13.5, 17.5, fieldRec, 0, False)

keepGameRunning = True

isGettingStartingPosition = True

while isGettingStartingPosition:

    hasClicked = False

    for event in pg.event.get():
        if event.type == pg.QUIT:   
           isGettingStartingPosition = False
           keepGameRunning = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                isGettingStartingPosition = False
                keepGameRunning = False
        if event.type == pg.MOUSEBUTTONUP:
            hasClicked = True    
            print("Picked starting position! ")
            cg.moveTo(pg.mouse.get_pos()[0], pg.mouse.get_pos()[1], hasClicked)
            isGettingStartingPosition = False

    mainSurface.fill((100, 0, 100))

    mainSurface.blit(fieldPic, fieldRec) # Display image on the screen

    cg.displayHUD(pg.mouse.get_pos()[0], pg.mouse.get_pos()[1])

    cg.dragStartingPos(pg.mouse.get_pos()[0], pg.mouse.get_pos()[1])

    cg.update()

    pg.display.flip() # HAVE AFTER ALL GRAPHICS UPDATES HAVE FINISHED
    
    pg.display.set_icon(appIcon)



while keepGameRunning:
    
    hasClicked = False

    for event in pg.event.get():
        if event.type == pg.QUIT:   
           keepGameRunning = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                keepGameRunning = False
            if event.key == pg.K_s:
                cg.saveToProject()
                keepGameRunning = False
            cg.switchAction(event.key)
        if event.type == pg.MOUSEBUTTONUP:
            hasClicked = True
        
            
            
        

        
        
    mainSurface.fill((100, 0, 100))

    mainSurface.blit(fieldPic, fieldRec) # Display image on the screen

    cg.displayHUD(pg.mouse.get_pos()[0], pg.mouse.get_pos()[1])

    cg.moveTo(pg.mouse.get_pos()[0], pg.mouse.get_pos()[1], hasClicked)

    cg.update()

    pg.display.flip() # HAVE AFTER ALL GRAPHICS UPDATES HAVE FINISHED





