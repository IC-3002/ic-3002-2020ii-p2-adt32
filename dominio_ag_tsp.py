from dominio_ag import DominioAG
from dominio_tsp import DominioTSP
from datos.MatrizCiudades import *
class DominioAGTSP(DominioAG, DominioTSP):
    """
    Representa el objeto de dominio que conoce los detalles de implementación y modelamiento
    del problema del vendedor viajero para ser resuelto con algoritmos genéticos.

    Las soluciones se modelan como listas de enteros, donde cada número representa
    una ciudad específica. Si el grafo contiene n ciudades, la lista siempre contiene
    (n-1) elementos. La lista nunca contiene elementos repetidos y nunca contiene la 
    ciudad de inicio y fin del circuito.

    Métodos:
    generar(n)
        Construye aleatoriamente una lista de listas que representa n 
        posibles soluciones al problema.

    cruzar(sol_a, sol_b)
        Produce una nueva posible solución cruzando las dos soluciones dadas por parámetro.

    mutar(sol)
        Produce una nueva solución aplicando un ligero cambio a la solución dada por
        parámetro.
    """

    def __init__(self, ciudades_rutacsv, ciudad_inicio):
        """Construye un objeto de modelo de dominio para una instancia
        específica del problema del vendedor viajero para ser resuelto
        con algoritmos genéticos.

        Entradas:
        ciudades_rutacsv (str)
            Ruta al archivo csv que contiene la matriz de pesos entre las ciudades
            para las que se quiere resolver el problema del vendedor viajero.

        ciudad_inicio (str)
            Nombre de la ciudad que será el inicio y fin del circuito a calcular.

        Salidas:
            Una instancia de DominioAGTSP correctamente inicializada.
        """
        
        # Pendiente: implementar este constructor
        self.numCiudad = 0
        self.numsCiudades = []
        self. ciudad_inicio = ciudad_inicio
        self.cities, self.matriz = getMatrizCiudad(ciudades_rutacsv)
        for i in range(0, len(self.cities)):
            if self.ciudad_inicio == self.cities[i]:
                self.numCiudad = i
                break
        for i in range(0, len(self.cities)):
            self.numsCiudades.append(i)


    def generar_n(self, n):
        """Construye aleatoriamente una lista de listas que representa n 
        posibles soluciones al problema.

        Entradas:
        n (int)
            Número de soluciones aleatorias a generar.

        Salidas:
        (list) Lista que contiene n listas, cada una representando
        una posible solución al problema modelado por el objeto de dominio.
        """
        
        # Pendiente: implementar este método

        solutions = []

        for i in range(0, n):
            pivot = list(range(0,len(self.cities))) 
            pivot.remove(self.numCiudad)
            random.shuffle(pivot)
            solutions.append(pivot)
        return solutions

    def cruzar(self, sol_a, sol_b):
        """Produce una nueva posible solución cruzando las dos soluciones dadas por parámetro.
        Entradas:
        sol_a (estructura de datos)
            Estructura de datos que modela la solución antecesora A que será cruzada con la B

        sol_b (estructura de datos)
            Estructura de datos que modela la solución antecesora B que será cruzada con la A

        Salidas:
        (estructura de datos) Una nueva solución producto del cruzamiento entre las soluciones A y B
        """

        # Pendiente: implementar este método

        end = []
        i   = 0
        while(len(sol_a)> i):
            if sol_a[i] == sol_b[i]:
                end.append(sol_a[i])
                i+=1
            else:
                end.append('x')
                i+=1
        for i in range(0, len(end)):
            if end[i] == 'x':
                control = True
                while(control):
                    x = random.randint(0, len(self.cities)-1)
                    if x == self.numCiudad:
                        x = random.randint(0, len(self.cities)-1)
                    elif x in end:
                        x = random.randint(0, len(self.cities)-1)
                    else:
                        end[i] = x
                        control = False

        return end

    def mutar(self, sol):
        """Produce una nueva solución aplicando un ligero cambio a la solución dada por
        parámetro.

        Entradas:
        sol (estructura de datos)
            La solución a mutar.
        
        Salidas:
        (estructura de datos) Una nueva solución que refleja un ligero cambio con respecto 
        a la solución dada por parámetro
        """

        # Pendiente: implementar este método
        end = []

        for i in range(0, len(sol)):
            end.append(sol[i])

        randX = random.randint(0, len(sol)-1)
        randY = random.randint(0, len(sol)-1)
        while(randX == randY):
            randX = random.randint(0, len(sol)-1)
            randY = random.randint(0, len(sol)-1)
        temp = end[randX]
        end[randX] = end[randY]
        end[randY] = temp
        return end
