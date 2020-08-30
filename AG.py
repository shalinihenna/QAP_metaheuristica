import random

#VARIABLES GLOBALES
population = [] #Arreglo de arreglos
of_result = [] #Arreglo de mejor función objetivo de cada generacion
solution_result = [] #Arreglo de solución objetivo de cada generación
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
#Generar la población inicial
def initialPopulation(maxIndividuals, positions):
	i = 0
	while i < maxIndividuals:
		#print (i)
		individual = list(range(1,positions+1))
		random.shuffle(individual)
		#print (individual)
		population.append(individual)
		i += 1

#Evaluación de una solución en la función objetivo
def objectiveFunction(solution):
    sum = 0
    n = len(solution)
    for i in range(n):
        for j in range(n):
            aux = flow[i][j] * distance[solution[i]-1][solution[j]-1]
            sum += aux
    return sum

#Evaluación de cada individuo de la población en la función objetivo
def evaluate(population):
    ov_population = [] #Objective values: Valores objetivos de cada individuo de la población
    i = 0
    while i < len(population):
        ov_population.append(objectiveFunction(population[i]))
        i += 1
    return ov_population

#Selección por Torneo
def selection_tournament(maxParents,maxIndividuals):
    parents = []
    length_tournament = round(0.3*maxIndividuals)
    it_parent = 0
    while it_parent < maxParents:
        copy_population = population.copy()
        random_population = []
        i = 0
        print("------------------------")
        print("length_tournament",length_tournament)
        while i < length_tournament:
            print("i: ",i)
            randIndividual = random.choice(copy_population)
            random_population.append(randIndividual)
            print("random_population: ",random_population)
            copy_population.remove(randIndividual)
            print("copy_population",copy_population)
            print()
            i += 1

        #Escoge el mejor de los guardados en random_population
        ov_population = evaluate(random_population)
        print("ov_population: ", ov_population)
        minIndividual_index = ov_population.index(min(ov_population))
        possible_parent = random_population[minIndividual_index]
        while possible_parent in parents:
            print("entro")
            random_population.remove(possible_parent)
            if len(random_population) == 0:
                break
            else:
                ov_population = evaluate(random_population)
                print("ov_population: ", ov_population)
                minIndividual_index = ov_population.index(min(ov_population))
                possible_parent = random_population[minIndividual_index]

        parents.append(random_population[ov_population.index(min(ov_population))])
        print("Parents: ",parents)
        it_parent += 1

#PRUEBAS------------------------
#flow = [[0,3,0,2],[3,0,0,1],[0,0,0,4],[2,1,4,0]]
#distance = [[0,22,53,0],[22,0,40,0],[53,40,0,55],[0,0,55,0]]

#hola = objectiveFunction([7,5,12,2,1,3,9,11,10,6,8,4])
#hola2 = funcionObjetivo([7,5,12,2,1,3,9,11,10,6,8,4],flow,distance)
#hola = objectiveFunction([3,13,6,4,18,12,10,5,1,11,8,7,17,14,9,16,15,2])
#hola2 = funcionObjetivo([3,13,6,4,18,12,10,5,1,11,8,7,17,14,9,16,15,2],flow,distance)
#print (hola)
#print(hola2)
#print(hola2)
#PRUEBAS------------------------

#--------------MAIN------------
#Copiar y pegar en una función AG()
def AG():
    generation = 0
    while generation < maxGenerations:
        #a. Evaluar
        print("population",population)
        ov_population = evaluate(population)
        print("ov_population",ov_population)
        of_result.append(min(ov_population))
        solution_result.append(population[ov_population.index(min(ov_population))])
        print ("of_result",of_result)
        print ("solution_result", solution_result)
        print()

        #b. Seleccion de los padres
        #selection_tournament(maxIndividuals/2,maxIndividuals)

        #c. Reproduccion
        #    - Recombinacion
        #    - Mutacion
        #d. Reemplazo
        generation += 1


fileNameFlow = input("Ingrese el nombre del archivo de flujo: ")
fileNameDistance = input("Ingrese el nombre del archivo de distancias: ")
flow = readFile(fileNameFlow)
distance = readFile(fileNameDistance)
maxIndividuals = int(input("Ingrese la cantidad maxima de individuos en una poblacion: "))
maxGenerations = int(input("Ingrese la cantidad maxima de generaciones: "))
initialPopulation(maxIndividuals, len(distance[0]))
selection_tournament(int(maxIndividuals/2),maxIndividuals)
#AG()
