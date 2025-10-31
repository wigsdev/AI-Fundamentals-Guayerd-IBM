# 🧠 Clase 4 – Estructuras de Control, Funciones y NumPy

## 🎯 Objetivos

*   Comprender cómo hacer que los programas tomen decisiones y repitan acciones.
*   Crear y reutilizar funciones.
*   Introducir el uso de la librería NumPy para análisis de datos numéricos.

## 🧩 1. El arte de preguntar en IA

Las preguntas son la base de todo análisis:

*   Orientan decisiones y evitan la improvisación.
*   Transforman datos en conocimiento útil.
*   Conectan problemas con objetivos claros.

### Tipos de indagación:

| Tipo      | Pregunta                | Ejemplo         |
| :-------- | :---------------------- | :-------------- |
| Anticipar | ¿Qué ocurrirá después?  | Predicciones    |
| Comparar  | ¿En qué se diferencian? | Clasificaciones |
| Explorar  | ¿Qué patrones existen?  | Agrupamientos   |
| Explicar  | ¿Por qué sucede esto?   | Causas y correlaciones |

### Estructurar un análisis:

1.  **Definir el problema** (qué, por qué, cuándo).
2.  **Organizar los datos** (qué, cómo, limitaciones).
3.  **Diseñar el enfoque** (relaciones, variables, validación).

## ⚙️ 2. Estructuras de Control

Permiten decidir y repetir dentro de un programa.

### 🔸 Condicionales (if, elif, else)

Evalúan una condición booleana (`True` o `False`).

**Ejemplo:**

```python
edad = 20
if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")
```

### 🔸 Bucles

Permiten repetir código mientras se cumpla una condición o haya elementos.

*   **`for`**: recorre secuencias
    ```python
    for i in range(5):
        print(i)
    ```
*   **`while`**: repite mientras la condición sea verdadera
    ```python
    x = 0
    while x < 3:
        print(x)
        x += 1
    ```

### 🔸 Control de bucles

| Instrucción | Función                        |
| :---------- | :----------------------------- |
| `break`     | Rompe el bucle                 |
| `continue`  | Salta a la siguiente iteración |
| `pass`      | No hace nada (placeholder)     |

**Ejemplo:**

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

### 🔸 Patrones de iteración

| Patrón      | Descripción                       | Ejemplo                 |
| :---------- | :-------------------------------- | :---------------------- |
| Acumulador  | Suma o multiplica valores         | `suma += x`             |
| Contador    | Cuenta elementos que cumplen condición | `if x > 10: contar += 1` |
| Buscador    | Encuentra un valor                | `if x == 15: break`     |
| Filtro      | Procesa solo ciertos elementos    | `if x % 2 == 0:`        |

## 🧮 3. Funciones en Python

Bloques de código que realizan una tarea y pueden reutilizarse.

### 🔹 Sintaxis básica

```python
def nombre_funcion(parametros):
    # código
    return resultado
```

### 🔹 Ejemplo

```python
def cuadrado(x):
    return x * x

print(cuadrado(5))  # 25
```

### 🔹 Ventajas

*   Evitan repetir código.
*   Facilitan el mantenimiento.
*   Mejoran la organización.

### 🔹 Reglas

*   No empezar con números ni usar palabras reservadas.
*   Nombres descriptivos.
*   Pueden tener valores por defecto.
*   Pueden retornar múltiples valores.

### 🔹 Funciones integradas más comunes

| Categoría       | Función                | Ejemplo                 |
| :-------------- | :--------------------- | :---------------------- |
| Entrada/Salida  | `print()`, `input()`   | `input("Nombre: ")`      |
| Conversión      | `int()`, `float()`, `str()` | `int("5") → 5`          |
| Matemáticas     | `abs()`, `round()`, `max()`, `sum()` | `sum([1,2,3]) → 6`      |
| Colecciones     | `len()`, `range()`, `sorted()` | `len("Hola") → 4`       |

## 🌡️ Ejercicio 1 – Registro de temperaturas

**Objetivo:**

*   Pedir la temperatura de 5 días.
*   Mostrar promedio, máxima y mínima.
*   Contar cuántos días > 25°C.

**Solución:**

```python
temperaturas = []
for i in range(5):
    temp = float(input(f"Temperatura día {i+1}: "))
    temperaturas.append(temp)

prom = sum(temperaturas) / len(temperaturas)
print("Promedio:", prom)
print("Máxima:", max(temperaturas))
print("Mínima:", min(temperaturas))
dias_calidos = sum(t > 25 for t in temperaturas)
print("Días con más de 25°C:", dias_calidos)
```

## 📚 4. Librerías y NumPy

### 🔹 ¿Qué es una librería?

Conjunto de funciones predefinidas que amplían las capacidades de Python.

**Ventajas:**

*   Ahorra tiempo.
*   Optimiza el procesamiento.
*   Permite análisis de grandes volúmenes de datos.

### 🔹 NumPy (Numerical Python)

**Instalación:**

```bash
pip install numpy
```

**Uso:**

```python
import numpy as np
```

**Características:**

*   Procesa arrays multidimensionales.
*   Soporta operaciones vectorizadas (más rápidas que listas).
*   Base de librerías como Pandas y Scikit-learn.

### 🔹 Arrays NumPy

```python
import numpy as np
vector = np.array([1, 2, 3])
matriz = np.array([[1, 2], [3, 4]])
```

**Operaciones básicas:**

```python
vector + 2          # Suma escalar
vector * 3          # Multiplicación escalar
np.sqrt(vector)     # Raíz cuadrada
np.arange(0, 10, 2) # Secuencia
```

**Propiedades:**

| Propiedad     | Descripción                   |
| :------------ | :---------------------------- |
| `array.shape` | Dimensiones                   |
| `array.ndim`  | Número de dimensiones         |
| `array.size`  | Cantidad total de elementos   |
| `array.dtype` | Tipo de datos                 |
| `array.nbytes`| Memoria total                 |

## 💰 Ejercicio 2 – Primeras ventas

**Enunciado:**

*   Ingresar los montos de las primeras 10 ventas.
*   Calcular promedio, total, mayor y menor.
*   Mostrar las ventas por encima del promedio.

**Solución:**

```python
import numpy as np

ventas = np.array([float(input(f"Venta {i+1}: ")) for i in range(10)])

prom = np.mean(ventas)
total = np.sum(ventas)
mayor = np.max(ventas)
menor = np.min(ventas)

print("
Promedio:", prom)
print("Total:", total)
print("Mayor:", mayor)
print("Menor:", menor)
print("Ventas sobre el promedio:", ventas[ventas > prom])
```

## 🧱 Proyecto: Tienda Aurelion

**Entregables:**

*   Documentación en Markdown
*   Programa interactivo en Python
*   Dashboard en Power BI
*   Presentación explicando problema, solución y hallazgos

**Evaluación:**

*   Claridad del tema y problema.
*   Correcta estructura de datos (según clase 2).
*   Pseudocódigo y diagrama funcional.
*   Programa sin errores.
*   Uso de Copilot documentado.
