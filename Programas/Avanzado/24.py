#Introducir N cantidad de lados de un polígono regular. Determina la medida de cada angulo
# Pedir la cantidad de lados del polígono al usuario
N = int(input("Ingrese la cantidad de lados del polígono: "))

# Calcular la medida de cada ángulo utilizando la fórmula
angulo = (N-2) * 180 / N

# Imprimir el resultado
print("La medida de cada ángulo en un polígono regular de", N, "lados es:", angulo)
