#Encontrar los angulos de un triangulo rectangulo de lados 5,12 y 13, hasta el minuto mas cercano
import math

# Lados del triángulo
a = 5
b = 12
c = 13

# Ángulo agudo opuesto al lado a
cos_a = b / c
sin_a = a / c
angle_a = math.degrees(math.acos(cos_a))

# Ángulo agudo opuesto al lado b
cos_b = a / c
sin_b = b / c
angle_b = math.degrees(math.acos(cos_b))

# Ángulo agudo opuesto al lado c (hipotenusa)
tan_c = a / b
angle_c = math.degrees(math.atan(tan_c))

# Imprimir los ángulos hasta el minuto más cercano
print(f"Ángulo a: {round(angle_a)}°")
print(f"Ángulo b: {round(angle_b)}°")
print(f"Ángulo c: {round(angle_c)}°")
