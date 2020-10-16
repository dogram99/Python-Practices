from accessify import *


class BankAccount:
    """Python Public Protected Private"""

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def print_public_data(self):
        print(self.name,
              self.balance,
              self.passport)

    def print_protected_data(self):
        print(self._name,
              self._balance,
              self._passport)

    def print_private_data(self):
        indificate_passport = int(input('Введите ваши паспортные данные: '))
        if indificate_passport == self.__passport:
            print(self.__name,
                  self.__balance,
                  self.__passport)
        else:
            print('Не правильные данные!')
            BankAccount.print_private_data(self)


account1 = BankAccount('Alex', '35000', 69382941)
# account1.print_private_data()
# print(dir(account1))
print(account1._BankAccount__passport)
# print(account1.__name)
# print(account1.__balance)
# print(account1.__passport)
