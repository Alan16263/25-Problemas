#Encontrar el valor de senx y cosx para x =30, 45, 60 y 90 grados
import math
# Convertir ángulos a radianes
x_30 = math.radians(30)
x_45 = math.radians(45)
x_60 = math.radians(60)
x_90 = math.radians(90)

# Calcular sin(x) y cos(x)
sin_30 = math.sin(x_30)
cos_30 = math.cos(x_30)
sin_45 = math.sin(x_45)
cos_45 = math.cos(x_45)
sin_60 = math.sin(x_60)
cos_60 = math.cos(x_60)
sin_90 = math.sin(x_90)
cos_90 = math.cos(x_90)

# Imprimir resultados
print("Para x=30°: sin(x) =", sin_30, "cos(x) =", cos_30)
print("Para x=45°: sin(x) =", sin_45, "cos(x) =", cos_45)
print("Para x=60°: sin(x) =", sin_60, "cos(x) =", cos_60)
print("Para x=90°: sin(x) =", sin_90, "cos(x) =", cos_90)
