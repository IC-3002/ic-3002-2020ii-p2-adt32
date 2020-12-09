import csv
import random

def getMatrizCiudad(nameFile):
	fichero = nameFile
	results = []
	with open(fichero,encoding="utf-8") as csvfile:
		reader = csv.reader(csvfile) 
		for lista in reader: # Cada fila es una lista
			results.append(lista)

	cities, matriz = fixMatriz(results)
	return cities, matriz

def fixMatriz(matriz):

	cities = []
	for i in range(0,1):
		for j in range(len(matriz[i])):
			cities.append(matriz[i][j])
	cities.pop(0)
	matriz.pop(0)

	matrix = []

	for i in range(0, len(matriz)):
		lista = []
		for j in range(1, len(matriz[i])):
			lista.append(matriz[i][j])
		matrix.append(lista)

	return cities, matrix

