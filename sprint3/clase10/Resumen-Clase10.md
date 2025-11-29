# Clase 10 - Fundamentos de IA IBM

## Machine Learning | Fundamentos

### Objetivos de la clase

- Machine Learning
- Tipos de aprendizajes
- Algoritmos básicos
- Métricas de evaluación

---

## 1. Conceptos Fundamentales: La Jerarquía de la IA

Se presenta un esquema de conjuntos concéntricos para entender la relación entre términos:

1. **Inteligencia Artificial (IA):** Cualquier técnica que permite a los ordenadores imitar el comportamiento humano.
2. **Machine Learning (ML):** Subconjunto de técnicas de IA que utilizan métodos estadísticos para permitir que las máquinas mejoren con la experiencia.
   - *Definición:* Algoritmos que aprenden patrones de datos para hacer predicciones.
   - *Características:* Mejora automáticamente con la experiencia y encuentra patrones sin programación explícita.
3. **Deep Learning (DL):** Subconjunto de ML que hace factible el cálculo de redes neuronales multicapa.

### ¿Qué es Machine Learning?

Algoritmos que aprenden patrones de datos para hacer predicciones:
- Sistema que mejora automáticamente con la experiencia
- Encuentra patrones sin programación explícita
- Hace predicciones sobre datos nuevos
- Aplicación práctica de Inteligencia Artificial

---

## 2. ¿Cómo funciona el Machine Learning?

### Ejemplo del Filtro de Spam

**El Problema:** Distinguir entre correos de interés (Inbox) y correos no deseados (Spam).

**La Solución:** Un **Algoritmo Clasificador**.

**Proceso:**
1. **Entrada:** Correos electrónicos.
2. **Modelo:** Identifica patrones y abstracciones (palabras clave como "príncipe", "cuenta bancaria", "herencia").
3. **Salida:** Clasificación en carpeta SPAM o INBOX.

> **Definición de Algoritmo en ML:** Conjunto de instrucciones que permiten aprender patrones, ajustar relaciones entre variables y generar predicciones.

### ¿Cómo aprenden las máquinas?

**¿En qué se diferencia del aprendizaje humano?**

Un algoritmo en ML es un conjunto de instrucciones que permiten:
- Aprender patrones a partir de datos
- Ajustar relaciones entre variables
- Generar predicciones o clasificaciones

> "Es el procedimiento que guía el aprendizaje del modelo a partir de los datos"

---

## 3. Tipos de Aprendizaje en Machine Learning

### A. Aprendizaje Supervisado (Supervised Learning)

Usa datos **etiquetados** (entrada y salida conocida). Aprende de ejemplos con respuestas correctas.

El aprendizaje supervisado permite modelar la relación entre las características medidas de los datos y alguna asociada con ellos. Es decir, podremos predecir **y** para nuevos datos **X** de los cuales no conozcamos la salida.

**Modelo Matemático:**
Buscamos una función $f$ que determine la salida $y$ a partir de la entrada $X$.
- $X$: Atributos (Variables independientes).
- $y$: Etiqueta (Variable objetivo).

#### Se divide en dos tareas principales:

#### 1. Regresión

**Definición:** Predice valores numéricos continuos
- Encuentra relación lineal entre variables
- Resultado: línea que mejor ajusta los datos
- Aplicaciones: precios, ventas, temperaturas, tiempo
- *Algoritmo ejemplo:* **Regresión Lineal** - Encuentra la línea que mejor se ajusta a los datos.

**Ejemplo:** Predecir precio de casa según metros cuadrados

#### 2. Clasificación

**Definición:** Las etiquetas son categorías (Sí/No, Gato/Perro, Spam/No Spam)
- Clasifica datos en dos o más categorías
- Decisión sí/no, verdadero/falso
- Asigna probabilidad a cada clase
- Aplicaciones: diagnósticos, aprobación préstamos
- *Algoritmo ejemplo:* **Clasificación Binaria** - Asigna probabilidad a cada clase (0 o 1).

**Ejemplo:** Email es spam (1) o no spam (0)

---

### B. Aprendizaje No Supervisado (Unsupervised Learning)

Trabaja con datos **sin etiquetas**. Descubre patrones o estructuras ocultas.

#### Tareas principales:

#### 1. Clustering (Agrupamiento)

Agrupa datos similares sin etiquetas previas:
- Agrupa datos según similitudes (segmentación de clientes)
- Encuentra grupos naturales en datos
- No conoce respuesta correcta de antemano
- Aplicaciones: segmentación clientes, organización de documentos

**Ejemplo:** Descubrir tipos de compradores en una tienda

#### 2. Reducción de Dimensionalidad

- Busca representaciones más concisas de los datos

---

### C. Aprendizaje por Refuerzo (Reinforcement Learning)

- Usado en navegación de robots, IA de juegos y decisiones en tiempo real

---

## 4. Algoritmos Clásicos de Machine Learning

### Primeros algoritmos de Machine Learning

1. **Sistemas Expertos:** Basados en reglas "Si-Entonces" definidas por humanos expertos. No aprenden de los datos por sí mismos, sino de reglas cargadas en una base de conocimiento.
2. **Árbol de Decisión:** Estructura donde cada nodo es una pregunta a los datos que ramifica hacia una resolución o clasificación.
3. **K-Vecinos Más Cercanos (K-NN):** Clasifica una nueva instancia según la categoría mayoritaria de sus "K" vecinos más cercanos en el espacio de datos.

