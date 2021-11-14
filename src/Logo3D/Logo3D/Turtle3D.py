import math

class Turtle3D():
    
    def __init__(self):
        self.home()

    def home(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.angle = 0
        self.pendown = True

    def move(self, d):
        self.x += (d * math.cos(math.radians(self.angle)))
        self.y += (d * math.sin(math.radians(self.angle)))

    def turn(self, r):
        self.angle += r
        self.angle %= 360