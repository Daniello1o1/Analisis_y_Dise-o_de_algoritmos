arregl = []
def burbuja(arreg):
    aux = 0
    for i in range(1, len(arreg)):
        for j in range(0, len(arreg)-i):
            if(arreg[j]>arreg[j+1]):
                aux = arreg[j]
                arreg[j] = arreg[j+1]
                arreg[j+1] = aux
    return arreg
def burbujarec(arreg, izq, der, pos):
    if(pos == 1):
        aux = 0
        if(arreg[pos]<arreg[pos-1]):
            aux = arreg[pos]
            arreg[pos] = arreg[pos-1]
            arreg[pos-1] = aux
    else:
        aux = 0
        if(der<izq):
            der = burbujarec(arreg, arreg[pos-1], der, pos-1)
            izq = burbujarec(arreg, arreg[pos-2], izq, pos-2)
            aux = der
            der = izq
            izq = aux
    return arreg
print("Inserte el numero de elementos")
n = int(input())
for i in range(0,n):
    print("Inserte el elemento")
    r = int(input())
    arregl.append(r)
print(arregl)
print("Metodo iterativo:")
print(burbuja(arregl))
print("Metodo recursivo")
print(burbuja(burbujarec(arregl, arregl[n-2], arregl[n-1], n-1)))