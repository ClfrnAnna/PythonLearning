# todo:
#   Создайте класс Pet с атрибутам имя, вес и уровень сытости.
#   Напишите метод info, который в качестве результата выдает эти атрибуты.
#   Напишите метод hungry, который возвращает уровень сытости и комментирует: если меньше 5, то «голоден», если больше 10, то «сыт».
#   Напишите метод feed, который передает питомцу некоторую еду, которая прибавляется к уровню сытости и вызывает метод info.

class Pet:
    def __init__(self, name, weigth, hungerLevel):
        self.name = name
        self.weigth = weigth
        self.hungerLevel = hungerLevel

    def info(self):
        print(f"name:{self.name}, weigth:{self.weigth}, hungerLevel: {self.hungerLevel}")

    def hungry(self, hungerLevel):
        if self.hungerLevel < 5:
            print("Hungry")
        else:
            print("No hungry")

    def feed(self, food):
        self.food = food
        self.hungerLevel = self.food + self.hungerLevel
        self.info()


pet = Pet("Mark", 50, 3)
pet.info()
pet.hungry(pet.hungerLevel)
pet.feed(5)
pet.hungry(pet.hungerLevel)
