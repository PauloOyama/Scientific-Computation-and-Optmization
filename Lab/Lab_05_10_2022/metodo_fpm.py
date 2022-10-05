def calculo_polinomio(polinomio: list[int], x: float) -> float:
    sum = 0
    for i in range(len(polinomio)):
        x_part = x ** i
        sum += polinomio[i] * x_part

    return sum


def fpm(polinomio: list[int], interval: list[float], tolerancia: float, past_x: float, f_x0: float):
    a = interval[0]
    b = interval[1]
    f_a = calculo_polinomio(polinomio, a)
    f_b = calculo_polinomio(polinomio, b)

    if f_a*f_b >= 0:
        return past_x

    # divide 2
    x1 = 0
    f_past_x = calculo_polinomio(polinomio, past_x)
    if f_x0 != 0:
        if f_past_x * f_x1 > 0:
            if f_a*f_x1 > 0:
                f_a = f_a/2
            else:
                f_b = f_b/2

    else: 
        x1_upper_part = (a*abs(f_b)) + (b*abs(f_a))
        x1_lower_part = abs(f_b - f_a)

        x1 = x1_upper_part/x1_lower_part

    # print(f"The value from past x = {past_x}")

    f_x1 = calculo_polinomio(polinomio, x1)
    print(f"The value from current x = {x1}")
    print(f"The value from current f_x = {f_x1}")

    tamanho_passo = abs((x1 - past_x)/x1)

    if f_x1 == 0 or tamanho_passo == 0:
        return x1

    elif abs(f_x1) <= tolerancia or abs(tamanho_passo) <= tolerancia:
        return x1

    # achando o intervalo
    a_res = f_a*f_x1

    if a_res < 0:
        # b eh modificado
        interval[1] = x1
    else:
        interval[0] = x1

    return fpm(polinomio, interval, tolerancia, x1, f_x1)


grau = int(input("Grau do polinomio = "))

coeficientes = []

for i in range(grau):
    coef = int(input(f"Coefieciente a{i} = "))
    coeficientes.append(coef)

coef_a = int(input("Intervalo A = "))
coef_b = int(input("Intervalo B = "))

interval = [coef_a, coef_b]

tolerancia = float(input("Tolerancia = "))

res = fpm(coeficientes, interval, tolerancia, interval[0], 0)
print(res)
