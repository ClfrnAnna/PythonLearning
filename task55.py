# #todo: Написать авторизацию пользователя в систему.
# При реализации авторизации спроектировать абстрактный класс и реализовать методы в наследуемом классе
# login, check_password, check_login

# При запуске программы пользователю необходимо ввести
# логин и пароль, поэтапно.
# login: _________
# password: ________
#
# При неправильном вводе логина должно генерироваться пользовательское исключение LoginNotFound
# Введеный пароль должен проверятся на длину. Длина должна быть более 8 символов иначе генерируем пользовательское
# исключение LengthError
# При вводе некорректного пароля генерируем соответсвуещее исключение
# При успешном заходе генерируем исключение "Доступ разрешен!"

from abc import ABC, abstractmethod


class Absclass(ABC):
    def __init__(self):
        pass


class CheckUser(Absclass):
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def loginUser(self):
        self.check_password(self)
        self.check_login(self)
        if (self._checklog == 1) and (self._checkpas == 1):
            print("Доступ разрешен!")

    def check_password(self):
        pasRef = "123456789"
        if (len(self.password) < 8):
            raise LengthError
        elif (len(self.password) > 8) and (self.password != pasRef):
            print("Password is not coreect")
        else:
            self._checkpas = 1

    def check_login(self):
        loginRef = "Anna"
        if self.login != loginRef:
            raise LoginNotFound
        else:
            self._checklog = 1


login = input("login: ")
password = input("password: ")
user = CheckUser
user.__init__(CheckUser, login, password)
user.loginUser(CheckUser)
