from ravage2d.math.vector import Vector2



class Camera:
    def __init__(self):
        self.position = Vector2(0, 0)

        self.focus_object = None
        self.focus_offset = Vector2(0, 0)

    def focus(self, object):
        self.focus_object = object
