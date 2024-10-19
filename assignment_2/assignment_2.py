def read_matrix_from_csv(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            row = line.strip().split(',')
            matrix.append([int(num) for num in row])
    return matrix


def multiply_matrices(matrix1, matrix2):    #multiply function
    result = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result


def write_matrix_to_csv(matrix, file_path):      #write to matrix funct
    with open(file_path, 'w') as file:
        for row in matrix:
            file.write(','.join(map(str, row)) + '\n')


matrix1 = read_matrix_from_csv('/content/drive/MyDrive/DS_foundation/assignment_2/f1.csv')
matrix2 = read_matrix_from_csv('/content/drive/MyDrive/DS_foundation/assignment_2/f2.csv')


result_matrix = multiply_matrices(matrix1, matrix2)


write_matrix_to_csv(result_matrix, 'result.csv')        #new file

print("Matrix multiplication result has been written to 'result.csv'")
