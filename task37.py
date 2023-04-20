# todo: Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной функции в процессе выполнения кода.
# Выгрузить статистику подсчета в файл debug.log в формате: Название функции, кол-во вызовов, дата-время последнего выполнения
# Пример:
# render, 10,  12.05.2022 12:00
# show,    5,  12.05.2022 12:02
# render, 15,  12.05.2022 12:07
#
# Декоратор должен применяться для различных функций с переменным числом аргументов.
# Статистику вызовов необходимо записывать в файл при каждом запуске скрипта.

import datetime, pickle, json


def counterDec(f):
    def wrapped(*args, **kwargs):
        wrapped.count += 1
        wrapped.dt = datetime.datetime.today()
        return f(*args, **kwargs)

    wrapped.count = 0
    return wrapped


@counterDec
def fun(x, y):
    return x + y


for i in range(3):
    print("Sum = ", fun(6, 7))

with open("debug.log", "a") as filew:
    data = filew.write(str(fun.count) + " " + str(fun.dt) + "\n")

with open("debug.log", "r") as filer:
    data = filer.read()

print(data)
