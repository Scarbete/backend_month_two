class Person:
    def __init__(self, name, age):
        self.__age = age
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    def __str__(self):
        return f'Name: {self.__name}, age: {self.__age}'


# код запуститься если он является основным
if __name__ == '__main__':
    person = Person(name='Quasar', age=20)
    print(person)
