class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.normal = (self.end - self.start).perp().normalize()
