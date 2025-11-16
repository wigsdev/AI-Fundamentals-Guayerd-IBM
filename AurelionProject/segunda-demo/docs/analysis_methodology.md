# Documentación Actualizada del Análisis - Proyecto Aurelion

## 1. Introducción

**Objetivo:** Este documento detalla el proceso de análisis y la estructura narrativa del notebook `AnalisisProjectAurelionFinal.ipynb`. El objetivo es documentar la metodología utilizada para generar los hallazgos y la lógica de la presentación.

**Fuente de Datos:** `ventas_limpias.csv`.

---

## 2. Configuración y Carga de Datos

El primer paso consistió en preparar el entorno de análisis en Jupyter.
* **Importación de Librerías:** `pandas`, `matplotlib`, `seaborn`, y `mlxtend`.
* **Configuración Visual:** Se estableció un tema `dark_background` (`plt.style.use()`) y se estandarizó la eliminación de los bordes superior y derecho (`rcParams`) para todos los gráficos.
* **Pre-procesamiento:** Se aseguró que la columna `fecha` estuviera en el formato `datetime` correcto.

---

## 3. Análisis Exploratorio y Estadístico (EDA)

Esta sección se estructuró de forma didáctica en tres partes para construir un argumento claro sobre la naturaleza de los datos.

1.  **Estadísticas Descriptivas (Gráfico de Barras):**
    * **Propósito:** Introducir y comparar visualmente las métricas clave: **Media, Mediana y Desviación Estándar**. La diferencia visual entre la barra de Media y Mediana sirve como la primera pista de asimetría.
2.  **Distribución (Histogramas):**
    * **Propósito:** Mostrar la "forma" de los datos, confirmando el sesgo a la derecha en `importe` y `precio_unitario`.
3.  **Identificación de Outliers (Diagramas de Caja):**
    * **Propósito:** Diagnosticar la *causa* de la asimetría (los outliers) y validar por qué la **Mediana** es el indicador más robusto del "ticket típico".
    
* **Conclusión de la Sección:** Esta sección es puramente descriptiva ("el qué"). Concluye con la interpretación de los hallazgos de correlación, pero las *acciones* (el "qué hacer") se reservan para la sección final.

---

## 4. Análisis Comercial Básico

Se realizaron agrupaciones (`groupby`) para entender las dimensiones de negocio.
* **Análisis:** Ventas por Categoría, Ventas por Ciudad, y Frecuencia de Métodos de Pago.
* **Propósito:** Obtener una "fotografía" rápida del rendimiento: qué se vende (Alimentos), dónde (Río Cuarto) y cómo pagan (Efectivo).
* **Conclusión de la Sección:** La sección concluye con interpretaciones y recomendaciones tácticas específicas para cada gráfico (ej. incentivar QR, enfocar marketing en ciudades secundarias).

---

## 5. Análisis Temporal

Se crearon columnas `mes` y `dia_semana` para identificar patrones de estacionalidad.
* **Análisis:** Gráfico de línea de Ventas Mensuales y gráfico de barras de Ventas por Día de la Semana.
* **Propósito:** Identificar los picos y valles de la demanda.
* **Conclusión de la Sección:** Concluye identificando los puntos débiles (ej. Sábado, mes de Abril) y fuertes (ej. Martes), con recomendaciones específicas de calendario promocional.

---

## 6. Análisis de Rendimiento de Productos

Se agruparon las ventas por `nombre_producto` para identificar los extremos del catálogo.
* **Análisis:** Gráfico de barras Top 5 (Más Vendidos) y Bottom 5 (Menos Vendidos) por cantidad.
* **Propósito:** Identificar los "productos estrella" y los "productos problema".
* **Conclusión de la Sección:** Concluye con recomendaciones tácticas sobre gestión de inventario y evaluación de catálogo.

---

## 7. Segmentación de Clientes (RFM)

Se realizó un análisis avanzado para clasificar a los clientes por su valor (Recencia, Frecuencia, Monetario).
* **Análisis:** Cálculo de R, F y M; asignación de segmentos (ej. "Campeones", "En Riesgo").
* **Propósito:** Pasar de un análisis de "ventas" a uno de "clientes", identificando los grupos más valiosos.
* **Conclusión de la Sección:** Concluye con recomendaciones de CRM altamente específicas para cada segmento (ej. fidelizar "Campeones", reactivar "En Riesgo").

---

## 8. Análisis de Canasta (Reglas de Asociación)

Se utilizó el algoritmo **Apriori** (`mlxtend`) para encontrar patrones de compra conjunta.
* **Análisis:** Preparación de matriz *one-hot*, generación de reglas, y visualización del Top 10 por `Lift`.
* **Propósito:** Descubrir oportunidades de *cross-selling* (venta cruzada) no evidentes.
* **Conclusión de la Sección:** Concluye con recomendaciones tácticas claras sobre *bundles* y *layout* de tienda.

---

## 9. Análisis de Pareto (80/20)

Como cierre de la fase analítica, se cuantificó el "Principio de Pareto".
* **Análisis:** Cálculo del porcentaje de productos y clientes que generan el 80% de los ingresos.
* **Propósito:** Confirmar la tesis de que el negocio es impulsado por una "minoría vital".
* **Conclusión de la Sección:** Concluye con la recomendación estratégica de *focalizar* esfuerzos en este grupo vital.

---

## 10. Estrategias y Plan de Acción (Sección Final)

Esta sección final tiene un propósito diferente. **No introduce nuevos hallazgos**. Su función es actuar como la **síntesis ejecutiva y estratégica** de toda la presentación:

1.  **Agrupación Estratégica:** Toma todas las recomendaciones tácticas de las secciones 4-9 y las **agrupa** en 3 grandes pilares estratégicos (ej. "Estrategia de Foco", "Estrategia Comercial", "Estrategia de Operaciones").
2.  **Priorización:** Presenta un plan de implementación priorizado (`Plan 30/60/90 Días`).
3.  **Visión a Futuro:** Sugiere análisis adicionales (`Sugerencias de Visualización Adicional`).
4.  **Cierre:** Provee la `Síntesis Final` o conclusión general del proyecto.

Esta estructura está diseñada para una presentación en grupo, donde cada miembro concluye su sección (4-9) y el presentador final utiliza la sección 10 para unificar todos los puntos en un plan de acción coherente.