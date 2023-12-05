# Algoritmo Genético para el Problema del Viajante

Este proyecto implementa un algoritmo genético en Python para resolver el Problema del Viajante, que consiste en encontrar la ruta más corta que visite todas las ciudades dadas una vez y regrese al punto de partida.

## Descripción del Código

El código proporcionado utiliza un algoritmo genético para encontrar la mejor ruta entre un conjunto de ciudades. Aquí hay un resumen del código:

- **Ciudades y Coordenadas:** Se define un diccionario de ciudades con sus ubicaciones como coordenadas (x, y).

- **Función de Distancia:** Se implementa una función para calcular la distancia euclidiana entre dos ciudades.

- **Función de Aptitud:** Se define una función de aptitud que evalúa la calidad de una ruta en términos de la distancia total recorrida.

- **Algoritmo Genético:** El algoritmo evolutivo genera y evalúa poblaciones de rutas, selecciona las mejores rutas, realiza cruces y mutaciones para evolucionar hacia soluciones óptimas.

## Cómo Ejecutar el Código

1. Asegúrate de tener Python instalado en tu sistema.
2. Copia el código en un archivo Python (por ejemplo, `problema_viajante.py`).
3. Ejecuta el script:

    ```bash
    python problema_viajante.py
    ```

4. El programa imprimirá la mejor ruta encontrada y la distancia mínima recorrida.

## Personalización

Si deseas modificar el conjunto de ciudades o ajustar parámetros del algoritmo, puedes hacerlo directamente en el código.

## Contribuciones

¡Contribuciones son bienvenidas! Si encuentras mejoras o tienes sugerencias, no dudes en abrir un problema o enviar una solicitud de extracción.
