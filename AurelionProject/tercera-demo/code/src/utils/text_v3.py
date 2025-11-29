# -*- coding: utf-8 -*-
# Proyecto: Tienda Aurelion - 3° Demo Asincrónica
# Curso: Fundamentos de Inteligencia Artificial (IBM)
# Descripción: Textos de documentación para el visor interactivo v3 (Refactorizado).

# -------------------------------------------------------
# 1. Definición del Problema y Contexto
# -------------------------------------------------------
definicion_problema = """
El modelo fue entrenado para detectar clientes en riesgo de abandono, 
definido como aquellos sin actividad de compra en los últimos 90 días. 
Esta ventana de tiempo permite al negocio reaccionar antes de que el 
cliente se pierda definitivamente.
"""

# -------------------------------------------------------
# 2. Rendimiento del Modelo
# -------------------------------------------------------
rendimiento_general = """
El modelo Random Forest optimizado ha demostrado un rendimiento excelente 
en el conjunto de prueba. A continuación se detallan sus componentes.
"""

metricas_clave = """
*   AUC-ROC Score: Cercano a 1.00. Esto indica que el modelo tiene una 
    capacidad casi perfecta para distinguir entre clientes activos y 
    clientes en riesgo de churn basándose en sus patrones históricos 
    (Frecuencia, Monetario, Antigüedad).
*   Recall (Clase Churn): El modelo identifica correctamente a la gran 
    mayoría de los clientes que efectivamente están en churn. Esto es 
    crítico para no dejar pasar oportunidades de retención.
"""

interpretacion_errores = """
Interpretación de Errores (Matriz de Confusión)
*   Falsos Negativos (Riesgo): Son mínimos. El modelo rara vez clasifica a un 
    cliente en riesgo como "Activo".
*   Falsos Positivos (Costo): También son bajos. Pocos clientes activos son 
    clasificados erróneamente como en riesgo, lo que optimiza el presupuesto 
    de las campañas de retención.
"""

# -------------------------------------------------------
# 3. Factores Clave de Churn (Feature Importance)
# -------------------------------------------------------
factores_clave = """
El análisis de importancia de características revela qué impulsa la predicción 
del modelo (excluyendo la recencia directa):

1.  Monetario Total: Los clientes que han gastado menos históricamente tienen 
    una mayor tendencia al abandono.
2.  Frecuencia de Compras: La baja frecuencia es un predictor fuerte de 
    inactividad futura.
3.  Antigüedad: Los clientes nuevos (baja antigüedad) son más volátiles que 
    los clientes antiguos.
"""

# -------------------------------------------------------
# 4. Estrategias y Recomendaciones
# -------------------------------------------------------
estrategias_introduccion = """
Basado en los hallazgos del modelo, se proponen las siguientes acciones 
estratégicas para mitigar el churn.
"""

campanas_activacion = """
A. Campañas de Activación Temprana
*   Objetivo: Atacar el factor "Antigüedad".
*   Acción: Implementar un "Onboarding" agresivo para clientes nuevos en sus 
    primeros 30-60 días para asegurar que realicen su segunda y tercera compra 
    rápidamente.
"""

segmentacion_valor = """
B. Segmentación por Valor (Monetario)
*   Objetivo: Priorizar recursos.
*   Acción: No tratar a todos los clientes en riesgo por igual. Cruzar la 
    predicción de Churn con el valor histórico (monetario_total).
    *   Alto Valor + Riesgo Churn: Llamada personalizada o incentivo fuerte (VIP).
    *   Bajo Valor + Riesgo Churn: Email automatizado de reactivación.
"""

incentivos_frecuencia = """
C. Incentivos de Frecuencia
*   Objetivo: Mejorar el hábito de compra.
*   Acción: Programas de lealtad que premien la *cantidad* de visitas (Frecuencia) 
    más que solo el monto gastado, para generar hábito en los clientes esporádicos.
"""