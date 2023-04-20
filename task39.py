# todo 1: создайте модуль serializer

# В модуле реализуйте три функции сериализации
# Функция сериализует объект в байтовый поток pickle
# Параметры
# obj - сериализуемый объект
# file - файл для сериализации к примеру "data.pkl"
def to_pickle(obj, file):
    pass
    # ваш код


#  Функция сериализует объект в json
#  Параметры
# obj - сериализуемый объект
# file - файл для сериализации к примеру "data.json"
def to_json(obj, file):
    pass
    # ваш код


# Функция сериализует объект в yaml
# Параметры
# obj - сериализуемый объект
# file - файл для сериализации к примеру "data.yml"


# todo 2: Cоздайте модуль deserializer. В модуле реализуйте три функции десериализации


# Функция десериализует объект из файла типа pickle
# file - файл для десериализации к примеру "data.pkl"
def from_pickle(file):
    pass
    # ваш код


# Функция десериализует объект из файла типа json
# from_json - функция сереализует объект в json
# Параметры
# file - файл для десериализации к примеру "data.json"
def from_json(file):
    pass
    # ваш код


# Функция десериализует объект из файла типа yaml
# Параметры
# file - файл для десериализации к примеру "data.yml"
def from_yaml(file):
    pass
    # ваш код


# todo 3: Cоздайте пакет из двух модулей serializer и deserializer.

# Импортируйте модули пакета в отдельный файл и протестируйте все функции.

# todo 1: создайте модуль serializer
import pickle, json
import yaml
from yaml.loader import SafeLoader


def to_yaml(obj, file):
    with open(file, "wt") as f:
        yaml.dump(obj, f)


def to_json(obj, file):
    with open(file, "wt") as f:
        json.dump(obj, f)


def to_pickle(obj, file):
    with open(file, "wb") as f:
        pickle.dump(obj, f)


# todo 2: Cоздайте модуль deserializer. В модуле реализуйте три функции десериализации


def from_pickle(file):
    with open(file, "rb") as f:
        data=pickle.load(f)
        return data


def from_json(file):
    with open(file, "rt") as f:
        data=json.load(f)
        return data


def from_yaml(file):
    with open(file, "r") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data

to_pickle(1, "data.pkl")
to_json(1, "data.json")
to_yaml(1, "data.yml")
print(from_pickle("data.pkl"))
print(from_json("data.json"))
print(from_yaml("data.yml"))

import serializerModule,  deserializerModule

serializerModule.to_pickle(1, "data.pkl")
serializerModule.to_json(1, "data.json")
serializerModule.to_yaml(1, "data.yml")
print(deserializerModule.from_pickle("data.pkl"))
print(deserializerModule.from_json("data.json"))
print(deserializerModule.from_yaml("data.yml"))


