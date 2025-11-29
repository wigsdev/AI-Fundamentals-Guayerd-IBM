import pandas as pd
import joblib
import sys
import os

def load_model():
    """Carga el modelo entrenado desde el archivo .joblib"""
    # Obtener la ruta del directorio del script actual
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construir la ruta al modelo: desde src/interactive/ subir a code/ y luego a models/
    model_path = os.path.join(script_dir, '..', '..', 'models', 'churn_model.joblib')
    model_path = os.path.normpath(model_path)  # Normalizar la ruta
    
    if not os.path.exists(model_path):
        print(f"❌ Error: No se encontró el modelo en '{model_path}'.")
        print("   Asegúrate de ejecutar el notebook de entrenamiento primero.")
        print(f"   Ruta esperada: {model_path}")
        sys.exit(1)
    
    try:
        model = joblib.load(model_path)
        print(f"✅ Modelo cargado exitosamente desde: {os.path.basename(model_path)}")
        return model
    except Exception as e:
        sys.exit(f"❌ Error al cargar el modelo: {e}")

def show_risk_reference():
    """Muestra los indicadores de riesgo y estrategias de retención."""
    print("\n⚠️ --- INDICADORES DE RIESGO DE ABANDONO --- ⚠️")
    print("El modelo evalúa el riesgo basándose en el comportamiento del cliente:\n")
    print("🔴 RIESGO ALTO (>70%): Cliente a punto de abandonar")
    print("   → Acción: Contacto urgente, descuento agresivo, llamada personal\n")
    print("🟡 RIESGO MEDIO (30-70%): Señales de alerta")
    print("   → Acción: Email preventivo, encuesta de satisfacción, cupón\n")
    print("🟢 RIESGO BAJO (15-30%): Cliente estable")
    print("   → Acción: Fidelización estándar, mantener comunicación\n")
    print("🌟 CLIENTE IDEAL (<15%): Muy baja probabilidad de abandono")
    print("   → Acción: Programa VIP, atención prioritaria\n")
    print("----------------------------------------------------")
    print("💡 Factores clave: Ticket promedio alto, compra diversificada, antigüedad\n")

def get_user_input():
    """Solicita los datos del cliente por consola con validación básica."""
    print("\n--- Ingrese los datos del cliente ---")
    try:
        frecuencia = int(input("1. Frecuencia de Compras (Total de veces que vino): "))
        monetario = float(input("2. Monetario Total (Total gastado $): "))
        antiguedad = int(input("3. Antigüedad (Días desde el registro): "))
        articulos = int(input("4. Total de Artículos comprados: "))
        
        # Cálculo automático del ticket promedio
        ticket_promedio = monetario / frecuencia if frecuencia > 0 else 0
        
        return {
            'frecuencia_compras': frecuencia,
            'monetario_total': monetario,
            'antiguedad_dias': antiguedad,
            'total_articulos': articulos,
            'ticket_promedio': ticket_promedio
        }
    except ValueError:
        print("⚠️ Error: Por favor ingrese solo números válidos.")
        return None

def make_prediction(model, data):
    """Realiza la predicción y muestra el resultado con semáforo de riesgo de 4 niveles."""
    # Convertir diccionario a DataFrame
    df = pd.DataFrame([data])
    features = ['frecuencia_compras', 'monetario_total', 'antiguedad_dias', 'total_articulos', 'ticket_promedio']
    X = df[features]
    
    # Obtener probabilidad de Churn (Clase 1)
    probability = model.predict_proba(X)[0][1] * 100
    
    print("\n--- 📊 DIAGNÓSTICO DEL CLIENTE ---")
    print(f"Probabilidad de Abandono (Churn): {probability:.1f}%")
    
    # Validar si cumple criterios de Cliente Ideal
    cumple_frecuencia = data['frecuencia_compras'] >= 3
    cumple_monetario = data['monetario_total'] >= 70000
    cumple_ticket = data['ticket_promedio'] >= 20000
    cumple_antiguedad = data['antiguedad_dias'] >= 365
    cumple_articulos = data['total_articulos'] >= 20
    
    es_ideal = all([cumple_frecuencia, cumple_monetario, cumple_ticket, cumple_antiguedad, cumple_articulos])
    
    # Semáforo de Riesgo (4 niveles)
    if probability < 15 and es_ideal:
        print("🌟 NIVEL: CLIENTE IDEAL (Riesgo Mínimo)")
        print("👉 ESTRATEGIA: Mantener satisfacción. Incluir en programa VIP.")
        print("   Este cliente tiene muy baja probabilidad de abandono.")
    elif probability < 30:
        print("🟢 NIVEL: RIESGO BAJO")
        print("👉 ESTRATEGIA: Fidelización estándar. Monitorear periódicamente.")
        print("   Probabilidad de abandono baja, pero requiere atención continua.")
    elif 30 <= probability <= 70:
        print("🟡 NIVEL: RIESGO MEDIO - ⚠️ ALERTA")
        print("👉 ESTRATEGIA DE RETENCIÓN: Contacto preventivo inmediato.")
        print("   • Enviar email personalizado con encuesta de satisfacción")
        print("   • Ofrecer cupón de descuento (10-15%)")
        print("   • Investigar posibles problemas en la experiencia")
    else:
        print("🔴 NIVEL: RIESGO ALTO - 🚨 CRÍTICO")
        print("👉 ESTRATEGIA DE RETENCIÓN URGENTE:")
        print("   • Llamada personal del gerente en 24-48 horas")
        print("   • Descuento agresivo (20-30%) o beneficio exclusivo")
        print("   • Identificar causa raíz del descontento")
        print("   ⚠️ Sin acción, este cliente probablemente abandonará")

def main():
    print("=========================================")
    print("🤖 Sistema de Predicción de Churn - Aurelion v2.0")
    print("=========================================")
    
    model = load_model()
    
    while True:
        print("\n¿Qué deseas hacer?")
        print("1. Evaluar riesgo de churn de un cliente")
        print("2. Ver indicadores de riesgo y estrategias")
        print("3. Salir")
        
        opcion = input("Selecciona una opción (1-3): ")
        
        if opcion == '1':
            data = get_user_input()
            if data:
                make_prediction(model, data)
        elif opcion == '2':
            show_risk_reference()
        elif opcion == '3':
            print("\n👋 ¡Hasta luego!")
            break
        else:
            print("⚠️ Opción no válida.")

if __name__ == "__main__":
    main()
