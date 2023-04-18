# todo: Даны переменные A, B, C. Изменить их значения, переместив содержимое A в B, B — в C, C — в A,
# и вывести новые значения переменных A, B, C.

A = int(input("A "))
B = int(input("B "))
C = int(input("C "))

buf=B
B=A
A=C
C=buf

print("A", A, "\n",  "B",  B,"\n",  "C", C)



