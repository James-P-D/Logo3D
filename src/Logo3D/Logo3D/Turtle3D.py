import math

class Turtle3D():
    
    def __init__(self):
        self.home()

    def home(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.horizontal_angle = 0
        self.vertical_angle = 0
        self.pendown = True

    def move(self, d):
        r1 = math.radians(self.horizontal_angle)
        r2 = math.radians(self.vertical_angle)
        self.x += d * (math.cos(r2) * math.cos(r1))
        self.y += d * (math.cos(r2) * math.sin(r1))
        self.z += d * (math.sin(r2))

    def horizontal_turn(self, r):
        self.horizontal_angle += r
        self.horizontal_angle %= 360

    def vertical_turn(self, r):
        self.vertical_angle += r
        self.vertical_angle %= 360