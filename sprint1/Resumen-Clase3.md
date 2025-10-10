# 🐍 Clase 3 – Introducción a Python

## 🎯 Objetivos
- Configurar el entorno de desarrollo (VS Code + Python + Jupyter).
- Comprender conceptos básicos del lenguaje.
- Usar variables, tipos de datos, operadores y colecciones.

## 🧰 1. Preparación del entorno

| Herramienta         | Uso principal                                                        |
| :------------------ | :------------------------------------------------------------------- |
| **VS Code**         | Editor de código multiplataforma con extensiones y terminal integrada. |
| **Python**          | Lenguaje de programación usado para IA, análisis de datos y automatización. |
| **Jupyter Notebooks** | Cuadernos interactivos para código, texto y gráficos (`.ipynb`).      |

**Extensiones recomendadas:**
- Paquete de idioma en español
- Python
- Jupyter
- GitHub Copilot

## 💡 2. ¿Qué es programar?
Programar es crear una secuencia lógica de pasos para alcanzar un objetivo.
*Ejemplo: indicar a un robot los pasos para llegar a una meta (arriba, abajo, izquierda, derecha).*

**Características clave:**
- Orden correcto de pasos
- Posibilidad de múltiples soluciones
- Evaluar la mejor (óptima)

## 🧭 3. Conceptos del entorno Python

| Concepto            | Descripción                                    |
| :------------------ | :--------------------------------------------- |
| **Editor**          | Donde se escribe el código (VS Code).          |
| **Extensión**       | Añade funcionalidades (por ejemplo, Python o Jupyter). |
| **Intérprete**      | Ejecuta el código.                             |
| **Terminal integrada** | Permite correr programas dentro del editor.    |
| **Depurador**       | Revisa el código paso a paso.                  |
| **Script**          | Archivo `.py` con código lineal.               |
| **Notebook**        | Archivo interactivo `.ipynb` con texto y código. |

## ⚙️ 4. Buenas prácticas
- Crear una carpeta por proyecto.
- Guardar con nombres descriptivos.
- Activar guardado automático.
- Revisar el intérprete seleccionado.
- Documentar el código con comentarios (`#` o `""" """`).

## 🐍 5. Fundamentos de Python

#### Funciones integradas comunes
| Función     | Descripción                  |
| :---------- | :--------------------------- |
| `print()`   | Muestra texto o valores.     |
| `input()`   | Pide datos al usuario.       |
| `len()`     | Devuelve longitud de un objeto. |
| `type()`    | Informa tipo de dato.        |
| `range()`   | Genera secuencia numérica.   |

#### Sentencias y estructuras de control
- **Condicionales:** `if`, `elif`, `else`
- **Bucles:** `for`, `while`
- **Funciones:** `def nombre():`

## 🔤 6. Variables y tipos de datos

**Reglas de nombres:**
- No comenzar con número.
- No usar espacios ni guiones.
- No usar palabras reservadas (`for`, `int`, etc.).

**Tipos básicos:**
| Tipo   | Ejemplo      | Descripción |
| :----- | :----------- | :---------- |
| `int`  | `5`          | Entero      |
| `float`| `3.14`       | Decimal     |
| `str`  | `"Hola"`     | Texto       |
| `bool` | `True`/`False` | Lógico      |
| `None` | —            | Sin valor   |

**Conversión de tipos:**
```python
str(3)  # '3'
int("5")  # 5
round(3.1416, 2)  # 3.14
```

## ➕ 7. Operadores
| Tipo          | Ejemplo                | Descripción                |
| :------------ | :--------------------- | :------------------------- |
| **Aritméticos** | `+`, `-`, `*`, `/`, `%`, `**` | Operaciones matemáticas    |
| **Comparación** | `==`, `!=`, `<`, `>`, `<=`, `>=` | Comparaciones lógicas      |
| **Lógicos**     | `and`, `or`, `not`     | Combinación de condiciones |
| **Asignación**  | `+=`, `-=`, `*=`       | Actualizar variables       |
| **Pertenencia** | `in`, `not in`         | Buscar en listas o cadenas |

## 🧾 8. Texto y formato
```python
nombre = "Ana"
edad = 25
print(f"Hola {nombre}, tienes {edad} años.")
```

**Funciones útiles:**
`.lower()`, `.upper()`, `.strip()`, `.replace()`, slicing `[inicio:fin]`

## 👩‍💻 9. Entrada y salida
```python
nombre = input("¿Cuál es tu nombre? ")
print("Hola", nombre)
```

**Opciones de `print`:**
- `sep` → define el separador
- `end` → cambia el salto de línea

## 🧮 10. Ejercicio: Calcular edad
**Enunciado:** Crear un programa que calcule la edad según el año de nacimiento.

**Solución en Python:**
```python
nombre = input("¿Cuál es tu nombre? ")

anio_nac = int(input("¿En qué año naciste? "))


anio_actual = 2025

edad = anio_actual - anio_nac
mayor = edad >= 18

print(f"Hola {nombre}, tienes {edad} años.")
print("¿Eres mayor de edad?", mayor)
print("Tipo de dato de edad:", type(edad))
```

## 📦 11. Colecciones (estructuras de datos)

### Listas
```python
frutas = ["manzana", "pera", "banana"]
frutas.append("uva")
frutas[0] = "kiwi"
```
**Métodos comunes:** `append()`, `insert()`, `remove()`, `sort()`, `reverse()`, `count()`, `copy()`

### Tuplas
```python
coordenadas = (10, 20)
```
- Ordenadas, pero inmutables.
- Útiles para datos fijos o claves de diccionarios.

### Diccionarios
```python
persona = {"nombre": "Juan", "edad": 30}
print(persona["nombre"])
persona["edad"] = 31
```
**Métodos útiles:** `keys()`, `values()`, `items()`, `get()`, `update()`, `pop()`

### Sets (conjuntos)
```python
colores = {"rojo", "azul", "rojo"}
# Resultado: {'rojo', 'azul'} -> elimina duplicados
```
- No tienen orden ni índices. Útiles para eliminar repetidos y comparar elementos.

---

## 🛒 Ejercicio: Lista de compras
**Objetivo:** Registrar productos y calcular total y producto más caro.

**Solución:**
```python
productos = {}
for i in range(3):
    nombre = input("Producto: ")
    precio = float(input("Precio: "))
    productos[nombre] = precio

total = sum(productos.values())
caro = max(productos, key=productos.get)

print("\nLista de productos:", productos)
print("Total a pagar:", total)
print("Producto más caro:", caro)
```

---

## 🧱 Proyecto: Tienda Aurelion
**Entregables:**
- Documentación (`Documentacion.md`)
- Programa en Python para leer la documentación
- Dashboard en Power BI
- Presentación oral de resultados
