def formatToEquation(fucObj:str,restrictions: list[str] ): 
    values = [[]]
    for i in range(len(restrictions)):
        for j in range(len(restrictions[i])):
            if ord(restrictions[i][j]) > 47 and ord(restrictions[i][j]) < 58:
                #check -1 index
                isNegative = False
                if restrictions[i][j-1] == '0':
                    if restrictions[i][j-2] == '-':
                        isNegative = True
                        pass
                elif restrictions[i][j-1] == '-':
                    isNegative = True
                if isNegative is not True:
                    values[i].append(int())



eqObj  = input("Qual a funcao objetivo ? ")
eqObjValue = input("A funcao eh de maximizacao ? (y/N) ")
maxm = False

eq = []
inps = input("Quantas restricoes ? ")
for i in range(int(inps)):
    eqs = input(f'Qual a restricao {(i+1)}? ')
    eq.append(eqs)

print(eq)

if eqObjValue.lower().strip() == 'y':
    maxm = True
elif eqObjValue.lower().strip() == 'n':
    pass
else: 
    print("Funcao de restricao nao identificada ")
    exit()

formatToEquation(eqObj,eq)