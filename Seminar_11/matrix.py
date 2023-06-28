# Создайте класс Матрица. Добавьте методы для:
#
#     вывода на печать,
#     сравнения,
#     сложения,
#     *умножения матриц


class Matrix:
    '''Добавлен класс вывода матриц на печать, их сравнения и сложения.'''

    def __init__(self, matrix: list) -> None:
        '''Создание матрицы'''
        self.matrix = matrix

    def print_matrix(self):
        '''Вывод матрицы на печать.'''

        print_m = ''
        for i in range(len(self.matrix)):
            print_m = print_m + '\t'.join(map(str, self.matrix[i])) + "\n"
        return print_m

    def compare(self, other):
        '''Сравнение матриц.'''

        if self.matrix == other.matrix:
            return 'Матрицы равны'
        elif self.matrix > other.matrix:
            return f'Матрица {self.matrix} \n больше, чем \n' \
                   f'матрица {other.matrix}'
        else:
            return f'Матрица {other.matrix} \n больше, чем \n' \
                   f'матрица {self.matrix}'

    def __add__(self, other):
        '''Сложение матриц'''
        result = []
        elem = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                s = self.matrix[i][j] + other.matrix[i][j]
                elem.append(s)
                if len(elem) == len(self.matrix[i]):
                    result.append(elem)
                    elem = []
        return result


if __name__ == "__main__":
    arr_1 = Matrix(
        [[0, 1, 1, 1, 0],
         [1, 0, 1, 0, 1],
         [1, 1, 0, 1, 0],
         [1, 0, 1, 0, 1],
         [0, 1, 0, 1, 0]])

    arr_2 = Matrix(
        [[0, 1, 1, 1, 1],
         [1, 0, 1, 0, 1],
         [1, 1, 0, 1, 0],
         [1, 0, 1, 0, 1],
         [1, 1, 0, 1, 0]])

    arr_sum = arr_1 + arr_2

    arr_comp = arr_1.compare(arr_2)
    print(arr_1.print_matrix(), '\n')
    print(arr_2.print_matrix(), '\n')
    print(f'Сумма {arr_sum}, \n')
    print(arr_comp, '\n')
    print(f'А еще я могу умножать матрицы, но это потом ))\n')
    help(Matrix)