
class Figure:
    """
    unit - (единица измерения величин)
    """
    unit = 'см'

    def __init__(self):
        self.__perimeter = 0

    @property
    def perimetr(self):
        return self.__perimeter

    @perimetr.setter
    def perimetr(self, value):
        self.__perimeter = value

    def calculate_area(self):
        """
        (подсчет площади фигуры)
        :return:
        """
        pass

    def calculate_perimeter(self):
        """
        (подсчет периметра фигуры)
        :return:
        """
        pass

    def info(self):
        """
        (вывод полной информации о фигуре)
        :return:
        """
        pass


class Square(Figure):
    """
    __side_length - (длина одной стороны квадрата)
    """
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length
        self.perimetr = self.calculate_perimeter()

    def calculate_perimeter(self):
        square_sides_count = 4
        square_perimeter = self.__side_length * square_sides_count
        return square_perimeter

    def calculate_area(self):
        square_area = self.__side_length * self.__side_length
        return square_area

    def info(self):
        print(
            f'\nSquare side length: {self.__side_length}{self.unit}'
            f'\nPerimetr: {self.perimetr}{self.unit}'
            f'\nArea: {self.calculate_area()}{self.unit}'
        )


class Rectangle(Figure):
    """
    length: (длина)
    width: (ширина)
    """
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width
        self.perimetr = self.calculate_perimeter()

    def calculate_area(self):
        result = (self.__width * self.__length)
        return result

    def calculate_perimeter(self):
        result = (self.__width + self.__length) * 2
        return result

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
