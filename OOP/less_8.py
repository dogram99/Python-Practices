# Моносостояние: Инициализируется словарь при создании класса, а не экземпляра класса.
# При создании экземпляра всем экземплярам присваивается ссылка на один и тот же словарь,
# с которым и работают в итоге все экземпляры.

class Cat:
    __share_attr__ = {
        'breed': 'pers',
        'color': 'black'
    }

    def __init__(self):
        self.__dict__ = Cat.__share_attr__


new_cat = Cat()
print(new_cat)
