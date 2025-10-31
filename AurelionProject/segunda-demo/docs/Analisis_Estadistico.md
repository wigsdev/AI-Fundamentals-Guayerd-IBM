# Documentación del Análisis Estadístico - Tienda Aurelion

Este documento resume el proceso de análisis estadístico descriptivo realizado sobre los datos de ventas de la Tienda Aurelion. El análisis completo, incluyendo el código fuente, se encuentra en el cuaderno de Jupyter `../code/analisis_estadistico_aurelion.ipynb`.

## Proceso de Análisis

El análisis se estructuró en los siguientes pasos, siguiendo las directrices del proyecto:

### 1. Carga y Preparación de Datos
- **Fuente de Datos:** `ventas_limpias.csv`
- **Librerías Utilizadas:** `pandas` para la manipulación de datos, y `matplotlib`/`seaborn` para la visualización.
- **Acción:** Se cargaron los datos en un DataFrame de pandas para su procesamiento.

### 2. Cálculo de Estadísticas Básicas
Se calcularon las siguientes métricas para las variables numéricas clave (`cantidad`, `precio_unitario_x`, `importe`):
- **Media:** Promedio de los valores.
- **Mediana:** Valor central de los datos.
- **Moda:** Valor más frecuente.
- **Desviación Estándar:** Medida de la dispersión de los datos.

### 3. Análisis de la Distribución de Datos
Se generaron histogramas para visualizar cómo se distribuyen los datos de las variables numéricas. Esto permite identificar si la distribución es normal, sesgada, etc.

### 4. Estudio de Correlaciones
Se calculó una matriz de correlación y se visualizó como un mapa de calor (heatmap) para identificar la fuerza y dirección de la relación lineal entre las variables.

### 5. Detección de Outliers (Valores Atípicos)
Se utilizaron diagramas de caja (boxplots) para identificar visualmente la presencia de outliers en las variables numéricas, los cuales podrían requerir una investigación más a fondo.

### 6. Interpretación y Conclusiones
Cada paso del análisis incluye un espacio para la interpretación de los resultados, culminando en una sección de conclusiones generales para la toma de decisiones de negocio.

## Conclusión del Proceso
El cuaderno de Jupyter proporciona una guía completa y ejecutable para entender las características principales de los datos de ventas de la tienda, desde las métricas más básicas hasta la identificación de patrones y anomalías.
