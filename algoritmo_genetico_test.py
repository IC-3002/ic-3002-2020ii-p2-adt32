import unittest

from algoritmo_genetico import optimizar
from dominio_ag_tsp import DominioAGTSP

class PruebaAlgoritmoGenetico(unittest.TestCase):

    def test_optimizar(self):
        dominio = DominioAGTSP('datos/ciudades_cr.csv', 'Santa Cruz')
        sol = optimizar(dominio, 100, 0.1, 0.5, 1000)
        print(sol)
        self.assertTrue(dominio.validar(sol))