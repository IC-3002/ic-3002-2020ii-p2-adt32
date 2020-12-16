from dominio import Dominio
from datos.MatrizCiudades import *


class DominioTSP(Dominio):
    """
    Esta clase modela el dominio del problema del Vendedor Viajero para su resolución
    con algoritmos probabilísticos.

    Las soluciones se modelan como listas de enteros, donde cada número representa
    una ciudad específica. Si el grafo contiene n ciudades, la lista siempre contiene
    (n-1) elementos. La lista nunca contiene elementos repetidos y nunca contiene la 
    ciudad de inicio y fin del circuito.

    Métodos:
    generar()
        Construye aleatoriamente una lista que representa una posible solución al problema.

    fcosto(sol)
        Calcula el costo asociado con una solución dada.

    vecino(sol)
        Calcula una solución vecina a partir de una solución dada.

    validar(sol)
        Valida que la solución dada cumple con los requisitos del problema.

    texto(sol)
        Construye una representación en hilera legible por humanos de la solución
        con el fin de reportar resultados al usuario final.
    """

    def __init__(self, ciudades_rutacsv, ciudad_inicio):
        """Construye un objeto de modelo de dominio para una instancia
        específica del problema del vendedor viajero.

        Entradas:
        ciudades_rutacsv (str)
            Ruta al archivo csv que contiene la matriz de pesos entre las ciudades
            para las que se quiere resolver el problema del vendedor viajero.

        ciudad_inicio (str)
            Nombre de la ciudad que será el inicio y fin del circuito a calcular.

        Salidas:
            Una instancia de DominioTSP correctamente inicializada.
        """

        # Pendiente: implementar este constructor
        self.numCiudad = 'x'
        self.ciudad_inicio = ciudad_inicio
        self.numsCiudades = []
        self.cities, self.matriz = getMatrizCiudad(ciudades_rutacsv)
        for i in range(0, len(self.cities)):
            if self.ciudad_inicio == self.cities[i]:
                self.numCiudad = i
                break
        for i in range(0, len(self.cities)):
            self.numsCiudades.append(i)


    def validar(self, sol):
        """Valida que la solución dada cumple con los requisitos del problema.

        Si n es el número de ciudades en el grafo, la solución debe:
        - Tener tamaño (n-1)
        - Contener sólo números enteros menores que n (las ciudades se numeran de 0 a (n-1))
        - No contener elementos repetidos
        - No contener la ciudad de inicio/fin del circuito

        Entradas:
        sol (list)
            La solución a validar.

        Salidas:
        (bool) True si la solución es válida, False en cualquier otro caso
        """
        # Pendiente: implementar este método
        if self.numCiudad == 'x':
            return False
        elif len(sol)!= len(self.cities)-1:
            return False
        elif self.numMenores(sol) == False:
            return False
        elif self.repedidos(sol) == False:
            return  False
        
        elif self.ciudadInicialValdidacion(sol) == False:
            return  False
        else:
            return True
    
        
    def texto(self, sol):
        """Construye una representación en hilera legible por humanos de la solución
        con el fin de reportar resultados al usuario final.

        La hilera cumple con el siguiente formato:
        Nombre ciudad inicio -> Nombre ciudad 1 -> ... -> Nombre ciudad n -> Nombre ciudad inicio

        Entradas:
        sol (list)
            Solución a representar como texto legible

        Salidas:
        (str) Hilera en el formato mencionado anteriormente.
        """

        # Pendiente: implementar este método
        hilera = self.cities[self.numCiudad]+' -> '
        for i in range(0, len(sol)):
            hilera+= self.cities[sol[i]]+ ' -> '
        hilera+= self.cities[self.numCiudad]
        return hilera

    def generar(self):
        """Construye aleatoriamente una lista que representa una posible solución al problema.

        Entradas:
        ninguna

        Salidas:
        (list) Una lista que representa una solución válida para esta instancia del vendedor viajero
        """

        # Pendiente: implementar este método
        pivot = list(range(0,len(self.cities))) 
        if self.numCiudad != 'x':
            pivot.remove(self.numCiudad)
        random.shuffle(pivot)

        return pivot

    def fcosto(self, sol):
        """Calcula el costo asociado con una solución dada.

        Entradas:
        sol (list)
            Solución cuyo costo se debe calcular

        Salidas:
        (float) valor del costo asociado con la solución
        """

        # Pendiente: implementar este método

        costo = 0.0
        copy = []
        if self.numCiudad != 'x':
            copy.append(self.numCiudad)
        for i in range(0, len(sol)):
            copy.append(sol[i])
        if self.numCiudad != 'x':
            copy.append(self.numCiudad)
        for i in range(0, len(copy)-1):
            costo += float(self.matriz[copy[i]][copy[i+1]])
        return costo

    def vecino(self, sol):
        """Calcula una solución vecina a partir de una solución dada.

        Una solución vecina comparte la mayor parte de su estructura con 
        la solución que la origina, aunque no son exactamente iguales. El 
        método transforma aleatoriamente algún aspecto de la solución
        original.

        Entradas:
        sol (list)
            Solución a partir de la cual se originará una nueva solución vecina

        Salidas:
        (list) Solución vecina
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

    def numMenores(self, sol):
        for i in range(0, len(sol)):
            if sol[i]> len(self.cities)-1:
                return False
        return True
    def repedidos(self, sol):
        repetido = []

        unico = []
        for x in sol:
            if x not in unico:
                unico.append(x)
            else:
                if x not in repetido:
                    repetido.append(x)
        if repetido != []:
            return False 
        return True
    def ciudadInicialValdidacion(self, sol):

        for i in range(0, len(sol)):
            if self.numCiudad == sol[i]:
                return False
        return True
