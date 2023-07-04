def triangMatrizDown(matrix_M: list[list[float]],) -> list[list[float]]:
    matrix_line = []
    columns_length = len(matrix_M)
    pivo = 0

    while columns_length > 0:
        greater_line = findGreaterLine(matrix_M, pivo)

        # Modificando a matrix ter a maior linha sendo a primeira
        flag = matrix_M[0]
        matrix_M[0] = matrix_M[greater_line]
        matrix_M[greater_line] = flag

        # iterate in the lines

        for i in range(1, columns_length):

            coef = (matrix_M[i][pivo])/(matrix_M[0][pivo])

            # iterate in the columns
            for j in range(len(matrix_M[i])):
                minus_part = coef * matrix_M[0][j]
                new_value = matrix_M[i][j] - minus_part
                matrix_M[i][j] = new_value

        # remove first line and add in another list
        matrix_line.append(matrix_M[0])
        matrix_M[::] = matrix_M[1:]
        pivo += 1

        columns_length = len(matrix_M)
    return matrix_line


def triangMatrizUp(matrix_M: list[list[float]],) -> list[list[float]]:

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
    return matrix_line


def jordanMethod(matrix_M: list[list[float]],):
    matrix_result = triangMatrizDown(matrix_M)
    matrix_result = triangMatrizUp(matrix_result)

    res = {}
    for i in range(len(matrix_result)):
        line_len = len(matrix_result[0]) - 1
        x = matrix_result[i][line_len] / matrix_result[i][i]
        res[f'X_{i}'] = x
    return res, matrix_result


def findGreaterLine(matrix: list[list[float]], column: int) -> int:
    values = []
    for i in range(len(matrix)):
        values.append(matrix[i][column])

    flag = values.copy()
    values.sort(reverse=True)
    line_greater = flag.index(values[0])
    return line_greater


# ------------------------------------------ #
#           Input Section                    #
# ------------------------------------------ #

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


result, matriz = jordanMethod(matrix_M=matrix_M)

print("Matriz com metodo aplicado")
for i in range(len(matriz)):
    print(matriz[i])

print("Resultados")
print(result)
