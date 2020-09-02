import numpy
import matplotlib.pyplot as plt
import random
import math
from random import randint
from numpy import *
import time


distance = []
flow = []
bestObjective= [] # mejores objetivos de cada temperatura
temperature= []
p= []
o= [] # mejores objetivos actuales para cada iteracion con UNA temperatura
#------------- Instancias 20 ---------------
time_instances= []
inst_best_objetive= []          # mejor objetivo de SA
inst_best_objetive_t= []        # mejores objetivos de cada temperatura
inst_best_objetive_current= []  # mejores objetivos para cada iteracion con UNA temperatura
#-------------------------------------------
#------------- Grafico dual---------------
bestObjective_dual= []
temperature_dual= []
p_dual= []
o_dual= []
#-------------------------------------------


GA=[11370, 11688, 9552, 11326, 15496, 12142, 12300, 14108, 10202, 11326, 13184, 13372, 10096, 12250, 12222, 10612, 11924, 10192, 11518, 11668]
SA=[16346, 17324, 15390, 15540, 17068, 11538, 13838, 17354, 16742, 15144, 16068, 18214, 15184, 16392, 16262, 16668, 15920, 16764, 17400, 15694]

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
def SA(Tmax, Tmin, iteration, alpha):
    global o,p,bestObjective,temperature
    o=[]
    p=[]
    bestObjective=[]
    temperature=[]
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
        t = t * alpha

    inst_best_objetive_current.append(o)
    inst_best_objetive_t.append(bestObjective)
    #graficar(bestObjective, p, o, mejorObjetivo, temperature)

    return mejorObjetivo


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

    '''grafico = plt.plot(p)
    plt.setp(grafico,"linestyle","none","marker","s","color","g","markersize","1")
    plt.ylabel(u"Probabilidad")
    plt.xlabel(u"Valor Óptimo : " + str(mejorObjetivo))
    plt.show()

    grafico = plt.plot(temperature)
    plt.setp(grafico,"linestyle","none","marker","s","color","g","markersize","1")
    plt.ylabel(u"Temperatura")
    plt.xlabel(u"Valor Óptimo : " + str(mejorObjetivo))
    plt.show()'''
# Grafico de las 20 instancias al ejecutar una misma configuración
def graficar_inst_20(instancesO,instancesC):
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

    cont=0
    for i in instancesC:
        graficoMejores = plt.plot(i)
        plt.setp(graficoMejores,"linestyle","none","marker","s","color",colors[cont],"markersize","1")
        cont+=1
    plt.title(u"Simulated annealing QAP")
    plt.legend(y)
    plt.ylabel(u"Valor objetivo")
    plt.xlabel(u"Iteraciones")
    plt.show()

#----------------- Gráfico de cajas y bigotes---------------------
# Comparativa de metaheuristicas con configuraciones iguales
def grafico_cajas(ov_meta1, ov_meta2):
    #d1=list(set(ov_meta1))
    #d2=list(set(ov_meta2))
    print("d1 ov_meta1", ov_meta1)
    print("d2 ov_meta2", ov_meta2)
    data=[ov_meta1,ov_meta2]
    fig,ax = plt.subplots()
    ax.set_title('Comparativa entre dos metaheuristicas distintas')
    ax.boxplot(data)
    plt.show()


# ------------ MAIN ---------------------
def main():
    print("Simulated annealing QAP")
    global distance, flow
    mejorObjetivo_dual=[]

    #------------------ CONFIGURACION-------------------------

    alpha= .99         #float(input('Ingrese valor de alpha: '))
    Tmax= 10000         #float(input('Ingrese temperatura máxima: '))
    Tmin= 1             #float(input('Ingrese temperatura mínima: '))
    iteration= 100       #int(input('Ingrese el numero de iteraciones: '))

    nameD= "Dchr25a.dat"#input('Nombre del archivo de distancias: ')
    nameF= "Fchr25a.dat"#input('Nombre del archivo de flujos: ')
    distance= readFile(nameD)
    flow= readFile(nameF)

    #SA(Tmax, Tmin, iteration, alpha)
    i=0
    while i < 20:
        start_time = time.time()
        inst_best_objetive.append(SA(Tmax, Tmin, iteration, alpha))
        time_instances.append((time.time() - start_time))
        print("--- %s seconds ---" % (time.time() - start_time))
        i+=1
    #------------------------------------
    #print(inst_best_objetive)
    graficar_inst_20(inst_best_objetive, inst_best_objetive_current)

    #------------------COMPARATION-------------------------
    #ov_GA=[]
    #for elem in GA:
    #    ov_GA.append(objectiveFunction(elem))
    #GA=[11370, 11688, 9552, 11326, 15496, 12142, 12300, 14108, 10202, 11326, 13184, 13372, 10096, 12250, 12222, 10612, 11924, 10192, 11518, 11668]
    #SA=[16346, 17324, 15390, 15540, 17068, 11538, 13838, 17354, 16742, 15144, 16068, 18214, 15184, 16392, 16262, 16668, 15920, 16764, 17400, 15694]
    #grafico_cajas(SA,GA)


main()
