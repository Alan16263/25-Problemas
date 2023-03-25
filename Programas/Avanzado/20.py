#Convertir cooordenadas poares a rectangulares 
import math

# Convertir la ecuación r = cos(3θ) a coordenadas rectangulares
for i in range(0, 361, 30):  # Calcular para varios valores de θ
    theta = math.radians(i)
    r = math.cos(3 * theta)
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    print(f"Para θ = {i}°: (x, y) = ({x:.2f}, {y:.2f})")
print("--------------------------------------------")
# Convertir la ecuación r = sin(3θ) a coordenadas rectangulares
for i in range(0, 361, 30):
    theta = math.radians(i)
    r = math.sin(3 * theta)
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    print(f"Para θ = {i}°: (x, y) = ({x:.2f}, {y:.2f})")
print("--------------------------------------------")
# Convertir la ecuación r = sin(θ) + cos(θ) a coordenadas rectangulares
for i in range(0, 361, 30):
    theta = math.radians(i)
    r = math.sin(theta) + math.cos(theta)
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    print(f"Para θ = {i}°: (x, y) = ({x:.2f}, {y:.2f})")
