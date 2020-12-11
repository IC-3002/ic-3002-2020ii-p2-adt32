import random, collections

def cruzar(sol_a, sol_b):

    puntoDeCruce = len(sol_a)//2

    parte1A = sol_a[0:puntoDeCruce]
    parte1B = sol_a[puntoDeCruce:]

    parte2A = sol_b[0:puntoDeCruce]
    parte2B = sol_b[puntoDeCruce:]

    sol_final = parte1A + parte2B

    unico = []
    unicoPos = []
    repetido = []
    repetidoPos = []

    for x in range(0,len(sol_final)):
        if sol_final[x] not in unico:
            unico.append(sol_final[x])
            unicoPos.append(x)

        else:
            if x not in repetido:
                repetido.append(sol_final[x])
                repetidoPos.append(x)
                
    for i in range(0, len(repetido)):
        control = True
        while(control):
            x = random.randint(0, 16)
            if x == 0:
                x = random.randint(0, 16)
            elif x in repetido:
                x = random.randint(0, 16)
            elif x in sol_final:
                x = random.randint(0, 16)
            else:
                sol_final[repetidoPos[i]] = x
                control = False
    return sol_final


print(cruzar([1,2,3,5], [1,2,2,2]))