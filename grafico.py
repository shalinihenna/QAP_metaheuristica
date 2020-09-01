# --------------------Grafico DUAL -------------------------------
# grafico con los mejores obetivos, probabilidad de aceptación,
# el mejor objetivo encontrado por cada temperatura, y la funcion de temperatura
def graficar(bestObjective, p, o, mejorObjetivo, temperature):
    # --------------------Mejores valores objetivos-------------------------------
    #print(bestObjective)
    print("o[0]")
    print(len(o[0]))
    print("o[1]")
    print(len(o[1]))
    exit()
    plt.figure(1, figsize=(10,10))
    plt.subplot(2, 1, 1)
    graficoMejores1 = plt.plot(bestObjective[0])
    plt.setp(graficoMejores1,"linestyle","none","marker","s","color","b","markersize","1")
    plt.title(u"Simulated annealing QAP")
    plt.ylabel(u"Valor objetivo")
    plt.xlabel(u"Valor Óptimo : " + str(mejorObjetivo[0]))

    plt.subplot(2, 1, 2)
    graficoMejores2 = plt.plot(bestObjective[1])
    plt.setp(graficoMejores2,"linestyle","none","marker","s","color","b","markersize","1")
    #plt.title(u"Simulated annealing QAP")
    plt.ylabel(u"Valor objetivo")
    plt.xlabel(u"Valor Óptimo : " + str(mejorObjetivo[1]))

    plt.show()

    # --------------------Mejores valores actuales-------------------------------
    plt.figure(2, figsize=(10,10))
    plt.subplot(2, 1, 1)
    grafico1 = plt.plot(o[0])
    plt.setp(grafico1,"linestyle","none","marker","s","color","r","markersize","1")
    plt.ylabel(u"Valor actual")
    plt.xlabel(u"Valor Óptimo : " + str(mejorObjetivo[0]))

    plt.subplot(2, 1, 2)
    #aux=o[1]
    grafico2 = plt.plot(o[1])
    plt.setp(grafico2,"linestyle","none","marker","s","color","r","markersize","1")
    plt.ylabel(u"Valor actual")
    plt.xlabel(u"Valor Óptimo : " + str(mejorObjetivo[1]))

    plt.show()

    # --------------------PROBABILIDADES-------------------------------
    plt.figure(3, figsize=(10,10))
    plt.subplot(2, 1, 1)
    grafico1 = plt.plot(p[0])
    plt.setp(grafico1,"linestyle","none","marker","s","color","indigo","markersize","1")
    plt.ylabel(u"Probabilidad")
    plt.xlabel(u"Valor Óptimo : " + str(mejorObjetivo[0]))

    plt.subplot(2, 1, 2)
    grafico2 = plt.plot(p[1])
    plt.setp(grafico2,"linestyle","none","marker","s","color","indigo","markersize","1")
    plt.ylabel(u"Probabilidad")
    plt.xlabel(u"Valor Óptimo : " + str(mejorObjetivo[1]))

    plt.show()

    # --------------------Temperatura-------------------------------
    plt.figure(4, figsize=(10,10))
    plt.subplot(2, 1, 1)
    grafico1 = plt.plot(temperature[0])
    plt.setp(grafico1,"linestyle","none","marker","s","color","g","markersize","1")
    plt.ylabel(u"Temperatura")
    plt.xlabel(u"Valor Óptimo : " + str(mejorObjetivo[0]))

    plt.subplot(2, 1, 2)
    grafico2 = plt.plot(temperature[1])
    plt.setp(grafico2,"linestyle","none","marker","s","color","g","markersize","1")
    plt.ylabel(u"Temperatura")
    plt.xlabel(u"Valor Óptimo : " + str(mejorObjetivo[1]))
    plt.show()
