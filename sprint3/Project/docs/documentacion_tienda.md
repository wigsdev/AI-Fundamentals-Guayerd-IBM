# Proyecto Machine Learning: Tienda de Ropa Online

## 1. Entendimiento del Negocio

### Contexto
Una tienda de ropa online busca optimizar sus estrategias de marketing y ventas mediante el uso de Machine Learning para comprender mejor el comportamiento de sus clientes y predecir conversiones.

### Objetivos de Negocio
- **Aumentar la tasa de conversión** identificando usuarios con alta probabilidad de compra
- **Optimizar el presupuesto de marketing** enfocándose en los canales más efectivos
- **Predecir el valor de las transacciones** para mejorar la gestión de inventario
- **Personalizar la experiencia del usuario** según su comportamiento de navegación

### Problemas a Resolver con ML

1. **Clasificación (Predicción de Compra)**: ¿Comprará el usuario o no?
2. **Regresión (Predicción de Importe)**: ¿Cuánto gastará el usuario si compra?

---

## 2. Entendimiento de los Datos

### Descripción del Dataset

El dataset `datos_marketing.csv` contiene información de 12 sesiones de usuarios en la tienda online.

| Variable | Tipo | Descripción | Valores |
|----------|------|-------------|---------|
| `visitas` | Numérica | Número de visitas previas del usuario | 1-6 |
| `fuente` | Categórica | Canal de origen del tráfico | ads, org, email |
| `dispositivo` | Categórica | Tipo de dispositivo usado | mob, desk |
| `desc` | Binaria | Usuario vio página de descuentos | 0 (No), 1 (Sí) |
| `items` | Numérica | Número de productos vistos | 1-9 |
| `tiempo` | Numérica | Tiempo en el sitio (minutos) | 1-10 |
| `carrito` | Binaria | Agregó productos al carrito | 0 (No), 1 (Sí) |
| `compra` | Binaria | **Variable objetivo (Clasificación)** | 0 (No), 1 (Sí) |
| `importe` | Numérica | **Variable objetivo (Regresión)** | 0-210 |

### Características del Dataset
- **Tamaño**: 12 registros (dataset pequeño para fines educativos)
- **Variables predictoras (X)**: 7 variables (visitas, fuente, dispositivo, desc, items, tiempo, carrito)
- **Variables objetivo (y)**: 2 variables (compra, importe)
- **Valores faltantes**: No se observan valores nulos

---

## 3. Diseño de la Solución ML

### 3.1 Modelo de Clasificación

#### Objetivo
Predecir si un usuario realizará una compra (`compra = 1`) o no (`compra = 0`).

#### Algoritmo Seleccionado
**Regresión Logística** (`LogisticRegression` de Scikit-learn)

#### Justificación
- Es un algoritmo de **aprendizaje supervisado** para clasificación binaria
- Funciona bien con datasets pequeños
- Proporciona probabilidades interpretables
- Es un modelo base ideal para establecer un benchmark
- Permite identificar qué variables influyen más en la decisión de compra

#### Variables de Entrada (X)
```python
X = ['visitas', 'fuente_encoded', 'dispositivo_encoded', 'desc', 'items', 'tiempo', 'carrito']
```

#### Variable de Salida (y)
```python
y = 'compra'  # 0 o 1
```

#### Métricas de Evaluación
- **Accuracy**: Porcentaje de predicciones correctas sobre el total
- **Matriz de Confusión**: Para analizar falsos positivos y falsos negativos
- **Interpretación**: 
  - Verdaderos Positivos (VP): Usuarios que compraron y fueron correctamente identificados
  - Falsos Positivos (FP): Usuarios que NO compraron pero fueron clasificados como compradores
  - Verdaderos Negativos (VN): Usuarios que NO compraron y fueron correctamente identificados
  - Falsos Negativos (FN): Usuarios que compraron pero NO fueron identificados

---

### 3.2 Modelo de Regresión

#### Objetivo
Predecir el importe de la compra para usuarios que realizan una transacción.

#### Algoritmo Seleccionado
**Regresión Lineal** (`LinearRegression` de Scikit-learn)

#### Justificación
- Es un algoritmo de **aprendizaje supervisado** para predicción de valores continuos
- Establece relaciones lineales entre variables predictoras y el importe
- Es interpretable y permite identificar qué factores influyen en el monto de compra
- Funciona bien como modelo base para comparación

#### Variables de Entrada (X)
```python
X = ['visitas', 'fuente_encoded', 'dispositivo_encoded', 'desc', 'items', 'tiempo', 'carrito']
```

#### Variable de Salida (y)
```python
y = 'importe'  # Valor numérico continuo
```

