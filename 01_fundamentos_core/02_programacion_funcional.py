# Ejercicios de 02 programacion funcional.py
"""
NIVEL 1: PROGRAMACIÓN FUNCIONAL EN PYTHON
Conceptos clave: Funciones como ciudadanos de primera clase, Lambdas, Map, Filter y Reduce.
"""

from typing import List, Callable
from functools import reduce

# 1. FUNCIONES LAMBDA (Funciones anónimas)
# Ideales para operaciones rápidas de una sola línea.
# Sintaxis: lambda argumentos: expresion
cuadrado = lambda x: x ** 2
print(f"Cuadrado de 5: {cuadrado(5)}")


# 2. MAP (Transformación de datos)
# Aplica una función a cada elemento de un iterable.
numeros: List[int] = [1, 2, 3, 4, 5]
# Convertimos cada número a string y le agregamos un prefijo
ids_usuarios = list(map(lambda x: f"ID-{x:03d}", numeros))
print(f"IDs Generados: {ids_usuarios}")


# 3. FILTER (Selección de datos)
# Filtra elementos que cumplen una condición (devuelven True).
precios: List[float] = [120.5, 45.0, 9.99, 200.0, 15.75]
# Solo productos "Premium" (precio > 100)
productos_premium = list(filter(lambda p: p > 100, precios))
print(f"Productos Premium: {productos_premium}")


# 4. REDUCE (Acumulación de datos)
# Reduce un iterable a un único valor. No viene por defecto, se importa de functools.
gastos: List[float] = [10.5, 20.0, 5.25]
total_gastos = reduce(lambda acumulador, elemento: acumulador + elemento, gastos)
print(f"Total acumulado: {total_gastos}")


# 5. HIGHER-ORDER FUNCTIONS (Funciones de orden superior)
# Son funciones que reciben otras funciones como argumentos.
def aplicar_operacion(n: int, operacion: Callable[[int], int]) -> int:
    """Ejemplo pro: Usamos Callable para tipar funciones."""
    return operacion(n)

resultado_final = aplicar_operacion(10, lambda x: x * 3)
print(f"Resultado Función Superior: {resultado_final}")

# --- RETO PARA TI ---
# Usa 'filter' y 'map' juntos en una sola línea para:
# 1. Tomar la lista 'edades'
# 2. Filtrar solo los mayores de 18
# 3. Multiplicar sus edades por 10
edades = [12, 25, 18, 40, 15, 30]
# Tu código aquí:
# resultado_reto = ...