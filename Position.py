import copy

class Position():

    def __init__(self):
        self.x = 0
        self.y = 0
        self.angle = 0

    def copy(self):
        return copy.deepcopy(self)

    def set(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def add(self, pos):
        self.x += pos.x
        self.y += pos.y
        self.angle += pos.angle
        if self.angle > 360:
            self.angle -= 360
        
    def print(self):
        print("(", round(self.x,2),",", round(self.y,2),",", round(self.angle,2),")",end="\t")

NO_MOVEMENT = Position()
