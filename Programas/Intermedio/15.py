#Factoriza el trinomio 3x^2+4x-48 en factores primos
import math

# Coeficientes del trinomio
a = 3
b = 4
c = -48

# Encontrar las raíces utilizando la fórmula cuadrática
discriminante = b**2 - 4*a*c
if discriminante < 0:
    print("El trinomio no tiene raíces reales")
else:
    raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
    raiz2 = (-b - math.sqrt(discriminante)) / (2*a)

    # Escribir el trinomio en términos de sus raíces
    trinomio = "a * (x - ",raiz1,") * (x -", raiz2 , ")"

    # Imprimir el trinomio en términos de sus factores primos
    print(f"{trinomio} se factoriza en factores primos como:")
    print(f"{a}(x - {raiz1})(x - {raiz2})")
