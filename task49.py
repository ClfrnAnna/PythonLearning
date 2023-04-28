# todo:
#  Определите класс Person. В конструктор которого передается фамилия и возраст ('Иванов', 29)
#  Реализуйте через магические методы условие, при котором возраст у объекта не будет меняться после инициализации.

class Person:
    def __init__(self, secondname, age):
        self.secondname = secondname
        self.age = age

    def __setattr__(self, attr, value):
        if attr == "age":
            existent_value = self.__dict__.get(attr)
            if existent_value is None:
                self.__dict__[attr] = value
            else:
                self.__dict__[attr] = existent_value
        else:
            existent_value = self.__dict__.get(attr)
            if existent_value is None:
                self.__dict__[attr] = value
            else:
                self.__dict__[attr] = value


person = Person("Иванов", 34)
print(person.secondname, person.age)
person.age = 50
print(person.secondname, person.age)
person.secondname = "Петров"
print(person.secondname, person.age)


