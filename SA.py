import numpy
#import matplotlib.pyplot as plt
import random
import math

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
    print(readFile("Dchr12a.dat"))
    return matrix

def initialSolution():
    individual = list(range(1,positions+1))
    random.shuffle(individual)
# Función SA
#def SA(Tmax, Tmin, ):
