# 📊 Clase 8 – Visualización con Python

---

## 🎯 Objetivos
- Comprender la **importancia de la visualización de datos**.  
- Aprender a crear gráficos con **Matplotlib** y **Seaborn**.  
- Aplicar buenas prácticas de diseño y comunicación visual.  

---

## 📈 1. Tipos de visualización

| Tipo | Propósito | Ejemplo |
|------|------------|----------|
| **Evolución temporal** | Mostrar cambios a lo largo del tiempo | Ventas mensuales |
| **Comparación categórica** | Comparar grupos o categorías | Ventas por sucursal |
| **Relación entre variables** | Analizar correlaciones | Precio vs demanda |
| **Distribución de datos** | Ver patrones y dispersiones | Edades de clientes |

### Ejemplos:
- **Líneas:** evolución de ventas durante 12 meses.  
- **Barras:** comparar satisfacción entre sucursales.  
- **Dispersión:** relación precio–demanda.  
- **Histograma:** distribución de edades.  

---

## 🧮 2. Librería Matplotlib

**Matplotlib** es la base para todos los gráficos en Python.  
Compatible con **NumPy** y **Pandas**, permite exportar en **PNG, PDF, SVG**, etc.

### 🔹 Instalación y uso
```bash
pip install matplotlib
```
```python
import matplotlib.pyplot as plt
```

---

## ⚙️ 3. Elementos fundamentales

| Elemento | Código | Propósito |
|-----------|---------|-----------|
| Crear figura | `plt.figure(figsize=(8,6))` | Define tamaño del gráfico |
| Agregar datos | `plt.plot(x, y)` | Dibuja líneas o puntos |
| Título | `plt.title('Texto')` | Agrega contexto |
| Ejes | `plt.xlabel('Eje X')`, `plt.ylabel('Eje Y')` | Claridad de variables |
| Mostrar | `plt.show()` | Renderiza el gráfico |

---

## 📉 4. Tipos de gráficos en Matplotlib

### 🔸 Gráficos de líneas
Para **series temporales** o tendencias.
```python
plt.plot(meses, ventas, marker='o')
plt.title("Evolución de Ventas")
plt.xlabel("Mes")
plt.ylabel("Ventas ($)")
plt.show()
```

### 🔸 Gráficos de barras
Para **comparaciones categóricas**.
```python
plt.bar(categorias, valores)
plt.title("Ventas por Categoría")
plt.xlabel("Categoría")
plt.ylabel("Ventas ($)")
plt.show()
```

- `plt.barh()` → barras horizontales.  
- Se pueden agrupar usando `width` o subplots.

### 🔸 Gráficos de dispersión
Para mostrar **relaciones entre variables**.
```python
plt.scatter(precio, demanda)
plt.title("Relación Precio - Demanda")
plt.xlabel("Precio")
plt.ylabel("Demanda")
plt.show()
```

### 🔸 Histogramas
Para **distribuciones y detección de outliers**.
```python
plt.hist(datos, bins=10, alpha=0.7)
plt.title("Distribución de Edades")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.show()
```

---

## 🧩 5. Otras funcionalidades útiles

- **Subplots** → crear varios gráficos en una misma figura.
  ```python
  fig, axs = plt.subplots(1, 2)
  axs[0].plot(x, y)
  axs[1].bar(x, y)
  plt.show()
  ```
- **Leyendas** → `plt.legend(['Serie A', 'Serie B'])`
- **Estilo** → `plt.style.use('ggplot')` o `plt.grid(True)`

---

## 🎨 6. Mejores prácticas de visualización

| Aspecto | Recomendación |
|----------|----------------|
| **Títulos** | Claros y descriptivos |
| **Colores** | Usar paletas consistentes y legibles |
| **Texto** | Evitar saturar con etiquetas |
| **Ejes** | Mantener proporciones coherentes |
| **Claridad** | Gráficos simples, directos y comparativos |

