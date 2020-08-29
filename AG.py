import random

#VARIABLES GLOBALES
population = [] #Arreglo de arreglos
results = [] #Arreglo de mejor función objetivo de cada generacion
flow = [] #Datos de la matriz de flujo
distance = [] #Datos de la matriz de distancias

#FUNCIONES
def readFile(name):
    name = "data/"+name + ".txt"
    file = open(name,'r')
    matrix = []
    row = []
    for line in file:
        row = line.split()
        rowInt = []
        for element in row:
            rowInt.append(int(element))
        matrix.append(rowInt)
    file.close()
    print (matrix)
    return matrix

#Falta revisar repetidos
def initialPopulation(maxIndividuals, positions):
	i = 0
	while i < maxIndividuals:
		print (i)
		individual = list(range(1,positions+1))
		random.shuffle(individual)
		print (individual)
		population.append(individual)
		i += 1

def objectiveFunction(solution):
    sum = 0
    for positionI, elementI in enumerate(solution): #position = ubicacion // elemento = instalacion
        for positionJ, elementJ in enumerate(solution):
            aux = flow[elementI-1][elementJ-1]*distance[positionI][positionJ]
            sum += aux
    return sum


#PRUEBAS------------------------
#flow = [[0,3,0,2],[3,0,0,1],[0,0,0,4],[2,1,4,0]]
#distance = [[0,22,53,0],[22,0,40,0],[53,40,0,55],[0,0,55,0]]
#hola = objectiveFunction([2,1,4,3])
#print (hola)
#PRUEBAS------------------------

#EJECUCIÓN MAIN (PRINCIPAL)
#readFile("Dchr12a.dat")
#readFile("Dchr12a.dat")
#readFile("Dchr12a.dat")
#readFile("Dchr12a.dat")

#initialPopulation(10,12)
#print (population)
#1. readFile
#2. initialPopulation
#3. Pedir generation máxima maxGeneration
#generation = 0
#while generation < maxGeneration
#a. Evaluar
#b. Seleccion
#c. Reproduccion
#    - Recombinacion
#    - Mutacion
#d. Reemplazo
