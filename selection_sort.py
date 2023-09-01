from typing import List
import time


def find_smallest(arr: List) -> int:
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr: List) -> List:
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

my_list = [15, 64, 33, 44, 15, 0, 3, 46, 21, 99]
print(f'Оригинальный список {my_list}')
start_time = time.monotonic()
print(f'Отсортированный список {selection_sort(my_list)}')
print(f'Время выполнения алгоритма: {time.monotonic() - start_time}')
