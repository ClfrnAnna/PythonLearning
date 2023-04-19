# todo:
#  Напишите рекурсивную функцию sumn(n), которая вычисляет и печатает сумму чисел от 0 до n.

def sumn(n):
    if n == 1:
        return 1
    return n + sumn(n - 1)
print(sumn(int(input())))