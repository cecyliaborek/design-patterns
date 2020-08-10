class DrawingAPIOne(object):
    """Implementation dependent"""

    def draw_circle(self, x, y, radius):
        print(f'API 1 drawing a circle at ({x}, {y}) with the radius of {radius}')


class DrawingAPITwo(object):
    """Implementation dependent"""

    def draw_circle(self, x, y, radius):
        print(f'API 2 drawing a circle at ({x}, {y}) with the radius of {radius}')

class Circle(object):
    """Implementation independent"""

    def __init__(self, x, y, radius, drawing_api):
        self.x = x
        self.y = y
        self.radius = radius
        self.drawing_api = drawing_api

    def draw(self):
        """Implementation specific abstraction taken care of by another class: DrawingAPI***"""
        self.drawing_api.draw_circle(self.x, self.y, self.radius)

    def scale(self, percent):
        """Implementation independent"""
        self.radius *= percent


circle1 = Circle(1, 2, 3, DrawingAPIOne())

circle1.draw()