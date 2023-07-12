import pygame as pg
import UI
import Connector as C
#Scenes contain the data and logic of a Scene 
class Scene():
    #Any UI Elements of a scene
    UIObjects = []
    def __init__(self) -> None:
        pass
    #Loading the scene, the start variables of a scene 
    def LoadScene(self):
        pass
    #Updates the Current Scene 
    def UpdateScene(self, Inputs):
        pass
    pass
#The Main menu
class MainMenu(Scene):

    def __init__(self) -> None:
        #Declares the UI Elements of a scene
        StartButton = UI.MainMenuButton(365, 200, 150, 40,(30,30,30))
        StartButtonText = UI.Text(390, 208, "Start Auton", "helvetica", 20, False, False, (60,60,60))
        MainText = UI.Text(300, 50, "Auton Maker", "helvetica", 50, False, False, (30,30,30))
        #Appends them to the UIObjects
        self.UIObjects.append(StartButton)
        self.UIObjects.append(StartButtonText)
        self.UIObjects.append(MainText)
        super().__init__()
    def LoadScene(self):
        #fills the background 
        C.Main.Inst.mainSurface.fill((100,100, 100))
        super().LoadScene()
    pass
#The Main, Auton Scene. A lot of this code is relic code from main
class MainScene(Scene):
    #If the starting position is being selected, this is True
    isGettingStartingPosition = True
    #Decaleres the field rec. The other way of getting the fieidl rec was not giving me the x and y coords
    #If you are to change the fieldPic, change this as well or problems will arrise
    fieldRec = pg.Rect(200, 75, 500, 500)
    def __init__(self) -> None:
        super().__init__()
        #Assigns the field pic
        self.fieldPic = pg.image.load("overunderfield.png").convert()
        #Assigns the field rec's center 
        self.fieldRec.center = pg.display.get_window_size()[0]//2, pg.display.get_window_size()[1]//2
    def LoadScene(self):
        #fills the background of a scene
        C.Main.Inst.mainSurface.fill((100, 0, 100))        
        super().LoadScene()
    def UpdateScene(self, Inputs):
        #fills the background
        C.Main.mainSurface.fill((100,0,100))
        #Dsiplays the field Pic
        C.Main.mainSurface.blit(self.fieldPic, self.fieldRec)
        
        #Updates the Bot
        C.Main.Inst.Bot.update()
        #Displays the HUD
        C.Main.Inst.Bot.displayHUD(pg.mouse.get_pos()[0], pg.mouse.get_pos()[1])
        #If the Starting Position is true, the bot will drag arround the mouse
        if self.isGettingStartingPosition == True:
            C.Main.Inst.Bot.dragStartingPos(pg.mouse.get_pos()[0], pg.mouse.get_pos()[1])
        #Loops over the Inputs
        for x in Inputs:
            #If a key is pressed,
            if x.type == pg.KEYDOWN:
                #check if the user wants to switch Action
                C.Main.Inst.Bot.switchUIAction(x.key)
                #Update the UIHAndler for said key
                C.Main.Inst.CodeGenerator.switchCodeAction(x.key)
            #if the User clicks, 
            if x.type == pg.MOUSEBUTTONUP:
                #if the User CLicks sand is Starting position, 
                if self.isGettingStartingPosition:
                    #moveTo teh Starting Position and set the isGettingStartingPosition to False
                    print("Picked starting position! ")
                    C.Main.Inst.CodeGenerator.moveTo(pg.mouse.get_pos()[0], pg.mouse.get_pos()[1], True)
                    C.Main.Inst.Bot.AppendLocation(pg.mouse.get_pos()[0], pg.mouse.get_pos()[1])
                    self.isGettingStartingPosition = False
                #else
                elif self.isGettingStartingPosition == False:
                    #Append the Location where the User Clicked
                    print("Is clicked")
                    C.Main.Inst.Bot.AppendLocation(pg.mouse.get_pos()[0], pg.mouse.get_pos()[1])
                    C.Main.Inst.CodeGenerator.moveTo(pg.mouse.get_pos()[0], pg.mouse.get_pos()[1], True)

        super().UpdateScene(Inputs)
        #Update the Bot
        C.Main.Inst.Bot.update()
        pg.display.flip()
    pass
#Loads Scenes
class SceneLoader():
    ActiveScene = None
    NewScene = "MainMenu"
    SceneTransitionTime = 0
    TotalSceneTransitionTime = 20
    #Loads a New Scene
    def LoadScene(self, NewScene):
        #Wipes the Current Scene
        self.WipeCurrentScene()
        #Loads the New Scene
        NewScene.LoadScene()
        #Adds the Scene's UI
        C.Main.Inst.UIHandler.AddSubscribers(NewScene.UIObjects)
        #Loads the UI
        C.Main.Inst.UIHandler.LoadObjects()
        #Sets the Active Scene to the New Scene
        self.ActiveScene = NewScene
        pass
    #Wipes the Current Scene
    def WipeCurrentScene(self):
        #Checks if there is a Scene to be wiped
        if self.ActiveScene != None:
            #Deletes the UI
            C.Main.Inst.UIHandler.DeleteSubscribers()
            #Fills teh background black
            C.Main.Inst.mainSurface.fill((0,0,0))
            #sets the SceneTransitionTime to Zero
            self.SceneTransitionTime = 0
            pass
        pass
    #Updates the Currrnt Scene
    def UpdateActiveScene(self, Inputs):
        #Checks if there is an active scene and if teh SceneTransition time is equal or greater than the TSTT
        if self.ActiveScene != None and self.SceneTransitionTime >= self.TotalSceneTransitionTime:
            self.ActiveScene.UpdateScene(Inputs)
        #If there is a scene, but the other condition is false, then update the SceneTransitionTime
        if self.SceneTransitionTime < self.TotalSceneTransitionTime:
            self.SceneTransitionTime += 1
        #This is done to giev a buffer in between scenes, because excess inputs,
        #(such as button presses on the Start Menu), may do other things in another Scene
        #(such as get the Starting Position).
        pass