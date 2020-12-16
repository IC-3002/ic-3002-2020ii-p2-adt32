import math, random

def optimizar(dominio, temperatura = 10e32, tasa_enfriamiento = 0.95):
    """Algoritmo de optimización estocástica simulated annealing.

    Entradas:
    dominio (Dominio)
        Un objeto que modela el dominio del problema que se quiere aproximar.

    temperatura (float/int)
        Temperatura inicial del algoritmo, se recomienda un número alto

    tasa_enfriamiento (float)
        Porcentaje de enfriamiento de la temperatura durante cada iteración, el valor
        por defecto es 0.95, lo que indica una tasa de enfriamiento del 5%.

    Salidas:
        (estructura de datos) Estructura de datos según el dominio, que representa una
        aproximación a la mejor solución al problema.
    """

    # Pendiente: implementar esta función

    sol = dominio.generar()
    costo = dominio.fcosto(sol)
    while temperatura > tasa_enfriamiento:
        solPrima = dominio.vecino(sol)
        costoPrima = dominio.fcosto(sol)
        p = math.exp(-(costoPrima-costo)/temperatura)
        pAzar= random.uniform(0, 1)
        if (costoPrima < costo) or (pAzar <= p):
            sol = solPrima
            costo = costoPrima
        temperatura = temperatura * tasa_enfriamiento
    return sol

