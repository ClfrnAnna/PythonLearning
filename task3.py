# todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().
# При решении задачи обратите внимание какой тип вы получаете через функцию input().

A = int(input("A "))
B = int(input("B "))
C = int(input("C "))
print('AC ', abs(A-C))
print('BC ', abs(B-C))
print('Сумма ', abs(A-C) + abs(B-C))

