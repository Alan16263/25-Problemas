#Si se sacan 2 cartas de una baraja comun de 542 cartas, que porcentaje de veces las cartas seran un aas y una cara?
import random

num_experiments = 1000000  # Número de experimentos a realizar
count = 0  # Contador de veces que se saca un as y una cara

for i in range(num_experiments):
    # Seleccionar dos cartas al azar de una baraja común de 52 cartas
    cards = random.sample(range(1, 53), 2)

    # Verificar si la primera carta es un as y la segunda es una cara
    if cards[0] in [1, 14, 27, 40] and cards[1] in [11, 12, 13, 24, 25, 26, 37, 38, 39, 50, 51, 52]:
        count += 1

    # Verificar si la segunda carta es un as y la primera es una cara
    elif cards[1] in [1, 14, 27, 40] and cards[0] in [11, 12, 13, 24, 25, 26, 37, 38, 39, 50, 51, 52]:
        count += 1

# Calcular el porcentaje de veces que se saca un as y una cara
percentage = (count / num_experiments) * 100

print(f"El porcentaje de veces que se saca un as y una cara es: {percentage:.2f}%")
