def calcular_temperatura_promedio(datos_temperaturas):
    temperaturas_ciudades = {}

    for ciudad, datos_semanales in datos_temperaturas.items():
        total_temperaturas = 0
        cantidad_temperaturas = 0

        for semana in datos_semanales:
            for temperatura in semana:
                total_temperaturas += temperatura
                cantidad_temperaturas += 1

        temperatura_promedio = total_temperaturas / cantidad_temperaturas
        temperaturas_ciudades[ciudad] = temperatura_promedio

    return temperaturas_ciudades


# Ejemplo de datos de temperaturas por ciudad y semana
datos_temperaturas = {
    'Baños de Agua Santa': [[25, 26, 27], [24, 23, 22], [28, 29, 30]],
    'Latacunga': [[20, 21, 22], [23, 24, 25], [19, 18, 17]]
}

temperaturas_promedio = calcular_temperatura_promedio(datos_temperaturas)

for ciudad, temperatura_promedio in temperaturas_promedio.items():
    print(f"La temperatura promedio en {ciudad} es: {temperatura_promedio}")