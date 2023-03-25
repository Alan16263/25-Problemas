#Resolver el siste de ecuaciones lineas
#109x+71y-260=0
#-89x+29y+18=0
import numpy as np

# Coeficientes de las ecuaciones
A = np.array([[109, 71], [-89, 29]])
# Términos independientes
B = np.array([260, -18])

# Resolver el sistema de ecuaciones
X = np.linalg.solve(A, B)

# Imprimir las soluciones
print("x =", X[0])
print("y =", X[1])
