# 🤖 Clase 5 – Copilot Chat y Prompts

## 🎯 Objetivos

*   Aprender a usar GitHub Copilot Chat dentro de VS Code.
*   Comprender qué es un prompt y cómo redactarlo eficazmente.
*   Aplicar buenas prácticas de interacción con IA generativa.

## ⚙️ 1. ¿Qué es Copilot Chat?

Es una herramienta de inteligencia artificial integrada en entornos de desarrollo como VS Code, basada en modelos de lenguaje (LLM).

### 🔹 Funciones principales

*   Asiste en redacción, análisis y programación.
*   Responde en lenguaje natural.
*   Puede generar, explicar, corregir y documentar código.

### 💻 Acceso y requisitos

*   Extensión instalada de GitHub Copilot.
*   Sesión iniciada con una cuenta de GitHub.
*   **Atajos rápidos:**
    *   Abrir panel: `Ctrl + Shift + I`
    *   Chat completo: `Ctrl + Alt + I`
    *   Inline chat: `Ctrl + I`
    *   Aceptar sugerencia: `Tab`
    *   Rechazar: `Esc`

### ⚙️ Selector de modelos

Puedes elegir distintos motores de IA según el contexto:

| Modelo              | Enfoque                 | Ejemplo                   |
| :------------------ | :---------------------- | :------------------------ |
| GPT-5 mini          | Rápido, ideal para sugerencias cortas | Explicar código           |
| Claude Sonnet 3.5   | Razonamiento detallado  | Refactorización compleja  |
| Gemini 2.5 Pro      | Equilibrado, analítico  | Análisis de proyectos     |

## 💬 2. Modos de uso en VS Code

| Modo    | Descripción                        | Uso recomendado                     |
| :------ | :--------------------------------- | :---------------------------------- |
| `Ask`   | Consultas rápidas                   | Explicar o corregir una línea       |
| `Edit`  | Modifica código directamente       | Reescribir una función              |
| `Agent` | Tareas complejas y conversacionales | Proyectos, flujos o múltiples archivos |

**Otras funciones útiles:**

*   **Autocompletado** → Sugiere código a medida que escribes.
*   **Acciones rápidas** → Icono de 💡 para mejorar código.
*   **Conversación en el editor** → Chat contextual en tiempo real.

## 🧩 3. Comandos de Copilot Chat

Copilot usa comandos con `/`, referencias con `#` y contexto con `@`.

### 🔹 Comandos rápidos (`/`):

| Comando      | Acción                     |
| :----------- | :------------------------- |
| `/explain`   | Explica el código seleccionado |
| `/fix`       | Sugerir correcciones         |
| `/test`      | Generar casos de prueba      |
| `/doc`       | Crear documentación        |
| `/optimize`  | Mejorar rendimiento        |

### 🔹 Contextos (`@`):

| Contexto      | Ámbito                   |
| :------------ | :----------------------- |
| `@workspace`  | Todo el proyecto         |
| `@file`       | Solo el archivo actual   |
| `@selection`  | Código seleccionado      |
| `@terminal`   | Ejecuta comandos         |
| `@vscode`     | Consultas sobre VS Code  |

### 🔹 Referencias (`#`):

Permite vincular issues, commits o archivos de GitHub.
**Ejemplo:** `#42` → Issue número 42.

## 🧠 4. Concepto de “Contexto”

Copilot usa la información del entorno (archivo, selección, historial de conversación) para generar respuestas más precisas.

👉 Cuanto más contexto das, mejores resultados obtienes.

## ✍️ 5. Prompting: el arte de dar instrucciones a la IA

**Prompting** = redactar instrucciones claras, estructuradas y con propósito.

### 🔹 Estructura de un buen prompt

| Elemento      | Descripción                  | Ejemplo                                                 |
| :------------ | :--------------------------- | :------------------------------------------------------ |
| **Contexto**  | Situación o nivel del usuario  | “Soy principiante en Python.”                           |
| **Objetivo**  | Qué debe lograr              | “Explica cómo crear una función que calcule promedios.” |
| **Formato**   | Tipo de respuesta            | “Con ejemplos de código comentado.”                     |
| **Restricciones** | Límites o condiciones        | “Usando solo conceptos básicos.”                        |

### 📋 Mejores prácticas

*   Sé específico y da contexto.
*   Define el resultado esperado.
*   Incluye ejemplos de entrada/salida.
*   Repite el proceso con preguntas iterativas (refinar).
*   Usa *role prompting* (“Actúa como un profesor de Python”).
*   Usa *chaining prompting* (encadenar respuestas previas).

### 💡 Tipos de prompts

| Tipo          | Ejemplo                                       | Uso                |
| :------------ | :-------------------------------------------- | :----------------- |
| **Consulta**    | “¿Qué es una función lambda en Python?”       | Teoría o definición |
| **Creación**    | “Crea una función que calcule IVA y total.”   | Código nuevo       |
| **Análisis**    | “Identifica errores en este código.”          | Debugging          |
| **Optimización**| “Mejora este código para hacerlo más eficiente.” | Rendimiento        |
| **Documentación**| “Documenta esta función con docstrings.”      | Buenas prácticas   |

### 🚫 Errores comunes

| Prompt débil                             | Problema            | Mejora                                                              |
| :--------------------------------------- | :------------------ | :------------------------------------------------------------------ |
| “Haz una función que calcule algo.”      | Vago, sin contexto  | “Crea una función que calcule el promedio de una lista de números.” |
| “Este código tiene errores.”             | Sin detalle         | “Corrige el error en la línea 12 del código que genera una división por cero.” |
| “Explica machine learning.”              | Muy general         | “Explica los tipos de aprendizaje automático con ejemplos simples.” |

## 🧱 6. Buenas prácticas generales

*   Copilot no sustituye al programador, te asiste.
*   Revisa siempre el código antes de usarlo.
*   Empieza con tareas simples.
*   Observa los bugs o errores lógicos.
*   No dependas totalmente de la IA.

## 🧩 7. Ejercicio: “Identifica el comando correcto”

| Acción                      | Comando / Contexto correcto |
| :-------------------------- | :-------------------------- |
| Entender código complejo    | `/explain`                  |
| Solicitar ayuda sobre VS Code | `@vscode`                   |
| Identificar bucle infinito  | `/fix`                      |
| Generar casos de prueba     | `/test`                     |
| Buscar en todo el proyecto  | `@workspace`                |
| Crear documentation         | `/doc`                      |

## 🧮 8. Proyecto – Tienda Aurelion

**Objetivos del sprint:**

*   Configurar Copilot Chat en VS Code.
*   Crear carpeta del proyecto y archivo `Instrucciones.md`.
*   Migrar el programa `.py` del proyecto.
*   Generar la documentación Markdown con ayuda de Copilot.
*   Aplicar y documentar las mejoras sugeridas por la IA.

**Criterios de evaluación:**

*   Tema, problema y solución claros.
*   Dataset bien definido (según Clase 2).
*   Pseudocódigo y diagrama coherentes.
*   Código funcional sin errores.
*   Evidencias del uso de Copilot documentadas.

## 🧩 9. Sprint del curso

| Sprint | Tema                   | Entregable             |
| :----- | :--------------------- | :--------------------- |
| 1°     | Inteligencia Artificial | Demo asincrónica       |
| 2°     | Python                 | Desarrollo técnico     |
| 3°     | Machine Learning       | Modelo y análisis      |
| 4°     | Power BI               | Visualización de datos |
