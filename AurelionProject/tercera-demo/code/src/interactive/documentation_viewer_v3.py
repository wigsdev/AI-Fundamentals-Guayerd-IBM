# -*- coding: utf-8 -*-
# Proyecto: Tienda Aurelion - 3° Demo Asincrónica
# Curso: Fundamentos de Inteligencia Artificial (IBM)
# Adaptación: implementación de menú para el tercer entregable

import os
import sys

# Agregar el directorio src al path para poder importar desde utils
script_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(script_dir, '..')
sys.path.insert(0, os.path.normpath(src_dir))

from utils import text_v3

# -------------------------------------------------------
# FUNCIÓN: LIMPIAR_PANTALLA
# -------------------------------------------------------
def limpiar_pantalla():
    """Limpia la pantalla de la terminal (compatible con Windows, macOS y Linux)."""
    os.system('cls' if os.name == 'nt' else 'clear')

# -------------------------------------------------------
# FUNCIÓN: MOSTRAR_MENU
# -------------------------------------------------------
def mostrar_menu(menu, titulo):
    """Muestra un menú dado un diccionario y un título."""
    print(f'===========================================')
    print(f'      {titulo}      ')
    print(f'===========================================')
    for key, value in menu.items():
        print(f'{key}. {value[0]}')
    # Ajusta el texto de salida según el menú que se esté mostrando
    if titulo == 'REPORTE DE PREDICCIÓN DE CHURN':
        print(f'{len(menu) + 1}. Salir')
    else:
        print(f'{len(menu) + 1}. Volver al menú principal')
    print('===========================================')

# -------------------------------------------------------
# FUNCIÓN: MOSTRAR_CONTENIDO
# -------------------------------------------------------
def mostrar_contenido(titulo, contenido):
    """Muestra el contenido de una sección."""
    limpiar_pantalla()
    print(f'--- {titulo} ---\n')
    print(contenido)
    input('\nPresione Enter para volver al menú...')

# -------------------------------------------------------
# FUNCIÓN PRINCIPAL
# -------------------------------------------------------
def main():
    # INICIO
    # Cargar textos y estructura del menú desde text_v3
    textos_documentacion = {
        '1': ('Definición del Problema y Contexto', text_v3.definicion_problema),
        '2': ('Rendimiento del Modelo', {
            '1': ('Introducción al Rendimiento', text_v3.rendimiento_general),
            '2': ('Métricas Clave', text_v3.metricas_clave),
            '3': ('Interpretación de Errores', text_v3.interpretacion_errores)
        }),
        '3': ('Factores Clave de Churn', text_v3.factores_clave),
        '4': ('Estrategias y Recomendaciones', {
            '1': ('Introducción a Estrategias', text_v3.estrategias_introduccion),
            '2': ('Campañas de Activación Temprana', text_v3.campanas_activacion),
            '3': ('Segmentación por Valor', text_v3.segmentacion_valor),
            '4': ('Incentivos de Frecuencia', text_v3.incentivos_frecuencia)
        })
    }

    # Bucle principal del menú
    while True:
        limpiar_pantalla()
        mostrar_menu(textos_documentacion, 'REPORTE DE PREDICCIÓN DE CHURN')
        opcion_usuario = input('\nIngrese el número de la opción: ')

        if opcion_usuario in textos_documentacion:
            titulo, contenido = textos_documentacion[opcion_usuario]
            if isinstance(contenido, dict):
                # Este bloque se mantiene por si se decide añadir submenús en el futuro
                while True:
                    limpiar_pantalla()
                    mostrar_menu(contenido, titulo.upper())
                    opcion_submenu = input('\nIngrese el número de la opción: ')
                    
                    if opcion_submenu in contenido:
                        sub_titulo, sub_contenido = contenido[opcion_submenu]
                        mostrar_contenido(sub_titulo, sub_contenido)
                    elif opcion_submenu == str(len(contenido) + 1):
                        break
                    else:
                        input('\nOpción no válida. Presione Enter para intentar de nuevo...')
            else:
                # Mostrar contenido directamente
                mostrar_contenido(titulo, contenido)
        elif opcion_usuario == str(len(textos_documentacion) + 1):
            print('\nSaliendo del programa.')
            break
        else:
            input('\nOpción no válida. Presione Enter para intentar de nuevo...')

    # FIN

# -------------------------------------------------------
# EJECUCIÓN DEL PROGRAMA
# -------------------------------------------------------
if __name__ == '__main__':
    main()
