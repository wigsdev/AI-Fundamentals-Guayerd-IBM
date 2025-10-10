# Instrucciones para Copilot

A continuación se presentan ejemplos de prompts o instrucciones que se podrían haber utilizado con un asistente de IA como GitHub Copilot para desarrollar este proyecto.

## 1. Generar el programa principal

**Prompt:**
"Necesito crear un programa en Python que funcione como un visor de documentación interactivo desde la terminal. El programa debe:
1. Importar un módulo llamado `textos` que contiene la documentación en variables.
2. Mostrar un menú con 4 opciones de documentación y una 5ta para salir.
3. Limpiar la pantalla cada vez que se muestra el menú.
4. Pedir al usuario que ingrese una opción.
5. Si la opción es válida (1-4), limpiar la pantalla, mostrar el texto correspondiente y esperar a que el usuario presione Enter para volver al menú.
6. Si la opción es 5, terminar el programa.
7. Si la opción no es válida, mostrar un mensaje de error."

## 2. Separar los textos

**Prompt inicial (con el texto de `Documentación.md` seleccionado):**
"Toma este texto Markdown y conviértelo en un módulo de Python llamado `textos.py`. Cada sección principal (delimitada por `##`) debe ser una variable de tipo string multilínea. Por ejemplo, la sección `## 1. Tema, problema y solución` debe convertirse en una variable llamada `tema_problema_solucion`."

## 3. Mejorar la usabilidad

**Prompt:**
"Tengo un bucle `while` que imprime un menú en la terminal. ¿Cómo puedo hacer para que la pantalla se limpie cada vez que el menú se muestra? El código debe funcionar tanto en Windows como en Linux/macOS."
