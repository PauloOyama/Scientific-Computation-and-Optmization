
def sassenfeldMethod(matrix_coef: list[list[float]]):
    '''
    Check if the given [matrix_coef] converge in to an answer or not
    '''

    length_matrix = len(matrix_coef)
    b_list = []

    for i in range(length_matrix):
        lst_func = matrix_coef[i][:i] + matrix_coef[i][i+1:]
        if i == 0:
            coef = abs(1/matrix_coef[i][i])
            sum = 0
            for j in range(len(lst_func)):
                sum += abs(lst_func[j])

            b_list.append(coef*sum)

        else:
            coef = abs(1/matrix_coef[i][i])
            sum = 0
            for j in range(len(lst_func)):
                if j < len(b_list):
                    sum += abs(lst_func[j]) * b_list[j]
                else:
                    sum += abs(lst_func[j])

            b_list.append(coef*sum)

    b_list.sort(reverse=True)
    return b_list[0] < 0


def find_X(matrix_coef: list[list[float]], matrix_terms: list[float], x_guess: list[float]) -> list[float]:

    x_list = []
    for i in range(len(matrix_coef)):
        sum = 0
        coef = 1/matrix_coef[i][i]
        first_part = [-z for z in matrix_coef[i][:i]]
        last_part = [-h for h in matrix_coef[i][i+1:]]
        lst_func = [matrix_terms[i]] + first_part + last_part
        x_mod = x_guess[:i] + x_guess[i+1:]

        for j in range(len(lst_func)):
            if j == 0:
                sum += lst_func[0]
            elif j <= len(x_list):
                sum += lst_func[j]*x_list[j-1]
            else:
                sum += lst_func[j]*x_mod[j-1]

        x_list.append(coef*sum)

    return x_list


def GaussSeidelMethod(matrix_coef: list[list[float]], matrix_terms: list[float], x_guess: list[float], tolerance: float):
    '''
    Given a matrix and a guess about it's roots, return an approximation to the roots
    '''
    new_x_guess = find_X(matrix_coef, matrix_terms, x_guess)

    result = [abs((x - y)/x) for x, y in zip(new_x_guess, x_guess)]
    result.sort(reverse=True)
    max = result[0]

    if (max) < tolerance:
        return new_x_guess
    else:
        return GaussSeidelMethod(matrix_coef, matrix_terms, new_x_guess, tolerance)

    # ------------------------------------------ #
    #           Input Section                    #
    # ------------------------------------------ #


number_lines = int(input("Qual o numero de linhas ? "))
number_terms = int(
    input("Qual o numero de termos (coef + termos independentes) ? "))
matrix_coef = []
matrix_terms = []
for i in range(number_lines):
    line_M = []
    for j in range(number_terms):
        if j + 1 == number_terms:
            x = float(input(f'Qual o valor de b = '))
            matrix_terms.append(x)
        else:
            x = float(input(f'Qual o valor de X_{j+1} = '))
            line_M.append(x)
    matrix_coef.append(line_M)
tolerance = float(input("Qual a tolerancia do erro ? "))


# Checking convergency

has_not_convergency = sassenfeldMethod(matrix_coef=matrix_coef)

if has_not_convergency:
    print("Sistema nao converge")
    exit()
else:
    answer = GaussSeidelMethod(
        matrix_coef, matrix_terms, [-1, 0, 1], tolerance)
    print("As aproximacoes das raizes sao, ")
    print(answer)
