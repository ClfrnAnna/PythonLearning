# Написать игру "Поле чудес"
#
# Отгадываемые слова и описание лежат в разных  массивах по одинаковому индексу.
# words = ["оператор", "конструкция", "объект"]
# desc_  = [ "Это слово обозначает наименьшую автономную часть языка программирования", "..", ".." ]
# Пользователю выводится определение слова и количество букв в виде шаблона. Стиль шаблона может быть любым.
# Слово из массива берется случайным порядком. Принимая из ввода букву мы ее открываем
# в случае успеха а в случае неуспеха насчитывам штрафные балы. Игра продолжается до 10 штрафных баллов
# либо победы.
#
# Пример вывода:
#
# "Это слово обозначает наименьшую автономную часть языка программирования"
#
# ▒  ▒  ▒  ▒  ▒  ▒  ▒  ▒
#
# Введите букву: O
#
# O  ▒  ▒  ▒  ▒  ▒  O  ▒
#
#
# Введите букву: Я
#
# Нет такой буквы.
# У вас осталось 9 попыток !
# Введите букву:

from random import randint
from typing import List
def FindChar(char, word, wordOut):
    LwordOut=list(wordOut)
    Lword=list(word)
    Lchar=list(char)
    for i in range(len(Lword)):

        if word[i] in Lchar:
            LwordOut[i]=Lchar

    # print(LwordOut))
    all=" , ".join(map(str, LwordOut))
    print(all)
    return LwordOut



    # IndexChar=word.find(char)
    # LwordOut[IndexChar]=char
    # return LwordOut


# x = words[randChoiceDesc].replace(Let, " _ ")
# print(x)

words = ["оператор", "конструкция", "объект"]
desc = ["Это слово обозначает наименьшую автономную часть языка программирования",
        "Структура взаимного расположения частей", "Единица структуры"]

randChoiceDesc = randint(0, 3)
print(desc[randChoiceDesc], "\n")
CountLet = len(words[randChoiceDesc])
wordOut="_" * CountLet
print("_" * CountLet, CountLet, "букв", "\n")
i = 10
Count = 0
while (Count < CountLet):
    Let = input("Введите букву\n")
    if Let in words[randChoiceDesc]:
        wordOut = FindChar(Let, words[randChoiceDesc], wordOut)
        Count = Count + len(Let)
        if (len(Let) == CountLet) and (Let in words[randChoiceDesc]) or (Count >= CountLet):
            print("Вы выиграли :)\n")
            break
    else:
        i = i - 1
        print("Нет такой буквы, осталось", i, "попыток" "\n")
        if i == 0:
            print("Вы проиграли :(")