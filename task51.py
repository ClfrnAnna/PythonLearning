#todo:
# Определите класс Person. При создании объекта p=Person(‘Иванов’, ‘Михаил’, ‘Федорович’) необходимо ввести полное имя человека.
# При печати объекта должно выводиться следующее:
# print(p) # чивородеФлиахиМвонавИ

class Person:
    def __init__(self, *args):
        self.fullname = args
        print(self.fullname)

    @property
    def fullname(self):
        return self.__fullname

    @fullname.setter
    def fullname(self, args):
        self.__fullname = str("")
        for i in args:
            self.__fullname=str(''.join(reversed(i))) + self.__fullname
        self.__fullname = "".join(self.__fullname)

p=Person("Иванов", "Михаил", "Федорович")