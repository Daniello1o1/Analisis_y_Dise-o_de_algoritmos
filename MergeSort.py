def merge(izq, der):
    ordenado = []
    i_izq, i_der = 0, 0
    while i_izq < len(izq) and i_der < len(der):
        if izq[i_izq] < der[i_der]:
            ordenado.append(izq[i_izq])
            i_izq += 1
        else:
            ordenado.append(der[i_der])
            i_der += 1
    ordenado.extend(izq[i_izq:])
    ordenado.extend(der[i_der:])

    return ordenado

def MergeS(arreglo):
    if(len(arreglo)<=1):
        return arreglo
    else:
        mitad = len(arreglo)//2
        izq = arreglo[:mitad]
        der = arreglo[mitad:]
        
        izq = MergeS(izq)
        der = MergeS(der)
        
        return merge(izq, der)
if __name__ == '__main__':
    arreglo = [4, 2, 3, 1, 5, 7, 6, 8, 9]
    print("Arreglo desordenado: ",arreglo)
    ordenado = MergeS(arreglo)
    print("Arreglo Ordenado: ", ordenado)
