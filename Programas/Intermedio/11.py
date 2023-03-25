#Resolver la siguiente ecuacion 6x^2 -17x +5 =0
import math

a = 6
b = -17
c = 5

discriminante = b**2 - 4*a*c

if discriminante < 0:
    print("La ecuación no tiene solución real")
elif discriminante == 0:
    x = -b / (2*a)
    print("La solución única es:", x)
else:
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    print("Las soluciones son:", x1, "y", x2)
