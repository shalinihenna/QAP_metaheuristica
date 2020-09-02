import random
from random import randint
import matplotlib.pyplot as plt
import numpy as np
import time

"""
    La poblacion se define como una lista que contiene un diccionario entonces

    population[0] = {
        'solucion': [1,2,3,5,6],
        'valor_objetivo': 12
    }
"""

def swap(p0,p1,solution):
    temp = solution[p0]
    solution[p0] = solution[p1]
    solution[p1] = temp
    return solution

def neighborhood(solution):
    p0= randint(0,len(solution)-1)
    p1= randint(0,len(solution)-1)
    neighbour= swap(p0,p1,solution)
    return neighbour

def objectiveFunction(solution):
    sum = 0
    n = len(solution)
    for i in range(n):
        for j in range(n):
            aux = flow[i][j] * distance[solution[i]-1][solution[j]-1]
            sum += aux
    return sum

def evaluatePopulation(population):
    m = len(population)
    for i in range(m):
        of_value = objectiveFunction(population[i]['solucion'])
        population[i]['valor_objetivo'] = of_value
    return population


############# Torneo ##################
def minPopulation(population):
    best_index = 0
    best_value = 99999999
    m = len(population)
    for i in range(m):
        if population[i]['valor_objetivo'] <= best_value:
            best_index = i
            best_value = population[i]['valor_objetivo']
    return population[best_index]


def tournament(population, size_population):
    parents = []

    tour_times = 50 #para la cantidad de padres
    tour_size = 5 #los individuos que participan en el torneo

    for _ in range(tour_times):
        tournament = []
        for _ in range(tour_size):
            index = random.randint(0, size_population - 1)
            tournament.append(population[index])

        best = minPopulation(tournament)
        parents.append(best)
    return parents

############# Poblacion inicial ##################

def generateRandomSolution(size):
    inst = list(range(1, size + 1))
    random.shuffle(inst)
    return inst

def initialPopulation(size_population, size_solution):
    #Genera una poblacion de forma aleatoria
    population = []
    for _ in range(size_population):
        individual = {
            'valor_objetivo': 0,
            'solucion': generateRandomSolution(size_solution)
        }

        population.append(individual)

    return population
####################################################



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

def printPopulation(arr, number):
    for i in range(number):
        print(f"    {arr[i]}")
    print()

def mutation(offspring,mutationProbability):
    probability = random.random()
    if probability < mutationProbability:
        offspring = neighborhood(offspring)
    return offspring


def recombination(parents,mutationProbability,offsprings_size):
    offsprings = []
    it_offspring = 0
    while it_offspring < offsprings_size:
        p = random.sample(parents, k=2)
        offspring1, offspring2 = one_point_crossover(p[0]['solucion'],p[1]['solucion'])
        offspring_1 = {
            'valor_objetivo': 0,
            'solucion': offspring1
        }
        offspring_2 = {
            'valor_objetivo': 0,
            'solucion': offspring2
        }
        offspring_1['solucion'] = mutation(offspring_1['solucion'],mutationProbability)
        offspring_2['solucion'] = mutation(offspring_2['solucion'],mutationProbability)
        offsprings.append(offspring_1)
        offsprings.append(offspring_2)
        it_offspring += 2
    return offsprings

def one_point_crossover(parent1, parent2):
    #x = int((len(parent1))/2)
    x = int(len(parent1)/2)
    offspring1_new = np.append(parent1[:x], [0]*x)
    i = x
    while 0 in offspring1_new:
        for element in parent2:
            if element not in offspring1_new:
                offspring1_new[i] = element
                i+=1
    j = x
    offspring2_new = np.append(parent2[:x], [0]*x)
    while 0 in offspring2_new:
        for element in parent1:
            if element not in offspring2_new:
                offspring2_new[j] = element
                j+=1
    return offspring1_new, offspring2_new

def replaceOffsprings(offsprings, size_population,population):
    new_population = []
    new_population = offsprings + population
    new_population = sorted(new_population, key=lambda k: k['valor_objetivo'])
    aux = []
    for i in range(0,size_population):
        aux.append(new_population[i])
    return aux

