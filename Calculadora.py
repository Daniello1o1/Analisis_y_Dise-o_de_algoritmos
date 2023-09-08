import time, os
r=0
inicio=0
fin=0
c1 = True
while(c1==True):
    print("\tMenu\n")
    print("1)Elegir dos numeros")
    print("2)Salir")
    print(">>", end="")
    m1 = input()
    m1 = int(m1)
    os.system("cls")
    if(m1==1):
        c2 = True
        print("Introduzca el primer numero: ")
        print(">>", end="")
        num1 = input()
        print("Introduzca el segundo numero: ")
        print(">>", end="")
        num2 = input()
        num1 = float(num1)
        num2 = float(num2)
        os.system("cls")
        while(c2==True):
            print("1) Sumar")
            print("2) Restar")
            print("3) Multiplicar")
            print("4) Dividir")
            print("5) Regresar")
            print("Introduzca la opcion")
            print(">>", end="")
            m2 = input()
            m2 = int(m2)
            os.system("cls")
            if(m2!=5):
                if(m2==1):
                    inicio = time.time()
                    r = num1+num2
                    fin = time.time()
                elif(m2==2):
                    inicio=time.time()
                    r = num1-num2
                    fin = time.time()
                elif(m2==3):
                    inicio=time.time()
                    r = num1*num2
                    fin = time.time()
                elif(m2==4):
                    inicio = time.time()
                    r = num1/num2
                    fin = time.time()
                diferencia = fin-inicio
                print("El resultado es de ", r, " y la operación tardó ", diferencia, "segundos")
                os.system("pause")
                os.system("cls")
            else:
                c2=False
    elif(m1==2):
        c1=False
print("Saliendo...")
time.sleep(1.5)