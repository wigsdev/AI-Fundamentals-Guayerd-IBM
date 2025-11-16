# -*- coding: utf-8 -*-
# Proyecto: Tienda Aurelion - 2° Demo Asincrónica
# Curso: Fundamentos de Inteligencia Artificial (IBM)
# Adaptación: implementación de menú y submenú para el segundo entregable

import texts_v2
import os

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
    print(f'{len(menu) + 1}. Salir' if titulo == 'VISOR DE DOCUMENTACIÓN AURELION V2' else f'{len(menu) + 1}. Volver al menú principal')
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
    # Cargar textos y estructura del menú
    textos_documentacion = {
        '1': ('Limpieza y Transformación de Datos', texts_v2.data_cleaning_transformations),
        '2': ('Análisis Exploratorio y Estadístico', texts_v2.analisis_exploratorio),
        '3': ('Análisis de Negocio', {
            '1': ('Ventas por Categoría de Producto', texts_v2.ventas_por_categoria),
            '2': ('Ventas por Ciudad', texts_v2.ventas_por_ciudad),
            '3': ('Método de Pago Más Utilizado', texts_v2.metodo_pago)
        }),
        '4': ('Análisis de Series Temporales', texts_v2.analisis_series_temporales),
        '5': ('Análisis de Productos', texts_v2.analisis_productos),
        '6': ('Segmentación de Clientes (RFM)', texts_v2.segmentacion_clientes),
        '7': ('Análisis de Canasta de Mercado', texts_v2.analisis_canasta),
        '8': ('Análisis de Pareto', texts_v2.analisis_pareto),
        '9': ('Estrategias y Plan de Acción', texts_v2.estrategias_plan_accion)
    }

    # Bucle principal del menú
    while True:
        limpiar_pantalla()
        mostrar_menu(textos_documentacion, 'VISOR DE DOCUMENTACIÓN AURELION V2')
        opcion_usuario = input('\nIngrese el número de la opción: ')

        if opcion_usuario in textos_documentacion:
            titulo, contenido = textos_documentacion[opcion_usuario]
            if isinstance(contenido, dict):
                # Manejar submenú
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
