import math
class Figure:
    def calculate_area(self):
        pass

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class krug(Figure):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

class RightTriangle(Figure):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

class Trapezoid(Figure):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def calculate_area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

# Примеры использования
rectangle = Rectangle(2, 4)
circle = krug(2)
right_triangle = RightTriangle(2, 4)
trapezoid = Trapezoid(2, 4, 2)

print("Площадь прямоугольника:", rectangle.calculate_area())
print("Площадь круга:", circle.calculate_area())
print("Площадь прямоугольного треугольника:", right_triangle.calculate_area())
print("Площадь трапеции:", trapezoid.calculate_area())