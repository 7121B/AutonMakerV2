import pygame as pg
import math 
import Connector as C
import SceneLoader as SL
#The UIHandler Handles most of the UI in a scene 
class UIHandler():
    #The Subscribers of the UIHandler 
    Subscribers = []
    #Updates all of the UI
    def Update(self, MouseX, MouseY, UpdateText):
        for x in self.Subscribers:
            x.Update(MouseX, MouseY, UpdateText)
        pass
    #Addds a UIElement to the Subscribers
    def AddSubscriber(self, Object):
        self.Subscribers.append(Object)
        pass
    #Adds multiple UIElements to the Subscribers
    def AddSubscribers(self, Objects):
        for x in Objects:
            self.Subscribers.append(x)
    #Delets subscribers from the List and memory
    def DeleteSubscribers(self):
        for x in self.Subscribers:
            del x
        self.Subscribers.clear()
        pass
    #Draws the Subscribers on the Screen
    def LoadObjects(self):
        for x in self.Subscribers:
            x.Draw()
        pass
    pass

#The base class for a UI Class
class UIElement():
    def __init__(self, Xpos, Ypos) -> None:
        pass
    #The update function, Only Triggered by UIHandler
    def Update(self, MouseX, MouseY, UpdateText):
        return
    #The Draw function, only Triggered by UIHandler
    def Draw(self):
        pass
    pass
#Button class. A UIElement that reacts when clicked
class Button(UIElement):
    #XPos : the X Position of the Button
    #YPos : the Y Position of the Button
    #SizeX : The X Size of the Button
    #SizeY : The Y Size of the Button
    #Color : The Color of the Button
    #Optional- 
    #Text : What the Button Says
    #Font : The Font of the Text
    #FontSize : The size of the Font

    def __init__(self,  Xpos, Ypos, SizeX, SizeY, Color, Text = "", Font = "", FontSize = 0) -> None:
        self.ButtonRect = pg.Rect(Xpos, Ypos, SizeX, SizeY)
        self.Color = Color       
        pg.draw.rect(C.Main.Inst.mainSurface, self.Color, self.ButtonRect)
        self.Text = Text
        self.Font = Font
        self.FontSize = FontSize
        if Text != "":
            Source = pg.font.SysFont(self.Font, self.FontSize, False, False).render(self.Text,False,(0,0,0), None)
            C.Main.Inst.mainSurface.blit(Source, ((self.ButtonRect.topleft[0]+self.ButtonRect.centerx + + self.FontSize)/2, (self.ButtonRect.topleft[1]+ self.ButtonRect.centery)/2), area=None, special_flags = 0)
            pass
        pass
    #The Update Function
    def Update(self, MouseX, MouseY, UpdateText):
        #If a Mouseclick was Pressed AND the mouse was over the Button, Interact.
        if UpdateText == "MOUSEBUTTONUP":
            if self.Pressed(MouseX, MouseY):
                self.Interaction()
        pass
    #The Interaction Function.
    def Interaction(self):
        pass
    #Checks if the Mouse is over the Button
    def Pressed(self, MouseX, MouseY) -> bool:
        return self.ButtonRect.collidepoint(MouseX, MouseY)
    #Draws the Button
    def Draw(self):
        pg.draw.rect(C.Main.Inst.mainSurface, self.Color, self.ButtonRect)
        if self.Text != "":
            Source = pg.font.SysFont(self.Font, self.FontSize, False, False).render(self.Text,False,(0,0,0), None)
            C.Main.Inst.mainSurface.blit(Source, ((self.ButtonRect.topleft[0]+self.ButtonRect.centerx + self.FontSize)/2, (self.ButtonRect.topleft[1]+ self.ButtonRect.centery)/2), area=None, special_flags = 0)
            pass
#The Main Menu Button
class MainMenuButton(Button):
    def __init__(self,  Xpos, Ypos, SizeX, SizeY, Color, Text = "", Font = "", FontSize = 0) -> None:
        super().__init__(Xpos, Ypos, SizeX, SizeY, Color, Text, Font, FontSize)
    #Upon Interaction, Load the Main Scene
    def Interaction(self):
        print("I am Main Button, and I am being Pressed")
        C.Main.Inst.SceneLoader.LoadScene(SL.MainScene())
        return super().Interaction()
#Renders Text
class Text(UIElement):
    RenderText = ""
    #XPos : the X Position of the Text
    #YPos : the Y Position of the Text
    #Size : the Font Size
    #RenderText : The Text wished to be displayed
    #Font : the Sys Font of your Choosing
    #Bold : Whether or not the Text is Bolded
    #Italicized : Whether or not the Text is Italicized
    #Color : The Color of the Text
    def __init__(self, Xpos, Ypos,RenderText : str, Font : str, Size : int, Bold : bool, Italicized : bool, Color = (0,0,0)):
        self.Xpos = Xpos
        self.Ypos = Ypos

        self.Size = Size
        self.RenderText = RenderText
        self.Font = Font 
        self.Bold = Bold
        self.Italicized = Italicized
        self.Color = Color

        self.Draw()
        pass
    #Changes the Text
    def ChangeText(self, Text):
        self.RenderText = Text
        self.Draw()
        pass
    #Draws the Text
    def Draw(self):
        self.RenderFont = pg.font.SysFont(self.Font, self.Size, self.Bold, self.Italicized)
        self.RenderSurface = self.RenderFont.render(self.RenderText, False, self.Color, None)
        C.Main.Inst.mainSurface.blit(self.RenderSurface, (self.Xpos, self.Ypos))
        return super().Draw()
#Renders an Image
class Image(UIElement):
    #XPos : the X Position of the Image
    #YPos : the Y Position of the Image
    #Texture : the path to the Texture of the Image
    def __init__(self, Xpos, Ypos, Texture :str) -> None:
        self.Xpos = Xpos
        self.Ypos = Ypos

        self.Texture = pg.image.load(Texture).convert()
        C.Main.Inst.mainSurface.blit(self.Texture, (self.Xpos, self.Ypos))
        super().__init__(Xpos, Ypos)
    #Draws the Image
    def Draw(self):
        C.Main.Inst.mainSurface.blit(self.Texture, (self.Xpos, self.Ypos))
        super().Draw()
