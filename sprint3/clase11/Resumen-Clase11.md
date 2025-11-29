# Clase 11: Machine Learning - Modelado con Scikit-learn

*Fuente: Material de Guayerd en colaboración con IBM SkillsBuild*

---

## 1. Objetivos de la clase

- **Preparación de datos**: Limpieza y transformación
- **División train/test**: Separación de datos para validación
- **Proceso de entrenamiento**: Ajuste del modelo
- **Evaluación de modelos**: Uso de métricas
- **Algoritmos específicos**: Implementación práctica

---

## 2. ¿Qué es Scikit-learn?

Es una biblioteca de Python estándar para Machine Learning.

### Características

- Algoritmos listos para usar
- Integración con NumPy y Pandas
- Herramientas de evaluación y validación

### Instalación y uso

```bash
pip install scikit-learn
```

```python
from sklearn import [módulo]
```

**Documentación:** [scikit-learn.org](https://scikit-learn.org)

### Uso 

- Procesamiento de los datos
- Modelos de Clasificación y Regresión
- Métricas de evaluación de algoritmos

### Flujo de Trabajo (Pipeline)

Scikit-learn es adecuado para seguir un pipeline donde se encapsula todo el proceso de los datos:

1. Obtención de datos
2. Tratamiento y preparación de datos
3. Entrenamiento
4. Testeo
5. Visualización e interpretación

---

## 3. Estructura de Scikit-Learn

La librería trabaja con **Clases y métodos uniformes**:

| Tipo de Objeto | Método Principal | Función |
|----------------|------------------|---------|
| **Estimadores** | `fit()` | Aprenden de los datos (entrenamiento) |
| **Transformadores** | `transform()` | Modifican los datos (preprocesamiento) |
| **Predictores** | `predict()` | Generan predicciones (modelado) |
| **Modelos** | `score()` | Evalúan el rendimiento (métricas) |

### Pasos generales a seguir

1. **Crear el objeto**: `objeto = Clase(parametros)`
2. **Entrenar/Aprender**: `objeto.fit(Datos)`
3. **Transformar** (si aplica): `objeto.transform(Datos)`

---

## 4. Herramientas de Preprocesamiento

Las siguientes clases son las herramientas disponibles para procesar datos:

### A. SimpleImputer (Rellenar valores faltantes)

Rellena valores nulos (NaN) con una estrategia definida (ej. promedio).

**Ejemplo de Código:**

```python
from sklearn.impute import SimpleImputer

# Estrategia: media (promedio)
imp = SimpleImputer(strategy='mean')

# Ajustamos con los datos de clics
clics = usuarios_df.clics_por_hora.values
imp.fit(clics.reshape(-1,1))
print(imp.statistics)

# Transformamos los datos
clics_imputed = imp.transform(clics.reshape(-1,1))

usuarios_df['clics_por_hora_imputed'] = clics_imputed
usuarios_df
```

**Tabla de Ejemplo (Resultados):**

Se observa cómo los valores NaN se reemplazan por el promedio calculado (aprox 182.67).

| ID | edad | clics_por_hora | explorador | clics_por_hora_imputed |
|----|------|----------------|------------|------------------------|
| 0  | 32   | 156.0          | Chrome     | 156.000000            |
| 1  | 20   | NaN            | Opera      | 182.666667            |
| 2  | 41   | 210.0          | Firefox    | 210.000000            |
| 3  | 20   | 210.0          | Chrome     | 210.000000            |
| 4  | 35   | NaN            | Explorer   | 182.666667            |
| 5  | 42   | 130.0          | Firefox    | 130.000000            |

---

### B. OneHotEncoder (Variables Nominales)

Convierte variables categóricas en columnas binarias (dummies).

> **Nota:** Para N categorías, a veces son necesarias N-1 columnas si se quiere evitar redundancia, aunque el ejemplo muestra todas.

**Ejemplo Visual de Transformación:**

```python
from sklearn.preprocessing import OneHotEncoder
onehot_encoder = OneHotEncoder(sparse = False)

# Preparación de los datos (reshape es necesario para una sola feature)
exploradores = usuarios_df.explorador.values.reshape(-1,1)

# Ajustar el encoder a los datos
onehot_encoder.fit(exploradores)

# Verificar las categorías encontradas
onehot_encoder.categories_
# Salida esperada: [array(['Chrome', 'Explorer', 'Firefox', 'Opera'], dtype=object)]

# Transformar los datos
explorador_encoded = onehot_encoder.transform(exploradores)
print(explorador_encoded)

# Asignar cada columna codificada al DataFrame original manualmente
usuarios_df['chrome_encoded'] = explorador_encoded[:,0]
usuarios_df['explorer_encoded'] = explorador_encoded[:,1]
usuarios_df['firefox_encoded'] = explorador_encoded[:,2]
usuarios_df['opera_encoded'] = explorador_encoded[:,3]

# Mostrar el DataFrame resultante
usuarios_df
```

Si explorador es "Chrome", se marca 1 en la columna Chrome y 0 en las demás.

| explorador | chrome_encoded | explorer_encoded | firefox_encoded | opera_encoded |
|------------|----------------|------------------|-----------------|---------------|
| Chrome     | 1.0            | 0.0              | 0.0             | 0.0           |
| Opera      | 0.0            | 0.0              | 0.0             | 1.0           |
| Firefox    | 0.0            | 0.0              | 1.0             | 0.0           |

---

### C. LabelEncoder (Variables Categóricas a Numéricas)

Asigna un número entero único a cada categoría.

**Ejemplo:**

- Chrome → 0
- Explorer → 1
- Firefox → 2
- Opera → 3

---

### D. KBinsDiscretizer

Para discretización y binning (agrupar continuos en rangos), la principal diferencias con Pandas es que Scikit-learn decide los límites de los bines de acuerdo a una la estrategia que le pasemos de parámetro.

### E. SelectKBest

Selecciona los mejores atributos del dataset en base a diferentes criterios de evaluación. Puede servir como respaldo o referencia del análisis que se está realizando sobre los datos.

```python
from sklearn import preprocessing
le = preprocessing.LabelEncoder()

# El método fit aprende las categorías únicas de la columna 'explorador'
le.fit(usuarios_df['explorador'])

# transform convierte las categorías de texto en números enteros
# Guardamos el resultado en una nueva columna llamada 'explorador_le'
usuarios_df['explorador_le'] = le.transform(usuarios_df['explorador'])

# Mostramos el DataFrame para ver la nueva columna
usuarios_df
```
---

## 5. Del Proceso al Código (El Flujo Principal)

El flujo estándar de modelado incluye 4 pasos clave:
- Division: train_test_split
- Entrenamiento: fit()
- Predicción: predict()
- Evaluación: metrics

### Paso 1: División (Train/Test Split)

Separamos los datos para evaluar si el modelo generaliza bien y no solo memoriza.

- **Train (70-80%)**: Para entrenar
- **Test (20-30%)**: Para evaluar con datos no vistos

```python
from sklearn.model_selection import train_test_split

# X = variables predictoras, y = etiqueta a predecir
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
```
> De esta manera comprobamos si el modelo generaliza y no solo memoriza
---

### Paso 2: Entrenamiento (Fit)

El modelo aprende patrones a partir de los datos de entrenamiento:
- Usa las variables de entrada (`X_train`) y las etiquetas(`y_train`.)
- Ajusta los parámetros internos para minimizar el error
- Este paso se realiza con el método `fit()`

**Comando para regresión lineal:**

```python
from sklearn.linear_model import LinearRegression

modelo = LinearRegression()
modelo.fit(X_train, y_train)
```

**Comando para clasificación binaria:**

```python
from sklearn.linear_model import LogisticRegression

modelo = LogisticRegression()
modelo.fit(X_train, y_train)
```

---

### Paso 3: Predicciones (Predict)

El modelo aplica lo aprendido para generar resultados sobre datos no vistos.
- Usa el conjunto de prueba (`X_test`)
- Devuelve valores numéricos (regresión) o clases/probabilidades (clasificación)
- Se utiliza el método `predict()`

```python
# Regresión lineal
predicciones = modelo.predict(X_test)

# Generar probabilidades (solo clasificación binaria)
probabilidades = modelo.predict_proba(X_test)
```

---

### Paso 4: Evaluación (Metrics)

El modelo se valida comparando las predicciones con los valores reales.
- **Accuracy**: Porcentaje de predicciones correctas
- **Matriz de confusión**: tabla que muestra aciertos y errores en predicciones.
- **Error promedio**: distancia entre predicciones y valores reales.

#### Métricas de Clasificación

**Accuracy**: Porcentaje de ***predicciones correctas sobre el total**
- Se aplica en clasificación
- Mide cuantas veces acertó el modelo
- valor entre 0 y 1 (mas cercano a 1, mejor)

```python
from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred)
```

**Matriz de Confusión**: Tabla que **resume los aciertos y errores** de clasificación.
- Filas = valores reales
- Columnas = predicciones del modelo
- Permite ver que clases confunde

```python
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, y_pred)
```

**Ejemplo de Matriz de Confusión:**

Interpretación: Se evaluó la detección de clientes premium.
- Calcular predicciones correctas
- Evaluar detección de clientes premium (valor 1)
- Explicar el valor 50 en la matriz

| **Accuracy: 0.92** | | |
| :--- | :---: | :---: |
| Matriz de confusión | Pred 0 | Pred 1 |
| **Real 0:** | 850 | 50 |
| **Real 1:** | 30 | 70 |

> El valor 50 indica **Falsos Positivos**: Clientes que NO eran premium (0) pero el modelo dijo que SÍ (1).

#### Métricas de Regresión

**Error Promedio (MSE)**: Mide la diferencia media entre valores reales y predichos.
- Se aplica en regresión
- Indica que tan lejos están las predicciones
- Cuanto mas bajo, mejor

```python
from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, y_pred)
```
---

### Paso 5: Visualizacion de resultados

Las métricas se pueden representar gráficamente para interpretar mejor el rendimiento
- **Heatmap de matriz de confusión**: muestra aciertos y errores en una tabla de colores.
- **Barra de métricas**: compara valores como accuracy y error promedio

```python
# Comando heatmap
matriz = confusion_matrix(y_test, predicciones)
sns.heatmap(matriz, annot=True, fmt="d")

# Comando barras
plt.bar(['Accuracy','Error'], [accuracy, error_promedio])
plt.show()

```
### Pipeline

```python

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, mean_squared_error

# División
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Entrenamiento
modelo = LogisticRegression()
modelo.fit(X_train, y_train)

# Predicciones
y_pred = modelo.predict(X_test)

# Evaluación
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Matriz de confusión:\n", confusion_matrix(y_test, y_pred))
print("Error promedio:", mean_squared_error(y_test, y_pred))
```
---

## 6. Caso Práctico: Venta de Ropa Online

Se presenta un dataset para practicar el flujo completo.

### Datos del Dataset

| visitas | fuente | dispositivo | desc | items | tiempo | carrito | compra | importe |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| 3 | ads | mob | 1 | 6 | 5 | 1 | 1 | 120 |
| 1 | org | desk | 0 | 2 | 1 | 0 | 0 | 0 |
| 4 | email | mob | 1 | 5 | 7 | 1 | 1 | 90 |
| 2 | org | mob | 0 | 3 | 3 | 0 | 0 | 0 |
| 5 | ads | desk | 0 | 7 | 8 | 1 | 1 | 150 |
| 1 | email | desk | 0 | 1 | 2 | 1 | 0 | 0 |
| 3 | org | mob | 1 | 4 | 4 | 0 | 0 | 0 |
| 6 | ads | mob | 1 | 9 | 10 | 1 | 1 | 210 |
| 2 | email | desk | 0 | 3 | 3 | 0 | 0 | 0 |
| 4 | org | desk | 1 | 5 | 6 | 1 | 1 | 110 |
| 2 | ads | mob | 0 | 2 | 3 | 0 | 0 | 0 |
| 5 | email | desk | 1 | 8 | 9 | 1 | 1 | 180 |

### Tareas a realizar

1. Preparar los datos (Encoding de 'fuente' y 'dispositivo')
2. Dividir en train/test
3. Entrenar modelo de **Clasificación** (predecir 'compra' si/no)
4. Calcular Accuracy y visualizar Matriz de Confusión
5. Entrenar modelo de **Regresión** (predecir 'importe')
6. Calcular Error Promedio

---

## 7. Proyecto Final: Tienda Aurelion (Sprints)

Detalles sobre la entrega del 3º Sprint / Demo.

### Modalidad

Asincrónica (Carpeta en Drive)

### Contenidos a entregar

1. **Documentación actualizada (.md)**:

    - Objetivo (predecir o clasificar)
    - Algoritmo elegido y justificación
    - Entradas (X) y salida (y)
    - Métricas de evaluación
    - Modelo ML implementado
    - División train/test y entrenamiento
    - Predicciones y métricas calculadas
    - Resultados en uno o más gráficos

2. **Programa actualizado (.py)**:
    - Información actualizada del proyecto

3. **Resultados**:
   - Gráficos (heatmap, barras de error)
   - Métricas calculadas

---