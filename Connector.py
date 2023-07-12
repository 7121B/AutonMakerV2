#Boilerplate Singleton class 
#https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
#Inst is the current reference
class Singleton(object):
    Inst = None
    def __new__(class_):
        if not isinstance(class_.Inst, class_):
            class_.Inst = object.__new__(class_)
        return class_.Inst
#This is the Main Singleton class.
#The variables in here must have significant cause for being here
class Main(Singleton):
    
    def __new__(self, mainSurface, UIHandler, UIBot, SceneLoader, CodeGenerator) -> None:
        super().__new__(self)
        self.mainSurface = mainSurface
        self.UIHandler = UIHandler
        self.Bot = UIBot
        self.SceneLoader = SceneLoader
        self.CodeGenerator = CodeGenerator
    pass
