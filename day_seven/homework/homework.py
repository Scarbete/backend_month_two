from typing import List, Union


# binary_search
def binary_search(target: int, data: List[int]) -> str:
    """
    Как работает:
    Делим список пополам
    Сравниваем средний элемент с target
    Если это не он, продолжаем поиск только в одной половине списка
    Повторяем до тех пор, пока не найдем target или список (data) не закончится
    :param target: int
    :param data: List[int]
    :return: str
    """
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return f'Элемент {target} найден по индексу {mid}'
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return f'Элемент {target} не найден в списке'


number_list = [1, 3, 5, 7, 9, 11, 13, 22]
target_for_bs1 = 7
target_for_bs2 = 22
print(binary_search(target_for_bs1, number_list))
print(binary_search(target_for_bs2, number_list))


# bubble_sort
def bubble_sort(data: List[Union[int, str]]) -> List[Union[int, str]]:
    """
    Как работает:
    Проходим по списку, сравнивая соседние элементы
    Если элементы в неправильном порядке, меняем их местами
    Повторяем процесс несколько раз, пока список не будет полностью отсортирован
    :param data: List[int, str]
    :return: List[int, str]
    """
    n = len(data)

    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp

    return data


unsorted_data1 = [64, 34, 25, 12, 22, 11, 90]
unsorted_data2 = ['c', 'b', 'a', 'b', 'c']
sorted_data1 = bubble_sort(unsorted_data1)
sorted_data2 = bubble_sort(unsorted_data2)
print('Отсортированный список чисел:', sorted_data1)
print('Отсортированный список букв:', sorted_data2)
