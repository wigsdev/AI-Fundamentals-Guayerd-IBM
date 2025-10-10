# -*- coding: utf-8 -*-

tema_problema_solucion = """
1. Tema, problema y solución
Este proyecto simula la gestión de una Tienda a partir de datos sintéticos.
El objetivo es disponer de un escenario consistente para practicar análisis, visualización y modelado.
"""

dataset_referencia = """
2. Dataset de referencia: fuente, definición, estructura, tipos y escala de medición
Fuente: datos generados con fines educativos.
Definición: base que representa una Tienda, con catálogo de productos, registro de clientes y operaciones de venta.
"""

estructura_tablas = """
Estructura por tabla:

### Productos (productos.csv) — ~100 filas
| Campo | Tipo | Escala |
| :--- | :--- | :--- |
| id_producto | int | Nominal |
| nombre_producto| str | Nominal |
| categoria | str | Nominal |
| precio_unitario| int | Razón |

### Clientes (clientes.csv) — ~100 filas
| Campo | Tipo | Escala |
| :--- | :--- | :--- |
| id_cliente | int | Nominal |
| nombre_cliente | str | Nominal |
| email | str | Nominal |
| ciudad | str | Nominal |
| fecha_alta | date | Intervalo|

### Ventas (ventas.csv) — ~120 filas
| Campo | Tipo | Escala |
| :--- | :--- | :--- |
| id_venta | int | Nominal |
| fecha | date | Intervalo |
| id_cliente | int | Nominal |
| nombre_cliente | str | Nominal |
| email | str | Nominal |
| medio_pago | str | Nominal |

### Detalle_Ventas (detalle_ventas.csv) — ~300 filas
| Campo | Tipo | Escala |
| :--- | :--- | :--- |
| id_venta | int | Nominal |
| id_producto | int | Nominal |
| nombre_producto | str | Nominal |
| cantidad | int | Razón |
| precio_unitario | int | Razón |
| importe | int | Razón |
"""

sugerencias_copilot = """
4. Sugerencias y mejoras aplicadas con Copilot
* Separar la documentación en plantillas reutilizables (por ejemplo, textos.py) y desacoplarla del código del menú. (APLICADA)
* Proveer un modo “búsqueda” para localizar palabras clave dentro de la documentación (e.g., “precio”, “escala”). (DESCARTADA para esta demo)
* Agregar una opción “exportar sección” para guardar en .txt/.md lo mostrado por pantalla. (DESCARTADA para esta demo)
* Incluir tests mínimos para el router de opciones (verifica que cada número abra la sección correcta). (DESCARTADA para esta demo)
"""

escalas_medicion = """
### Escalas de medición

Las escalas de medición son utilizadas para clasificar y medir los datos. En este proyecto, encontramos las siguientes:

- **Nominal:** Se usan para etiquetar variables sin ningún orden cuantitativo. Son como categorías o nombres.
    - *Ejemplos:* `id_producto`, `nombre_producto`, `categoria`, `id_cliente`, `nombre_cliente`, `email`, `ciudad`, `medio_pago`.

- **Intervalo:** Son escalas numéricas en las que conocemos el orden y la diferencia exacta entre los valores. El cero es arbitrario y no significa ausencia de la variable.
    - *Ejemplos:* `fecha_alta`, `fecha` (Las fechas son un tipo de dato de intervalo).

- **Razón:** Similares a las de intervalo, pero con un cero absoluto que sí indica la ausencia de la variable. Permiten todas las operaciones aritméticas.
    - *Ejemplos:* `precio_unitario`, `cantidad`, `importe`.
"""