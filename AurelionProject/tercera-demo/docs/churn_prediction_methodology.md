# Metodología de Predicción de Churn - Proyecto Aurelion

## 1. Introducción

**Objetivo:** Este documento detalla la metodología técnica utilizada en el notebook `machine_learning_aurelion_project.ipynb` para construir un modelo predictivo de abandono de clientes (Churn). El objetivo es identificar patrones de comportamiento que señalen un alto riesgo de inactividad.

**Fuente de Datos:**
*   `clean_sales.csv`: Histórico transaccional de ventas.
*   `clientes.xlsx`: Maestro de clientes (utilizado para identificar clientes inactivos que no aparecen en las ventas).

---

## 2. Configuración y Definición del Problema

El entorno de análisis se configuró utilizando Python y sus librerías estándar de ciencia de datos (`pandas`, `numpy`, `scikit-learn`).

*   **Definición de Churn:** Se estableció una regla de negocio basada en la inactividad. Un cliente se considera "Churn" (1) si no ha realizado compras en los últimos **90 días** (Umbral de Churn). Si ha comprado dentro de ese periodo, se considera "Activo" (0).

---

## 3. Ingeniería de Características (Feature Engineering)

Dado que los datos originales son transaccionales (una fila por venta), se realizó una transformación para obtener un dataset centrado en el cliente (una fila por cliente). Se calcularon las métricas **RFM + T**:

*   **Recencia (`recencia_dias`):** Días transcurridos desde la última compra hasta la fecha de corte. *(Nota: Esta variable se usa para etiquetar, pero se excluye del entrenamiento para evitar fuga de datos).*
*   **Frecuencia (`frecuencia_compras`):** Cantidad total de transacciones únicas.
*   **Monetario (`monetario_total`):** Suma total del importe gastado.
*   **Antigüedad (`antiguedad_dias`):** Días desde que el cliente se registró.
*   **Total Artículos:** Cantidad total de productos comprados.
*   **Ticket Promedio:** Gasto promedio por transacción.

**Integración de Inactivos:** Se incorporaron clientes del archivo maestro que no tenían transacciones, asignándoles valores por defecto (Recencia=365, Frecuencia=0) y etiquetándolos automáticamente como Churn.

---

## 4. Implementación del Modelo

Se seleccionó el algoritmo **Random Forest Classifier** por su robustez y capacidad para manejar relaciones no lineales.

*   **Pipeline de Procesamiento:** Se implementó un flujo automatizado (`sklearn.pipeline.Pipeline`) que incluye:
    1.  **Escalado:** `StandardScaler` para normalizar las características numéricas.
    2.  **Clasificador:** `RandomForestClassifier` con balanceo de clases (`class_weight='balanced'`).

*   **Optimización (GridSearchCV):** Se utilizó validación cruzada para encontrar los mejores hiperparámetros, optimizando:
    *   `n_estimators`: Número de árboles.
    *   `max_depth`: Profundidad máxima del árbol.
    *   `min_samples_split`: Mínimo de muestras para dividir un nodo.

---

## 5. Evaluación del Modelo

El rendimiento del modelo se evaluó utilizando un conjunto de prueba (20% de los datos) y las siguientes métricas y visualizaciones:

*   **Reporte de Clasificación:** Precision, Recall y F1-Score para ambas clases.
*   **AUC-ROC:** Para medir la capacidad de distinción global del modelo.
*   **Matriz de Confusión:** Para visualizar los falsos positivos y falsos negativos.
*   **Importancia de Características:** Para identificar qué variables tienen mayor peso en la predicción.
