# 📊 Clase 7 – Estadística Aplicada con Python

## 🎯 Objetivos
- Comprender los conceptos de **estadística descriptiva**.
- Analizar la **distribución de datos** y las **relaciones entre variables**.
- Aplicar **medidas estadísticas** con Python (Pandas).

---

## 📈 1. ¿Qué es la estadística aplicada?
Conjunto de **técnicas para entender y resumir datos**, que permiten:
- Describir características principales.  
- Detectar patrones o tendencias.  
- Medir relaciones entre variables.  
- Apoyar la toma de decisiones basada en evidencia.

---

## 🐼 2. Exploración con Pandas

| Función | Propósito | Resultado |
|----------|------------|------------|
| `df.describe()` | Resumen estadístico general | Media, mediana, min, max, etc. |
| `df.info()` | Información del dataset | Tipos, nulos y memoria |
| `df.value_counts()` | Frecuencias de categorías | Conteo por valores |
| `df.groupby().agg()` | Estadísticas por grupo | Promedios y totales por segmento |

```python
df.groupby('Categoria')['Ventas'].agg(['mean','max','min'])
```

---

## 📏 3. Estadística descriptiva

| Medida | Comando | Descripción |
|---------|----------|-------------|
| **Media** | `df['col'].mean()` | Promedio aritmético |
| **Mediana** | `df['col'].median()` | Valor central |
| **Moda** | `df['col'].mode()` | Valor más frecuente |
| **Desviación estándar** | `df['col'].std()` | Nivel de dispersión |

---

## 📊 4. Medidas de posición

| Medida | Comando | Interpretación |
|---------|----------|----------------|
| **Mínimo / Máximo** | `df['col'].min() / max()` | Límites del rango |
| **Cuartiles** | `df['col'].quantile([0.25,0.5,0.75])` | Divide datos en 4 partes |
| **Rango** | `df['col'].max() - df['col'].min()` | Diferencia entre valores extremos |

**Ejemplo interpretativo:**
- Media: 45  
- Mediana: 38  
- Moda: 35  
- Desviación estándar: 15  
- Rango: 80 (min: 20, máx: 100)

📌 **Conclusión:** los salarios son variables y dispersos; la media > mediana indica una distribución sesgada a la derecha.

---

## 🧭 5. Distribuciones de datos

| Tipo de distribución | Característica | Ejemplo |
|-----------------------|----------------|----------|
| **Normal** | Simétrica (campana de Gauss) | Alturas, pesos |
| **Sesgada** | Cola hacia un lado | Ingresos |
| **Bimodal** | Dos picos | Tráfico en horas pico |
| **Multimodal** | Varios picos | Preferencias diversas |
| **Uniforme** | Frecuencias similares | Números aleatorios |

💡 **Identificación:**
- Si media ≈ mediana → distribución normal o uniforme.  
- Si son muy diferentes → hay sesgo o asimetría.

---

## 🔗 6. Correlaciones

| Valor | Interpretación |
|--------|----------------|
| +1 | Correlación positiva perfecta |
| 0 | Sin relación lineal |
| -1 | Correlación negativa perfecta |

```python
df[['var1','var2']].corr()
```

📊 **Ejemplo:**
- Ventas y Publicidad = 0.85 → relación fuerte y directa.  
- Precio y Demanda = -0.90 → relación inversa.

⚠️ **Errores comunes:**
- Correlación ≠ causalidad.  
- Media y mediana diferentes indican valores extremos.

---

## 📏 7. Evaluación de confiabilidad

| Concepto | Descripción |
|-----------|--------------|
| **Desviación estándar baja** | Datos consistentes |
| **Desviación estándar alta** | Datos dispersos |
| **Outliers** | Revisar antes de eliminar, pueden ser errores o información relevante |

---

## 🧩 8. Ejercicio – Rendimiento E-commerce

**Dataset:**

| Mes | Ventas ($) | Visitantes | Conversión (%) | Publicidad ($) | Productos Vendidos |
|-----|-------------|-------------|----------------|----------------|--------------------|
| Ene | 45,000 | 15,000 | 3.2 | 8,500 | 450 |
| Feb | 52,000 | 18,200 | 2.9 | 9,800 | 520 |
| Mar | 38,000 | 12,500 | 3.8 | 7,200 | 380 |
| Abr | 61,000 | 20,500 | 3.1 | 11,200 | 610 |
| May | 48,000 | 16,800 | 2.7 | 9,500 | 480 |

```python
import pandas as pd

data = {
  'Mes':['Ene','Feb','Mar','Abr','May'],
  'Ventas':[45000,52000,38000,61000,48000],
  'Visitantes':[15000,18200,12500,20500,16800],
  'Conversion':[3.2,2.9,3.8,3.1,2.7],
  'Publicidad':[8500,9800,7200,11200,9500],
  'Productos':[450,520,380,610,480]
}

df = pd.DataFrame(data)

# 1. Eficiencia (ROI)
df['Eficiencia'] = df['Ventas'] / df['Publicidad']
print("Mayor eficiencia:", df.loc[df['Eficiencia'].idxmax(), 'Mes'])

# 2. Mejor conversión
print("Mejor conversión:", df.loc[df['Conversion'].idxmax(), 'Mes'])

# 3. Ticket promedio
df['Ticket'] = df['Ventas'] / df['Productos']
print(df[['Mes','Ticket']])

# 4. Correlación
print(df[['Visitantes','Ventas']].corr())
```

**Conclusiones:**
- Abril tiene la mayor eficiencia.  
- Marzo muestra la mejor conversión.  
- Ticket promedio ≈ $100 por producto.  
- Fuerte correlación entre visitantes y ventas.

---

## 🧱 9. Proyecto – Tienda Aurelion

Etapa: **Análisis estadístico descriptivo**

**Tareas del equipo:**
1. Calcular estadísticas básicas (media, mediana, moda, desvío).  
2. Identificar tipo de distribución.  
3. Calcular correlaciones.  
4. Detectar outliers.  
5. Interpretar resultados para la toma de decisiones.  
6. Documentar todo con ayuda de **Copilot**.
