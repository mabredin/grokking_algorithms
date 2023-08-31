from typing import List


def summa(arr: List) -> int:
    if len(arr) == 1:
        return arr[0]
    x = arr.pop(0)
    return x + summa(arr)
    
    
def get_length(arr: List) -> int:
    if len(arr) == 1:
        return 1
    arr.pop(0)
    return 1 + get_length(arr)


def get_max(arr: List) -> int:
    pass

    
ll = [1, 2, 3, 4, 5]
print(summa(ll))
ll = [1, 2, 3, 4, 5]
print(get_length(ll))
ll = [1, 2, 3, 4, 5]
print(get_max(ll))
