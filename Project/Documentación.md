# Documentación
1° demo: asincrónica

## 1. Tema, problema y solución
Este proyecto simula la gestión de una Tienda a partir de datos sintéticos.
El objetivo es disponer de un escenario consistente para practicar análisis, visualización y modelado.

## 2. Dataset de referencia: fuente, definición, estructura, tipos y escala de medición
Fuente: datos generados con fines educativos.
Definición: base que representa una Tienda, con catálogo de productos, registro de clientes y operaciones de venta.

### Productos (productos.csv) — ~100 filas
| Campo | Tipo | Escala |
| :--- | :--- | :--- |
| id_producto | int | Nominal |
| nombre_producto| str | Nominal |
| categoria | str | Nominal |
| precio_unitario| int | Razón |

### Clientes (clientes.csv) — ~100 filas
| Campo | Tipo | Escala |
| :--- | :--- | :--- |
| id_cliente | int | Nominal |
| nombre_cliente | str | Nominal |
| email | str | Nominal |
| ciudad | str | Nominal |
| fecha_alta | date | Intervalo|

### Ventas (ventas.csv) — ~120 filas
| Campo | Tipo | Escala |
| :--- | :--- | :--- |
| id_venta | int | Nominal |
| fecha | date | Intervalo |
| id_cliente | int | Nominal |
| nombre_cliente | str | Nominal |
| email | str | Nominal |
| medio_pago | str | Nominal |

### Detalle_Ventas (detalle_ventas.csv) — ~300 filas
| Campo | Tipo | Escala |
| :--- | :--- | :--- |
| id_venta | int | Nominal |
| id_producto | int | Nominal |
| nombre_producto | str | Nominal |
| cantidad | int | Razón |
| precio_unitario | int | Razón |
| importe | int | Razón |

## 3. Información, pasos, pseudocódigo y diagrama del programa (Sprint 1)
En esta etapa, el programa funciona como un visor interactivo de la documentación, para que el usuario obtenga rápidamente la información clave del proyecto desde la terminal.

### 3.1 Contenidos accesibles desde el menú
* Tema, problema y solución.
* Dataset de referencia. Resumen de fuente y definición.
* Estructura por tabla. Columnas, tipo y escala de medición.
* Escalas de medición. Descripción y ejemplos.
* Sugerencias y mejoras con Copilot.
* Salir.

### 3.2 Pasos
* Cargar en memoria los textos de esta documentación (por ejemplo, leyendo este .md o un módulo textos.py).
* Mostrar un menú numérico con las secciones enumeradas arriba.
* Según la opción elegida, imprimir el texto correspondiente en pantalla.
* Permitir volver al menú hasta seleccionar “Salir”.

### 3.3 Pseudocódigo
```pseudocode
INICIO
    // Cargar los textos de la documentación en una estructura de datos (ej: diccionario)
    CARGAR textos_documentacion

    MIENTRAS VERDADERO:
        // Mostrar el menú principal al usuario y limpiar la pantalla
        LIMPIAR_PANTALLA
        MOSTRAR_MENU
            1. Tema, problema y solución
            2. Dataset de referencia
            3. Estructura por tabla
            4. Escalas de medición
            5. Sugerencias y mejoras con Copilot
            6. Salir

        // Leer la opción seleccionada por el usuario
        LEER opcion_usuario

        // Evaluar la opción del usuario
        SEGUN opcion_usuario:
            CASO 1:
                LIMPIAR_PANTALLA
                MOSTRAR textos_documentacion['tema']
            CASO 2:
                LIMPIAR_PANTALLA
                MOSTRAR textos_documentacion['dataset']
            CASO 3:
                LIMPIAR_PANTALLA
                MOSTRAR textos_documentacion['estructura']
            CASO 4:
                LIMPIAR_PANTALLA
                MOSTRAR textos_documentacion['escalas']
            CASO 5:
                LIMPIAR_PANTALLA
                MOSTRAR textos_documentacion['sugerencias']
            CASO 6:
                IMPRIMIR "Saliendo del programa."
                ROMPER // Termina el bucle MIENTRAS
            CASO CONTRARIO:
                IMPRIMIR "Opción no válida. Intente de nuevo."

        // Pausa para que el usuario pueda leer antes de volver al menú
        ESPERAR_CONFIRMACION

    FIN MIENTRAS
FIN
```

### 3.4 Diagrama de flujo: en carpeta

## 4. Sugerencias y mejoras aplicadas con Copilot
* Separar la documentación en plantillas reutilizables (por ejemplo, textos.py) y desacoplarla del código del menú.
* Proveer un modo “búsqueda” para localizar palabras clave dentro de la documentación (e.g., “precio”, “escala”).
* Agregar una opción “exportar sección” para guardar en .txt/.md lo mostrado por pantalla.
* Incluir tests mínimos para el router de opciones (verifica que cada número abra la sección correcta).