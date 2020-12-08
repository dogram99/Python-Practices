# Магические методы __str__ & __repr__

class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"The object Lion => {self.name}"

    def __str__(self):
        return f"Lion = {self.name}"


lion1 = Lion('Simba')
print(lion1.__dict__)
print(lion1)
lion2 = Lion('Alex')
print(lion2.__dict__)
print(lion2)
