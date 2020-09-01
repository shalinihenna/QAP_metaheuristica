import numpy
import matplotlib.pyplot as plt
import random
import math
from random import randint
from numpy import *
import time


distance = []
flow = []
bestObjective= []
temperature= []

inst_best_objetive= []
inst_best_objetive_t= []
inst_best_objetive_current= []
time_instances= []

p= []
o= []
alpha= 0
beta= 0

GA=[[10, 5, 9, 6, 7, 11, 8, 4, 12, 3, 2, 1], array([11,  6,  1,  3,  5, 12,  7,  8,  2, 10,  9,  4]), array([ 7,  5,  1,  3,  2, 10,  8,  6,  4, 11,  9, 12]), array([ 7,  5,  1,  3,  2, 10,  8, 11,  9,  6, 12,  4]), array([ 7,  5,  1, 10,  2,  3, 12, 11,  9,  6,  8,  4]), array([ 7,  1,  5,  8,  2, 10,  3, 11,  9,  6, 12,  4]), array([ 7,  5,  1,  2, 10,  3,  8, 11,  9,  6, 12,  4]), array([ 7,  5,  1,  2, 10,  3,  8, 11,  9,  6, 12,  4]), array([ 7,  5,  1,  2, 10,  3,  8, 11,  9,  6, 12,  4]), array([ 7,  5,  1,  2, 10,  3,  8, 11,  9,  6, 12,  4]), array([ 7,  5, 10,  2,  1,  3,  8, 11,  9,  6, 12,  4]), array([ 7,  5, 10,  2,  1,  3,  8, 11,  9,  6, 12,  4]), array([ 7,  5,  9,  2,  1,  3, 12, 11, 10,  6,  8,  4]), array([ 7,  5, 10,  2,  1,  3,  8, 11, 12,  6,  9,  4]), array([ 7,  5,  8,  2,  1,  3, 10, 11,  9,  6, 12,  4]), array([ 7,  5,  8,  2,  1,  3, 10, 11,  9,  6, 12,  4]), array([ 7,  5,  8,  2,  1,  3, 10, 11, 12,  6,  9,  4]), array([ 7,  5,  8,  2,  1,  3, 10, 11, 12,  6,  9,  4]), array([ 7,  5,  8,  2,  1,  3, 10, 11, 12,  6,  9,  4]), array([ 7,  5,  8,  2,  1,  3, 10, 11, 12,  6,  9,  4]), array([ 7,  5,  8,  2,  1,  3, 10, 11, 12,  6,  9,  4]), array([ 7,  5,  8,  2,  1,  3, 10, 11, 12,  6,  9,  4]), array([ 7,  5,  8,  2,  1,  3, 10, 11, 12,  6,  9,  4]), array([ 7,  5,  8,  2,  1,  3, 10, 11, 12,  6,  9,  4]), array([ 7,  5,  8,  2,  1,  3, 10, 11, 12,  6,  9,  4]), array([ 7,  5,  8,  2,  1,  3, 10, 11, 12,  6,  9,  4]), array([ 7,  5,  8,  2,  1,  3, 10, 11, 12,  6,  9,  4]), array([ 7,  5,  8,  2,  1,  3, 10, 11, 12,  6,  9,  4]), array([ 7,  5,  8,  2,  1,  3, 10, 11, 12,  6,  9,  4]), array([ 7,  5,  8,  2,  1,  3, 10, 11, 12,  6,  9,  4]), array([ 7,  5,  8,  2,  1,  3, 10, 11, 12,  6,  9,  4]), array([ 7,  5,  8,  2,  1,  3, 10, 11, 12,  6,  9,  4]), array([ 7,  5,  8,  2,  1,  3, 10, 11, 12,  6,  9,  4]), array([ 7,  5,  8,  2,  1,  3, 10, 11, 12,  6,  9,  4]), array([ 7,  5,  8,  2,  1,  3, 10, 11, 12,  6,  9,  4]), array([ 7,  5,  8,  2,  1,  3, 10, 11, 12,  6,  9,  4]), array([ 7,  5,  8,  2,  1,  3, 10, 11, 12,  6,  9,  4]), array([ 7,  5,  8,  2,  1,  3, 10, 11, 12,  6,  9,  4]), array([ 7,  5,  8,  2,  1,  3, 10, 11, 12,  6,  9,  4]), array([ 7,  5,  8,  2,  1,  3, 10, 11, 12,  6,  9,  4]), array([ 7,  5,  8,  2,  1,  3, 10, 11, 12,  6,  9,  4]), array([ 7,  5,  8,  2,  1,  3, 10, 11, 12,  6,  9,  4]), array([ 7,  5,  8,  2,  1,  3, 10, 11, 12,  6,  9,  4]), array([ 7,  5,  8,  2,  1,  3, 10, 11, 12,  6,  9,  4]), array([ 7,  5,  8,  2,  1,  3, 10, 11, 12,  6,  9,  4]), array([ 7,  5,  8,  2,  1,  3, 10, 11, 12,  6,  9,  4]), array([ 7,  5,  8,  2,  1,  3, 10, 11, 12,  6,  9,  4]), array([ 7,  5,  8,  2,  1,  3, 10, 11, 12,  6,  9,  4]), array([ 7,  5,  8,  2,  1,  3, 10, 11, 12,  6,  9,  4]), array([ 7,  5,  8,  2,  1,  3, 10, 11, 12,  6,  9,  4]), array([ 7,  5,  8,  2,  1,  3, 10, 11, 12,  6,  9,  4])]

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
    global o,bestObjective
    o=[]
    bestObjective= []
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
    inst_best_objetive_current.append(o)
    inst_best_objetive_t.append(bestObjective)

    return mejorObjetivo


