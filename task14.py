#todo: Введите список lst, состоящий из чисел. Найдите и напечатайте наименьшее число из списка lst.
# B Python есть функция min, которая решает эту задачу. Но напишите свою функцию, которая не использует функцию min.

lst=[12, 5, 65, 45]
print(lst)
print(min(lst))

minValue=lst[0]
for i in range(len(lst)):
    if lst[i]<=minValue:
        minValue=lst[i]
print(minValue)

