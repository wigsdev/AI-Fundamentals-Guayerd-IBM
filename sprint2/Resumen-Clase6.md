# 🧠 Clase 6 – Limpieza y Transformación de Datos con Python (Pandas)

## 🎯 Objetivos

- Comprender el proceso de limpieza y preparación de datos (Etapa 3 del ciclo de vida del dato).
- Aprender a usar Pandas para manipular, inspeccionar y transformar datasets.
- Identificar y corregir errores, duplicados, valores faltantes y formatos inconsistentes.

---

## 📊 1. Limpieza y transformación de datos

Es la **etapa 3** del ciclo de vida del dato, esencial para garantizar calidad antes del análisis.

**Propósito:**
- Eliminar errores e inconsistencias.
- Estandarizar formatos.
- Aumentar la fiabilidad y utilidad de los datos.

> 👉 **Estandarizar** = aplicar criterios comunes a todo el dataset.

---

## 💾 2. Formatos de datos más comunes

| Formato       | Descripción                         | Ejemplo de uso                    |
|---------------|-------------------------------------|-----------------------------------|
| **CSV**       | Datos tabulares separados por comas   | Exportaciones de sistemas o Excel |
| **JSON**      | Datos anidados y flexibles          | APIs o configuraciones            |
| **Excel (.xlsx)** | Hojas de cálculo                    | Informes corporativos             |
| **Bases de datos**| Estructuras relacionales            | SQL, MySQL, SQLite                |

> 📍 Pandas puede leer y escribir todos estos formatos.

---

## 🧰 3. Pandas (Panel Data)

### 🔹 Instalación y uso
```python
pip install pandas

import pandas as pd
```

### 🔹 Estructuras principales

| Estructura      | Descripción                       | Ejemplo        |
|-----------------|-----------------------------------|----------------|
| **Series (.s)**   | Arreglo unidimensional (índice + valor) | Columna única  |
| **DataFrame (.df)** | Tabla bidimensional de Series     | Conjunto de datos |

---

## 📥 4. Lectura de archivos con Pandas

| Formato | Comando                         | Parámetros útiles             |
|---------|---------------------------------|-------------------------------|
| **CSV**   | `pd.read_csv("archivo.csv")`    | `encoding='utf-8'`, `sep=';'`   |
| **JSON**  | `pd.read_json("archivo.json")`  | `orient='records'`            |
| **Excel** | `pd.read_excel("archivo.xlsx")` | `sheet_name="Hoja1"`          |

> ➡️ Todos los comandos devuelven un DataFrame listo para analizar.

---

## 🔍 5. Inspección inicial del dataset

| Aspecto             | Comando                | Descripción                       |
|---------------------|------------------------|-----------------------------------|
| **Dimensiones**       | `df.shape`             | Filas × columnas                  |
| **Tipos de datos**    | `df.dtypes`            | Variables numéricas o categóricas |
| **Valores faltantes** | `df.isnull().sum()`    | Conteo de celdas vacías           |
| **Primeros registros**| `df.head()`            | Vista rápida del inicio           |
| **Resumen general**   | `df.info()`            | Tipos y memoria                   |

---

## ⚠️ 6. Desafíos comunes en los datos

| Problema           | Descripción                | Ejemplo                         |
|--------------------|----------------------------|---------------------------------|
| **Valores faltantes**| Celdas vacías o NaN        | Edad sin registrar              |
| **Duplicados**       | Registros repetidos        | Cliente ingresado dos veces     |
| **Inconsistencias**  | Diferentes formatos        | “Argentina”, “argentina”, “ARG” |
| **Atípicos**         | Valores extremos           | Salario de 999999               |
| **Tipos incorrectos**| Texto en lugar de número   | “12” en vez de 12               |

---

## 🧩 7. Tratamiento de valores faltantes

| Estrategia                   | Comando                               | Descripción                  |
|------------------------------|---------------------------------------|------------------------------|
| **Detección**                  | `df.isnull()` o `df.isna()`           | Identificar celdas vacías    |
| **Eliminación**                | `df.dropna()`                         | Quitar filas con valores faltantes |
| **Rellenar con valor constante** | `df.fillna(0)`                        | Sustituir por 0 o texto      |
| **Rellenar con estadístico**   | `df.fillna(df['columna'].median())`   | Usar promedio o mediana      |

---

## 📑 8. Eliminación de duplicados

| Estrategia             | Comando                                       | Descripción             |
|------------------------|-----------------------------------------------|-------------------------|
| **Detección**            | `df.duplicated()`                             | Marca duplicados (True/False) |
| **Eliminación total**    | `df.drop_duplicates()`                        | Quita duplicados completos |
| **Por columnas**         | `df.drop_duplicates(subset=['col1', 'col2'])` | Según variables clave   |
| **Mantener primero/último**| `keep='first'` o `keep='last'`                | Conserva uno            |

---

## 🧮 9. Inconsistencias de formato

