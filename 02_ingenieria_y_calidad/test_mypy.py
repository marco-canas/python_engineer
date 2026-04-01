

#Para utilizar **mypy**, debes entender que Python es un lenguaje de tipado 
# dinámico (puedes cambiar el tipo de una variable sobre la marcha), 
# pero **mypy** lo convierte en algo parecido a Java o C# en cuanto a seguridad, 
# revisando tu código antes de que lo ejecutes.

#Aquí tienes los pasos para integrarlo en tu flujo de trabajo de ingeniero.


# ## 1. Instalación
# Como estamos siguiendo una estructura profesional, lo ideal es instalarlo en tu 
# entorno virtual. Desde tu terminal en la carpeta del proyecto:

#```bash
#pip install mypy
#```

## 2. El concepto: Type Hinting
#Mypy no funciona por arte de magia; necesita que tú le des "pistas" (*hints*). 



#Escribe este código de prueba en un archivo nuevo llamado `test_mypy.py` dentro de tu carpeta `02_ingenieria_y_calidad`:

# test_mypy.py

def calcular_area(radio: float) -> float:
    return 3.1416 * (radio ** 2)

# Caso correcto
print(calcular_area(10.5))

# Caso incorrecto (Esto no dará error en Python normal, pero sí en Mypy)
print(calcular_area("diez")) 


## 3. Ejecución de Mypy
#Ahora, pide a mypy que revise tu archivo desde la terminal:

#```bash
#mypy test_mypy.py
#```

# **El resultado será algo como esto:**
#> `test_mypy.py:9: error: Argument 1 to "calcular_area" has incompatible type "str"; expected "float"`

#¡Felicidades! Acabas de evitar un error que normalmente solo encontrarías cuando el programa fallara en manos del usuario.

#---

### 4. Uso avanzado con la librería `typing`
#A medida que tus estructuras sean más complejas, necesitarás herramientas más potentes:

#```python
#from typing import List, Dict, Optional, Union

# Una lista que solo acepta enteros
#numeros: List[int] = [1, 2, 3]

# Una variable que puede ser un String o None (muy común en bases de datos)
#usuario_id: Optional[str] = None

# Una función que acepta tanto enteros como flotantes
#def procesar_dato(dato: Union[int, float]) -> None:
#    print(dato)


## 5. Configuración profesional (`mypy.ini`)
#Un Python Engineer no escribe los comandos largos cada vez. Crea un archivo llamado `mypy.ini` en la raíz de tu proyecto para estandarizar las reglas:

#```ini
#[mypy]
#python_version = 3.10
#warn_return_any = True
#warn_unused_configs = True
#disallow_untyped_defs = True  # Te obliga a tipar todas las funciones


## 🛠️ Tu tarea de hoy
#1. Ve a tu archivo `02_ingenieria_y_calidad/04_estatic_typing_mypy.py`.
#2. Escribe una función que reciba un diccionario y devuelva una lista de sus llaves.
#3. Agrégale **Type Hinting** completo.
#4. Ejecuta `mypy` sobre ese archivo y corrige cualquier error que te marque.

#¿Quieres que te muestre cómo configurar **VS Code** para que te marque estos errores en rojo automáticamente mientras escribes, sin tener que usar la terminal?