#### Métricas de Evaluación
- **MSE (Mean Squared Error)**: Error cuadrático medio entre valores reales y predichos
- **RMSE (Root Mean Squared Error)**: Raíz del MSE, en las mismas unidades que el importe
- **R² Score**: Coeficiente de determinación (qué tan bien el modelo explica la variabilidad)

---

## 4. Preparación de Datos

### Transformaciones Necesarias

#### 4.1 Encoding de Variables Categóricas

**Variables Nominales** (sin orden jerárquico):
- `fuente`: ads, org, email → **One-Hot Encoding**
- `dispositivo`: mob, desk → **One-Hot Encoding**

**Método**: `pd.get_dummies()` o `OneHotEncoder` de Scikit-learn

#### 4.2 División de Datos

```python
train_test_split(X, y, test_size=0.3, random_state=42)
```

- **70% Entrenamiento**: Para que el modelo aprenda patrones
- **30% Prueba**: Para evaluar el rendimiento con datos no vistos
- `random_state=42`: Para reproducibilidad de resultados

---

## 5. Proceso de Modelado

### Pipeline de Machine Learning

```
1. Carga de datos → Pandas DataFrame
2. Análisis exploratorio → Estadísticas descriptivas y visualizaciones
3. Preprocesamiento → Encoding de variables categóricas
4. División → train_test_split
5. Entrenamiento → fit() con datos de entrenamiento
6. Predicción → predict() con datos de prueba
7. Evaluación → Cálculo de métricas
8. Visualización → Gráficos de resultados
```

### Implementación con Scikit-learn

#### Clasificación
```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

modelo_clasificacion = LogisticRegression()
modelo_clasificacion.fit(X_train, y_train)
y_pred = modelo_clasificacion.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
matriz = confusion_matrix(y_test, y_pred)
```

#### Regresión
```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

modelo_regresion = LinearRegression()
modelo_regresion.fit(X_train, y_train)
y_pred = modelo_regresion.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
```

---

## 6. Evaluación y Resultados

### Criterios de Éxito

#### Modelo de Clasificación
- **Accuracy > 70%**: El modelo debe predecir correctamente al menos 7 de cada 10 casos
- **Bajo número de Falsos Negativos**: No queremos perder oportunidades de venta
- **Interpretabilidad**: Poder identificar qué variables son más importantes

#### Modelo de Regresión
- **RMSE bajo**: El error promedio debe ser menor al 20% del importe promedio
- **R² > 0.6**: El modelo debe explicar al menos el 60% de la variabilidad
- **Predicciones coherentes**: Los valores predichos deben estar en rangos realistas

---

## 7. Limitaciones y Riesgos

### Limitaciones Técnicas
- **Dataset pequeño** (12 registros): Puede no capturar toda la variabilidad del comportamiento real
- **Posible overfitting**: Con pocos datos, el modelo puede memorizar en lugar de generalizar
- **Variables limitadas**: Pueden existir otros factores no capturados (ej. precio, categoría de producto)

### Riesgos de Negocio
- **Sesgo en los datos**: Si los datos no son representativos de todos los segmentos de clientes
- **Cambios en el comportamiento**: Patrones pueden cambiar con el tiempo (estacionalidad, tendencias)
- **Decisiones automatizadas**: Confiar ciegamente en el modelo sin validación humana

### Mitigaciones
- Validar resultados con expertos de negocio
- Actualizar el modelo periódicamente con nuevos datos
- Usar el modelo como apoyo a la decisión, no como única fuente
- Monitorear métricas de rendimiento en producción

---

## 8. Despliegue y Próximos Pasos

### Aplicaciones Prácticas
1. **Segmentación de usuarios**: Identificar perfiles de alto valor
2. **Campañas personalizadas**: Enviar ofertas a usuarios con alta probabilidad de compra
3. **Optimización de UX**: Mejorar la experiencia en dispositivos con baja conversión
4. **Gestión de inventario**: Predecir demanda según patrones de compra

### Mejoras Futuras
- Incorporar más datos históricos
- Probar algoritmos más complejos (Random Forest, XGBoost)
- Implementar validación cruzada (Cross-Validation)
- Crear un dashboard interactivo en Power BI
- Desarrollar un sistema de recomendación de productos

---

## 9. Referencias

- **Metodología**: CRISP-DM (Cross-Industry Standard Process for Data Mining)
- **Biblioteca**: Scikit-learn 1.x
- **Lenguaje**: Python 3.x
- **Documentación**: [scikit-learn.org](https://scikit-learn.org)

---

**Última actualización**: 2025-11-28  
**Autor**: Proyecto Fundamentos de IA - IBM SkillsBuild & Guayerd