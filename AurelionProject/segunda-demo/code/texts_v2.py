# -*- coding: utf-8 -*-
# Proyecto: Tienda Aurelion - 2° Demo Asincrónica
# Curso: Fundamentos de Inteligencia Artificial (IBM)
# Descripción: Textos de documentación para el visor interactivo v2.

# -------------------------------------------------------
# 0. Limpieza y Transformación de Datos
# -------------------------------------------------------
data_cleaning_transformations = """
0. Limpieza y Transformación de Datos

Este documento detalla el proceso de limpieza y preparación de datos llevado a cabo para los datasets de la tienda Aurelion. El objetivo principal fue consolidar la información de ventas, clientes, productos y detalles de ventas en un único dataset limpio y coherente, listo para el análisis.

El proceso se ejecutó utilizando la librería `pandas` en un notebook de Jupyter y consistió en los siguientes pasos:

1. Carga de Datos
   - Se cargaron los archivos .xlsx: `clientes`, `detalle_ventas`, `productos`, y `ventas`.

2. Inspección Inicial
   - Se usaron `df.info()`, `df.isnull().sum()`, y `df.head()` para identificar problemas.
   - Hallazgos: inconsistencia en nombres de columnas (ej. `ID_Venta` vs. `id_venta`).

3. Proceso de Limpieza y Transformación
   - Manejo de Duplicados: Se eliminaron con `df.drop_duplicates(inplace=True)`.
   - Manejo de Valores Faltantes: Se eliminaron filas sin `nombre_cliente`.
   - Corrección de Nombres de Columnas: Se estandarizaron las claves para los merges (ej. `id_venta`).

4. Unión de los Datos (Merge)
   - Se unieron las cuatro tablas para crear un único DataFrame (`ventas_full_df`).

5. Guardado de Datos Limpios
   - El DataFrame final se guardó como `ventas_limpias.csv`, listo para el análisis.
"""

# -------------------------------------------------------
# 1. Análisis Exploratorio y Estadístico
# -------------------------------------------------------
analisis_exploratorio = """
1. Análisis Exploratorio y Estadístico

- Interpretación de Estadísticas Clave
  - Importe y Precio Unitario: La Media es notablemente más alta que la Mediana, lo que indica la presencia de valores atípicos (ventas de importe muy alto) que inflan el promedio. La Mediana es una métrica más representativa del valor "típico" de una transacción.
  - Cantidad: La Media (aprox. 2.96) y la Mediana (3.0) son muy similares, lo que sugiere que la cantidad de productos por venta es consistente y no presenta valores extremos.
  - Desviación Estándar: La alta dispersión en `Importe` y `Precio Unitario` confirma una gran variabilidad en los datos (ventas y precios muy baratos y muy caros).

- Interpretación de la Distribución de Variables
  - Precio Unitario: La mayoría de los productos tiene un precio inferior a $3,000, con un pico de frecuencia cercano a los $2,000. Los precios más altos son menos comunes.
  - Cantidad por Venta: La distribución es bastante uniforme, con una ligera mayor frecuencia en ventas de 1 a 3 unidades.
  - Importe por Venta: La mayoría de las transacciones se concentra en importes inferiores a $10,000, con un pico entre $5,000 y $8,000. Existen ventas excepcionales con valores superiores a $20,000.

- Detección de Outliers (Valores Atípicos)
  - Precio Unitario y Cantidad: No se observan outliers significativos, lo que sugiere una distribución estable y predecible.
  - Importe: Se identifican outliers claros por encima de $20,000, confirmando la existencia de transacciones de alto valor que se desvían del comportamiento general.

- Matriz de Correlación
  - Cantidad e Importe (Correlación: 0.60): Moderada y positiva. A más productos, mayor es el importe de la venta.
  - Importe y Precio Unitario (Correlación: 0.68): Moderada y positiva. A mayor precio del producto, mayor es el importe total.
  - Cantidad y Precio Unitario (Correlación: -0.07): Muy débil, casi nula. El precio de un producto no parece influir en la cantidad que se compra.
"""

