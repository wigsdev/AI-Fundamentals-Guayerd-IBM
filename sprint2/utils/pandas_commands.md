# Hoja de trucos de comandos de Pandas

## Importar Pandas
```python
import pandas as pd
```

## Estructuras de datos
*   **Series:** Un arreglo etiquetado unidimensional capaz de contener cualquier tipo de dato.
    ```python
    s = pd.Series([1, 2, 3, 4, 5])
    ```
*   **DataFrame:** Una estructura de datos etiquetada bidimensional con columnas de tipos potencialmente diferentes. Es como una hoja de cálculo o una tabla de SQL.
    ```python
    data = {'col1': [1, 2, 3], 'col2': ['A', 'B', 'C']}
    df = pd.DataFrame(data)
    ```

## Creando DataFrames
*   Desde un diccionario:
    ```python
    df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    ```
*   Desde una lista de listas:
    ```python
    df = pd.DataFrame([[1, 2], [3, 4]], columns=['col1', 'col2'])
    ```

## Entrada/Salida (E/S)
*   **Leer CSV:** `pd.read_csv('file.csv')`
*   **Escribir CSV:** `df.to_csv('file.csv', index=False)`
*   **Leer Excel:** `pd.read_excel('file.xlsx')`
*   **Escribir Excel:** `df.to_excel('file.xlsx', index=False)`
*   **Leer SQL:** `pd.read_sql('SELECT * FROM table', connection)`
*   **Escribir SQL:** `df.to_sql('table_name', connection, if_exists='replace')`
*   **Leer JSON:** `pd.read_json('file.json')`
*   **Escribir JSON:** `df.to_json('file.json')`

## Viendo e Inspeccionando Datos
*   **Primeras `n` filas:** `df.head(n)` (por defecto n=5)
*   **Últimas `n` filas:** `df.tail(n)` (por defecto n=5)
*   **Forma del DataFrame (filas, columnas):** `df.shape`
*   **Estadísticas de resumen para columnas numéricas:** `df.describe()`
*   **Detalles de índice, tipo de dato y memoria:** `df.info()`
*   **Valores únicos y conteos para una Serie:** `s.value_counts()`
*   **Valores únicos y conteos para todas las columnas:** `df.apply(pd.Series.value_counts)`

## Selección e Indexación
*   **Seleccionar una columna:** `df['column_name']` o `df.column_name`
*   **Seleccionar múltiples columnas:** `df[['col1', 'col2']]`
*   **Seleccionar filas por etiqueta:** `df.loc[row_label]` o `df.loc[row_start:row_end]`
*   **Seleccionar filas por posición entera:** `df.iloc[row_index]` o `df.iloc[row_start:row_end]`
*   **Indexación booleana (filtrado):** `df[df['column_name'] > value]`

## Limpieza de Datos
*   **Renombrar columnas:** `df.rename(columns={'old_name': 'new_name'})`
*   **Verificar valores nulos:** `df.isnull()`
*   **Verificar valores no nulos:** `df.notnull()`
*   **Eliminar filas con algún valor nulo:** `df.dropna()`
*   **Eliminar columnas con algún valor nulo:** `df.dropna(axis=1)`
*   **Rellenar valores nulos:** `df.fillna(value)`
*   **Cambiar tipo de dato:** `df['column'].astype(new_type)`
*   **Reemplazar valores:** `df['column'].replace(old_value, new_value)`

## Operaciones
*   **Aplicar una función a una Serie/columna:** `df['column'].apply(function)`
*   **Aplicar una función a filas/columnas de un DataFrame:** `df.apply(function, axis=1)` (para filas) o `axis=0` (para columnas)
*   **Ordenar por valores:** `df.sort_values(by='column_name', ascending=True)`
*   **Agrupar datos:** `df.groupby('column_name')`
*   **Agregar datos:** `df.groupby('column_name').mean()` (o `.sum()`, `.count()`, `.min()`, `.max()`, `.std()`, `.median()`)
*   **Fusionar DataFrames:** `pd.merge(df1, df2, on='key_column')`
*   **Concatenar DataFrames:** `pd.concat([df1, df2])`