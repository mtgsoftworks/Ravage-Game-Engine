from ravage2d import DISPATCHER
from ravage2d.gameobject import GameObject
from ravage2d.trigger import Trigger



class Stage:
    def __init__(self):
        self.gameobjects = list()
        self.triggers = list()

    def __repr__(self):
        return f"<ravage2d.Stage({self.__class__.__name__})>"

    def created(self):
        pass

    def update(self):
        pass

    def engine_init_finished(self):
        pass

    def add(self, component):
        # Component is Trigger
        if isinstance(component, Trigger):
            self.triggers.append(component)

        # Component is GameObject
        elif component.__base__ == GameObject:
            gameobject = component(self)
            self.gameobjects.append(gameobject)
            gameobject.stage = self
            gameobject.created()

    def get(self, gameobject):
        for gobj in self.gameobjects:
            if gobj.__class__.__name__ == gameobject: return gobj
