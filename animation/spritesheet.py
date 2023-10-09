class Source:
    def __init__(self):
        self.width = None
        self.height = None
        self.texture = None

    def __repr__(self):
        return f"<heat2d.animation.spritesheet.Source()>"

    @property
    def size(self): return self.width, self.height



class SpriteSheet:
    def __init__(self, name, filepaths):
        self.name = name
        self.filepaths = filepaths
        self.sources = list()

    def __repr__(self):
        return f"<heat2d.animation.SpriteSheet()>"
