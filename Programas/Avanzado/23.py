#Un programa que encuentre los 3 angulos de un triangulo, dados los 3 lados 
import math

# Pedir los lados del triángulo al usuario
a = float(input("Ingrese la longitud del lado a: "))
b = float(input("Ingrese la longitud del lado b: "))
c = float(input("Ingrese la longitud del lado c: "))

# Calcular los ángulos utilizando la Ley de los cosenos
cos_A = (b**2 + c**2 - a**2) / (2*b*c)
cos_B = (a**2 + c**2 - b**2) / (2*a*c)
cos_C = (a**2 + b**2 - c**2) / (2*a*b)

# Convertir los valores de coseno a ángulo (en grados)
A = math.degrees(math.acos(cos_A))
B = math.degrees(math.acos(cos_B))
C = math.degrees(math.acos(cos_C))

# Imprimir los resultados
print("Los ángulos del triángulo son:")
print("A =", A)
print("B =", B)
print("C =", C)
