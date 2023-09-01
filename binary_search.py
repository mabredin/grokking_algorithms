from typing import List, Optional


def binary_search(list: List, item: int) -> Optional[int]:
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

            
my_list = [1, 2, 5, 5, 8, 9, 11, 29, 29, 30]
items_for_search = [1, 5, 8, 11, 29]

for i in items_for_search:
    print(f'Значение {i} иммеет индекс {binary_search(my_list, i)}')
