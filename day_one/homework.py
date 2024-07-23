from typing import Dict, List


class Person:
    def __init__(self, full_name: str, age: int, is_married: bool) -> None:
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self) -> str:
        return f'name={self.full_name}, age={self.age}, is_married={self.is_married}'


class Student(Person):
    def __init__(self, full_name: str, age: int, is_married: bool, marks: Dict[str, int]) -> None:
        super().__init__(full_name, age, is_married)
        self.marks = marks

    def average_rate(self) -> str:
        result = sum(self.marks.values()) // len(self.marks.keys())
        return f'{self.full_name} average rate {result}'


class Teacher(Person):
    salary = 10000

    def __init__(self, full_name: str, age: int, is_married: bool, experience: int) -> None:
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def calculate_salary(self) -> int:
        bonus_years = max(0, self.experience - 3)
        bonus = bonus_years * (self.salary * 0.05)
        total_salary = round(self.salary + bonus)
        return total_salary


teacher = Teacher(full_name='Maybe Yato', age=20, is_married=False, experience=5)
print(teacher.introduce_myself())
print(teacher.calculate_salary())


def create_students() -> List[Student]:
    aesthetic = Student(
        full_name='Aesthetic',
        age=18,
        is_married=False,
        marks={
            'Algebra': 5,
            'Physics': 5,
            'Story': 4
        }
    )
    naarkz = Student(
        full_name='Naarkz',
        age=22,
        is_married=False,
        marks={
            'Algebra': 3,
            'Physics': 2,
            'Story': 5
        }
    )
    quasar = Student(
        full_name='Quasar',
        age=19,
        is_married=False,
        marks={
            'Algebra': 2,
            'Physics': 2,
            'Story': 2
        }
    )
    return [aesthetic, naarkz, quasar]


students = create_students()

for student in students:
    print(
        f'\n{student.introduce_myself()}'
        f'\n{student.average_rate()}'
    )