# -------------------------------------------------------
# 2. Análisis de Negocio
# -------------------------------------------------------
ventas_por_categoria = """
- Ventas por Categoría de Producto
  - Alimentos: Domina las ventas con un total de $2,214,681. Es la principal fuente de ingresos del negocio.
  - Limpieza: Genera un total de $436,736, representando una porción significativamente menor de los ingresos.
  - Recomendación: Implementar estrategias para fortalecer las ventas en "Limpieza" (ej. combos con Alimentos) para diversificar los ingresos.
"""

ventas_por_ciudad = """
- Ventas por Ciudad
  - Río Cuarto: Lidera las ventas con $792,203, consolidándose como el mercado principal.
  - Alta Gracia y Córdoba: Mercados de gran relevancia con ventas de $481,504 y $481,482 respectivamente.
  - Ciudades con menor rendimiento: Carlos Paz ($353,852), Villa María ($313,350) y Mendiolaza ($229,026).
  - Recomendación: Enfocar esfuerzos de marketing y distribución en las ciudades con menor participación para potenciar su crecimiento.
"""

metodo_pago = """
- Método de Pago Más Utilizado
  1. Efectivo: 111 transacciones.
  2. QR: 91 transacciones.
  3. Transferencia: 72 transacciones.
  4. Tarjeta: 69 transacciones.
  - Recomendación: Fomentar métodos digitales (QR), que ya tienen alta adopción, para mejorar la eficiencia operativa.
"""

# -------------------------------------------------------
# 3. Análisis de Series Temporales
# -------------------------------------------------------
analisis_series_temporales = """
3. Análisis de Series Temporales

- Evolución de Ventas Mensuales
  - Se observa una caída en ventas durante los primeros meses, seguida de un fuerte repunte en abril y mayo, donde se alcanzan los $550,000.
  - Recomendación: Implementar promociones durante los meses de baja (enero-marzo) y anticipar la demanda de inventario para los meses de repunte (abril-mayo).

- Distribución de Ventas por Día de la Semana
  - Días más fuertes: El Martes es el día de mayores ventas (aprox. $600,000).
  - Día más débil: El Sábado presenta el desempeño más bajo, lo cual es atípico en retail.
  - Recomendación: Implementar ofertas especiales los Sábados para incentivar el consumo y reforzar las campañas los Martes para maximizar los ingresos en el día pico.
"""

# -------------------------------------------------------
# 4. Análisis de Productos
# -------------------------------------------------------
analisis_productos = """
4. Análisis de Productos

- Top 5 Productos Más Vendidos (por cantidad)
  1. Salsa de Tomate 500g: 25 unidades
  2. Queso Rallado 150g: 22 unidades
  3. Hamburguesas Congeladas x4: 21 unidades
  4. Vino Blanco 750ml: 20 unidades
  5. Aceitunas Verdes 200g: 19 unidades

- Bottom 5 Productos Menos Vendidos (por cantidad)
  1. Maní Salado 200g: 2 unidades
  2. Detergente Líquido 750ml: 2 unidades
  3. Chocolate con Leche 750g: 3 unidades
  4. Alfajor Triple: 3 unidades
  5. Galletitas Vainilla: 3 unidades

- Recomendación: Asegurar el stock de los productos Top 5 ("vitales"). Evaluar la rentabilidad de los Bottom 5; considerar descontinuarlos o usarlos en bundles de liquidación.
"""

# -------------------------------------------------------
# 5. Segmentación de Clientes (Análisis RFM)
# -------------------------------------------------------
segmentacion_clientes = """
5. Segmentación de Clientes (Análisis RFM)

- Clientes Activos (Campeones, Leales, etc.): Representan la mayor proporción.
- Clientes en Riesgo: Muestran señales de desconexión (ej. baja frecuencia reciente).
- Clientes Inactivos (Hibernando, etc.): Han perdido el interés.
- Recomendación: Personalizar las estrategias: recompensar a los clientes leales (fidelización), reactivar a los que están en riesgo (retención) y diseñar campañas de recuperación para los inactivos.
"""

