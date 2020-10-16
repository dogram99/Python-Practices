# Атрибуты класса => переменная, описание которой создает программист при создании класса.
# Экземпляр класса => это конкретный объект данного класса, за которым закрепляется определенная память.

class Person:
    """Необязательная строка документации класса"""
    name = 'Ivan'
    age = 21


print(Person.__dict__)  # mappingproxy
print(getattr(Person, 'name', 'undefined'))
print(getattr(Person, 'lastname', 'undefined'))

setattr(Person, 'lastname', 'Ivanov')
print(getattr(Person, 'lastname', 'undefined'))

Person.name = 'Misha'
print(getattr(Person, 'name', 'undefined'))

print(getattr(Person, 'lastname', 'before'))
del Person.lastname
print(getattr(Person, 'lastname', 'error'))
