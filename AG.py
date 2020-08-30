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

'''
def objectiveFunction(solution):
    sum = 0
    print(list(enumerate(solution)))
    for positionI, elementI in enumerate(solution): #position = ubicacion // elemento = instalacion
        print ("i: ", positionI, elementI-1)
        for positionJ, elementJ in enumerate(solution):
            print ("j: ", positionJ, elementJ-1)
            aux = flow[elementI-1][elementJ-1]*distance[positionI][positionJ]
            #print ("aux: ",aux)
            sum += aux
        print ("suma de iteracion i",positionI,": ",sum)
        print()
    return sum
'''

def objectiveFunction(solution):
    sum = 0
    n = len(solution)
    for i in range(n):
        for j in range(n):
            aux = flow[i][j] * distance[solution[i]-1][solution[j]-1]
            sum += aux
    return sum

#PRUEBAS------------------------
#flow = [[0,3,0,2],[3,0,0,1],[0,0,0,4],[2,1,4,0]]
#distance = [[0,22,53,0],[22,0,40,0],[53,40,0,55],[0,0,55,0]]
flow = readFile("Fchr18a.dat")
distance = readFile("Dchr18a.dat")
#hola = objectiveFunction([7,5,12,2,1,3,9,11,10,6,8,4])
#hola2 = funcionObjetivo([7,5,12,2,1,3,9,11,10,6,8,4],flow,distance)
#hola = objectiveFunction([3,13,6,4,18,12,10,5,1,11,8,7,17,14,9,16,15,2])
#hola2 = funcionObjetivo([3,13,6,4,18,12,10,5,1,11,8,7,17,14,9,16,15,2],flow,distance)
#print (hola)
#print(hola2)
#print(hola2)
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
