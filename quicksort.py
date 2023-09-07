from typing import List
import time
from random import randint


# Версия, когда берется 1й элемент списка
def quicksort_v1(array: List) -> List:
    if len(array) < 2:
        return array
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quicksort_v1(less) + [pivot] + quicksort_v1(greater)


# Версия, когда берется элемент, находящийся в середине списка
def quicksort_v2(arr: list) -> list:
    if len(arr) < 2:
        return arr
    pivot = arr.pop(len(arr) // 2)
    less = [i for i in arr if i <= pivot]
    greater = [i for i in arr if i > pivot]
    return quicksort_v2(less) + [pivot] + quicksort_v2(greater)



# Версия, когда берется случайный элемент списка
def quicksort_v3(arr: list) -> list:
    if len(arr) < 2:
        return arr
    pivot = arr.pop(randint(0, len(arr) - 1))
    less = [i for i in arr if i <= pivot]
    greater = [i for i in arr if i > pivot]
    return quicksort_v3(less) + [pivot] + quicksort_v3(greater)


count = int(input('Введите количество элементов: ').strip())
my_list = []
for i in range(count):
    my_list.append(randint(0, 10))
print(f'Оригинальный список: {my_list}\n')

group_quicksort = {
    1: quicksort_v1,
    2: quicksort_v2,
    3: quicksort_v3
}

for i in range(1, 4):
    ll = my_list[:]
    start_time = time.monotonic()
    print(f'Version {i}')
    print(f'Отсортированный список: {group_quicksort[i](ll)}')
    print(f'Время выполнения алгоритма: {time.monotonic() - start_time}')
