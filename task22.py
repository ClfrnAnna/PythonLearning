# todo: Напишите функцию, которая шифрует строку, содержащую латинские буквы с помощью шифра Цезаря. Каждая буква сдвигается на заданное число n позиций вправо. Пробелы, знаки препинания не меняются. Например, для n = 1.
# a → b,   b → c,    p → q,    y → z,    z V a
# A → B,   B → C,   Z → A
# Т.е. заголовок функции будет def code(string, n):
# В качестве результата печатается сдвинутая строка.


#     #Math y=(x+k)%n
def code(string, n):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Result = []
    LengthABC = len(ABC)
    for j in range(len(Str)):
        if Str[j].islower() is True:
            Result.append(abc[(abc.find(Str[j]) + key) % LengthABC])
        if Str[j].isupper() is True:
            Result.append(ABC[(ABC.find(Str[j]) + key) % LengthABC])
        if Str[j] == " ":
            Result.append(" ")
    print('Result: ', '"', ''.join(Result), '"', sep='')


Str = list(input())
key = int(input())
code(Str, key)


