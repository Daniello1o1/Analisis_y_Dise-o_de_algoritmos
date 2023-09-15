fibo = []
n = 0
def Fibonacci(numero):
    fibo.insert(0, 1)
    fibo.insert(1, 1)
    for i in range(2,numero):
        next = fibo[i-2] + fibo[i-1]
        fibo.append(next)

print("Introduzca el numero de la sucecion fibonacci:\n>>",end="")
n = input()
n = int(n)
Fibonacci(n)
print(fibo)