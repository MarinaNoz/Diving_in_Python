#Напишите функцию для транспонирования матрицы

def transpositions(my_matrix):
    
    matrix_trans = [[my_matrix [j][i] for j in range(len(my_matrix))] for i in range(len(my_matrix[0]))]
    return matrix_trans
   

my_matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(my_matrix)
print(transpositions(my_matrix))