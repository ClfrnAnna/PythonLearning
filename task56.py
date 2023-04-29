# todo: Создать абстрактный класс Press (пресса) содержащий:
# Поля: название, цена за единицу.
# В классе должны быть абстрактные методы:
# метод SetPrice (без параметров) – установка цены.
# Метод Info - информация (без параметров), который возвращает строку, содержащую информацию об объекте.
#
# На его основе реализовать дочерние классы:
# Magazine - журнал,
# Book- книга.

from abc import ABC, abstractmethod


class Press(ABC):
    name = "Papers"
    price = 0.99

    @abstractmethod
    def SetPrice(self):
        pass

    @abstractmethod
    def Info(self):
        pass
class Magazine(Press):
    def SetPrice(self, price):
        self.price = price

    def Info(self):
        print("Price: ", self.price)


class Book(Press):
    def SetPrice(self, price):
        self.price = price

    def Info(self):
        print("Price: ", self.price)


magasinVogue = Magazine
bookBussines = Book

magasinVogue.SetPrice(Magazine, 1)
bookBussines.SetPrice(Book, 10)

bookBussines.Info(Book)
magasinVogue.Info(Magazine)

