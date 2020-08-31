import numpy
import matplotlib.pyplot as plt
import random
import math
from random import randint
import time

distance = []
flow = []
bestObjective= []
temperature= []
instances= []
p= []
o= []
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

# Función Objetivo
def objectiveFunction(solution):
    sum = 0
    n = len(solution)
    for i in range(n):
        for j in range(n):
            aux = flow[i][j] * distance[solution[i]-1][solution[j]-1]
            sum += aux
    return sum

# SA:
# entrada:
#           Tmax = temperatura maxima,
#           Tmin = temperatura minima,
#           iteration = máximo de iteraciones internas
#           funtionT = función de enfriamiento
# salida: matriz con los datos
def SA(Tmax, Tmin, iteration, funtionT):
    s0= initialSolution(len(distance))  #Solución inicial
    sCurrent= s0.copy()                 #Solución actual
    t=Tmax                              #Temperatura Máxima
    mejorObjetivo = objectiveFunction(sCurrent)
    mejorSolucion = sCurrent.copy()
    o.append(mejorObjetivo)
    ofActual=objectiveFunction(sCurrent)
    while t > Tmin:
        it=0
        while it < iteration:
            sNew=neighborhood(sCurrent)
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
    #graficar(bestObjective, p, o, mejorObjetivo, temperature)
    return mejorObjetivo

#graficar
def graficar(bestObjective, p, o, mejorObjetivo, temperature):
    graficoMejores = plt.plot(bestObjective)
    plt.setp(graficoMejores,"linestyle","none","marker","s","color","b","markersize","1")
    plt.title(u"Simulated annealing QAP")
    plt.ylabel(u"Valor objetivo")
    plt.xlabel(u"Valor Óptimo : " + str(mejorObjetivo))
    plt.show()

    grafico = plt.plot(o)
    plt.setp(grafico,"linestyle","none","marker","s","color","r","markersize","1")
    plt.ylabel(u"Valor actual")
    plt.xlabel(u"Valor Óptimo : " + str(mejorObjetivo))
    plt.show()

    grafico = plt.plot(p)
    plt.setp(grafico,"linestyle","none","marker","s","color","g","markersize","1")
    plt.ylabel(u"Probabilidad")
    plt.xlabel(u"Valor Óptimo : " + str(mejorObjetivo))
    plt.show()

    grafico = plt.plot(temperature)
    plt.setp(grafico,"linestyle","none","marker","s","color","g","markersize","1")
    plt.ylabel(u"Temperatura")
    plt.xlabel(u"Valor Óptimo : " + str(mejorObjetivo))
    plt.show()

#-------------
def graficar_inst_20(instances):
    graficoMejores = plt.plot(instances)
    plt.setp(graficoMejores,"linestyle","none","marker","s","color","b","markersize","1")
    plt.title(u"Simulated annealing QAP")
    plt.ylabel(u"Valor objetivo")
    plt.xlabel(u"Iteraciones")
    plt.show()

# ---------------------------------
def main():
    print("Simulated annealing QAP")
    global distance, flow, beta, alpha
    nameD= "Dchr12a.dat"#input('Nombre del archivo de distancias: ')
    nameF= "Fchr12a.dat"#input('Nombre del archivo de flujos: ')
    beta= 1             #float(input('Ingrese valor de beta: '))
    alpha= .99          #float(input('Ingrese valor de alpha: '))
    Tmax= 12000000000   #float(input('Ingrese temperatura máxima: '))
    Tmin= 1             #float(input('Ingrese temperatura mínima: '))
    iteration= 100      #int(input('Ingrese el numero de iteraciones: '))
    distance= readFile(nameD)
    flow= readFile(nameF)
    #--------Instancias-----------------
    i=0
    while i < 10:
        start_time = time.time()
        instances.append(SA(Tmax, Tmin, iteration, 2))
        print("--- %s seconds ---" % (time.time() - start_time))
        i+=1
    #------------------------------------
    graficar_inst_20(instances)

main()

#graficar(bestObjective, p, o, mejorObjetivo, temperature)

#Prueba 1
# Dchr12a.dat   Fchr12a.dat
# beta= 0.2  alpha= 0.1  tMax= 50 tMin= 4 iter= 20 solucion= 46028
# beta= 0.1  alpha= 0.2  tMax= 100 tMin= 4 iter= 50 solucion= 49854
# Dchr18a.dat Fchr18a.dat