def graficar(mejorObjetivo):
    graficoMejores = plt.plot(of_result)
    plt.setp(graficoMejores,"linestyle","none","marker","s","color","b","markersize","1")
    plt.title(u"Algoritmo Genético QAP")
    plt.ylabel(u"Valor objetivo")
    plt.xlabel(u"Valor Óptimo : " + str(min(mejorObjetivo)))
    plt.show()


def run(size_population, generations, size_solution,mutationProbability):
    #Genero la poblacion inicial
    of_result= []
    solution_result= []
    population = initialPopulation(size_population,size_solution)
    #printPopulation(population,100)
    #Por cada generacion
    for i in range(generations):
        #Evaluo population
        population = evaluatePopulation(population)
        best_objective_value = minPopulation(population)
        of_result.append(best_objective_value['valor_objetivo'])
        solution_result.append(best_objective_value['solucion'])
        #Selecciono padres
        parents = tournament(population, size_population)
        #printPopulation(parents,10)
        #reprodusco
        offsprings = recombination(parents,mutationProbability,size_population)
        #printPopulation(offsprings,10)
        #reemplazo
        population = replaceOffsprings(offsprings,size_population,population)
        #printPopulation(population,10)
        random.shuffle(population)


    population = evaluatePopulation(population)
    best_objective_value = minPopulation(population)
    of_result.append(best_objective_value['valor_objetivo'])
    solution_result.append(best_objective_value['solucion'])

    return of_result


    print("SOLUTION_RESULT: ",solution_result)

#------------------
# Grafico de las 20 instancias al ejecutar una misma configuración
def graficar_inst_20(instancesO,instancesC):
    #x=range(20)
    mejorObjetivo=min(instancesO)
    graficoMejores = plt.plot(instancesO)
    plt.setp(graficoMejores,"linestyle","none","marker","s","color","b","markersize","1")
    plt.title(u"Simulated annealing QAP")
    plt.ylabel(u"Valor objetivo")
    plt.xlabel(u"Valor Óptimo : " + str(mejorObjetivo))
    plt.show()

    colors =  ['black','red','gray','orange','gold','yellow','green','aqua','blue','indigo','pink','magenta','cyan','purple', 'teal', 'lime','turquoise','coral','navy','brown']
    y=['Instancia 1', 'Instancia 2','Instancia 3', 'Instancia 4','Instancia 5', 'Instancia 6','Instancia 7', 'Instancia 8','Instancia 9', 'Instancia 10',
    'Instancia 11', 'Instancia 12','Instancia 13', 'Instancia 14','Instancia 15', 'Instancia 16','Instancia 17', 'Instancia 18','Instancia 19','Instancia 20']

    print(len(instancesC))
    cont=0
    for i in instancesC:
        graficoMejores = plt.plot(i)
        plt.setp(graficoMejores,"linestyle","none","marker","s","color",colors[cont],"markersize","1")
        cont+=1
    plt.title(u"Algoritmo Genetico QAP")
    plt.ylabel(u"Valor objetivo")
    plt.legend(y)
    plt.xlabel(u"Iteraciones")
    plt.show()

############# Valores de entrada ##################
# CAMBIAR!
time_instances= []
inst_best_objetive= []
inst_best_objetive_current= []
generations = 50
size_population = 1000

size_solution = 12
mutationProbability = 0.5
distance = []
flow = []
of_result = [] #Arreglo de mejor función objetivo de cada generacion
solution_result = [] #Arreglo de solución objetivo de cada generación

distance= readFile("Dchr12a.dat")
flow= readFile("Fchr12a.dat")
#contiene la poblacion final
#population = run(size_population, generations, size_solution,mutationProbability)
#--------Instancias-----------------
i=0
while i < 20:
    start_time = time.time()
    ints= run(size_population, generations, size_solution,mutationProbability)
    inst_best_objetive_current.append(ints)
    inst_best_objetive.append(min(ints))
    time_instances.append((time.time() - start_time))
    print("--- %s seconds ---" % (time.time() - start_time))
    i+=1
#------------------------------------
print(inst_best_objetive)
graficar_inst_20(inst_best_objetive, inst_best_objetive_current)
