#todo:
# Сделайте функцию get_weekday() статической в классе Helper


#вторая часть task54.py

class Helper:
    @staticmethod
    def get_weekday(DayX):
        dictWeek = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
        if int(DayX)!=DayX:
            raise TypeError
        elif (int(DayX)==DayX) and ((DayX<1) or (DayX>7)):
            raise ValueError
        else:
            if DayX in dictWeek:
                print(dictWeek[DayX])


try:
    number = 7.8
    Helper.get_weekday(number)
except TypeError as e:
    print("Аргумент не является целым числом", f"{type(e)}")
except ValueError as e:
    print("Аргумент не принадлежит требуемому диапазону", f"{type(e)}")