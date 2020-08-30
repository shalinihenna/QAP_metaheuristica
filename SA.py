import numpy
import matplotlib.pyplot as plt
import random
import math
from random import randint

distance = []
flow = []
bestObjective= []
temperature= []
alpha= 0
beta= 0


# readFile: función que lee el archivo con los datos
# entrada: nombre del archivo
# salida: matriz con los datos
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

# initialSolution: Función generadora de la población aleatoria inicial
def initialSolution(positions):
    s0= list(range(1, positions+1))
    random.shuffle(s0)
    return s0

#swap
def swap(p0,p1,solution):
    temp = solution[p0]
    solution[p0] = solution[p1]
    solution[p1] = temp
    return solution

# neighborhood:
def neighborhood(solution):
    p0= randint(0,len(distance)-1)
    p1= randint(0,len(distance)-1)
    neighbour= swap(p0,p1,solution)
    return neighbour

def generaVecino(vecino):
    i = random.randint(2, len(vecino) - 1)
    j = random.randint(0, len(vecino) - i)
    vecino[j: (j + i)] = reversed(vecino[j: (j + i)])
    return(vecino)
# Función Objetivo
def objectiveFunction(solution):
    sum = 0
    n = len(solution)
    for i in range(n):
        for j in range(n):
            aux = flow[i][j] * distance[solution[i]-1][solution[j]-1]
            sum += aux
    return sum

# SA: Tmax, Tmin, iteration, funtionT
def SA(Tmax, Tmin, iteration, funtionT):
    s0= initialSolution(len(distance))  #solución inicial
    sCurrent= s0.copy()
    t=Tmax
    mejorObjetivo = objectiveFunction(sCurrent)
    mejorSolucion = sCurrent.copy()
    p= []
    o= [mejorObjetivo]
    ofActual=objectiveFunction(sCurrent)

    while t > Tmin:
        it=0
        #print("-----")
        #print(sCurrent)
        #print("-----")
        while it < iteration:
            #sNew= neighborhood(sCurrent)
            sNew=generaVecino(sCurrent)
            ofNuevo=objectiveFunction(sNew)
            delta= ofNuevo - ofActual
            if delta < 0:
                sCurrent=sNew.copy()
                ofActual=ofNuevo
                if ofNuevo < mejorObjetivo:
                    mejorObjetivo = ofNuevo
                    mejorSolucion = sNew.copy()
            else:
                probability= math.e ** - (delta/t)
                p.append(probability)
                if random.random() < probability:
                    sCurrent= sNew.copy()
                    ofActual=ofNuevo
            o.append(ofActual)
            temperature.append(t)
            it+=1
        bestObjective.append(mejorObjetivo)
        if funtionT == 1:
            t = t - beta
        else:
            t = t * alpha
    print(min(bestObjective))
    print(mejorObjetivo)
    graficar(bestObjective,p)
    graficar(p,p)
    graficar(o,p)
    return s0
#graficar
def graficar(bestObjective,temperature):
    plt.figure(1)
    graficoMejores = plt.plot(bestObjective)
    plt.setp(graficoMejores,"linestyle","none","marker","s","color","b","markersize","1")
    plt.title(u"Simulated annealing QAP")
    plt.ylabel(u"valor objetivo")
    plt.xlabel(u"iteraciones")
    plt.show()

# ---------------------------------
def main():
    print("hola")
    global distance, flow, beta, alpha
    nameD= "Dchr12a.dat"#input('Nombre del archivo de distancias: ')
    nameF= "Fchr12a.dat"#input('Nombre del archivo de flujos: ')
    beta= .2#float(input('Ingrese valor de beta: '))
    alpha= .99#float(input('Ingrese valor de alpha: '))
    Tmax= 60000000#float(input('Ingrese temperatura máxima: '))
    Tmin= 1#float(input('Ingrese temperatura mínima: '))
    iteration= 200#int(input('Ingrese el numero de iteraciones: '))
    distance= readFile(nameD)
    flow= readFile(nameF)
    SA(Tmax, Tmin, iteration, 2)

main()
#Prueba 1
# Dchr12a.dat   Fchr12a.dat
# beta= 0.2  alpha= 0.1  tMax= 50 tMin= 4 iter= 20 solucion= 46028
# beta= 0.1  alpha= 0.2  tMax= 100 tMin= 4 iter= 50 solucion= 49854
# Dchr18a.dat Fchr18a.dat
#
