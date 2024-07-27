# Инкапсуляция
# (__) - Приватный
# Полиморфизм, rewriting, перезапись
# getter, setter (get_, set_)
# props (getter, setter) - @property, @city.setter
# pass, raise


class Address:
    def __init__(self, city, street, number):
        self.__city = city
        self.__street = street
        self.__number = number

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value
        
    @property
    def street(self):
        return self.__street
    
    @street.setter
    def street(self, value):
        self.__street = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if isinstance(value, int) and value >= 0:
            self.__number = value
        else:
            raise ValueError('Value for number must be positive number')


class Animal:
    def __init__(self, name: str, age: int, address):
        # age isinstance
        if isinstance(age, int) and age >= 0:
            self.__age = age
        else:
            raise ValueError('Value for age must be positive number')

        # address isinstance
        if isinstance(address, Address):
            self.__address = address
        else:
            raise ValueError('Value for address must be of data type Address')

        self.__name = name
        self.__was_born()

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    def info(self):
        return (
            f'\n- Self info'
            f'\nName: {self.__name}'
            f'\nAge: {self.__age} years'
            f'\nBirth year: {self.get_birth_year()}'
            f'\n- Address'
            f'\nCity: {self.__address.city}'
            f'\nStreet {self.__address.street}'
            f'\nNumber {self.__address.number}'
        )

    # getter
    def get_age(self):
        return self.__age

    # setter
    def set_age(self, value):
        if isinstance(value, int) and value >= 0:
            self.__age = value
        else:
            raise ValueError('Value for age must be positive number')

    def get_birth_year(self):
        return 2024 - self.__age

    def __was_born(self):
        print(f'\nИноприщрилялец {self.__name} родился')

    def speak(self):
        # pass
        raise NotImplemented('Speak method must be overriden')


animal = Animal('Лунтик', 2, Address('Bishkek', 'shopokova', 101))
# animal = Animal('Лунтик', -2)
# animal = Animal('Лунтик', 'Three')

# - old case
# animal.__name = 'Kami Cat'
# animal.__age = 3
# animal.__age = 'Three'

# - setter and getter for class attribute
# animal.set_age(3)
# animal.set_age(-3)  # error
# animal.set_age('Three')  # error

print(animal.info())  # Не измениться - Kami, 2, 2022
# animal.__was_born()
# animal.__was_born()
# animal.__was_born()


class Cat(Animal):
    def __init__(self, name, age, address):
        # super(self, Cat).__init__(name, age)
        super().__init__(name, age, address)

    def speak(self):
        print('meow, meow')


class Dog(Animal):
    def __init__(self, name, age, commands, address):
        super().__init__(name, age, address)
        self.__commands = commands

    @property
    def command(self):
        return self.__commands
    
    @command.setter
    def command(self, value):
        self.__commands = value

    def info(self):
        return super().info() + f'\nCommands: {self.__commands}'

    def speak(self):
        print('bark, bark')


class Fish(Animal):
    def __init__(self, name, age, address):
        super().__init__(name, age, address)

    def speak(self):
        print('Fish not be speak')


fish = Fish('Lulu', 1, Address('Atlantis', 'Ice Castle', 99))


cat = Cat('Tom', 3, Address('Bishkek', 'Ala-Too', 2))
print(cat.info())

dog = Dog('Bobik', 5, 'Sit, Bark', Address('Osh', 'Karakol', 13))
print(dog.info())

ala_too_address = Address('Bishkek', 'Kok-Kya', 31)

#  @property getter and setter
ala_too_address.number = 1337
# ala_too_address.number = '123'  # error
# ala_too_address.number = -1  # error

print(ala_too_address.number)
print(dog.command)
# dog.command = 'Sit, Bark, Run'
dog.command += ', Run'
print(dog.command)
print(dog.info())

animal_list = [cat, dog, fish]

for i in animal_list:
    i.speak()
