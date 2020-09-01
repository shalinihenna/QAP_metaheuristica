import random
from random import randint
from operator import itemgetter
import matplotlib.pyplot as plt

#VARIABLES GLOBALES
population = [] #Arreglo de arreglos
of_result = [] #Arreglo de mejor función objetivo de cada generacion
solution_result = [] #Arreglo de solución objetivo de cada generación
flow = [] #Datos de la matriz de flujo
distance = [] #Datos de la matriz de distancias
population_with_ov = [] #Solución (arreglo) con su valor objetivo

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

#Swap entre dos valores de una solución
def swap(p0,p1,solution):
    temp = solution[p0]
    solution[p0] = solution[p1]
    solution[p1] = temp
    return solution

#Función swap para generar vecino:1
def neighborhood(solution):
    p0= randint(0,len(solution)-1)
    p1= randint(0,len(solution)-1)
    #print("swap entre posicion: ",p0,"y ",p1)
    neighbour= swap(p0,p1,solution)
    return neighbour

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
def evaluate(populations,attach):
    ov_population = [] #Objective values: Valores objetivos de cada individuo de la población
    i = 0
    while i < len(populations):
        #print("i: ",i, end = '')
        ov_population.append(objectiveFunction(populations[i]))
        '''
        if attach:
            aux = [populations[i],objectiveFunction(populations[i])]
            population_with_ov.append(aux)'''
        i += 1
    return ov_population

def evaluate_population(attach):
    ov_population = [] #Objective values: Valores objetivos de cada individuo de la población
    i = 0
    while i < len(population):
        ov_population.append(objectiveFunction(population[i]))
        if attach:
            aux = [population[i],objectiveFunction(population[i])]
            population_with_ov.append(aux)
        i += 1
    return ov_population

#Selección por Torneo
def selection_tournament(maxParents,maxIndividuals):
    #print("population: ", population)
    parents = []
    length_tournament = round(0.1*maxIndividuals)
    it_parent = 0

#
    while it_parent < maxParents:
        copy_population = population
        random_population = []
        for i  in range(0,length_tournament):
            index = random.randint(0,len(copy_population)-1)
            if copy_population[index] not in random_population:
                random_population.append(copy_population[index])


        #random_population = random.sample(copy_population,length_tournament)

        #Escoge el mejor de los guardados en random_population
        ov_population = evaluate(random_population,False)
        minIndividual_index = ov_population.index(min(ov_population))
        possible_parent = random_population[minIndividual_index]
        #print("random_p: ", random_population)
        #print("ov_population: ",ov_population)
        #print("pp ", possible_parent)
        parents.append(possible_parent)
        it_parent += 1
    #print("while maxParents terminada")
    #print("Parents: ",parents)
    #print()
    return parents

#Recombinación ordenada escogiendo 2 padres dominantes y cruzando esos dos con los demás
def crossover(parents):
    offsprings = []
    dominant_parents = random.sample(parents, k=2)
    #print("dominant: ", dominant_parents)
    for parent in dominant_parents:
        for p in parents:
            if parent != p:
                #print(len(p))
                crosspoint1 = random.choice(range(0, int(len(p)/2)))
                crosspoint2 = random.choice(range(int(len(p)/2),len(p)))
                #print("cp1: ",crosspoint1, "cp2: ", crosspoint2)
                offspring = [0]*len(p)
                #print ("offspring1: ",offspring)
                offspring[crosspoint1:crosspoint2+1] = parent[crosspoint1:crosspoint2+1] #copio tal cual el padre dominante
                #print ("offspring_medio: ",offspring)

                if crosspoint2 != len(p)-1:
                    crosspoint2+=1
                    crosspoint2_p = crosspoint2 #padre no dominante
                    crosspoint2_os = crosspoint2 #offspring
                else:
                    crosspoint2 = 0
                    crosspoint2_p = crosspoint2 #padre no dominante
                    crosspoint2_os = crosspoint2 #offspring

                while 0 in offspring:
                    if p[crosspoint2_p] not in offspring:
                        offspring[crosspoint2_os] = p[crosspoint2_p]
                        if crosspoint2_p != len(p)-1:
                            crosspoint2_p+=1
                        else:
                            crosspoint2_p = 0
                        if crosspoint2_os != len(offspring)-1:
                            crosspoint2_os+=1
                        else:
                            crosspoint2_os = 0
                    else:
                        if crosspoint2_p != len(p)-1:
                            crosspoint2_p+=1
                        else:
                            crosspoint2_p = 0

                #print ("offspring_final: ",offspring)
                offsprings.append(offspring)
    return offsprings