# Grafica_ grafico con los mejores obetivos, la probabilidad de aceptación,
# el mejor objetivo encontrado por cada temperatura, y la funcion de temperatura
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
    plt.setp(grafico,"linestyle","none","marker","s","color","indigo","markersize","1")
    plt.ylabel(u"Probabilidad")
    plt.xlabel(u"Valor Óptimo : " + str(mejorObjetivo))
    plt.show()

    grafico = plt.plot(temperature)
    plt.setp(grafico,"linestyle","none","marker","s","color","g","markersize","1")
    plt.ylabel(u"Temperatura")
    plt.xlabel(u"Valor Óptimo : " + str(mejorObjetivo))
    plt.show()

#------------------
# Grafico de las 20 instancias al ejecutar una misma configuración
def graficar_inst_20(instancesO,instancesC):
    #x=range(20)
    graficoMejores = plt.plot(instancesO)
    plt.setp(graficoMejores,"linestyle","none","marker","s","color","b","markersize","1")
    plt.title(u"Simulated annealing QAP")
    plt.ylabel(u"Valor objetivo")
    plt.xlabel(u"Instancia")
    plt.show()

    colors =  ['black','red','gray','orange','gold','yellow','green','aqua','blue','indigo','pink','magenta','cyan','purple', 'teal'
    , 'lime','turquoise','coral','navy','brown']

    #print(len(instancesC))
    cont=0
    for i in instancesC:
        graficoMejores = plt.plot(i)
        plt.setp(graficoMejores,"linestyle","none","marker","s","color",colors[cont],"markersize","1")
        cont+=1
    plt.title(u"Simulated annealing QAP")
    plt.ylabel(u"Valor objetivo")
    plt.xlabel(u"Iteraciones")
    plt.show()

#------------------
# Gráfico de cajas y bigotes
# Comparativa de metaheuristicas con configuraciones iguales
def grafico_cajas(ov_meta1, ov_meta2):
    d1=list(set(ov_meta1))
    d2=list(set(ov_meta2))
    print("d1 ov_meta1", d1)
    print("d2 ov_meta2", d2)
    data=[d1,d2]
    fig,ax = plt.subplots()
    ax.set_title('Comparativa entre dos metaheuristicas distintas')
    ax.boxplot(data)
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
    while i < 20:
        start_time = time.time()
        inst_best_objetive.append(SA(Tmax, Tmin, iteration, 2))
        time_instances.append((time.time() - start_time))
        print("--- %s seconds ---" % (time.time() - start_time))
        i+=1
    #------------------------------------
    ov_GA=[]
    for elem in GA:
        ov_GA.append(objectiveFunction(elem))
    print(min(inst_best_objetive_t[0]))
    #graficar_inst_20(inst_best_objetive, inst_best_objetive_current)
    grafico_cajas(inst_best_objetive_t[0], ov_GA)

main()

#graficar(bestObjective, p, o, mejorObjetivo, temperature)
