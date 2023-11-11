import matplotlib.pyplot as pl
import numpy as np
import time, random
def mochila_fraccionaria(capacidad, objetos):
    #Ordenar por valor/peso
    objetos.sort(key = lambda x: x[0]/x[1], reverse = True)
    total_objetos = 0.0
    mochila = []
    for valor, peso in objetos:
        #Si el objeto se puede guardar completo
        if capacidad >= peso:
            mochila.append((valor,peso))
            total_objetos += valor
            capacidad -= peso
        else:
            fracc = capacidad / peso
            mochila.append((valor * fracc, peso * fracc))
            total_objetos += valor * fracc
            break
    return total_objetos, mochila
def genlist():
    objetos = []
    capacidad = random.randint(1, 40)
    for i in range (0,1000):
        for j in range (0,2):
            objetos.append((random.randint(1,20),random.randint(1,20)))
    return capacidad, objetos
def taim(): 
    inicio = time.time()
    capacidad, objetos = genlist()
    mochila_fraccionaria(capacidad, objetos)
    fin = time.time()
    dif = fin - inicio
    tiempos.append(dif)
if __name__ == '__main__':
    tiempos = []
    for i in range(0,100):
        taim()
    x = np.linspace(0,2,100)
    pl.plot(tiempos)
    pl.show()
