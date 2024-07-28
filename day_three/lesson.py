from enum import Enum


class Color(Enum):
    WHITE = '#FFF'
    BLACK = '#000'
    GRAY = '#E2E2E2'


class MusicPlayable:
    """
    Класс Mixin в Python — это класс,
    предназначенный для добавления функциональности
    к другим классам через множественное наследование
    """
    @staticmethod
    def play_music(song):
        print(f'Now is playing {song}')

    @staticmethod
    def stop_music():
        print(f'Music stopped')


class Drawable:
    @staticmethod
    def draw(emoji):
        print(emoji)


class Smartphone(MusicPlayable, Drawable):
    pass


class Car(MusicPlayable, Drawable):
    def __init__(self, model, year, color):
        self.__model = model
        self.__year = year
        if isinstance(color, Color):
            self.__color = color
        else:
            raise ValueError('Color attruibute must be of data type Color')

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def year(self):
        return self.__year

    @model.setter
    def model(self, value):
        self.__model = value

    def drive(self):
        print('I can drive')

    def __str__(self):
        return f'Model: {self.__model}, Year: {self.__year}'

    def __gt__(self, other):
        return self.year > other.year


class FuelCar(Car):

    __total_fuel_amount = 1000

    @classmethod
    def get_total_fuel_amount(cls):
        return cls.__total_fuel_amount

    @staticmethod
    def get_fuel_type():
        return 'AI 98'

    def __init__(self, model, year, fuel_bank, color):
        Car.__init__(self, model, year, color)
        self.__fuel_bank = fuel_bank
        FuelCar.__total_fuel_amount -= fuel_bank

    @property
    def fuel_bank(self):
        return self.__fuel_bank

    @fuel_bank.setter
    def fuel_bank(self, value):
        self.__fuel_bank = value

    def drive(self):
        print('I can drive by using fuel')

    def __str__(self):
        return super().__str__() + f', Fuel bank: {self.__fuel_bank}'


class ElectroCar(Car):
    def __init__(self, model, year, battery, color):
        Car.__init__(self, model, year, color)
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.__battery = value

    def drive(self):
        print('I can drive by using electricity')

    def __str__(self):
        return super().__str__() + f', Battery: {self.__battery}'


class HybridCar(FuelCar, ElectroCar):
    def __init__(self, model, year, fuel_bank, battery, color):
        FuelCar.__init__(self, model, year, fuel_bank, color)
        ElectroCar.__init__(self, model, year, battery, color)


bmw = FuelCar('BMW M3 E92', 2007, 63, Color.BLACK)
print(bmw)

tesla = ElectroCar('Tesla Roadster', 2020, 80000, Color.WHITE)
print(tesla)

toyota = HybridCar('Toyota Highlander', 2024, 50, 40000, Color.WHITE)
print(toyota)

toyota.drive()
print(HybridCar.mro())  # FuelCar, ElectroCar, Car
toyota.draw('🚗')
toyota.play_music('(Fe!n Fe!n - Travis Scott)')

smartphone = Smartphone()
smartphone.draw('📱')
smartphone.play_music('(Kendrick Lamar, SZA - All the stars)')

print(Color.WHITE)

#  bad code
if tesla.model == 'Tesla Roadstr':
    print('Tesla is very good!')

#  good code
if tesla.color == Color.WHITE:
    print('The car is beautiful!')

number_1 = 9
number_2 = 5

print(f'Number 1 is bigger than Number 2: {number_1 > number_2}')
print(f'BMW is bigger than TOYOTA: {bmw > toyota}')
print(FuelCar.get_total_fuel_amount())
print(FuelCar.get_fuel_type())
