#todo: Дан генетический код ДНК (строка, состоящая из букв G, C, T, A)
# Постройте РНК, используя принцип замены букв: G → C, C → G, T → A, A→T.
# Напишите функцию, которая на вход получает ДНК, и возвращает РНК. Например:
# Ввод: GGCTAA
# Вывод: CCGATT


print("GGCTAA")
DNK=list("GGCTAA")
Dct={"G":"C", "C":"G",  "T":"A",  "A":"T"}
for i in DNK:
    str1=Dct.get(i)
    print(str1, end="")

# a=str1[len(str1)-1:] + str1[:-1]