#todo: Дан список из кортежей (Фамилия, премия). Напечатать эти кортежи в порядке убывания премии.
# Тех, у кого одинаковая премия, то печатать в алфавитном порядке.
#  Пример ввода:
# [(Иванов, 100), (Петров, 200), (Сидоров, 200), (Воробьев, 100), (Лунин, 200)]
# Вывод:
#     Лунин 200
#     Петров 200
#     Сидоров 200
#     Воробьев 100
#     Иванов 100
#
#     Примечание:
#     https://pythonist.ru/lyambda-funkczii-dlya-sortirovki-razlichnyh-spiskov-v-python/

lst=[("Иванов", 100), ("Петров", 200), ("Сидоров", 200), ("Воробьев", 100), ("Лунин", 200)]
print(lst)
sorted_list1 = list(reversed(sorted(lst, key=lambda x: x[0])))
sorted_list2 = list(reversed(sorted(sorted_list1, key=lambda x: x[1])))
print(sorted_list2)


