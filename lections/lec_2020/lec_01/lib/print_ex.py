def printf():
    """
    var = 'no_name'
    F-Строка: print(f"string {var}
    """
    name = input('Как вас зовут? ')
    print(f"Привет {name}")
    lastname = input('Как твоя фамилия? ')
    print(name, lastname)


if __name__ == '__main__':
    printf()
