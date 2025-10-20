# -*- coding: utf-8 -*-
# Proyecto: Tienda Aurelion - 1° Demo Asincrónica
# Curso: Fundamentos de Inteligencia Artificial (IBM)
# Adaptación: implementación fiel al pseudocódigo oficial
# Mantiene estructura modular y estilo limpio de la versión original

import textos
import os

# -------------------------------------------------------
# FUNCIÓN: LIMPIAR_PANTALLA
# -------------------------------------------------------
def limpiar_pantalla():
    """Limpia la pantalla de la terminal (compatible con Windows, macOS y Linux)."""
    os.system('cls' if os.name == 'nt' else 'clear')


# -------------------------------------------------------
# FUNCIÓN PRINCIPAL
# -------------------------------------------------------
def main():
    # INICIO
    # CARGAR textos_documentacion en una estructura de datos (diccionario)
    textos_documentacion = {
        '1': ('Tema, problema y solución', textos.tema_problema_solucion),
        '2': ('Dataset de referencia', textos.dataset_referencia),
        '3': ('Estructura por tabla', textos.estructura_tablas),
        '4': ('Escalas de medición', textos.escalas_medicion),
        '5': ('Sugerencias y mejoras con Copilot', textos.sugerencias_copilot)
    }

    # MIENTRAS VERDADERO
    while True:
        # LIMPIAR_PANTALLA
        limpiar_pantalla()

        # MOSTRAR_MENU
        print('===========================================')
        print('      VISOR DE DOCUMENTACIÓN AURELION      ')
        print('===========================================')
        print('Seleccione una opción para consultar:')
        for key, value in textos_documentacion.items():
            print(f'{key}. {value[0]}')
        print('6. Salir')
        print('===========================================')

        # LEER opcion_usuario
        opcion_usuario = input('\nIngrese el número de la opción: ')

        # SEGÚN opcion_usuario
        if opcion_usuario in textos_documentacion:
            limpiar_pantalla()
            print(f'--- {textos_documentacion[opcion_usuario][0]} ---\n')
            print(textos_documentacion[opcion_usuario][1])
        elif opcion_usuario == '6':
            print('\nSaliendo del programa.')
            break
        else:
            print('\nOpción no válida. Intente de nuevo.')

        # ESPERAR_CONFIRMACION
        input('\nPresione Enter para volver al menú...')

    # FIN


# -------------------------------------------------------
# EJECUCIÓN DEL PROGRAMA
# -------------------------------------------------------
if __name__ == '__main__':
    main()

