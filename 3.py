# Определение класса Shape для рисования плоских фигур
class Shape:
    def __init__(self):
        pass

    def Show(self):
        pass

    def Save(self, filename):
        pass

    def Load(self, filename):
        pass

class Square(Shape):
    def __init__(self, x, y, side_length):
        self.x = x
        self.y = y
        self.side_length = side_length

    def Show(self):
        print("Square: Left Top Corner:", self.x, self.y, "Side Length:", self.side_length)

    def Save(self, filename):
        with open(filename, 'a') as file:
            file.write(f"Square {self.x} {self.y} {self.side_length}\n")

    def Load(self, filename):
        with open(filename, 'r') as file:
            data = file.read().split()
            self.x = int(data[1])
            self.y = int(data[2])
            self.side_length = int(data[3])


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def Show(self):
        print("Rectangle: Left Top Corner:", self.x, self.y, "Width:", self.width, "Height:", self.height)

    def Save(self, filename):
        with open(filename, 'a') as file:
            file.write(f"Rectangle {self.x} {self.y} {self.width} {self.height}\n")

    def Load(self, filename):
        with open(filename, 'r') as file:
            data = file.read().split()
            self.x = int(data[1])
            self.y = int(data[2])
            self.width = int(data[3])
            self.height = int(data[4])


class Circle(Shape):
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def Show(self):
        print("Circle: Center:", self.center_x, self.center_y, "Radius:", self.radius)

    def Save(self, filename):
        with open(filename, 'a') as file:
            file.write(f"Circle {self.center_x} {self.center_y} {self.radius}\n")

    def Load(self, filename):
        with open(filename, 'r') as file:
            data = file.read().split()
            self.center_x = int(data[1])
            self.center_y = int(data[2])
            self.radius = int(data[3])


class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def Show(self):
        print("Ellipse: Top Corner:", self.x, self.y, "Width:", self.width, "Height:", self.height)

    def Save(self, filename):
        with open(filename, 'a') as file:
            file.write(f"Ellipse {self.x} {self.y} {self.width} {self.height}\n")

    def Load(self, filename):
        with open(filename, 'r') as file:
            data = file.read().split()
            self.x = int(data[1])
            self.y = int(data[2])
            self.width = int(data[3])
            self.height = int(data[4])

# Создание списка фигур
shapes = [Square(0, 0, 5), Rectangle(2, 3, 6, 4), Circle(1, 1, 3), Ellipse(4, 4, 5, 3)]


filename = "shapes.txt"
for shape in shapes:
    shape.Save(filename)


loaded_shapes = []
with open(filename, 'r') as file:
    for line in file:
        data = line.split()
        if data[0] == "Square":
            loaded_shape = Square(int(data[1]), int(data[2]), int(data[3]))
        elif data[0] == "Rectangle":
            loaded_shape = Rectangle(int(data[1]), int(data[2]), int(data[3]), int(data[4]))
        elif data[0] == "Circle":
            loaded_shape = Circle(int(data[1]), int(data[2]), int(data[3]))
        elif data[0] == "Ellipse":
            loaded_shape = Ellipse(int(data[1]), int(data[2]), int(data[3]), int(data[4]))
        loaded_shapes.append(loaded_shape)

for shape in loaded_shapes:
    shape.Show()