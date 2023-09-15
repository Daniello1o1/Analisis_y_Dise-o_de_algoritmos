def factorial(numero):
    r = 1
    for i in range(1,numero+1):
        r *= i
    return r
print("Introduzca el número a sacar factorial\n>>",end="")
n = int(input())
print("El factorial es de: ",factorial(n))