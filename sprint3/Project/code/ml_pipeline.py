"""
Script de Automatización - Análisis ML Tienda de Ropa Online
Proyecto: Fundamentos de IA - IBM SkillsBuild & Guayerd
Autor: Proyecto Sprint 3
Fecha: 2025-11-28

Este script automatiza todo el proceso de Machine Learning:
1. Carga y exploración de datos
2. Preprocesamiento (encoding)
3. División train/test
4. Entrenamiento de modelos (Clasificación y Regresión)
5. Evaluación con métricas
6. Generación de visualizaciones
7. Guardado de modelos
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import accuracy_score, confusion_matrix, mean_squared_error, r2_score
import pickle
import os
from datetime import datetime

# Configuración de visualización
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

class MLPipeline:
    """Pipeline completo de Machine Learning para análisis de tienda online"""
    
    def __init__(self, data_path):
        """
        Inicializa el pipeline
        
        Args:
            data_path (str): Ruta al archivo CSV con los datos
        """
        self.data_path = data_path
        self.df = None
        self.df_encoded = None
        self.X = None
        self.y_compra = None
        self.y_importe = None
        self.modelo_clasificacion = None
        self.modelo_regresion = None
        self.resultados = {}
        
        print("=" * 80)
        print("🚀 PIPELINE DE MACHINE LEARNING - TIENDA DE ROPA ONLINE")
        print("=" * 80)
        print(f"Fecha de ejecución: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    def cargar_datos(self):
        """Paso 1: Carga y exploración inicial de datos"""
        print("\n" + "=" * 80)
        print("📊 PASO 1: CARGA Y EXPLORACIÓN DE DATOS")
        print("=" * 80)
        
        self.df = pd.read_csv(self.data_path)
        print(f"\n✅ Dataset cargado exitosamente")
        print(f"   Dimensiones: {self.df.shape[0]} filas x {self.df.shape[1]} columnas")
        print(f"   Tasa de Conversión: {self.df['compra'].mean() * 100:.2f}%")
        print(f"   Importe Promedio (compras): ${self.df[self.df['compra']==1]['importe'].mean():.2f}")
        
        return self
    
    def preprocesar_datos(self):
        """Paso 2: Preprocesamiento - One-Hot Encoding"""
        print("\n" + "=" * 80)
        print("🔧 PASO 2: PREPROCESAMIENTO DE DATOS")
        print("=" * 80)
        
        self.df_encoded = self.df.copy()
        self.df_encoded = pd.get_dummies(
            self.df_encoded, 
            columns=['fuente', 'dispositivo'], 
            drop_first=False
        )
        
        print(f"\n✅ Variables categóricas codificadas")
        print(f"   Dimensiones: {self.df_encoded.shape[0]} filas x {self.df_encoded.shape[1]} columnas")
        print(f"   Nuevas columnas creadas: {self.df_encoded.shape[1] - self.df.shape[1]}")
        
        return self
    
    def dividir_datos(self):
        """Paso 3: División train/test"""
        print("\n" + "=" * 80)
        print("✂️  PASO 3: DIVISIÓN DE DATOS (TRAIN/TEST)")
        print("=" * 80)
        
        # Preparar features y targets
        self.X = self.df_encoded.drop(['compra', 'importe'], axis=1)
        self.y_compra = self.df_encoded['compra']
        self.y_importe = self.df_encoded['importe']
        
        # División para clasificación
        self.X_train_clf, self.X_test_clf, self.y_train_clf, self.y_test_clf = train_test_split(
            self.X, self.y_compra, test_size=0.3, random_state=42
        )
        
        # División para regresión
        self.X_train_reg, self.X_test_reg, self.y_train_reg, self.y_test_reg = train_test_split(
            self.X, self.y_importe, test_size=0.3, random_state=42
        )
        
        print(f"\n✅ Datos divididos:")
        print(f"   Train: {self.X_train_clf.shape[0]} registros (70%)")
        print(f"   Test: {self.X_test_clf.shape[0]} registros (30%)")
        
        return self
    
    def entrenar_clasificacion(self):
        """Paso 4: Entrenamiento del modelo de clasificación"""
        print("\n" + "=" * 80)
        print("🎯 PASO 4: MODELO DE CLASIFICACIÓN (Predicción de Compra)")
        print("=" * 80)
        
        # Entrenar modelo
        self.modelo_clasificacion = LogisticRegression(random_state=42, max_iter=1000)
        self.modelo_clasificacion.fit(self.X_train_clf, self.y_train_clf)
        
        # Predicciones
        y_pred_clf = self.modelo_clasificacion.predict(self.X_test_clf)
        
        # Métricas
        accuracy = accuracy_score(self.y_test_clf, y_pred_clf)
        matriz = confusion_matrix(self.y_test_clf, y_pred_clf)
        
        self.resultados['clasificacion'] = {
            'accuracy': accuracy,
            'matriz_confusion': matriz,
            'y_pred': y_pred_clf
        }
        
        print(f"\n✅ Modelo entrenado exitosamente")
        print(f"   Algoritmo: Regresión Logística")
        print(f"   Accuracy: {accuracy:.2%}")
        print(f"\n📊 Matriz de Confusión:")
        print(f"   VN: {matriz[0,0]} | FP: {matriz[0,1]}")
        print(f"   FN: {matriz[1,0]} | VP: {matriz[1,1]}")
        
        return self
    
    def entrenar_regresion(self):
        """Paso 5: Entrenamiento del modelo de regresión"""
        print("\n" + "=" * 80)
        print("💰 PASO 5: MODELO DE REGRESIÓN (Predicción de Importe)")
        print("=" * 80)
        
        # Entrenar modelo
        self.modelo_regresion = LinearRegression()
        self.modelo_regresion.fit(self.X_train_reg, self.y_train_reg)
        
        # Predicciones
        y_pred_reg = self.modelo_regresion.predict(self.X_test_reg)
        
        # Métricas
        mse = mean_squared_error(self.y_test_reg, y_pred_reg)
        rmse = np.sqrt(mse)
        r2 = r2_score(self.y_test_reg, y_pred_reg)
        
        self.resultados['regresion'] = {
            'mse': mse,
            'rmse': rmse,
            'r2': r2,
            'y_pred': y_pred_reg
        }
        
        print(f"\n✅ Modelo entrenado exitosamente")
        print(f"   Algoritmo: Regresión Lineal")
        print(f"   R² Score: {r2:.4f}")
        print(f"   RMSE: ${rmse:.2f}")
        print(f"   Error Relativo: {(rmse/self.y_test_reg.mean())*100:.2f}%")
        
        return self
    
    def generar_visualizaciones(self, output_dir='../results'):
        """Paso 6: Generación de visualizaciones"""
        print("\n" + "=" * 80)
        print("📈 PASO 6: GENERACIÓN DE VISUALIZACIONES")
        print("=" * 80)
        
        os.makedirs(output_dir, exist_ok=True)
        
        # 1. Matriz de Confusión
        plt.figure(figsize=(8, 6))
        sns.heatmap(
            self.resultados['clasificacion']['matriz_confusion'], 
            annot=True, fmt='d', cmap='Blues',
            square=True, linewidths=2
        )
        plt.title('Matriz de Confusión - Modelo de Clasificación', fontsize=14, fontweight='bold')
        plt.ylabel('Valor Real', fontsize=12)
        plt.xlabel('Valor Predicho', fontsize=12)
        plt.savefig(f'{output_dir}/matriz_confusion.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("   ✅ Guardado: matriz_confusion.png")
        
        # 2. Valores Reales vs Predichos (Regresión)
        plt.figure(figsize=(10, 6))
        plt.scatter(self.y_test_reg, self.resultados['regresion']['y_pred'], 
                   color='steelblue', s=100, alpha=0.7, edgecolor='black')
        min_val = min(self.y_test_reg.min(), self.resultados['regresion']['y_pred'].min())
        max_val = max(self.y_test_reg.max(), self.resultados['regresion']['y_pred'].max())
        plt.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2, label='Predicción Perfecta')
        plt.xlabel('Importe Real', fontsize=12)
        plt.ylabel('Importe Predicho', fontsize=12)
        plt.title('Valores Reales vs Predichos - Modelo de Regresión', fontsize=14, fontweight='bold')
        plt.legend()
        plt.grid(alpha=0.3)
        plt.savefig(f'{output_dir}/regresion_scatter.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("   ✅ Guardado: regresion_scatter.png")
        
        return self
    
    def guardar_modelos(self, output_dir='models'):
        """Paso 7: Guardado de modelos entrenados"""
        print("\n" + "=" * 80)
        print("💾 PASO 7: GUARDADO DE MODELOS")
        print("=" * 80)
        
        os.makedirs(output_dir, exist_ok=True)
        
        # Guardar modelo de clasificación
        with open(f'{output_dir}/modelo_clasificacion.pkl', 'wb') as f:
            pickle.dump(self.modelo_clasificacion, f)
        print("   ✅ Guardado: modelo_clasificacion.pkl")
        
        # Guardar modelo de regresión
        with open(f'{output_dir}/modelo_regresion.pkl', 'wb') as f:
            pickle.dump(self.modelo_regresion, f)
        print("   ✅ Guardado: modelo_regresion.pkl")
        
        return self
    
    def generar_reporte(self):
        """Genera un reporte final con todos los resultados"""
        print("\n" + "=" * 80)
        print("📋 REPORTE FINAL DE RESULTADOS")
        print("=" * 80)
        
        print("\n🎯 MODELO DE CLASIFICACIÓN:")
        print(f"   Accuracy: {self.resultados['clasificacion']['accuracy']:.2%}")
        print(f"   Interpretación: El modelo predice correctamente el {self.resultados['clasificacion']['accuracy']:.2%} de las compras")
        
        print("\n💰 MODELO DE REGRESIÓN:")
        print(f"   R² Score: {self.resultados['regresion']['r2']:.4f}")
        print(f"   RMSE: ${self.resultados['regresion']['rmse']:.2f}")
        print(f"   Interpretación: El modelo explica el {self.resultados['regresion']['r2']*100:.2f}% de la variabilidad")
        
        print("\n📊 INSIGHTS DE NEGOCIO:")
        print(f"   Tasa de Conversión: {self.df['compra'].mean()*100:.2f}%")
        print(f"   Importe Promedio: ${self.df[self.df['compra']==1]['importe'].mean():.2f}")
        print(f"   Tiempo Promedio en Sitio: {self.df['tiempo'].mean():.2f} minutos")
        
        print("\n" + "=" * 80)
        print("✅ PIPELINE COMPLETADO EXITOSAMENTE")
        print("=" * 80)
        
        return self
    
    def ejecutar_pipeline_completo(self):
        """Ejecuta todo el pipeline de ML de principio a fin"""
        try:
            (self
             .cargar_datos()
             .preprocesar_datos()
             .dividir_datos()
             .entrenar_clasificacion()
             .entrenar_regresion()
             .generar_visualizaciones()
             .guardar_modelos()
             .generar_reporte())
            
            print("\n🎉 ¡Pipeline ejecutado con éxito!")
            return True
            
        except Exception as e:
            print(f"\n❌ Error durante la ejecución: {str(e)}")
            import traceback
            traceback.print_exc()
            return False


def main():
    """Función principal"""
    # Ruta al dataset
    data_path = '../data/datos_marketing.csv'
    
    # Crear y ejecutar pipeline
    pipeline = MLPipeline(data_path)
    exito = pipeline.ejecutar_pipeline_completo()
    
    if exito:
        print("\n💡 Los modelos y visualizaciones están listos para usar!")
        print("   - Modelos guardados en: ../models/")
        print("   - Visualizaciones en: ../../results/")
    
    return 0 if exito else 1


if __name__ == "__main__":
    exit(main())