---

## 📊 7. Librería Seaborn

**Seaborn** está construida sobre Matplotlib, pero con una sintaxis más simple y visualmente atractiva.  
Ideal para **gráficos estadísticos**.

### 🔹 Instalación y uso
```bash
pip install seaborn
```
```python
import seaborn as sns
```

---

## 🧠 8. Gráficos principales en Seaborn

| Gráfico | Sintaxis | Uso |
|----------|-----------|-----|
| **Boxplot** | `sns.boxplot(data=df, x='cat', y='num')` | Outliers y cuartiles |
| **Violinplot** | `sns.violinplot(data=df, x='cat', y='num')` | Distribución y densidad |
| **Heatmap** | `sns.heatmap(df.corr(), annot=True)` | Matriz de correlaciones |
| **Scatterplot** | `sns.scatterplot(x='X', y='Y', data=df, hue='Categoria')` | Relación y segmentación |
| **Distplot** | `sns.histplot(data=df['col'], kde=True)` | Distribución con curva de densidad |

---

### 🧩 Boxplot – Componentes
- **Caja**: rango intercuartílico (Q1 a Q3).  
- **Línea central**: mediana.  
- **Bigotes**: 1.5×IQR (identifican outliers).  
- **Puntos**: valores atípicos.  

---

### 🔥 Heatmap – Partes principales
1. **Ejes (Axes):** representan variables.  
2. **Celdas (Cells):** cada color = valor numérico.  
3. **Annot:** valores numéricos visibles (`annot=True`).  
4. **Colorbar:** escala lateral de colores.  
5. **Etiquetas y título:** igual que en Matplotlib.

---

## 🧮 9. Aplicación – Visualizar rendimiento E-commerce

Usando los datos de la clase anterior (ventas mensuales):

| Visualización | Descripción |
|----------------|-------------|
| **Líneas** | Evolución de ventas mensuales |
| **Barras** | Comparación de eficiencia publicitaria (ventas/gasto) |
| **Dispersión** | Relación entre visitantes y ventas |
| **Heatmap** | Correlaciones entre ventas, visitantes y gasto |

Ejemplo:
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
  'Mes': ['Ene','Feb','Mar','Abr','May'],
  'Ventas': [45000,52000,38000,61000,48000],
  'Visitantes': [15000,18200,12500,20500,16800],
  'Publicidad': [8500,9800,7200,11200,9500]
}
df = pd.DataFrame(data)

# Línea - ventas mensuales
plt.plot(df['Mes'], df['Ventas'], marker='o')
plt.title('Evolución de Ventas Mensuales')
plt.show()

# Barras - eficiencia
df['Eficiencia'] = df['Ventas'] / df['Publicidad']
plt.bar(df['Mes'], df['Eficiencia'])
plt.title('Eficiencia Publicitaria')
plt.show()

# Dispersión - relación visitantes y ventas
plt.scatter(df['Visitantes'], df['Ventas'])
plt.title('Relación Visitantes vs Ventas')
plt.show()

# Heatmap - correlaciones
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlaciones entre Variables')
plt.show()
```

---

## 💼 10. Proyecto – Tienda Aurelion

**Etapa:** Visualización y comunicación de resultados  

**Tareas del equipo:**
1. Seleccionar **variables clave** del dataset.  
2. Crear **mínimo 3 visualizaciones** (línea, barra, dispersión, heatmap, etc.).  
3. **Identificar patrones** o correlaciones.  
4. **Interpretar resultados** según el problema.  
5. Documentar con **Copilot** las decisiones y hallazgos.

---

## 🎤 Demo 2 – Sincrónica
- Tema: Python (visualización y análisis).  
- Medio: presentación oral o notebook.  
- Entregables:
  - Dataset limpio (.csv)  
  - Programa actualizado (.py o .ipynb)  
  - Documentación (.md)  
  - 3 gráficos representativos  
  - Interpretación de resultados  