### Ejercicio: Identifica el Algoritmo

| Caso de Uso | Tipo de Algoritmo |
|-------------|-------------------|
| Banco detecta transacciones fraudulentas | Clasificación binaria |
| Empresa agrupa productos por características | Clustering |
| App predice tiempo de entrega de pedidos | Regresión |
| Sistema recomienda contenido a usuarios | Clustering |
| Hospital predice días de hospitalización | Regresión |
| Tienda online descubre tipos de compradores | Clustering |

---

## 5. Proceso de Machine Learning

### Flujo de trabajo general

1. **Definir problema**: qué queremos predecir
2. **Recolección de datos**: reunir información relevante
3. **Preparación de datos**: limpiar y organizar
4. **Entrenamiento**: el algoritmo aprende patrones
5. **Evaluación**: medir rendimiento con métricas

### Conceptos Clave

**Algoritmo vs Modelo:**
- **Algoritmo**: es el conjunto de instrucciones o reglas (la receta)
- **Modelo**: es el resultado del algoritmo entrenado (el plato listo)

### Metodología CRISP-DM (Cross-Industry Standard Process for Data Mining)

Metodología estándar para proyectos de minería de datos y machine learning.

**¿Qué es?** Un modelo de proceso estándar y flexible para guiar proyectos de minería de datos.

**¿Cómo funciona?** Incluye seis fases que forman un ciclo de vida para el proyecto:

1. **ENTENDIMIENTO DEL NEGOCIO**
2. **ENTENDIMIENTO DE LOS DATOS**
3. **PREPARACIÓN DE LOS DATOS**
4. **MODELADO**
5. **EVALUACIÓN**
6. **DESPLIEGUE**

**Usos:** Se aplica en análisis de datos para descubrir patrones, como la detección de actividades de blanqueo de dinero.

---

## 6. Preparación y Transformación de Datos

> Las máquinas solo entienden números. Debemos transformar las variables cualitativas.

### A. Variables Ordinales (Categorías con orden)

**Ejemplos:** Talles (S, M, L), Nivel educativo.

**Tratamiento:** Asignación numérica manteniendo el orden (Label Encoding).

**Código Python (Pandas):**
```python
# Ejemplo: Convertir género a 0 y 1
diccionario = {'male': 0, 'female': 1}
df['Sex_Map'] = df.Sex.map(diccionario)
df.head()
```

### B. Variables Nominales (Categorías sin orden)

**Ejemplos:** Nacionalidad, Color, Ciudad.

**Tratamiento:** **One-Hot Encoding** (Variables Dummies). Crea una columna binaria (0/1) por cada categoría.

**Código Python (Pandas):**
```python
# pd.get_dummies crea columnas separadas para cada categoría
df = pd.concat([df, pd.get_dummies(df['Sex'])], axis=1)
df.head()
```

### C. Variables Cuantitativas (Numéricas)

Se pueden agrupar en rangos (ej. edades en "niño", "adulto"). Este proceso se llama **Discretización** o **Binning**.

---

## 7. División de Datos (Data Split)

Para validar el modelo, los datos se dividen en:

1. **Entrenamiento (Train):** Usado para que el modelo aprenda patrones
2. **Prueba (Test):** Usado para evaluar el desempeño con datos nuevos
3. **Validación** (opcional): Ajusta parámetros sin tocar el conjunto de prueba

> Separar los conjuntos asegura que el modelo generalice bien

---

## 8. Métricas de Evaluación

### Definición

Son criterios de evaluación que permiten medir el rendimiento de un modelo y comprobar qué tan bien realiza sus predicciones.

### Métricas principales

- **Accuracy**: Porcentaje de predicciones correctas
- **Matriz de confusión**: tabla que muestra aciertos y errores en predicciones
- **Error promedio**: distancia entre predicciones y valores reales

> Se usan después de entrenar el modelo para validar resultados

---

## 9. Problemas Comunes en Machine Learning

### Overfitting (Sobreajuste)

Modelo memoriza datos de entrenamiento pero falla con datos nuevos

### Underfitting (Subajuste)

Modelo demasiado simple, no captura patrones importantes

> Ocurren durante el entrenamiento y se detectan en la evaluación

---

## 10. Aplicación Práctica

### Caso de Estudio: Venta de Ropa Online

Tu empresa quiere usar Machine Learning para aumentar ventas.

**Preguntas para reflexionar:**
- ¿Qué problemas de negocio podrías resolver con ML?
- ¿Qué tipo de algoritmo usarías para cada problema?
- ¿Qué limitaciones o riesgos consideras importantes?
- ¿Cómo sabrías si la solución es exitosa?

---

## 11. Proyecto: Tienda Aurelion

### Entregables

1. **Documentación**: notebook Markdown
2. **Desarrollo técnico**: programa Python
3. **Visualización de datos**: dashboard en Power BI
4. **Presentación oral**: problema, solución y hallazgos

### Diseño Conceptual ML - Trabajo en Equipo

En relación a la base de datos:

1. Define el objetivo (predecir o clasificar)
2. Elige y justifica el algoritmo
3. Indica entradas (X) y salida (y)
4. Especifica las métricas de evaluación

---
