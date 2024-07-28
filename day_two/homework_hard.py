
class Figure:
    """
    Базовый класс для фигур
    Атрибуты:
    unit: единица измерения величин (по умолчанию 'см')
    """
    unit = 'см'  # Атрибут класса

    def __init__(self):
        self.__perimeter = 0  # Приватный атрибут

    @property
    def perimetr(self):
        return self.__perimeter

    @perimetr.setter
    def perimetr(self, value):
        self.__perimeter = value

    def calculate_area(self):
        """
        Метод для подсчета площади фигуры
        """
        raise NotImplementedError('Этот метод должен быть переопределен в подклассах')

    def calculate_perimeter(self):
        """
        Метод для подсчета периметра фигуры
        """
        raise NotImplementedError('Этот метод должен быть переопределен в подклассах')

    def info(self):
        """
        Метод для вывода полной информации о фигуре
        """
        raise NotImplementedError("Этот метод должен быть переопределен в подклассах")


class Square(Figure):
    """
    Класс для квадрата, наследуется от Figure
    Атрибуты:
    __side_length: длина стороны квадрата
    """
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length
        self.perimetr = self.calculate_perimeter()  # Устанавливаем периметр при инициализации

    def calculate_perimeter(self):
        return self.__side_length * 4

    def calculate_area(self):
        return self.__side_length ** 2

    def info(self):
        print(
            f'\nSquare side length: {self.__side_length}{self.unit}'
            f'\nPerimetr: {self.perimetr}{self.unit}'
            f'\nArea: {self.calculate_area()}{self.unit}'
        )


class Rectangle(Figure):
    """
    Класс для прямоугольника, наследуется от Figure
    Атрибуты:
    __length: длина прямоугольника
    __width: ширина прямоугольника
    """
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width
        self.perimetr = self.calculate_perimeter()  # Устанавливаем периметр при инициализации

    def calculate_area(self):
        return self.__width * self.__length

    def calculate_perimeter(self):
        return 2 * (self.__length + self.__width)

    def info(self):
        print(
            f'\nRectangle length: {self.__length}{self.unit}'
            f'\nWidth: {self.__width}{self.unit}'
            f'\nArea: {self.calculate_area()}{self.unit}'
        )


figures = [
    Square(side_length=10),
    Square(side_length=15),
    Rectangle(length=10, width=5),
    Rectangle(length=15, width=10),
    Rectangle(length=20, width=5)
]

for figure in figures:
    figure.info()
