# todo:
#  Создайте класс Shape, объекты которого имеют атрибуты
#  Colour – строка, например, «Красный», «Синий»;
#  Square – площадь объекта.
#  Создайте несколько методов:
#  1) Установить цвет объекта.
#  2) Запросить цвет объекта и напечатать его.
#  3) Задать площадь объекта.
#  4) Запросить площадь  объекта.

class Shape:
    def __init__(self):
        self.Colour = "Красный", "Синий"
        self.Square = 50

    def changeColor(self, color):
        self.Colour = color

    def infoColor(self):
        print(f"Color: {self.Colour}")

    def changeSquare(self, square):
        self.Square = square

    def infoSquare(self):
        print(f"Square: {self.Square}")


shape = Shape()
shape.infoColor()
shape.Colour = "Зеленый"
shape.infoColor()
shape.infoSquare()
shape.Square = 40
shape.infoSquare()
