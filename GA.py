import random
from random import randint
import matplotlib.pyplot as plt

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
    tour_size = 20 #los individuos que participan en el torneo

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

def crossover(parents,mutationProbability):
    offsprings = []
    print("parents: ",len(parents))
    #dominant_parents = random.sample(parents, k=3)
    dominant_parents = []
    index_1 = random.randint(0,len(parents)-1)
    index_2 = random.randint(0,len(parents)-1)
    if index_1 == index_2 and index_2 == len(parents-1):
        index_2 -= 1
    dominant_parents.append(parents[index_1])
    dominant_parents.append(parents[index_2])

    for parent in dominant_parents:
        for p in parents:
            if parent != p:
                crosspoint1 = random.choice(list(range(0, int(len(p['solucion'])/2))))
                crosspoint2 = random.choice(list(range(int(len(p['solucion'])/2),len(p['solucion']))))
                offspring = {
                    'valor_objetivo': 0,
                    'solucion': [0]*len(p['solucion'])
                }
                offspring['solucion'][crosspoint1:crosspoint2+1] = parent['solucion'][crosspoint1:crosspoint2+1] #copio tal cual el padre dominante

                if crosspoint2 != len(p['solucion'])-1:
                    crosspoint2+=1
                    crosspoint2_p = crosspoint2 #padre no dominante
                    crosspoint2_os = crosspoint2 #offspring
                else:
                    crosspoint2 = 0
                    crosspoint2_p = crosspoint2 #padre no dominante
                    crosspoint2_os = crosspoint2 #offspring

                while 0 in offspring['solucion']:
                    if p['solucion'][crosspoint2_p] not in offspring['solucion']:
                        offspring['solucion'][crosspoint2_os] = p['solucion'][crosspoint2_p]
                        if crosspoint2_p != len(p['solucion'])-1:
                            crosspoint2_p+=1
                        else:
                            crosspoint2_p = 0
                        if crosspoint2_os != len(offspring['solucion'])-1:
                            crosspoint2_os+=1
                        else:
                            crosspoint2_os = 0
                    else:
                        if crosspoint2_p != len(p['solucion'])-1:
                            crosspoint2_p+=1
                        else:
                            crosspoint2_p = 0
                offspring['solucion'] = mutation(offspring['solucion'],mutationProbability)
                offsprings.append(offspring)
                print("OFFSPRINGS: ",offsprings)
    return offsprings

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
    plt.xlabel(u"Valor Óptimo : " + str(mejorObjetivo))
    plt.show()


def run(size_population, generations, size_solution,mutationProbability):
    #Genero la poblacion inicial
    population = initialPopulation(size_population,size_solution)
    #printPopulation(population,100)

    #Por cada generacion
    for i in range(generations):
        print("Generation: ",i)
        #Evaluo population
        print("Evaluacion")
        population = evaluatePopulation(population)
        best_objective_value = minPopulation(population)
        of_result.append(best_objective_value['valor_objetivo'])
        solution_result.append(best_objective_value['solucion'])
        #Selecciono padres
        print("Seleccion")
        parents = tournament(population, size_population)
        #printPopulation(parents,10)
        #reprodusco
        offsprings = crossover(parents,mutationProbability)
        print("Reproduccion con len: ",offsprings[0])
        #printPopulation(offsprings,5)

        #reemplazo

        population = replaceOffsprings(offsprings,size_population,population)
        #printPopulation(population,10)
        print("Reemplazo con len: ",len(population))
        print()


    population = evaluatePopulation(population)
    best_objective_value = minPopulation(population)
    of_result.append(best_objective_value['valor_objetivo'])
    solution_result.append(best_objective_value['solucion'])
    graficar(of_result)
############# Valores de entrada ##################
# CAMBIAR!

generations = 200
size_population = 100
size_solution = 12
mutationProbability = 0.2
distance = []
flow = []
of_result = [] #Arreglo de mejor función objetivo de cada generacion
solution_result = [] #Arreglo de solución objetivo de cada generación

distance= readFile("Dchr12a.dat")
flow= readFile("Fchr12a.dat")
#contiene la poblacion final
population = run(size_population, generations, size_solution,mutationProbability)
