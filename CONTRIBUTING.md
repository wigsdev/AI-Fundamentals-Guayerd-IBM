# Guía de Contribución

¡Gracias por tu interés en contribuir al repositorio del curso de AI Fundamentals! Tu ayuda es valiosa para mejorar la calidad del material y la estructura del proyecto.

Este repositorio está diseñado para ser un recurso de aprendizaje y consulta. Aunque no se aceptan soluciones a los ejercicios, hay muchas otras formas en las que puedes colaborar.

## 🚀 Cómo Contribuir

Puedes contribuir de las siguientes maneras:

1.  **Reportando Bugs o Errores**: Si encuentras un error tipográfico, un enlace roto o cualquier otro fallo en el contenido o la estructura del repositorio.
2.  **Sugiriendo Mejoras**: Si tienes ideas para mejorar la estructura, la documentación o añadir nuevos recursos que beneficien a todos.
3.  **Actualizando Contenido**: Si consideras que algún material está desactualizado o podría explicarse de una manera más clara.

## 📝 Proceso de Contribución

### 1. Reportar un Bug o Sugerir una Mejora

La forma más sencilla de contribuir es creando un **Issue** en GitHub.

-   **Para reportar un bug**: Utiliza la plantilla de [Bug Report](.github/ISSUE_TEMPLATE/bug_report.yml).
-   **Para sugerir una mejora**: Utiliza la plantilla de [Feature Request](.github/ISSUE_TEMPLATE/feature_request.yml).

Describe tu propuesta con el mayor detalle posible para que podamos entenderla y evaluarla correctamente.

### 2. Enviar un Pull Request

Si deseas realizar los cambios tú mismo, sigue estos pasos:

1.  **Haz un fork** del repositorio a tu cuenta de GitHub.
2.  **Clona tu fork** localmente:
    ```bash
    git clone https://github.com/[tu-usuario]/AI-Fundamentals-Guayerd-IBM.git
    ```
3.  **Añade el repositorio original** como remoto para mantenerlo actualizado:
    ```bash
    git remote add upstream https://github.com/wigsdev/AI-Fundamentals-Guayerd-IBM.git
    ```
4.  **Crea una rama descriptiva** para tus cambios:
    ```bash
    git checkout -b fix/error-tipografico-readme
    ```
    o
    ```bash
    git checkout -b feat/nueva-seccion-recursos
    ```
5.  **Realiza los cambios** en los archivos correspondientes.
6.  **Haz commit** de tus cambios con un mensaje claro y descriptivo:
    ```bash
    git commit -m "fix: Corrige error tipográfico en README.md"
    ```
7.  **Sube tus cambios** a tu fork:
    ```bash
    git push origin fix/error-tipografico-readme
    ```
8.  **Crea un Pull Request** desde tu fork a la rama `main` del repositorio original.

## ⚠️ Importante

-   **No subas soluciones de ejercicios**. Este repositorio está destinado a ser una guía y no un solucionario.
-   Asegúrate de que tus cambios no introduzcan errores de formato o enlaces rotos.
-   Mantén un código limpio y sigue las convenciones del proyecto si modificas algún script.

¡Gracias de nuevo por tu colaboración!