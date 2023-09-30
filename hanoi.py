ori = []
des = []
aux = []
def moverTorre(altura,origen, destino, auxiliar):
    if altura > 1:
        moverTorre(altura-1,origen,auxiliar,destino)
        moverDisco(origen,destino)
        if(origen[0]=='A'):
            ori = origen
        elif(origen[0]=='B'):
            aux = origen
        elif(origen[0]=='C'):
            des = origen
        
        if(auxiliar[0]=='A'):
            ori = auxiliar
        elif(auxiliar[0]=='B'):
            aux = auxiliar
        elif(auxiliar[0]=='C'):
            des = auxiliar
            
        if(destino[0]=='A'):
            ori = destino
        elif(destino[0]=='B'):
            aux = destino
        elif(destino[0]=='C'):
            des = destino

        print(ori,end="")
        print(aux,end="")
        print(des)
        moverTorre(altura-1,auxiliar,destino,origen)
def moverDisco(desde,hacia):
    hacia.append(desde.pop())
ori.append("A")
des.append("C")
aux.append("B")
print("Ingrese el numero de piezas para la torre de hanoi\n>>",end="")
n = int(input())
for i in range(n-1,0,-1):
    ori.append(i)
print("Resultado en pasos")
print("--------------------------")
print(ori,end="")
print(aux,end="")
print(des)
moverTorre(n,ori,des,aux)
print("--------------------------")