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

    res = []
    for i in range(len(matrix_result)):
        line_len = len(matrix_result[0]) - 1
        x = matrix_result[i][line_len] / matrix_result[i][i]
        res.append(x)
    return res


def findGreaterLine(matrix: list[list[float]], column: int) -> int:
    values = []
    for i in range(len(matrix)):
        values.append(matrix[i][column])

    flag = values.copy()
    values.sort(reverse=True)
    line_greater = flag.index(values[0])
    return line_greater

def makeMatriz(coef_x:list[float],coef_fx: list[float]):
    
    lst = []
    for i in range(len(coef_x)):
        line = []
        for j in range(len(coef_x)):
            line.append(coef_x[i]**j)
        line.append(coef_fx[i])
        lst.append(line)

    return lst

    
def interpolationMethod(coef_x:list[float],coef_fx: list[float]):

    matrix_M = makeMatriz(coef_x,coef_fx)

    res = jordanMethod(matrix_M=matrix_M)

    print("Polinomio Gerador da Matriz")
    for i in range(len(res)):
        if i == 0:
            print(f'P(x) = ( {res[i]} )', end='')
        else:
            print(f' + ( {res[i]}*x^{i} )', end='')


# ------------------------------------------ #
#           Input Section                    #
# ------------------------------------------ #

coef_x = []
coef_fx = [] 

while True:
    try:
        inps = float(input("(Ctrl + z to exit) x = "))
        coef_x.append(inps)
        inps = float(input("(Ctrl + z to exit) F(x) = "))
        coef_fx.append(inps)
    except EOFError:
        break

interpolationMethod(coef_x,coef_fx)