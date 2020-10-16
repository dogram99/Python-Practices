class Car:
    model = 'BMW'
    engine = 1.6


car1 = Car()
car1.age = 2007
print(Car.__dict__)
# Атрибут экземпляра класса:
print(car1.__dict__)