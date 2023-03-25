#Lanzar 8 dados 600 veces. Contar el número de cincos que salen en cada tiro. Imprimir la distribución
import random

# Inicializar el diccionario para almacenar la distribución
distribucion = {}

# Lanzar los dados 600 veces
for i in range(600):
    # Inicializar el contador de cincos en cada tiro
    cincos = 0
    # Lanzar los 8 dados
    for j in range(8):
        # Generar un número aleatorio entre 1 y 6 para simular el lanzamiento de un dado
        dado = random.randint(1, 6)
        # Si el resultado es un cinco, incrementar el contador de cincos en cada tiro
        if dado == 5:
            cincos += 1
    # Actualizar la distribución con el resultado de este tiro
    if cincos in distribucion:
        distribucion[cincos] += 1
    else:
        distribucion[cincos] = 1

# Imprimir la distribución de frecuencia
print("Distribución de frecuencia de cincos en 600 lanzamientos de 8 dados:")
for k, v in distribucion.items():
    print(k, "cincos:", v)
