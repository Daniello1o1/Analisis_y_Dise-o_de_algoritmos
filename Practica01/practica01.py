import os,time
def Burbuja(arre):
    aux = 0
    for i in range(1, n):
        for j in range(0, n-i):
            if(arre[j]>arre[j+1]):
                aux = arre[j]
                arre[j] = arre[j+1]
                arre[j+1] = aux
def BurbujaO(arre):
    i = 1
    aux = 0
    ordenado = False
    while(i<n and ordenado == False):
        ordenado = True
        for j in range(0, n-i):
            if(arre[j]>arre[j+1]):
                ordenado = False
                aux = arre[j]
                arre[j] = arre[j+1]
                arre[j+1] = aux
        i = i+1

c = True
n = 0
while(c):
    arre = []
    print("\tMenu")
    print("---------------------------------------")
    print("1) Ordenamiento Burbuja")
    print("2) Ordenamiento Burbuja Optimizado")
    print("3) Salir")
    print("---------------------------------------")
    print("Escoja un metodo para continuar:\n>>", end="")
    m = int(input())
    os.system("cls")
    if(m != 3):
        print("Ingrese el tamaño del arreglo a ordenar:\n>>", end="")
        n = int(input())
        os.system("cls")
        for i in range(0, n):
            print("Ingrese el elemento ", i+1, ":\n>>", end="")
            num = int(input())
            arre.append(num)
            os.system("cls")
        if(m == 1):
            Burbuja(arre)
        elif(m == 2):
            BurbujaO(arre)
        print("El arreglo ordenado es:\n", arre)
        os.system("pause")
    else:
        c = False
print("Saliendo...")
time.sleep(1.5)