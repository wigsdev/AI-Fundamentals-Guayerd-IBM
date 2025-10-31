# 🤖 Instrucciones para Copilot – Proyecto *Tienda Aurelion*

A continuación se presentan ejemplos de *prompts* que se podrían haber utilizado con un asistente de IA como **GitHub Copilot** o **ChatGPT** para desarrollar este proyecto.  
Estas instrucciones reflejan las etapas reales del desarrollo del visor interactivo de documentación implementado en Python.

---

## 1️⃣ Generar el programa principal (`programa.py`)

**Prompt utilizado:**

> “Necesito crear un programa en Python que funcione como un visor de documentación interactivo desde la terminal.  
> El programa debe:
> 1. Importar un módulo llamado `textos` que contiene la documentación en variables.  
> 2. Mostrar un menú con opciones numeradas para acceder a las secciones del proyecto (Tema, Dataset, Estructura, Escalas, Sugerencias).  
> 3. Limpiar la pantalla cada vez que se muestra el menú (compatible con Windows y Linux/macOS).  
> 4. Solicitar al usuario que ingrese una opción.  
> 5. Si la opción es válida (1–5), limpiar la pantalla, mostrar el texto correspondiente y esperar a que presione Enter para volver al menú.  
> 6. Si la opción es 6, mostrar un mensaje de salida y finalizar el programa.  
> 7. Si la opción no es válida, mostrar un mensaje de error y volver al menú.”  

**Resultado generado con Copilot/ChatGPT:**

Un programa funcional que implementa un **bucle `while True`**, usa `os.system()` para limpiar la pantalla,  
y maneja un diccionario de opciones que mapea los números del menú con las variables del módulo `textos.py`.

---

## 2️⃣ Separar los textos de la documentación (`textos.py`)

**Prompt utilizado:**

> “Convierte el contenido de `Documentacion.md` en un módulo de Python llamado `textos.py`.  
> Cada sección principal del documento (Tema, Dataset, Estructura, Escalas, Sugerencias) debe almacenarse como una variable multilínea (`""" ... """`).  
> Usa nombres de variables descriptivos como `tema_problema_solucion`, `dataset_referencia`, `estructura_tablas`, `escalas_medicion` y `sugerencias_copilot`.”  

**Resultado generado con Copilot/ChatGPT:**

Un módulo separado (`textos.py`) que organiza toda la documentación del proyecto en variables de texto multilínea,  
facilitando la lectura desde el programa principal sin mezclar lógica con contenido.

---

## 3️⃣ Mejorar la usabilidad del visor

**Prompt utilizado:**

> “Tengo un bucle `while` que imprime un menú en la terminal.  
> ¿Cómo puedo hacer para que la pantalla se limpie cada vez que se muestra el menú?  
> El código debe funcionar tanto en Windows como en Linux/macOS.”  

**Respuesta esperada:**

Copilot/ChatGPT sugiere implementar una función `limpiar_pantalla()` con el siguiente código:

```python
import os
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
```

Esta función se llama al inicio de cada iteración del menú para mantener la interfaz limpia y ordenada.

---

## 4️⃣ Optimizar la estructura general

**Prompt utilizado:**

> “Quiero que mi programa siga exactamente el pseudocódigo oficial del Sprint 1.  
> ¿Cómo puedo adaptar mi código existente para reflejar las secciones INICIO, MIENTRAS, SEGÚN y FIN de manera clara?”  

**Resultado generado:**

Copilot/ChatGPT ayudó a incorporar comentarios estructurados en `programa.py` (como `# INICIO`, `# MIENTRAS`, `# FIN`)  
para alinear el código al pseudocódigo presentado en la documentación oficial.

---

## 5️⃣ Aplicar sugerencias adicionales

**Prompt utilizado:**

> “Sugiere mejoras futuras que pueda aplicar en el Sprint 2 o 3,  
> como agregar búsqueda de palabras clave, exportar secciones a archivos `.txt` o `.md`, o incorporar tests automáticos.”  

**Resultado esperado:**

Una lista de mejoras documentadas en la sección **5️⃣ Sugerencias y mejoras con Copilot** del archivo `textos.py`,  
clasificadas como **Aplicadas** o **Pendientes**, para mostrar un proceso de mejora continua asistido por IA.

---

## ✅ Conclusión

Gracias al uso de **GitHub Copilot** y **ChatGPT**, el desarrollo del visor interactivo permitió:  

- Implementar el pensamiento computacional en Python.  
- Documentar correctamente el flujo del programa y sus componentes.  
- Separar la lógica de la información, siguiendo buenas prácticas de ingeniería de software.  

> Esta primera entrega demuestra cómo combinar herramientas de asistencia inteligente con razonamiento humano  
> para crear soluciones funcionales, explicables y bien documentadas.

