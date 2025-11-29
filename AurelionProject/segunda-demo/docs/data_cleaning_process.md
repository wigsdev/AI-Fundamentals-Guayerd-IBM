# Documentación del Proceso de Limpieza de Datos - Tienda Aurelion

## Introducción

Este documento detalla el proceso de limpieza y preparación de datos llevado a cabo para los datasets de la tienda Aurelion. El objetivo principal fue consolidar la información de ventas, clientes, productos y detalles de ventas en un único dataset limpio y coherente, listo para el análisis.

El proceso se ejecutó utilizando la librería `pandas` en un notebook de Jupyter y consistió en los siguientes pasos:

## 1. Carga de Datos

Se cargaron los siguientes cuatro archivos de formato `.xlsx` en DataFrames de pandas:

- `clientes.xlsx`: Información de los clientes.
- `detalle_ventas.xlsx`: Detalle de los productos en cada venta.
- `productos.xlsx`: Catálogo de productos.
- `ventas.xlsx`: Registro de las ventas realizadas.

## 2. Inspección Inicial

Se realizó una inspección inicial de cada DataFrame para identificar problemas comunes en los datos. Se utilizaron los siguientes métodos:

- `df.info()`: Para obtener un resumen de la estructura, el tipo de datos de cada columna y la cantidad de valores no nulos.
- `df.isnull().sum()`: Para contar la cantidad de valores faltantes por columna.
- `df.head()`: Para visualizar las primeras filas y tener una idea general de los datos.

**Hallazgos principales:**

- Se detectó que los nombres de las columnas de identificación (claves foráneas) no eran consistentes en mayúsculas y minúsculas (ej. `ID_Venta` vs. `id_venta`).
- Se observó que la columna de nombre del cliente en la tabla de clientes se llamaba `nombre_cliente` y no `Nombre`.
- No se encontraron valores nulos significativos, a excepción de algunos que se trataron en el siguiente paso.

## 3. Proceso de Limpieza y Transformación

### 3.1. Manejo de Duplicados

Se eliminaron las filas duplicadas en todos los DataFrames para evitar inconsistencias y registros repetidos. Se utilizó el método `df.drop_duplicates(inplace=True)`.

### 3.2. Manejo de Valores Faltantes

En el DataFrame de `clientes`, se decidió eliminar las filas donde el `nombre_cliente` estuviera ausente, ya que es un dato fundamental para la identificación del cliente. Se utilizó `clientes_df.dropna(subset=['nombre_cliente'], inplace=True)`.

### 3.3. Corrección de Nombres de Columnas

Durante el proceso de debugging, se identificó que las claves para unir las tablas no coincidían debido a diferencias de mayúsculas y minúsculas. Se corrigieron los nombres en el código para que coincidieran con los nombres reales de las columnas en los archivos de Excel:

- `ID_Venta` se corrigió a `id_venta`.
- `ID_Producto` se corrigió a `id_producto`.
- `ID_Cliente` se corrigió a `id_cliente`.

## 4. Unión de los Datos (Merge)

Una vez limpios los DataFrames, se procedió a unirlos para crear un único dataset consolidado. Las uniones se realizaron de la siguiente manera:

1.  Se unió `ventas_df` con `detalle_ventas_df` usando la columna `id_venta`.
2.  El resultado anterior se unió con `productos_df` usando la columna `id_producto`.
3.  Finalmente, el resultado se unió con `clientes_df` usando la columna `id_cliente`.

Esto resultó in un único DataFrame (`ventas_full_df`) con toda la información relacionada de cada transacción.

## 5. Guardado de Datos Limpios

El DataFrame final, limpio y unificado, se guardó en un nuevo archivo de formato CSV llamado `clean_sales.csv` dentro de la carpeta `Project/segunda-demo/output`. Este archivo está listo para ser utilizado en análisis posteriores.
