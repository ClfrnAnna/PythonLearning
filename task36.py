# todo:
# Реализовать декоратор который подсчитывает время выполнения функции.

import time


def timer(f):
    def wrapped(*args, **kwargs):
        t = time.perf_counter()
        res = f(*args, **kwargs)
        print("Time: ", t)
        return res

    return wrapped


@timer
def fun(x, y):
    return x + y


print("Sum = ", fun(6, 7))
