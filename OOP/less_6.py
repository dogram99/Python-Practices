class Cat:

    def __init__(self, name, breed='pers', age=1, color='white'):
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color
        print(self, name, breed, age, color)


new_cat = Cat('Tom')
