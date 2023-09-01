from typing import List
import time
from random import randint


def quicksort(array: List) -> List:
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


count = int(input('Введите количество элементов: ').strip())
my_list = []
for i in range(count):
    my_list.append(randint(0, 1000))
print(f'Оригинальный список: {my_list}')
start_time = time.monotonic()
print(f'Отсортированный список: {quicksort(my_list)}')
print(f'Время выполнения алгоритма: {time.monotonic() - start_time}')
