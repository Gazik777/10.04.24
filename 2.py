import math

class Figure:
    def calculate_area(self):
        pass

    def __int__(self):
        return int(self.calculate_area())

    def __str__(self):
        return "Фигура"

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def __str__(self):
        return f"Прямоугольник: ширина={self.width}, высота={self.height}"

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Круг: радиус={self.radius}"

class RightTriangle(Figure):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

    def __str__(self):
        return f"Прямоугольный треугольник: основание={self.base}, высота={self.height}"

class Trapezoid(Figure):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def calculate_area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

    def __str__(self):
        return f"Трапеция: основание1={self.base1}, основание2={self.base2}, высота={self.height}"

# Примеры использования
rectangle = Rectangle(5, 10)
circle = Circle(3)
right_triangle = RightTriangle(4, 6)
trapezoid = Trapezoid(3, 7, 5)

print(int(rectangle))
print(str(rectangle))

print(int(circle))
print(str(circle))

print(int(right_triangle))
print(str(right_triangle))

print(int(trapezoid))
print(str(trapezoid))