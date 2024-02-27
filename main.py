# Definir las ciudades, días de la semana y semanas
ciudades = ["Santo Domingo", "Baños de Aguan Santa", "Loja"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = ["Semana1", "Semana2", "Semana3"]

# Crear la matriz 3D inicializada con temperaturas aleatorias
import random
matriz_temperaturas = [[[random.randint(20, 30) for _ in dias_semana] for _ in semanas] for _ in ciudades]

# Mostrar la matriz inicial
print("Matriz de temperaturas inicial:")
for i, ciudad in enumerate(ciudades):
    for j, semana in enumerate(semanas):
        print(f"{ciudad} - {semana}: {matriz_temperaturas[i][j]}")

# Calcular el promedio de temperaturas por ciudad y semana
promedios = {}
for i, ciudad in enumerate(ciudades):
    for j, semana in enumerate(semanas):
        promedio = sum(matriz_temperaturas[i][j]) / len(matriz_temperaturas[i][j])
        promedios[f"{ciudad} - {semana}"] = promedio

# Mostrar los promedios de temperaturas por ciudad y semana
print("\nPromedio de temperaturas por ciudad y semana:")
for key, value in promedios.items():
    print(f"{key}: {value:.2f}")
