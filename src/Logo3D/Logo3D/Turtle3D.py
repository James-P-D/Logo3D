import math

class Turtle3D():
    x = 0
    y = 0
    z = 0
    angle = 0
    
    def __init__(self):
        pass

    def move(self, d):
        r = self.angle * (math.pi / 180)
        self.x += (d * math.cos(r))
        self.y += (d * math.sin(r))

    def turn(self, r):
        self.angle += r
        self.angle %= 360