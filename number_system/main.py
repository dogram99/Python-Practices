# -*- coding: utf-8 -*-
from termcolor import colored


def main():
    transfer_to_another_number_system()


def reverse(s):
    return s[::-1]


def transfer_to_another_number_system():
    list_base = []

    number_system = input(colored('Введите в какую систему счисления перевести: ', 'grey'))
    x = input(colored('Введите число которое хотите перевести: ', 'grey'))
    base = number_system

    def transfer(x):
        while x > 0:
            digit = x % base
            list_base.append(digit)
            x //= base
        print(colored('Перевод в ' + str(base) + '-ную систему счисления:\n', 'green'),
              colored(reverse(list_base), 'blue'))

    try:
        x = int(x)
        base = int(base)

        if x <= 0:
            print(colored('Число должно быть положительным: x >= 0', 'red'))
            transfer_to_another_number_system()
        else:
            transfer(x)

    except Exception as _error:
        print(colored(_error, 'red'))
        print(colored("Ошибка: должно быть число", 'red'))
        transfer_to_another_number_system()


main()
input('Нажмите Enter для выхода\n')
