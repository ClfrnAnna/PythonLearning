# todo: Задача 1 Переопределите метод __str__, чтобы в нем печатались все атрибуты объекта и их значения через запятую. Например:
# def __init__(self):
#     self.x = 0
#     self.y = 1
#
# Должно быть напечатано x:0, y:1


class Check:
    def __init__(self):
        self.x = 0
        self.y = 1

    def disp_info(self):
        print(f"x: {self.x}, y:{self.y}")


Check.x = 1
Check.y = 0
check = Check()
check.disp_info()
