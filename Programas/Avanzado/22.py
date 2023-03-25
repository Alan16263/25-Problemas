#Calcular el cuadrado, cubo, raiz cuadrada y raiz cubica de los enteros del 1 al 1000 en forma tabular
import pandas as pd
import math

# Creamos una lista con los enteros del 1 al 1000
enteros = list(range(1, 1001))

# Creamos un diccionario para almacenar los resultados
resultados = {'Entero': enteros,
              'Cuadrado': [x**2 for x in enteros],
              'Cubo': [x**3 for x in enteros],
              'Raiz cuadrada': [math.sqrt(x) for x in enteros],
              'Raiz cúbica': [x**(1/3) for x in enteros]}

# Creamos un dataframe a partir del diccionario
df = pd.DataFrame(resultados)

# Mostramos el dataframe
print(df)