#Mutación aplicada a una probabilidad a cada hijo
def mutation(offsprings,mutationProbability):
    #print()
    #print("OFFSPRINGS: ",offsprings)
    for os in offsprings:
        indice = offsprings.index(os)
        probability = random.random()
        #print("probabilidad: ",probability)
        if probability < mutationProbability:
            #print("hijo anterior: ",os)
            os = neighborhood(os)
            #print("hijo mutado: ",os)
            offsprings[indice] = os
            #GUardar en la misma posición de la lista
    #print ("OFFSPRINGS mutated:",offsprings)
    return offsprings

#Formar una sóla lista con la solución y su valor objetivo
def attachOV(offsprings):
    offsprings_with_ov = []
    ov_offsprings = evaluate(offsprings, False)
    for i in range(0,len(offsprings)):
        aux = [offsprings[i],ov_offsprings[i]]
        offsprings_with_ov.append(aux)
    return offsprings_with_ov

#Reemplazo de los hijos en la nueva población para la siguiente generación:
def replaceOffsprings(offsprings, maxIndividuals):
    new_population = []
    offsprings_with_ov = attachOV(offsprings)
    new_population = offsprings_with_ov + population_with_ov
    new_population = sorted(new_population, key=itemgetter(1))
    aux = []
    for i in range(0,maxIndividuals):
        aux.append(new_population[i])
    return aux

def deattach(solutions):
    just_solutions = []
    for element in solutions:
        just_solutions.append(element[0])
    return just_solutions

def graficar(mejorObjetivo):
    graficoMejores = plt.plot(of_result)
    plt.setp(graficoMejores,"linestyle","none","marker","s","color","b","markersize","1")
    plt.title(u"Algoritmo Genético QAP")
    plt.ylabel(u"Valor objetivo")
    plt.xlabel(u"Valor Óptimo : " + str(mejorObjetivo))
    plt.show()

#--------------MAIN------------
#Copiar y pegar en una función AG()



#PRUEBAS------------------------

fileNameFlow = input("Ingrese el nombre del archivo de flujo: ")
fileNameDistance = input("Ingrese el nombre del archivo de distancias: ")
flow = readFile(fileNameFlow)
distance = readFile(fileNameDistance)
maxIndividuals = int(input("Ingrese la cantidad maxima de individuos en una poblacion: "))
maxGenerations = int(input("Ingrese la cantidad maxima de generaciones: "))
mutationProbability = float(input("Ingrese una probabilidad de mutacion: "))
initialPopulation(maxIndividuals, len(distance[0]))

#parents = selection_tournament(int(maxIndividuals/2),maxIndividuals)
#print("population_with_ov: ",population_with_ov)
#parents=[[1,2,3,4,5,6,7,8,9],[9,3,7,8,2,6,5,1,4]]
#print("\nparents2: ",parents)
#crossover(parents)
#hola = mutation(parents,0.2)

#AG()

generation = 0
while generation < maxGenerations:
    print("----------------------------------")
    print("--------------GENERATION ",generation,"---------------")
    print("----------------------------------")
    #a. Evaluar
    #print("population",population)
    print("Evaluacion: ")
    ov_population = evaluate_population(True)
    #print("ov_population: ",ov_population)
    #print("population: ",population)
    #print("population with ov: ",population_with_ov)
    #print("ov_population",ov_population)
    of_result.append(min(ov_population))
    solution_result.append(population[ov_population.index(min(ov_population))])
    #print ("of_result",of_result)
    #print ("solution_result", solution_result)
    #print()
#--------------------------------------
    #b. Seleccion de los padres
    print("Seleccion: ")
    #print("pop: ", population)
    parents = selection_tournament(int(maxIndividuals/2),maxIndividuals)
#--------------------------------------
    #c. Reproduccion
    #    - Recombinacion
    print("Recombinacion: ")
    offsprings = crossover(parents)
#--------------------------------------
    #    - Mutacion
    print("Mutacion: ")
    offsprings_mutated = mutation(offsprings,mutationProbability)
    #print("HIJOS NUEVOS: ",offsprings_mutated)
#--------------------------------------
    #d. Reemplazo
    print("Reemplazo: ")
    new_population = replaceOffsprings(offsprings_mutated,maxIndividuals)
    #print()
    #print()
    #print("new_population: ",new_population)
    new_solutions = deattach(new_population)
#    print("new_solutions: ", new_solutions)
    population = new_solutions.copy()
    #print("population nueva: ", population)
    #print("POBLACION FINAL DEL GENERATE: ", population)
#--------------------------------------
    generation += 1
    print()

new_ov = evaluate_population(False)
best_objective_value = min(new_ov)
best_solution = population[new_ov.index(best_objective_value)]
of_result.append(best_objective_value)
solution_result.append(best_solution)
graficar(best_objective_value)