| Tipo         | Solución                        | Ejemplo                     |
|--------------|---------------------------------|-----------------------------|
| **Texto**      | `.str.lower()`, `.str.strip()`  | “ Cliente ” → “cliente”     |
| **Fechas**     | `pd.to_datetime(df['fecha'])`   | Unificar formato fecha      |
| **Números**    | `pd.to_numeric(df['precio'])`   | Asegurar tipo numérico      |
| **Categorías** | Reemplazar variaciones          | “Sí”, “si”, “SI” → “Sí”     |

---

## 📊 10. Valores atípicos (outliers)

**Definición:** Datos que se alejan mucho del resto del conjunto.

**Métodos para tratarlos:**
- **Boxplot:** visual para detectar extremos.
- **Filtrado por rango:** eliminar valores fuera de límites.
- **Criterio experto:** conocimiento del negocio.
- **Verificación manual:** revisar si son errores reales.

---

## 🔢 11. Tipos de datos incorrectos

| Acción                | Comando                       | Descripción         |
|-----------------------|-------------------------------|---------------------|
| **Verificar**           | `df.dtypes`                   | Mostrar tipo actual |
| **Convertir manualmente** | `df['columna'].astype('int')` | Cambiar tipo        |
| **Fechas**              | `pd.to_datetime()`            | Estandarizar fechas |
| **Números**             | `pd.to_numeric()`             | Forzar conversión   |

---

## 🔄 12. Transformaciones básicas

| Operación     | Comando                           | Descripción             |
|---------------|-----------------------------------|-------------------------|
| **Filtrado**    | `df[df['columna'] > 100]`         | Subconjunto de datos    |
| **Agrupación**  | `df.groupby('columna').mean()`    | Promedios por grupo     |
| **Ordenamiento**| `df.sort_values('columna')`       | Ordenar registros       |
| **Selección**   | `df[['col1', 'col2']]`            | Elegir columnas específicas |

---

## ☕ Ejercicio – “Café de barrio”

### Datos

| Mes | Ventas ($) | Temp (°C) | Publicidad ($) | Personal | Satisfacción |
|-----|------------|-----------|----------------|----------|--------------|
| Ene | 15000      | 18        | 800            | 4        | 4.2          |
| Feb | 22000      | 25        | 1200           | 5        | 4.5          |
| Mar | 18000      | 22        | 900            | 4        | 4.1          |
| Abr | 28000      | 28        | 1500           | 6        | 4.8          |
| May | 25000      | 30        | 1300           | 5        | 4.6          |

### 🧩 Tareas

- Calcular la correlación entre temperatura y ventas
- Identificar el mes con mejor retorno publicitario
- Analizar relación entre personal y satisfacción
- Proponer una estrategia con base en los datos

### Solución en Pandas:

```python
import pandas as pd

# --- Creación del DataFrame ---
# Se define un diccionario con los datos del café.
data = {
    'Mes': ['Ene','Feb','Mar','Abr','May'],
    'Ventas': [15000,22000,18000,28000,25000],
    'Temp': [18,25,22,28,30],
    'Publicidad': [800,1200,900,1500,1300],
    'Personal': [4,5,4,6,5],
    'Satisfaccion': [4.2,4.5,4.1,4.8,4.6]
}
# Se convierte el diccionario a un DataFrame de Pandas para poder analizarlo.
df = pd.DataFrame(data)


# --- Tarea 1: Calcular la correlación entre temperatura y ventas ---
# Se seleccionan las dos columnas y se aplica el método .corr() para ver su relación.
correlacion_temp_ventas = df['Temp'].corr(df['Ventas'])
print(f"1. Correlación Temperatura-Ventas: {correlacion_temp_ventas:.4f}")


# --- Tarea 2: Identificar el mes con mejor retorno publicitario ---
# Se calcula una nueva columna 'Retorno_Publicitario', dividiendo las ventas entre el gasto de publicidad.
df['Retorno_Publicitario'] = df['Ventas'] / df['Publicidad']
# Se busca el índice de la fila con el valor más alto en la nueva columna 'Retorno_Publicitario'.
indice_max_retorno = df['Retorno_Publicitario'].idxmax()
# Se usa .loc para obtener el nombre del 'Mes' en la fila con el mayor retorno.
mes_max_retorno = df.loc[indice_max_retorno, 'Mes']
print(f"2. Mes con mejor retorno publicitario: {mes_max_retorno}")


# --- Tarea 3: Analizar la relación entre personal y satisfacción ---
# Se calcula la correlación entre las columnas 'Personal' y 'Satisfaccion'.
correlacion_personal_satisfaccion = df['Personal'].corr(df['Satisfaccion'])
print(f"3. Correlación Personal-Satisfacción: {correlacion_personal_satisfaccion:.4f}")
```

---

## 🧱 13. Proyecto – Tienda Aurelion

**Tareas del equipo:**
- Usar Copilot para detectar y resolver problemas del dataset.
- Limpiar la base de datos con Pandas.
- Documentar el proceso en Markdown (`Documentacion.md`).