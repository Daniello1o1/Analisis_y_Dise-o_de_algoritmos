import time,random
import matplotlib.pyplot as pl
import numpy as np
def valido(sol,pos):
    for i in range(0,pos):
        if sol[pos] == sol[i] or abs(sol[pos]-sol[i]) == abs(pos-i):
            return False
    return True
            
def reina(n):
    i = 0
    c = 0
    sol = []
    sol.append(0)
    sw = True
    while sw:
        #print(sol)

        v = valido(sol,i)
        if v and i+1<n:
            sol.append(0)
            i += 1
        else:
            if v and i+1==n:
                c += 1
                #print("<<XXXXXXXXX>>")
            if sol[i]+1<n:
                sol[i] += 1
            else:
                while(sol[i]+1==n and sw):
                    if i == 0:
                        sw = False
                    else:
                        sol.pop(i)
                        i -= 1
                sol[i] += 1
    return c

def valido2(sol,pos):
    sw = True
    for i in range(0,pos):
        if abs(sol[pos]-sol[i]) == abs(pos-i):
            sw = False
    return sw 
            
def poda(n):
    i = 0
    c = 0
    sol = []
    num = []
    aux = []
    for j in range(1,n):
        num.append(j)
    
    sol.append(0)
    sw = True
    while sw:

        v = valido2(sol,i)
        if v and i+1<n:
            m = min(num)
            sol.append(m)
            num.remove(m)
            i+=1
        else:
            if v:
                c += 1
            while len(aux)==0 and sw:
                for j in range(0,len(num)):
                    if sol[i]<num[j]:
                        aux.append(num[j])
                if len(aux)!=0:
                    m = min(aux)
                    num.remove(m)
                    num.append(sol[i])
                    sol.pop(i)
                    sol.append(m)
                else:
                    if(i==0):
                        sw = False
                    else:
                        num.append(sol.pop(i))
                        i-=1
            aux.clear()
    return c

def heul(n):
    if(n%2==0):
        i = 0
        c = 0
        sol = []
        num = []
        aux = []
        for j in range(1,n):
            num.append(j)
        
        sol.append(0)
        sw = True
        while sw:

            v = valido2(sol,i)
            if v and i+1<n:
                m = min(num)
                sol.append(m)
                num.remove(m)
                i+=1
            else:
                if v:
                    c += 1
                while len(aux)==0 and sw:
                    for j in range(0,len(num)):
                        if sol[i]<num[j]:
                            aux.append(num[j])
                    if len(aux)!=0:
                        m = min(aux)
                        num.remove(m)
                        num.append(sol[i])
                        sol.pop(i)
                        sol.append(m)
                    else:
                        num.append(sol.pop(i))
                        i-=1
                    if i==0 and sol[i]==n/2:
                        sw = False
                aux.clear()
        return c*2
    else:
        return poda(n)
def tiempos():
    for i in range(7,13):
        dif = 0
        inicio = time.time()
        reina(i)
        fin = time.time()
        dif = fin-inicio
        tiempos_n.append(dif)
        
        inicio = time.time()
        poda(i)
        fin = time.time()
        dif = fin-inicio
        tiempos_p.append(dif)
        
        inicio = time.time()
        heul(i)
        fin = time.time()
        dif = fin-inicio
        tiempos_h.append(dif)
if __name__ == '__main__':
    tiempos_n = []
    tiempos_p = []
    tiempos_h = []
    tiempos()
    x = np.arange(7,13)
    pl.plot(x, tiempos_n, label="Normal")
    pl.plot(x, tiempos_p, label="Poda")
    pl.plot(x, tiempos_h, label="Heu")
    
    pl.ylabel('Tiempo')
    pl.xlabel('Valores')
    pl.legend()
    pl.show()