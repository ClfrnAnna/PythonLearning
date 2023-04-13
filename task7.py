# todo:  Даны три переменные: X, Y, Z. Их значения числа.
# Из данных произвольных чисел выбрать наибольшее.

# Пример:
# X = 5
# Y = 10
# Z = 3
# Ответ: Наибольшее число 10.
#
# X = 10
# Y = 12
# Z = -7
# Ответ: Наибольшее число 12.

X, Y, Z = map(int, input("Enter X, Y, Z  ").split())
maxValue = X
if Y > maxValue:
    maxValue = Y
if Z > maxValue:
    maxValue = Z
print(maxValue)

# another solution
# print(max(X, Y, Z))



