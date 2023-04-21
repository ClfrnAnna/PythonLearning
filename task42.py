# todo:
# Создайте функцию-генератор, которая создает последовательность числовых
# палиндромов: 1 2 3 4 5 6 7 8 9 11 22 33 44 55 66 77 88 99 101 111 121 131 141 151 161 171 181 191 202 212 …

def palindrom():
    count = 0
    while True:

        count += 1
        rev = 0
        n = count
        while (n > 0):
            dig = n % 10
            rev = rev * 10 + dig
            n = n // 10
        if (count == rev):
            yield count


count2 = 1
for i in palindrom():
    if count2 > 15:
        break
    print(i)
    count2 += 1

# palindrom()
