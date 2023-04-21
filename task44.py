# todo: Напишите программу, в которой используется две функции. В одной программа «спит» 2 секунды, в другой – 3 секунды. Пусть каждая функция возвращает время, которое она «проспала».
# Главная программа запускает цикл от 0 до 10, если число четное, то запускает функцию с 2 секундами, если нечетное, то функцию с 3 секундами. Накапливает сон обеих функций отдельно и печатает две суммы.
import time


def sleepingTwo():
    start = time.time()
    time.sleep(2)
    finish = time.time() - start
    return finish


def sleepingThree():
    start = time.time()
    time.sleep(3)
    finish = time.time() - start
    return finish


def main_prog():
    TimeTwo=0
    TimeThree=0
    for i in range(10):
        if i % 2 == 0:
            TimeTwo = TimeTwo + sleepingTwo()
        else:
            TimeThree = TimeThree + sleepingThree()
    return TimeThree + TimeTwo


print(main_prog())
