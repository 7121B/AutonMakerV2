
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

fieldPic = pg.image.load("overunderfield.jpg").convert() # Loads image, and then converts it to to have a 
    # consistent pixel format (higher speed)

fieldRec = fieldPic.get_rect()
fieldRec.center = screenWidth//2, screenHeight//2

cg = CodeGenerator.CodeGenerator(mainSurface, 13.5, 17.5, 0, False)

keepGameRunning = True

while keepGameRunning:
    
    hasClicked = False

    for event in pg.event.get():
        if event.type == pg.QUIT:   
           keepGameRunning = False
        if event.type == pg.K_ESCAPE:
           keepGameRunning = False
        if event.type == pg.MOUSEBUTTONUP:
            hasClicked = True
        cg.switchAction(event.type)
            
        

        
        
    mainSurface.fill((100, 0, 100))

    mainSurface.blit(fieldPic, fieldRec) # Display image on the screen

    cg.moveTo(pg.mouse.get_pos()[0], pg.mouse.get_pos()[1], hasClicked)

    cg.update()

    pg.display.flip() # HAVE AFTER ALL GRAPHICS UPDATES HAVE FINISHED





# while (1):

    # cg.moveTo(1, 1)

    # x = pg.mouse.get_pos()

    # pg.display.update()
        
    # print(x)





