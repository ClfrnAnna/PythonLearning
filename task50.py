# todo
# Создайте декоратор, которые переводит все текстовые аргументы функции в верхний регистр и возвращает их в виде списка текстовых аргументов.

def UpRegister(func):
    def wrapped(listFun):
        wrapped.txt = list("")
        for i in listFun:
            if isinstance(i, str):
                wrapped.txt.append(i.upper())
        res=func(listFun)
        return wrapped.txt
    return wrapped


@UpRegister
def func(arguments):
    print(arguments)


arg = "Привет", 123, "слово", 14, 15
print(func(arg))
