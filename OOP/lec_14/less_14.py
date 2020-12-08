# Пространоство имен класса

class DeportmentIT:
    PYTHON_DEV = 3
    GO_DEV = 2
    REACT_DEV = 1

    def info(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)

    def info_2(self):
        print(DeportmentIT.PYTHON_DEV, DeportmentIT.GO_DEV, DeportmentIT.REACT_DEV)

    @property
    def info_prop(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)

    @classmethod
    def info_class(cls):
        print(cls.PYTHON_DEV, cls.GO_DEV, cls.REACT_DEV)

    @staticmethod
    def info_static():
        print(DeportmentIT.PYTHON_DEV, DeportmentIT.GO_DEV, DeportmentIT.REACT_DEV)

    @classmethod
    def hiring_pyt_dev(cls):
        cls.PYTHON_DEV = cls.PYTHON_DEV + 1


it2 = DeportmentIT()
print(it2.PYTHON_DEV)
it2.hiring_pyt_dev()
it2.hiring_pyt_dev()
print(it2.PYTHON_DEV)
print(it2.__dict__)
it3 = DeportmentIT()
print(it2.PYTHON_DEV)
