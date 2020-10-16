# Декораторы — это, по сути, "обёртки", которые дают нам возможность изменить поведение функции, не изменяя её код.
class BankAccount:
    """Property decorator"""

    def __init__(self, name: str, balance: int):
        self.name = name
        self.__balance = balance

    @property
    def my_balance(self):
        print('get balance')
        return self.__balance

    @my_balance.setter
    def my_balance(self, value):
        print('set balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    @my_balance.deleter
    def my_balance(self):
        print('delete balance')
        del self.__balance

    # my_balance = my_property_balance.setter(my_balance)

    # my_balance = property(my_balance)
    # my_balance = my_balance.setter(set_balance)
    # my_balance = my_balance.deleter(delete_balance)

    # Тоже самое что и код выше ()
    # balance = property(fget=get_balance,
    #                    fset=set_balance,
    #                    fdel=delete_balance)


account1 = BankAccount('Alex', 1000)
account1_balance = account1.my_balance
print(account1_balance)

# isinstance() специально создана для проверки принадлежности данных определенному классу (типу данных):
print(isinstance(4.4, (int, str, float)))
