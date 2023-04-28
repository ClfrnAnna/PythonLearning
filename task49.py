# todo:
#  Определите класс Person. В конструктор которого передается фамилия и возраст ('Иванов', 29)
#  Реализуйте через магические методы условие, при котором возраст у объекта не будет меняться после инициализации.

class Person:
    secondname, age = ('Иванов', 29)

    def __setattr__(self, attr, value):
        if attr == "age":
            existen_value = self.__dict__.get(attr)
        else:
            self.__dict__[attr] = value


person = Person()
print("Исходные данные: ", person.secondname, person.age)
person.age = 50
print("После замены возраста: ", person.secondname, person.age)
person.secondname = "Петров"
print("После замены фамилии: ", person.secondname, person.age)
