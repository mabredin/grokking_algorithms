# Поиск самой длинной общей подстроки

"""
    Версия с приминением ООП
"""
class Matrix:
    def __init__(self, axisX, axisY) -> None:
        self.axisX = axisX
        self.axisY = axisY
        self.table = []
    
    def create_empty_matrix(self) -> None:
        for _ in range(self.axisY):
            self.table.append([0]*self.axisX)

    def fill_matrix(self, right_word: str, wrong_word: str) -> None:
        for i in range(self.axisY):
            for j in range(self.axisX):
                if right_word[i] == wrong_word[j]:
                    self.table[i][j] = 0 + 1 if i == 0 or j == 0 else self.table[i-1][j-1] + 1
                else:
                    self.table[i][j] = 0

    def get_maximum_and_supposed_word(self, right_word: str, maximum: int, supposed_word: str) -> tuple():
        for arr in self.table:
            inner_max = max(arr)
            if inner_max > maximum:
                maximum = inner_max
                supposed_word = right_word
        return (supposed_word, maximum)


def find_the_longest_substring(wrong_word: str) -> str:
    supposed_word = ''
    maximum = 0
    for right_word in right_words:
        table = Matrix(len(wrong_word), len(right_word))
        table.create_empty_matrix()
        table.fill_matrix(right_word, wrong_word)
        supposed_word, maximum = table.get_maximum_and_supposed_word(right_word, maximum, supposed_word)
    return supposed_word


right_words = [
    'fish', 'fort',
    'face', 'fado',
    'fact', 'font',
    'fade', 'fail'
    'fable', 'facet',
    'facia', 'fables',
]
wrong_words = [
    'fony', 'fosh',
    'rably', 'gond'
]

for word in wrong_words:
    supposed_word = find_the_longest_substring(word)
    print(f'Скорее всего, вы хотели ввести строку {supposed_word}, вместо {word}?')
    