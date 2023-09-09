# Поиск самой длинной общей подстроки

"""
    Версия с приминением простых функций
"""
def find_the_longest_substring(wrong_word: str) -> str:
    supposed_word = ''
    maximum = 0
    for right_word in right_words:
        table = create_empty_matrix(right_word, wrong_word)
        fill_matrix(right_word, wrong_word, table)
        supposed_word, maximum = get_maximum_and_supposed_word(table, right_word, maximum, supposed_word)
    
    return supposed_word, maximum


def create_empty_matrix(right_word: str, wrong_word: str) -> list:
    table = []
    for _ in range(len(right_word)):
        table.append([0]*len(wrong_word))
    return table


def fill_matrix(right_word: str, wrong_word: str, table: list) -> None:
    for i in range(len(right_word)):
        for j in range(len(wrong_word)):
            if right_word[i] == wrong_word[j]:
                table[i][j] = 0 + 1 if i == 0 or j == 0 else table[i-1][j-1] + 1
            else:
                table[i][j] = 0


def get_maximum_and_supposed_word(table: list, right_word: str, maximum: int, supposed_word: str) -> tuple:
        for arr in table:
            inner_max = max(arr)
            if inner_max > maximum:
                maximum = inner_max
                supposed_word = right_word
        return supposed_word, maximum


right_words = [
    'fish', 'fort',
    'face', 'fado',
    'fact', 'font',
    'fade', 'fail'
    'fable', 'facet',
    'facia', 'fables',
    'fort'
]
wrong_words = [
    'fony', 'fosh',
    'rably', 'gond'
]

for word in wrong_words:
    supposed_word, maximum = find_the_longest_substring(word)
    print(f'Скорее всего, вы хотели ввести строку {supposed_word}, вместо {word}?')
    print(f'Подстрока равна {maximum} элементов\n')
