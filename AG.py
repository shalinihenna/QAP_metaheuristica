import random

population = [] #Arreglo de arreglos
results = [] #Arreglo de mejor función objetivo de cada generacion


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
    print (matrix)
    return matrix

#Falta revisar repetidos 
def initialPopulation(maxIndividuals, positions):
	i = 0
	while i < maxIndividuals:
		print (i)
		individual = list(range(1,positions+1))
		random.shuffle(individual)
		print (individual)
		population.append(individual)
		i += 1


#initialPopulation(10,12)
#print (population)
#readFile("Dchr12a.dat")