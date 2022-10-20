def matrizTriangularBaixo(matrix_M: list[list[float]],) -> list[list[float]]:
    matrix_line = []
    columns_length = len(matrix_M)
    pivo = 0

    while columns_length > 0:
        greater_line = findGreaterLine(matrix_M, pivo)

        # Modificando a matrix para ser a maior linha
        flag = matrix_M[0]
        matrix_M[0] = matrix_M[greater_line]
        matrix_M[greater_line] = flag

        # matrix_M has the bigger line in it

        for i in range(1, columns_length):

            coef = (matrix_M[i][pivo])/(matrix_M[0][pivo])

            for j in range(len(matrix_M[i])):
                minus_part = coef * matrix_M[0][j]
                new_value = matrix_M[i][j] - minus_part
                matrix_M[i][j] = new_value

        matrix_line.append(matrix_M[0])
        matrix_M[::] = matrix_M[1:]
        pivo += 1

        columns_length = len(matrix_M)
    return matrix_line


def findGreaterLine(matrix: list[list[float]], column: int) -> int:
    values = []
    for i in range(len(matrix)):
        values.append(matrix[i][column])

    flag = values.copy()
    values.sort(reverse=True)
    line_greater = flag.index(values[0])
    return line_greater


number_lines = int(input("Qual o numero de linhas ? "))
number_terms = int(
    input("Qual o numero de termos (coef + termos independentes) ? "))


matrix_M = []
for i in range(number_lines):
    line_M = []
    for j in range(number_terms):
        if j + 1 == number_terms:
            x = float(input(f'Qual o valor de b = '))
        else:
            x = float(input(f'Qual o valor de X_{j+1} = '))

        line_M.append(x)

    matrix_M.append(line_M)


# matrix_M = [[1.0, 5.0, 1.0, 1.0], [5.0, 2.0, 3.0, 2.0], [2.0, 3.0, 2.0, 4.0]]
matrix_M = matrizTriangularBaixo(matrix_M)

matrix_line = []
columns_length = len(matrix_M)


while columns_length > 0:
    # matrix_M has the bigger line in it
    pivo = len(matrix_M) - 1

    for i in range(pivo-1, -1, -1):

        coef = (matrix_M[i][pivo])/(matrix_M[pivo][pivo])

        for j in range(len(matrix_M[i])):
            minus_part = coef * matrix_M[pivo][j]
            new_value = matrix_M[i][j] - minus_part
            matrix_M[i][j] = new_value

    matrix_line.append(matrix_M[pivo])
    matrix_M[::] = matrix_M[:pivo]

    columns_length = len(matrix_M)

matrix_line.reverse()
print(matrix_line)

res = {}
for i in range(len(matrix_line)):
    line_len = len(matrix_line[0]) - 1
    x = matrix_line[i][line_len] / matrix_line[i][i]
    res[f'X_{i}'] = x

print(res)


# nmudar daqui
