
class Figure:
    unit = 'см'

    def calculate_area(self):
        """
        (подсчет площади фигуры)
        """
        pass

    def info(self):
        """
        (вывод полной информации о фигуре)
        """
        pass


class Circle(Figure):
    """
    __radius: (радиус круга)
    """
    def __init__(self, radius: int):
        super().__init__()
        self.__radius = radius

    def calculate_area(self):
        p = 3.14  # число π
        result = round(p * (self.__radius ** 2))
        return result

    def info(self):
        print(
            f'\nCircle radius: {self.__radius}{self.unit}'
            f'\nCircle radius: {self.calculate_area()}{self.unit}'
        )


class RightTriangle(Figure):
    """
    (правильный треугольник - 90 градусов)
    """
    def __init__(self, side_a, side_b):
        super().__init__()
        self.__side_a = side_a
        self.__side_b = side_b
