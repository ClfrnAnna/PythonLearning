# todo:
#  Создайте класс Triangle с методом, который при создании объекта проверяет три переменный x, y, z на то,
#  что из них можно составить треугольник. Требования: все числа должны быть больше нуля, сумма любых двух должны быть больше третьего.

class Triangle:
    def check_tr(self, x, y, z):
        if (x > 0) and (y > 0) and (z > 0) and (x + y > z):
            print("True")
        else:
            print("False")


x = int(input())
y = int(input())
z = int(input())

Tr = Triangle()
Tr.check_tr(x, y, z)
