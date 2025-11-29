"""
Sistema de Generación de Reportes de Riesgo de Churn
Analiza toda la base de clientes y genera reportes ejecutivos
"""

import pandas as pd
from datetime import timedelta, datetime
import joblib
import os

def generate_churn_report(output_dir=None):
    """
    Genera un reporte completo de riesgo de churn para todos los clientes.
    
    Outputs:
    - Reporte en consola
    - CSV con clientes en riesgo alto
    - CSV con clientes en riesgo medio
    - CSV resumen ejecutivo
    """
    
    print("=" * 70)
    print("🔍 GENERANDO REPORTE DE RIESGO DE CHURN")
    print("=" * 70)
    
    # Obtener la ruta del directorio del script actual
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Configurar directorio de salida (por defecto: tercera-demo/output)
    if output_dir is None:
        output_dir = os.path.join(script_dir, '..', '..', '..', 'output')
    output_dir = os.path.normpath(output_dir)
    
    # Crear directorio de salida si no existe
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Cargar datos
    print("\n📥 Cargando datos...")
    # Ruta al archivo CSV: desde src/batch/ subir a AurelionProject/ y luego a segunda-demo/output/
    csv_path = os.path.join(script_dir, '..', '..', '..', '..', 'segunda-demo', 'output', 'clean_sales.csv')
    csv_path = os.path.normpath(csv_path)
    
    if not os.path.exists(csv_path):
        print(f"❌ Error: No se encontró el archivo de datos en '{csv_path}'")
        print("   Asegúrate de que el archivo clean_sales.csv existe en segunda-demo/output/")
        return None
    
    df = pd.read_csv(csv_path)
    print(f"   ✅ Datos cargados desde: {os.path.basename(csv_path)}")
    df['fecha'] = pd.to_datetime(df['fecha'])
    df['fecha_alta'] = pd.to_datetime(df['fecha_alta'])
    
    # Fecha de referencia
    ref_date = df['fecha'].max() + timedelta(days=1)
    
    # 2. Calcular RFM+T
    print("📊 Calculando métricas RFM+T...")
    df_rfm = df.groupby('id_cliente').agg({
        'fecha': lambda x: (ref_date - x.max()).days,
        'id_venta': 'nunique',
        'importe': 'sum',
        'cantidad': 'sum',
        'fecha_alta': lambda x: (ref_date - pd.to_datetime(x.min())).days
    }).reset_index()
    
    df_rfm.columns = ['id_cliente', 'recencia', 'frecuencia_compras', 
                      'monetario_total', 'total_articulos', 'antiguedad_dias']
    df_rfm['ticket_promedio'] = df_rfm['monetario_total'] / df_rfm['frecuencia_compras']
    
    # 3. Cargar modelo y predecir
    print("🤖 Aplicando modelo de predicción...")
    # Ruta al modelo: desde src/batch/ subir a code/ y luego a models/
    model_path = os.path.join(script_dir, '..', '..', 'models', 'churn_model.joblib')
    model_path = os.path.normpath(model_path)
    
    if not os.path.exists(model_path):
        print(f"❌ Error: No se encontró el modelo en '{model_path}'")
        print("   Asegúrate de ejecutar el notebook de entrenamiento primero.")
        return None
    
    model = joblib.load(model_path)
    print(f"   ✅ Modelo cargado desde: {os.path.basename(model_path)}")
    features = ['frecuencia_compras', 'monetario_total', 'antiguedad_dias', 
                'total_articulos', 'ticket_promedio']
    df_rfm['prob_churn'] = model.predict_proba(df_rfm[features])[:, 1] * 100
    
    # 4. Clasificar por nivel de riesgo
    df_rfm['nivel_riesgo'] = pd.cut(df_rfm['prob_churn'], 
                                     bins=[-1, 15, 30, 70, 100],
                                     labels=['Ideal', 'Bajo', 'Medio', 'Alto'])
    
    # 5. Generar estadísticas
    print("\n" + "=" * 70)
    print("📊 RESUMEN EJECUTIVO")
    print("=" * 70)
    print(f"\nFecha del reporte: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total de clientes analizados: {len(df_rfm)}")
    
    print("\n" + "=" * 70)
    print("DISTRIBUCIÓN POR NIVEL DE RIESGO:")
    print("=" * 70)
    distribucion = df_rfm['nivel_riesgo'].value_counts().sort_index()
    for nivel, cantidad in distribucion.items():
        porcentaje = (cantidad / len(df_rfm)) * 100
        emoji = {'Ideal': '🌟', 'Bajo': '🟢', 'Medio': '🟡', 'Alto': '🔴'}
        print(f"{emoji[nivel]} {nivel:10s}: {cantidad:3d} clientes ({porcentaje:5.1f}%)")
    
    # 6. Clientes en Riesgo Alto
    print("\n" + "=" * 70)
    print("🔴 CLIENTES EN RIESGO ALTO (Probabilidad > 70%) - ACCIÓN URGENTE")
    print("=" * 70)
    alto_riesgo = df_rfm[df_rfm['prob_churn'] > 70].sort_values('prob_churn', ascending=False)
    
    if len(alto_riesgo) > 0:
        print(f"\nTotal: {len(alto_riesgo)} clientes")
        print(f"Valor histórico en riesgo: ${alto_riesgo['monetario_total'].sum():,.0f}")
        print("\nTop 10 clientes con mayor riesgo:")
        print(alto_riesgo.head(10)[['id_cliente', 'frecuencia_compras', 'monetario_total', 
                                     'ticket_promedio', 'recencia', 'prob_churn']].to_string())
        
        # Guardar CSV
        csv_path = os.path.join(output_dir, 'clientes_riesgo_alto.csv')
        alto_riesgo.to_csv(csv_path, index=False)
        print(f"\n💾 Guardado en: {csv_path}")
    else:
        print("✅ No hay clientes en riesgo alto")
    
    # 7. Clientes en Riesgo Medio
    print("\n" + "=" * 70)
    print("🟡 CLIENTES EN RIESGO MEDIO (Probabilidad 30-70%) - PREVENCIÓN")
    print("=" * 70)
    medio_riesgo = df_rfm[(df_rfm['prob_churn'] >= 30) & (df_rfm['prob_churn'] <= 70)].sort_values('prob_churn', ascending=False)
    
    if len(medio_riesgo) > 0:
        print(f"\nTotal: {len(medio_riesgo)} clientes")
        print(f"Valor histórico en riesgo: ${medio_riesgo['monetario_total'].sum():,.0f}")
        print("\nTop 10 clientes:")
        print(medio_riesgo.head(10)[['id_cliente', 'frecuencia_compras', 'monetario_total', 
                                      'ticket_promedio', 'recencia', 'prob_churn']].to_string())
        
        # Guardar CSV
        csv_path = os.path.join(output_dir, 'clientes_riesgo_medio.csv')
        medio_riesgo.to_csv(csv_path, index=False)
        print(f"\n💾 Guardado en: {csv_path}")
    else:
        print("✅ No hay clientes en riesgo medio")
    
    # 8. Resumen Final
    print("\n" + "=" * 70)
    print("🎯 PLAN DE ACCIÓN RECOMENDADO")
    print("=" * 70)
    total_en_riesgo = len(df_rfm[df_rfm['prob_churn'] >= 30])
    valor_en_riesgo = df_rfm[df_rfm['prob_churn'] >= 30]['monetario_total'].sum()
    
    print(f"\n📌 Clientes que requieren atención inmediata: {total_en_riesgo}")
    print(f"   ({(total_en_riesgo/len(df_rfm)*100):.1f}% del total)")
    print(f"\n💰 Valor histórico total en riesgo: ${valor_en_riesgo:,.0f}")
    
    print("\n🚨 ACCIONES URGENTES (Riesgo Alto):")
    print("   1. Llamada personal del gerente en 24-48 horas")
    print("   2. Descuento agresivo (20-30%)")
    print("   3. Investigar causa raíz del descontento")
    
    print("\n⚠️  ACCIONES PREVENTIVAS (Riesgo Medio):")
    print("   1. Email personalizado con encuesta")
    print("   2. Cupón de reactivación (10-15%)")
    print("   3. Recordatorio de productos favoritos")
    
    # 9. Guardar resumen ejecutivo
    resumen = pd.DataFrame({
        'Nivel': ['Ideal', 'Bajo', 'Medio', 'Alto'],
        'Cantidad': [distribucion.get(nivel, 0) for nivel in ['Ideal', 'Bajo', 'Medio', 'Alto']],
        'Porcentaje': [(distribucion.get(nivel, 0)/len(df_rfm)*100) for nivel in ['Ideal', 'Bajo', 'Medio', 'Alto']],
        'Valor_Total': [df_rfm[df_rfm['nivel_riesgo'] == nivel]['monetario_total'].sum() 
                        for nivel in ['Ideal', 'Bajo', 'Medio', 'Alto']]
    })
    
    csv_path = os.path.join(output_dir, 'resumen_ejecutivo.csv')
    resumen.to_csv(csv_path, index=False)
    print(f"\n💾 Resumen ejecutivo guardado en: {csv_path}")
    
    print("\n" + "=" * 70)
    print("✅ REPORTE GENERADO EXITOSAMENTE")
    print("=" * 70)
    
    return df_rfm

if __name__ == "__main__":
    # Generar reporte
    df_resultado = generate_churn_report()
    
    if df_resultado is not None:
        print("\n📁 Archivos generados en el directorio 'output':")
        print("   - clientes_riesgo_alto.csv")
        print("   - clientes_riesgo_medio.csv")
        print("   - resumen_ejecutivo.csv")
