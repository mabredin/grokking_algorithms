from typing import List


def summa(arr: List) -> int:
    if arr == []:
        return 0
    return arr[0] + summa(arr[1:])
    
    
def get_length(arr: List) -> int:
    if arr == []:
        return 0
    return 1 + get_length(arr[1:])


def get_max(arr: List) -> int:
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    inner_max = get_max(arr[1:])
    return arr[0] if arr[0] > inner_max else inner_max

    
ll = [15, 64, 33, 44, 15]
print(f'Сумма элментов\t {summa(ll)}')
print(f'Длина массива\t {get_length(ll)}')
print(f'Максималное\t {get_max(ll)}')
