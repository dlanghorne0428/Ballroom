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
        
    def print(self):
        print("(",self.x,",",self.y,",",self.angle,")",end="\t")

NO_MOVEMENT = Position()
