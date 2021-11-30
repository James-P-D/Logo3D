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
                
        x_v1 = math.cos(r1) + math.sin(r1) + 0
        y_v1 = -math.sin(r1) + math.cos(r1) + 0
        z_v1 = 0 + 0 + 1

        x_v2 = math.cos(r2) + 0 + math.sin(r2)
        y_v2 = 0 + 1 + 0
        z_v2 = -math.sin(r2) + 0 + math.cos(r2)

        self.x += (d * x_v1) * (d * x_v2)
        self.y += (d * y_v1) * (d * y_v2)
        self.z += (d * z_v1) * (d * z_v2)

    def horizontal_turn(self, r):
        self.horizontal_angle += r
        self.horizontal_angle %= 360

    def vertical_turn(self, r):
        self.vertical_angle += r
        self.vertical_angle %= 360