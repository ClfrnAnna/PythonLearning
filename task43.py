#todo:
# Каждый третий четверг каждого месяца билеты в Эрмитаж бесплатны. Напечатайте список дат в 2023 году, когда вход бесплатен.
import calendar

days = []
for i in range(1, 13):
    c = calendar.monthcalendar(2023, i)
    week1 = c[0]
    week2 = c[2]
    week3 = c[3]
    if week1[calendar.THURSDAY]:
        day = week2[calendar.THURSDAY]
    else:
        day = week3[calendar.THURSDAY]
        s = '{0} {1}'.format(day, calendar.month_name[i])
        days.append(s)
print(", ".join(days))

