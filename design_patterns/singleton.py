class Singleton(type):
    """
    Restricts class to a single instantiation
    """
    _instances = dict()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args,
                                                                 **kwargs)
        else:
            print('Single instance already exists. Returning single instance.')
        return cls._instances[cls]


class Example(metaclass=Singleton):
    def __init__(self, a):
        self.a = a


if __name__ == '__main__':
    ex1 = Example(5)
    print(ex1.a)

    # attempt to make a new instance
    ex2 = Example(10)

    # this will still be 5 since a new instance is not made
    print(ex2.a)

    # both variables point to the same, single instance
    print(ex1 is ex2)
