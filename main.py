'''
import random

# Definir las ciudades y sus ubicaciones como coordenadas (x, y)
ciudades = {
    'A': (0, 0),  # Coordenadas de la ciudad A
    'B': (1, 3),  # Coordenadas de la ciudad B
    'C': (4, 1),  # Coordenadas de la ciudad C
    'D': (5, 4),  # Coordenadas de la ciudad D
    'E': (3, 6)   # Coordenadas de la ciudad E
}

# Función para calcular la distancia entre dos ciudades utilizando la fórmula de distancia euclidiana
def distancia(ciudad1, ciudad2):
    x1, y1 = ciudades[ciudad1]  # Obtener las coordenadas de la primera ciudad
    x2, y2 = ciudades[ciudad2]  # Obtener las coordenadas de la segunda ciudad
    # Aplicar la fórmula de distancia euclidiana entre dos puntos en un plano
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

"""
La función ciudades.keys() devuelve un objeto dict_keys que contiene las claves del diccionario de ciudades. 
Al convertirlo a una lista en la línea ruta = list(ciudades.keys()), creamos una lista de claves de ciudades.
"""
# Generar una ruta aleatoria que visite todas las ciudades una vez
ruta = list(ciudades.keys())  # Crear una lista de ciudades
random.shuffle(ruta)  # Barajar aleatoriamente la lista de ciudades

# Calcular la distancia total de la ruta sumando las distancias entre ciudades adyacentes y la última ciudad con la primera
distancia_total = sum(distancia(ruta[i], ruta[i + 1]) for i in range(len(ruta) - 1)) + distancia(ruta[-1], ruta[0])

# Imprimir la ruta inicial y su distancia total
print(f"Ruta inicial: {' -> '.join(ruta)} -> {ruta[0]}")  # Imprimir la ruta inicial en el formato 'A -> B -> C -> D -> E -> A'
print(f"Distancia total de la ruta inicial: {distancia_total}")  # Imprimir la distancia total de la ruta inicial
'''
import random

# Definir las ciudades y sus ubicaciones como coordenadas (x, y)
ciudades = {
    'A': (0, 0),
    'B': (1, 3),
    'C': (4, 1),
    'D': (5, 4),
    'E': (3, 6)
}

# Función para calcular la distancia entre dos ciudades
def distancia(ciudad1, ciudad2):
    x1, y1 = ciudades[ciudad1]
    x2, y2 = ciudades[ciudad2]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# Función de aptitud para evaluar la calidad de una ruta (distancia total)
def aptitud(ruta):
    return sum(distancia(ruta[i], ruta[i + 1]) for i in range(len(ruta) - 1)) + distancia(ruta[-1], ruta[0])

# Algoritmo genético para resolver el Problema del Viajante
def algoritmo_genetico(tamano_poblacion, generaciones):
    '''Se inicializa una población de rutas aleatorias. 
    Cada ruta es una lista de las claves de las ciudades en un orden aleatorio'''
    poblacion = [list(ciudades.keys()) for _ in range(tamano_poblacion)]  # 1. Inicializar la población con rutas aleatorias utilizando las claves de las ciudades.
    for _ in range(generaciones):  # 2. Iterar a lo largo del número de generaciones
        aptitudes = [(aptitud(ruta), ruta) for ruta in poblacion]  # 3. Calcular la aptitud de cada ruta en la población y crea una lista de tuplas que contienen la aptitud y la ruta correspondiente.
        aptitudes.sort()  # 4. Ordenar las rutas en función de su aptitud de menor a mayor.
     
        '''Se seleccionan las mejores rutas, es decir, las rutas con las menores distancias recorridas. 
        Estas rutas se seleccionan para formar la nueva población.'''
        '''La estructura general de la comprensión de lista [ruta for _, ruta in aptitudes[:tamano_poblacion // 2]] se denomina desempaquetado de tuplas. 
        Aquí, el símbolo subrayado _ se utiliza para representar la aptitud, que se descarta, y la variable ruta representa la ruta en sí. 
        Por lo tanto, mejores_rutas es una lista que contiene solo las rutas de las mejores soluciones dentro de la población, 
        en función de sus aptitudes.'''
        mejores_rutas = [ruta for _, ruta in aptitudes[:tamano_poblacion // 2]]  # 5. Seleccionar las mejores rutas , tomando la mitad de las rutas con menor aptitud.
        poblacion = [random.sample(mejores_rutas, 2) for _ in range(tamano_poblacion // 2)]  # 6. Crea una nueva población a partir de las mejores rutas seleccionadas, formando pares aleatorios de rutas seleccionadas.
        poblacion = [hijo for padres in poblacion for hijo in padres]  # 7. Actualizar la población con los hijos generados a partir de las mejores rutas.
        for ruta in poblacion:  # 8. Aplicar mutaciones a las rutas con una cierta probabilidad
            if random.random() < 0.2:
                i, j = sorted(random.sample(range(len(ruta)), 2))
                ruta[i], ruta[j] = ruta[j], ruta[i]
    mejor_ruta = min(poblacion, key=aptitud)  # 9. Encontrar la mejor ruta dentro de la población en función de su aptitud(distancia total) mínima.
    return mejor_ruta, aptitud(mejor_ruta)  # 10. Devolver la mejor ruta y su aptitud

# Aplicar el algoritmo genético y obtener la mejor ruta
mejor_ruta, distancia_minima = algoritmo_genetico(300, 3000)

# Imprimir la mejor ruta y su distancia mínima
print(f"Mejor ruta encontrada: {' -> '.join(mejor_ruta)} -> {mejor_ruta[0]}")
print(f"Distancia mínima: {distancia_minima}")