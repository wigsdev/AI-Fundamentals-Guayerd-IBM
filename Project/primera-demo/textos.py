# -*- coding: utf-8 -*-
# Proyecto: Tienda Aurelion - 1° Demo Asincrónica
# Curso: Fundamentos de Inteligencia Artificial (IBM)
# Descripción: Textos de documentación para el visor interactivo.

# -------------------------------------------------------
# 1. Tema, problema y solución
# -------------------------------------------------------
tema_problema_solucion = """
1️⃣ Tema, problema y solución

🧠 Tema:
Gestión de datos de una tienda minorista mediante la integración de información de clientes, productos y transacciones de venta.
El proyecto "Tienda Aurelion" utiliza datos sintéticos representativos de un comercio real para comprender cómo los sistemas de información pueden organizar, describir y analizar datos comerciales.

⚠️ Problema:
La tienda almacena sus registros en distintos archivos (clientes, productos, ventas y detalle_ventas), sin un sistema central que permita comprender la estructura y relación entre ellos.
Esta fragmentación de la información dificulta tareas clave como:
- identificar los productos más vendidos o las categorías con mayor demanda,
- analizar los medios de pago más utilizados,
- conocer la evolución de clientes por ciudad o fecha de alta,
- realizar proyecciones basadas en datos históricos.
En consecuencia, el negocio carece de una visión integrada y analítica de su operación, lo que limita la toma de decisiones basadas en evidencia.

💡 Solución:
Desarrollar un visor interactivo de documentación en Python que permite explorar, desde la terminal, toda la información descriptiva del proyecto:
- tema y propósito,
- definición y estructura del dataset,
- descripción de las tablas y escalas de medición,
- sugerencias de mejora para futuras etapas.
El objetivo de esta primera entrega es entender los datos antes de procesarlos o analizarlos.
El visor constituye el primer componente de una solución analítica más amplia, en la que luego podrán incorporarse visualizaciones y modelos predictivos.
"""

# -------------------------------------------------------
# 2. Dataset de referencia
# -------------------------------------------------------
dataset_referencia = """
2️⃣ Dataset de referencia

Fuente:
Datos sintéticos generados con fines educativos, para representar la operación de una tienda minorista.

Definición:
Conjunto de archivos que simulan un entorno de ventas, integrando catálogo de productos, registro de clientes, operaciones de venta y detalles de cada transacción.
"""

# -------------------------------------------------------
# 3. Estructura por tabla
# -------------------------------------------------------
estructura_tablas = """
3️⃣ Estructura por tabla

🛍️ Productos (productos.csv)
| Campo | Tipo | Escala |
| :--- | :--- | :--- |
| id_producto | int | Nominal |
| nombre_producto | str | Nominal |
| categoria | str | Nominal |
| precio_unitario | int | Razón |

👥 Clientes (clientes.csv)
| Campo | Tipo | Escala |
| :--- | :--- | :--- |
| id_cliente | int | Nominal |
| nombre_cliente | str | Nominal |
| email | str | Nominal |
| ciudad | str | Nominal |
| fecha_alta | date | Intervalo |

💳 Ventas (ventas.csv)
| Campo | Tipo | Escala |
| :--- | :--- | :--- |
| id_venta | int | Nominal |
| fecha | date | Intervalo |
| id_cliente | int | Nominal |
| nombre_cliente | str | Nominal |
| email | str | Nominal |
| medio_pago | str | Nominal |

📦 Detalle_Ventas (detalle_ventas.csv)
| Campo | Tipo | Escala |
| :--- | :--- | :--- |
| id_venta | int | Nominal |
| id_producto | int | Nominal |
| nombre_producto | str | Nominal |
| cantidad | int | Razón |
| precio_unitario | int | Razón |
| importe | int | Razón |
"""

# -------------------------------------------------------
# 4. Escalas de medición
# -------------------------------------------------------
escalas_medicion = """
4️⃣ Escalas de medición

Las escalas de medición permiten clasificar los datos según su tipo y nivel de análisis. En este proyecto se utilizan las siguientes:

- **Nominal:** identifican elementos sin un orden cuantitativo.
  Ejemplo: id_cliente, nombre_producto, categoria, ciudad, medio_pago.
- **Intervalo:** valores numéricos con diferencias medibles pero sin un cero absoluto.
  Ejemplo: fecha_alta, fecha (fechas de alta y de venta).
- **Razón:** datos numéricos con cero absoluto que permiten operaciones aritméticas.
  Ejemplo: cantidad, precio_unitario, importe.
"""

# -------------------------------------------------------
# 5. Sugerencias y mejoras con Copilot
# -------------------------------------------------------
sugerencias_copilot = """
5️⃣ Sugerencias y mejoras aplicadas con Copilot

✅ Aplicadas:
- Separar la documentación en plantillas reutilizables (textos.py).
- Limpiar la pantalla antes de mostrar el menú.
- Agregar pausa tras mostrar resultados.

🚧 Pendientes:
- Implementar modo "búsqueda" de palabras clave.
- Agregar opción "exportar sección" a archivo .txt o .md.
- Incluir tests automáticos para verificar la opción seleccionada.
"""
