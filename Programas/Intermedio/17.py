#Un triangulo rectangulo tiene un angulo de 42 25" y el lado opuesto a este angulo mide 25.4cm. Encontrar los otros lados del triangulo
import math

# Datos del triángulo
theta = math.radians(42.4167)  # 42° 25'' en radianes
opposite = 25.4  # Lado opuesto

# Calcular la hipotenusa
hypotenuse = opposite / math.sin(theta)

# Calcular el cateto adyacente
adjacent = hypotenuse * math.cos(theta)

# Imprimir los resultados
print(f"Hipotenusa: {hypotenuse:.2f} cm")
print(f"Cateto adyacente: {adjacent:.2f} cm")
