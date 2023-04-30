# todo: Создать абстрактный класс Transport (транспорт) содержащий:
# Поля:
# скорость;
# себестоимость перевозки груза;
# стоимость перевозки груза.
# В классе должны быть абстрактные методы:
# метод Cost (без параметров) – вычисление стоимости перевозки груза.
# Метод Info - информация (без параметров), который возвращает строку, содержащую информацию об объекте.
#
# На его основе реализовать дочерние классы:
# Marine - морской транспорт,
# Ground - наземный транспорт.


from abc import ABC, abstractmethod


class Transport(ABC):
    speed = 50
    costPrice = 70
    price = 100

    @abstractmethod
    def Cost(self):
        self.finalcost = self.speed * (self.price - self.costPrice)
        return self.finalcost

    @abstractmethod
    def Info(self):
        print(self.speed, self.costPrice, self.price, self.finalcost)


class Marine(Transport):
    def Cost(self):
        self.finalcost = self.speed * (self.price - self.costPrice)

    def Info(self):
        print("Скорость", self.speed, "Себестоимость", self.costPrice, "Стоимость", self.price, "Финальный прайс",
              self.finalcost)


class Ground(Transport):
    def Cost(self):
        self.finalcost = self.speed * (self.price - self.costPrice)

    def Info(self):
        print("Скорость", self.speed, "Себестоимость", self.costPrice, "Стоимость", self.price, "Финальный прайс",
              self.finalcost)


ship = Marine
car = Ground

ship.price = 100000000
ship.Cost(Marine)
ship.Info(Marine)

car.costPrice = 50
car.speed = 120
car.Cost(Ground)
car.Info(Ground)
