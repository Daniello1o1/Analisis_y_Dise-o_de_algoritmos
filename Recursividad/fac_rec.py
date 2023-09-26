def factorial(n):
    if(n == 1):
        return n
    else:
        return n*factorial(n-1)
print("Introduzca un valor\n>>", end="")
m = int(input())
print(factorial(m))