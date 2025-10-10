# -*- coding: utf-8 -*- 

import textos
import os

def limpiar_pantalla():
    # Función para limpiar la pantalla de la terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    # Diccionario para mapear opciones del menú a los textos
    opciones = {
        '1': ('Tema, problema y solución', textos.tema_problema_solucion),
        '2': ('Dataset de referencia', textos.dataset_referencia),
        '3': ('Estructura por tabla', textos.estructura_tablas),
        '4': ('Escalas de medición', textos.escalas_medicion),
        '5': ('Sugerencias y mejoras con Copilot', textos.sugerencias_copilot)
    }

    while True:
        limpiar_pantalla()
        print('--- MENÚ PRINCIPAL ---')
        print('Bienvenido al visor de documentación del proyecto.')
        print('Seleccione una opción para ver el contenido:')
        for key, value in opciones.items():
            print(f'{key}. {value[0]}')
        print('6. Salir')

        opcion = input('\nIngrese el número de la opción que desea consultar: ')

        if opcion in opciones:
            limpiar_pantalla()
            print(f'--- {opciones[opcion][0]} ---\n')
            print(opciones[opcion][1])
            input('\nPresione Enter para volver al menú...')
        elif opcion == '6':
            print('Gracias por utilizar el visor. ¡Hasta luego!')
            break
        else:
            print('Opción no válida. Por favor, intente de nuevo.')
            input('\nPresione Enter para continuar...')

if __name__ == '__main__':
    main()
