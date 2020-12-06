import random

def optimizar(dominio, tam_pobl, porc_elite, prob_mut, reps):
    """Algoritmo genético para optimización estocástica.

    Entradas:
    dominio (DominioAG)
        Un objeto que modela el dominio del problema que se quiere aproximar.
    
    tam_pobl (int)
        Tamaño de la población.
    
    porc_elite (float)
        Porcentaje de la población que se tomará como elite.
    
    prob_mut (float)
        Probabilidad de mutación, debe estar en el rango [0, 1]
    
    reps (int)
        Número de iteraciones a ejecutar.

    Salidas:
        (estructura de datos) Estructura de datos según el dominio, que representa una
        aproximación a la mejor solución al problema.
    """

    # Pendiente: implementar este método
    pobl = dominio.generar_n(tam_pobl)
    while reps >= 0:
        px = []
        for sol in pobl:
            aptitud = dominio.fcosto(sol)
            tupla = (sol, aptitud)
            px.append(tupla)

        px.sort(key=lambda x: x[1]) #llave aptitud
        for i in range(0, len(px)):
            pobl[i] = px[i][0]
        num_padres = int(len(pobl) * porc_elite)
        num_hijos = int(len(pobl) - num_padres)
        if num_padres != 0:
            sig_gen = pobl[0: num_padres]
        else:
            for sol in pobl:
                aptitud = dominio.fcosto(sol)
                tupla = (sol, aptitud)
                print(tupla)
                px.append(tupla)
                px.sort(key=lambda x: x[1]) #llave aptitud
            return px[0][0]

        descendencia = []
        while num_hijos > 0:
            padreA = sig_gen[random.randrange(0, len(sig_gen))]
            padreB = sig_gen[random.randrange(0, len(sig_gen))]
            hijo = dominio.cruzar(padreA, padreB)
            p = random.uniform(0, 1)

            if p <= prob_mut:
                hijo = dominio.mutar(hijo)
            descendencia.append(hijo)
            num_hijos = num_hijos - 1

        sig_gen = descendencia
        pobl = sig_gen
        reps = reps - 1
        print(sig_gen)

