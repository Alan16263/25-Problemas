#Impirmir el factorial de un numero dado
n = 7
factorial = 1

for i in range(1, n+1):
    factorial = factorial * i

print("El factorial de", n, "es", factorial)
