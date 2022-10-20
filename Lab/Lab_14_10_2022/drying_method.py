from sqlalchemy import Float


def calculatePolynomial(polynomial: list[float], value_x: float) -> float:
    sum = 0
    for i in range(len(polynomial)):
        x_part = value_x ** i
        sum += polynomial[i] * x_part

    return sum


def dryingMethod(X_i: float, X_j: float, polynomial: list[float], tolerance: float):

    f_X_i = calculatePolynomial(polynomial, X_i)
    f_X_j = calculatePolynomial(polynomial, X_j)

    # OPTIMIZATION CHECKING - if the intervals are the root
    if f_X_i == 0:
        return X_i
    elif f_X_j == 0:
        return X_j

    X_k_upper_part = (X_i*f_X_j) - (X_j * f_X_i)
    X_k_lower_part = f_X_j - f_X_i

    X_k = X_k_upper_part / X_k_lower_part

    f_X_k = calculatePolynomial(polynomial, X_k)

    step = (X_j - X_i)/X_j

    if f_X_k == 0 or step == 0:
        return X_k

    elif abs(f_X_k) <= tolerance or step <= tolerance:
        return X_k

    else:
        X_i = X_j
        X_j = X_k
        return dryingMethod(X_i, X_j, polynomial, tolerance)


# ------------------------------------------ #
#           Input Section                    #
# ------------------------------------------ #


grau = int(input("Grau do polinomio = "))

coeficientes = []

for i in range(grau):
    coef = float(input(f"Coefieciente a{i} = "))
    coeficientes.append(coef)

# X_j = X_(i + 1)
initial_xi = float(input("X0 inicial = "))
initial_xj = float(input("X1 inicial = "))

tolerance = float(input("Tolerancia = "))

result = dryingMethod(initial_xi, initial_xj, coeficientes, tolerance)

print(f"Result {result}")
