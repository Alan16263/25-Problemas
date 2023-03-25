#Resolver un sistema de ecuaciones lineales
# Definir los coeficientes de las ecuaciones
A = [[2, 4, -5], [3, -2, -2], [-4, 5, 3]]
B = [-3, 14, -10]

# Imprimir el sistema de ecuaciones
print("Sistema de ecuaciones:")
for i in range(len(A)):
    equation = f"{A[i][0]}x + {A[i][1]}y + {A[i][2]}z = {B[i]}"
    print(equation)

# Eliminación Gaussiana
n = len(B)
for i in range(n):
    # Dividir la i-ésima fila por el elemento diagonal
    factor = A[i][i]
    for j in range(i, n):
        A[i][j] /= factor
    B[i] /= factor

    # Restar la i-ésima fila de las filas siguientes
    for j in range(i+1, n):
        factor = A[j][i]
        for k in range(i, n):
            A[j][k] -= factor * A[i][k]
        B[j] -= factor * B[i]

# Sustitución hacia atrás
x = [0] * n
for i in range(n-1, -1, -1):
    x[i] = B[i]
    for j in range(i+1, n):
        x[i] -= A[i][j] * x[j]

# Imprimir los resultados
print("Solución:")
print(f"x = {x[0]:.2f}")
print(f"y = {x[1]:.2f}")
print(f"z = {x[2]:.2f}")
