# Назовем пароль хорошим, если
# его длина равна 9 или более символам
# в нем присутствуют большие и маленькие буквы любого алфавита
# в нем имеется хотя бы одна цифра
# Напишите программу, которая требует ввода нового пароля до тех пор, пока не будет введен хороший.
#
# На вход программе подается произвольное количество паролей, каждый на отдельной строке. Гарантируется, что среди них присутствует хороший.
#
#
# Для каждого введенного пароля программа должна вывести текст:
#
# LengthError, если длина введенного пароля меньше 9 символов
# LetterError, если в нем все буквы имеют одинаковый регистр
# DigitError, если в нем нет ни одной цифры
# Success!, если введенный пароль хороший
#
# После ввода хорошего пароля все последующие пароли должны игнорироваться.
# Примечание 1. Приоритет вывода сообщений об ошибке в случае невыполнения нескольких условий:
# LengthError, затем LetterError, а уже после DigitError.
#
#
# Sample Input 1:
#
# arr1
# Arrrrrrrrrrr
# arrrrrrrrrrrrrrr1
# Arrrrrrr1
# Sample Output 1:
#
# LengthError
# DigitError
# LetterError
# Success!
#
# Sample Input 2:
#
# beegeek
# Beegeek123все п
# Beegeek2022
# Beegeek2023
# Beegeek2024
# Sample Output 2:
# LengthError
# Success!

import re
def chech_password(listPassword):
    listError=[]
    for i in listPassword:
        res = [re.search(r"[a-z]", i), re.search(r"[A-Z]", i), re.search(r"[0-9]", i)]
        if all(res) and (len(i) > 8):
            listError.append('Success!')
            break
        else:
            if (len(i) < 9):
                listError.append('LengthError')
            elif (res[0] is None) or (res[1] is None):
                listError.append('LetterError')
            else:
                    listError.append('DigitError')


    return listError




# listPassword1 = ['beegeek', 'Beegeek123все', 'Beegeek2022', 'Beegeek2023', 'Beegeek2024']
# listPassword2 = ['arr1', 'Arrrrrrrrrrr', 'arrrrrrrrrrrrrrr1', 'Arrrrrrr1']

DoubleEnter=[]
listPassword=[]
while not DoubleEnter=="":
    DoubleEnter = input()
    listPassword.append(DoubleEnter)
listPassword.remove(DoubleEnter)

forprint=chech_password(listPassword)
print("\n".join(forprint))
