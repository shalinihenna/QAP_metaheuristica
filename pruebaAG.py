import random
from random import randint
from operator import itemgetter
import matplotlib.pyplot as plt

flow = [] #Datos de la matriz de flujo
distance = [] #Datos de la matriz de distancias
population = []
population_with_ov = [] #Solución (arreglo) con su valor objetivo
of_result = [] #Arreglo de mejor función objetivo de cada generacion
solution_result = [] #Arreglo de solución objetivo de cada generación

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

def initialPopulation(maxIndividuals, positions):
	i = 0
	while i < maxIndividuals:
		#print (i)
		individual = list(range(1,positions+1))
		random.shuffle(individual)
		#print (individual)
		population.append(individual)
		i += 1

def objectiveFunction(solution):
    sum = 0
    n = len(solution)
    for i in range(n):
        for j in range(n):
            aux = flow[i][j] * distance[solution[i]-1][solution[j]-1]
            sum += aux
    return sum

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

def selection_tournament(maxParents,maxIndividuals):
    parents = []
    length_tournament = round(0.1*maxIndividuals)
    it_parent = 0

    while it_parent < maxParents:
        copy_population = population
        random_population = []
        '''for i  in range(0,length_tournament):
            index = random.randint(0,len(copy_population)-1)
            random_population.append(copy_population[index])'''
        random_population = random.sample(copy_population,length_tournament)

        #Escoge el mejor de los guardados en random_population
        ov_population = evaluate(random_population,False)
        minIndividual_index = ov_population.index(min(ov_population))
        possible_parent = random_population[minIndividual_index]
        parents.append(possible_parent)
        it_parent += 1
    print("Parents: ",parents)
    print()
    return parents

def GA(maxIndividuals, maxGenerations, mutationProbability):
    initialPopulation(maxIndividuals,len(distance[0]))

    generation = 0
    while generation < maxGenerations:
        print("--------------GENERATION ",generation,"---------------")
        print("Evaluacion: ")
        ov_population = evaluate_population(True)
        of_result.append(min(ov_population))
        solution_result.append(population[ov_population.index(min(ov_population))])

        print("Seleccion: ")
        parents = selection_tournament(int(maxIndividuals/2),maxIndividuals)

        generation+=1

def main():
    print("AG QAP")
    global distance, flow
    nameD= "Dchr12a.dat"#input('Nombre del archivo de distancias: ')
    nameF= "Fchr12a.dat"#input('Nombre del archivo de flujos: ')
    maxIndividuals = 1000      #int(input('Ingrese el numero de iteraciones: '))
    maxGenerations = 20
    mutationProbability = 0.2
    distance= readFile(nameD)
    flow= readFile(nameF)

    GA(maxIndividuals,maxGenerations,mutationProbability)

main()
