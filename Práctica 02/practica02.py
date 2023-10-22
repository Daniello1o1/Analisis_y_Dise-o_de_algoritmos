import matplotlib.pyplot as pl
import numpy as np
import random, time
inicio = 0
tam = []
tiempos = []
for i in range(0,100):
    tam.append(random.randint(10,10000))
def genArreglo(j):
    arreglo = []
    for _ in range(tam[j]):
        arreglo.append(random.randint(0,100))
    return(arreglo)
def Merge(arr1,arr2,arr3):
    arr1.extend(arr2)
    arr1.extend(arr3)
    return arr1
def tiem_po(arre):
    inicio = time.time()
    #QS(arre)
    QS2(arre)
    fin = time.time()
    dif = fin - inicio
    tiempos.append(dif)
def QS(arre):
    if(len(arre)<=1):
        return arre
    else:
        aux1 = []
        aux2 = []
        aux3 = []
        sum = 0
        for i in range(0,len(arre)):
                sum += arre[i]
        mid1 = round(sum/len(arre))
        media = min(arre, key=lambda x: abs(x-mid1))
        arre.pop(arre.index(media))
        aux2.append(media)
        for i in range(0,len(arre)):
            if(arre[i]<=media):
                aux1.append(arre[i])
            else:
                aux3.append(arre[i])
        return Merge(QS(aux1),aux2,QS(aux3))
def QS2(arre):
    if(len(arre)<=1):
        return arre
    else:
        aux1 = []
        aux2 = []
        aux3 = []
        sum = 0
        for i in range(0,len(arre)):
                sum += arre[i]
        piv = arre[0]
        aux2.append(piv)
        arre.pop(0)
        for i in range(0,len(arre)):
            if(arre[i]<=piv):
                aux1.append(arre[i])
            else:
                aux3.append(arre[i])
        return Merge(QS2(aux1),aux2,QS2(aux3))
for i in range(0,100):
    tiem_po(genArreglo(i))
print(tiempos)
x = np.linspace(0,2,100)
pl.plot(tiempos)
pl.show()