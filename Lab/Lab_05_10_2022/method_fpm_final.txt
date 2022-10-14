def calculatePolynomial(polynomial: list[float], value_x: float) -> float:
    sum = 0
    for i in range(len(polynomial)):
        x_part = value_x ** i
        sum += polynomial[i] * x_part

    return sum


def falsePositiveModified(polynomial: list[float], interval: list[float], tolerance: float, past_x: float, f_x0: float, count: int):
    """
    [polynomial] is the polynomial's coefficient, [interval], goes from a(lower bound) to b(upper bound), 
    [tolerance] is the acceptable error, [past_x] is the last x value, [f_x0] is the last f(x) value
    """

    a = interval[0]
    b = interval[1]
    f_a = calculatePolynomial(polynomial, a)
    f_b = calculatePolynomial(polynomial, b)

    # OPTIMIZATION CHECKING - if the intervals are the root
    # if f_a == 0:
    #     return True, a, count
    # elif f_b == 0:
    #     return True, b, count

    if f_a*f_b >= 0:
        # There's none root between those two
        return False, past_x, 0

    # Divide f(a) or f(b) by 2
    # Comment from here to ...
    f_past_x = calculatePolynomial(polynomial, past_x)
    if f_x0 != 0:
        if f_past_x * f_x0 > 0:
            if f_a*f_x0 > 0:
                f_b = f_b/2
            else:
                f_a = f_a/2
    # ... here to make False Positive Method

    x_upper_part = (a*abs(f_b)) + (b*abs(f_a))
    x_lower_part = abs(f_b - f_a)
    x = x_upper_part/x_lower_part

    f_x = calculatePolynomial(polynomial, x)

    step_width = abs((x - past_x)/x)

    # Stop Conditions
    if f_x == 0 or step_width == 0:
        return True, x, count

    elif abs(f_x) <= tolerance or abs(step_width) <= tolerance:
        return True, x, count

    # New Interval
    if f_a*f_x < 0:
        last_x = interval[1]
        interval[1] = x
    else:
        last_x = interval[0]
        interval[0] = x

    return falsePositiveModified(polynomial, interval, tolerance, last_x, f_x, count + 1)


# ------------------------------------------ #
#           Input Section                    #
# ------------------------------------------ #


grau = int(input("Grau do polinomio = "))

coeficientes = []

for i in range(grau):
    coef = float(input(f"Coefieciente a{i} = "))
    coeficientes.append(coef)

coef_a = float(input("Intervalo - a  = "))
coef_b = float(input("Intervalo - b = "))

interval = [coef_a, coef_b]

tolerance = float(input("Tolerancia = "))

is_possible, response, count = falsePositiveModified(
    coeficientes, interval, tolerance, interval[0], 0, 0)

if is_possible:
    print("Eh possivel uma raiz nesse intervalo")
    print(f"Aproximacao da Raiz = {response}")
    print(f"Numero de Iteracoes necessarias = {count}")

else:
    print("Nao eh possivel uma raiz nesse intervalo")
