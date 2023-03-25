#Escribir un programa que trace ecuaciones de la recta y=mx + b
import matplotlib.pyplot as plt

m = 2  # pendiente
b = 1  # término independiente

x = range(-10, 11)
y = [m * xi + b for xi in x]

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico de la recta y = mx + b')
plt.grid()
plt.show()
