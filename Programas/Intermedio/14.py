#Simular el lanzamiento de un dado 60 veces y tabular los resultados
import random

# Crear una lista para contar el número de veces que aparece cada cara
contador = [0, 0, 0, 0, 0, 0]

# Simular el lanzamiento del dado 60 veces
for i in range(60):
    # Generar un número aleatorio entre 1 y 6 (inclusive) para simular una cara del dado
    cara = random.randint(1, 6)
    # Incrementar el contador para la cara correspondiente
    contador[cara-1] += 1

# Imprimir los resultados
print("El número de veces que apareció cada cara fue:")
for i in range(6):
    print("Cara", i+1, ":", contador[i])
