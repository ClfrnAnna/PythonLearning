# todo:  Ввести число n. Напечатать треугольник из символов +.
#  Пример для n = 5:
# +
# ++
# +++
# ++++
# +++++

n = int(input())
count = 1
for i in range(0, n):
    print("*" * count, "\n")
    count += 1
