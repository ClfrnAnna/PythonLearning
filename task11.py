# todo: Дан целочисленный массив размера N из 10 элементов.
# Преобразовать массив, увеличить каждый его элемент на единицу.
from random import randint

N = 10
lst = [randint(-N, N) for i in range(N)]
print(lst)
print([i + 1 for i in lst])
