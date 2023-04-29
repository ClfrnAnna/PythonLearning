# todo:
#  Функция get_weekday()
#  Реализуйте функцию get_weekday(), которая принимает один аргумент:
#
#  number — целое число (от 1 до 7 включительно)
#  Функция должна возвращать полное название дня недели на русском, который соответствует числу number, при этом:
#
#  если number не является целым числом, функция должна возбуждать исключение:
#  TypeError('Аргумент не является целым числом')
#  если number является целым числом, но не принадлежит отрезку [1;7]
#  функция должна возбуждать исключение:
#  ValueError('Аргумент не принадлежит требуемому диапазону')

#todo:
# Сделайте функцию get_weekday() статической в классе Helper

dictWeek={1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
def get_weekday(DayX):
    if int(DayX)!=DayX:
        raise TypeError
    elif (int(DayX)==DayX) and ((DayX<1) or (DayX>7)):
        raise ValueError
    else:
        if DayX in dictWeek:
            print(dictWeek[DayX])

try:
    number = 8
    get_weekday(number)
except TypeError as e:
    print("Аргумент не является целым числом", f"{type(e)}")
except ValueError as e:
    print("Аргумент не принадлежит требуемому диапазону", f"{type(e)}")

# вторая часть задания в task57.py