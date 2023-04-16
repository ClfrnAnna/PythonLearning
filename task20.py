# todo: Ввод: 2 слова, разделенных пробелами. Для ввода используем функцию s = input().split()
#  Определить, являются ли эти слова анаграммами (словами с одинаковым набором букв). Если да, то True. Если нет, то False.
#  (Примеры: АКВАРЕЛИСТ-КАВАЛЕРИСТ, АНТИМОНИЯ-АНТИНОМИЯ, АНАКОНДА-КАНОНАДА, ВЕРНОСТЬ-РЕВНОСТЬ, ВЛАДЕНИЕ-ДАВЛЕНИЕ, ЛЕПЕСТОК-ТЕЛЕСКОП)

s = input().split()
WordFirst = list(s[0])
WordSecond = list(s[1])
WordFirst.sort()
WordSecond.sort()
if (WordFirst == WordSecond) and (len(WordFirst) == len(WordSecond)):
    print("True")
else:
    print("False")