# -------------------------------------------------------
# 6. Análisis de Canasta de Mercado
# -------------------------------------------------------
analisis_canasta = """
6. Análisis de Canasta de Mercado (Reglas de Asociación)

- Asociación más fuerte (Lift = 24.0): `Coca Cola 1.5L` y `Cerveza Negra 1L`.
- Otras asociaciones fuertes (Lift > 20):
  - `Queso Azul 150g` y `Crema Dental 90g`.
  - `Verduras Congeladas Mix` y `Jugo de Manzana 1L`.
- Recomendación: Utilizar estas asociaciones para crear "combos" (cross-selling), optimizar la disposición de productos en la tienda y aumentar el ticket promedio.
"""

# -------------------------------------------------------
# 7. Análisis de Pareto
# -------------------------------------------------------
analisis_pareto = """
7. Análisis de Pareto

- Pareto de Productos
  - Hallazgo: El 80% de los ingresos es generado por solo el 52.63% de los productos (50 de 95).
  - Recomendación (Estratégica): Priorizar el 53% de productos "vitales" en gestión de inventario y marketing.

- Pareto de Clientes
  - Hallazgo: El 80% de los ingresos es generado por solo el 57.81% de los clientes (37 de 64).
  - Recomendación (Estratégica): La retención de este 58% de clientes "vitales" es más crítica que la adquisición de nuevos.
"""

# -------------------------------------------------------
# 8. Estrategias y Plan de Acción
# -------------------------------------------------------
estrategias_plan_accion = """
8. Estrategias y Plan de Acción

Basado en los hallazgos y recomendaciones específicas detalladas en cada sección anterior, se presenta el plan de acción consolidado para el negocio.

- Estrategias y Recomendaciones
  - 1. Estrategia de Foco (Basada en Pareto y RFM)
    - Prioridad #1 - Reactivación: Diseñar campañas de marketing personalizadas (email o cupones) dirigidas específicamente a los segmentos "En Riesgo" y "Necesitan Atención".
    - Prioridad #2 - Fidelización: Implementar un programa de "Clientes VIP" (Club de puntos, acceso exclusivo) para los segmentos "Campeones" y "Leales".
  - 2. Estrategia Comercial (Basada en Canasta y Temporalidad)
    - Bundles Inteligentes: Crear "Combos" basados en las reglas de asociación (ej. Combo Bebidas, Combo Frescos, Combo Limpieza/Hogar).
    - Layout de Tienda: Reorganizar físicamente las góndolas para posicionar los productos asociados.
    - Calendario Promocional:
      - Lanzar una campaña agresiva en Abril (mes más bajo).
      - Crear promociones de tráfico para los Sábados (día más bajo), ej. "Sábados de Ahorro".
      - Asegurar el stock para los Martes (día más fuerte).
  - 3. Estrategia de Operaciones y Expansión (Basada en Geo y Pagos)
    - Eficiencia de Pagos: Incentivar activamente el uso de QR (ej. "Pagando con QR, participas de...") para reducir los costos de manejo de efectivo.
    - Expansión Local: Lanzar campañas de marketing geo-localizadas en Mendiolaza y Carlos Paz para aumentar la penetración.
    - Gestión de Inventario: Utilizar el Pareto "53/80" para redefinir los niveles de stock de seguridad de los productos "vitales".

- Plan 30/60/90 Días
  - 30 días: Lanzamiento de 2 bundles + cupón de retención + incentivo QR
  - 60 días: Programa de puntos + reorganización de góndola según asociaciones
  - 90 días: Evaluar recompra por cohortes + ampliación de bundles y club de fidelidad

- Sugerencias de Visualización Adicional
  - Gráficos: Heatmap Día × Hora, Ticket promedio por método de pago, Cohortes de recompra.
  - Tablas: Top 10 clientes por Monetario y Frecuencia, Top 10 asociaciones por Lift.

- Síntesis Final
  El análisis confirma que el negocio presenta:
  - Crecimiento sostenido, aunque concentrado geográficamente.
  - Oportunidades claras de retención y fidelización.
  - Potencial de mejora operativa mediante digitalización de pagos y gestión predictiva de stock.
"""
