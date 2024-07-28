from typing import Union


class Computer:
    def __init__(self, cpu: Union[float, int], memory: int):
        """
        cpu: central processing unit
        memory: root corner memory
        :param cpu: (float, int)
        :param memory: (int)
        """
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self) -> Union[float, int]:
        return self.__cpu

    @cpu.setter
    def cpu(self, value: Union[float, int]) -> None:
        self.__cpu = value

    @property
    def memory(self) -> int:
        return self.__memory

    @memory.setter
    def memory(self, value: int):
        self.__memory = value

    def make_computations(self) -> int:
        """
        арифметические вычисления с атрибутами объекта cpu и memory
        :return: int
        """
        return round(self.__cpu * self.__memory)

    def __str__(self) -> str:
        return f'Computer(cpu: {self.__cpu}, memory: {self.__memory})'

    def __eq__(self, other) -> bool:
        """
        Определяет поведение оператора равенства
        :param other:
        :return: bool
        """
        return self.__memory == other

    def __ne__(self, other) -> bool:
        """
        Определяет поведение оператора неравенства
        :param other:
        :return: bool
        """
        return self.__memory != other

    def __lt__(self, other) -> bool:
        """
        Определяет поведение оператора меньше
        :param other:
        :return: bool
        """
        return self.__memory < other

    def __gt__(self, other) -> bool:
        """
        Определяет поведение оператора больше
        :param other:
        :return: bool
        """
        return self.__memory > other

    def __le__(self, other) -> bool:
        """
        Определяет поведение оператора меньше или равно
        :param other:
        :return: bool
        """
        return self.__memory <= other

    def __ge__(self, other) -> bool:
        """
        Определяет поведение оператора больше или равно
        :param other:
        :return:
        """
        return self.__memory >= other


class Phone:
    def __init__(self, sim_cards_list: list[str]):
        """
        :param sim_cards_list: (список симкард) (list[str])
        """
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self) -> list[str]:
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value: list[str]):
        self.__sim_cards_list = value

    def call(self, sim_card_number: int, call_to_number: str) -> None:
        """
        симуляция звонка в зависимости от переданного номера сим-карты
        :param sim_card_number: (int)
        :param call_to_number: (str)
        :return: None
        """
        if 1 <= sim_card_number <= len(self.__sim_cards_list):
            sim_card = self.__sim_cards_list[sim_card_number - 1]
            print(f'Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {sim_card}')
        else:
            print('Неверный номер сим-карты')

    def __str__(self):
        return f'Phone(sim_cards_list={self.__sim_cards_list})'


class SmartPhone(Computer, Phone):
    def __init__(self, cpu: Union[float, int], memory: int, sim_cards_list: list[str]):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    @staticmethod
    def use_gps(location: str) -> None:
        """
        распечатывает симуляцию проложения маршрута до локации
        :param location: (str)
        :return: None
        """
        print(f'Проложен маршрут до локации {location}')

    def __str__(self):
        return f'SmartPhone(cpu={self.cpu}, memory={self.memory}, sim_cards_list={self.sim_cards_list})'


# Создание объектов
computer = Computer(cpu=3.4, memory=16)
phone = Phone(sim_cards_list=['Beeline', 'Megacom'])
smartphone1 = SmartPhone(cpu=2.5, memory=32, sim_cards_list=['Beeline', 'O!'])
smartphone2 = SmartPhone(cpu=3.0, memory=64, sim_cards_list=['Megacom', 'O!'])

# Распечатка информации о созданных объектах
print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

# Опробование всех возможных методов
print(computer.make_computations())
phone.call(1, '+996 777 99 88 11')
phone.call(2, '+996 555 55 55 55')
print(smartphone1.make_computations())
smartphone1.call(1, '+996 777 99 88 11')
smartphone1.use_gps('Бишкек')
print(smartphone2.make_computations())
smartphone2.call(2, '+996 555 55 55 55')
smartphone2.use_gps('Ош')

# Сравнение объектов по атрибуту memory
print(computer == smartphone1)
print(smartphone1 < smartphone2)
print(smartphone1 > smartphone2)
print(smartphone1 <= smartphone2)
print(smartphone1 >= smartphone2)
