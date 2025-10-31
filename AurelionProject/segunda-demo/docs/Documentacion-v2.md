# Análisis de Ventas - Segunda Demo del Proyecto Aurelion

**Fecha de Análisis:** 2023-10-30

## 1. Objetivo del Análisis

El objetivo de este documento es presentar un análisis exploratorio de los datos de ventas del proyecto Aurelion. A través de estadísticas descriptivas, análisis de distribución y visualizaciones, se busca extraer insights clave sobre el comportamiento de los clientes, el rendimiento de los productos y las tendencias geográficas para fundamentar futuras decisiones de negocio.

## 2. Fuente de Datos

El análisis se basa en el archivo `ventas_limpias.csv`, que contiene datos de transacciones procesados y limpiados, listos para el análisis.

## 3. Resumen Ejecutivo (Principales Hallazgos)

1.  **Perfil de Compra:** El cliente promedio compra 3 artículos por transacción. Existen compras de valor atípicamente alto (outliers) que son infrecuentes pero muy importantes para el negocio y merecen un análisis detallado.
2.  **Foco del Negocio en Alimentos:** La categoría **Alimentos** es, por lejos, el principal motor de ingresos del negocio.
3.  **Mercados Geográficos Clave:** **Río Cuarto** y **Córdoba** son los mercados más importantes en términos de ventas.
4.  **Incorrelación Precio-Cantidad:** No existe una correlación significativa entre el precio de un artículo y la cantidad comprada.
5.  **Preferencia por Pagos Digitales:** Se observa una fuerte adopción de métodos de pago digitales como **QR** y **Tarjeta**.

---

## 4. Análisis Detallado

### 4.1. Estadísticas Descriptivas

A continuación se presenta un resumen estadístico de las variables numéricas clave:

| | cantidad | importe | precio_unitario |
|:---|---:|---:|---:|
| **count** | 343.0 | 343.0 | 343.0 |
| **mean** | 2.96 | 7730.1 | 2654.5 |
| **std** | 1.37 | 5265.5 | 1308.7 |
| **min** | 1.0 | 272.0 | 272.0 |
| **25%** | 2.0 | 3489.0 | 1618.5 |
| **50%** | 3.0 | 6702.0 | 2512.0 |
| **75%** | 4.0 | 10231.5 | 3876.0 |
| **max** | 5.0 | 24865.0 | 4982.0 |

- **Interpretación:** La cantidad promedio por línea de venta es cercana a 3 unidades. El `importe` muestra una alta desviación estándar, indicando una gran variabilidad en el valor de las transacciones, lo cual es consistente con la presencia de ventas de muy alto valor.

### 4.2. Distribución de Variables

- **Precio Unitario:** La distribución no sigue una campana de Gauss perfecta; presenta varios picos que podrían indicar diferentes rangos de precios.
- **Cantidad:** La distribución de la cantidad de productos por compra es bastante uniforme en su rango.
- **Importe:** La distribución del importe está **sesgada a la derecha**, lo que significa que la mayoría de las transacciones son de bajo valor, pero hay unas pocas con importes muy altos.

### 4.3. Detección de Outliers

- **Precio Unitario y Cantidad:** No se observan outliers significativos.
- **Importe:** Se detectan varios outliers que corresponden a las transacciones de mayor valor. No son errores, sino que representan las compras más grandes y de mayor interés para el negocio.

### 4.4. Análisis de Correlación

La relación lineal entre las variables numéricas se resume en la siguiente matriz:

| | cantidad | importe | precio_unitario |
|:---|---:|---:|---:|
| **cantidad** | 1.00 | 0.60 | -0.07 |
| **importe** | 0.60 | 1.00 | 0.68 |
| **precio_unitario**| -0.07| 0.68 | 1.00 |

- **Interpretación:**
    - Existe una **correlación positiva fuerte** (0.68) entre `importe` y `precio_unitario`.
    - Se observa una **correlación positiva moderada** (0.60) entre `importe` y `cantidad`.
    - Notablemente, **no hay una correlación significativa** (-0.07) entre `precio_unitario` y `cantidad`, indicando que el precio no es un factor decisivo en la cantidad de unidades que compra un cliente.

---

## 5. Gráficos Representativos y su Interpretación

1.  **Gráfico de Barras: Ventas Totales por Categoría**
    - **Interpretación:** La categoría "Alimentos" domina abrumadoramente las ventas.

2.  **Gráfico de Barras: Ventas Totales por Ciudad**
    - **Interpretación:** Río Cuarto y Córdoba son las ciudades líderes en ventas.

3.  **Gráfico de Barras: Frecuencia de Métodos de Pago**
    - **Interpretación:** Confirma la preferencia por métodos digitales (QR y Tarjeta).

---

## 6. Conclusiones y Próximos Pasos

El análisis revela un negocio con un fuerte enfoque en **Alimentos**, una sólida base de clientes en **Río Cuarto y Córdoba**, y una buena adopción de **pagos digitales**.

**Recomendaciones y Próximos Pasos:**

- **Analizar Clientes de Alto Valor:** Investigar las transacciones marcadas como outliers para identificar clientes VIP o patrones de compra mayorista.
- **Estrategia de Categorías:** Desarrollar campañas de marketing para la categoría "Alimentos" y considerar estrategias para impulsar "Limpieza".
- **Foco Geográfico:** Profundizar el análisis en las ciudades con menor rendimiento para diseñar campañas de marketing localizado.
- **Estrategia de Precios:** Dado que el precio no influye en la cantidad, explorar estrategias de "upselling" o "cross-selling".
