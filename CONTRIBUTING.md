# Guía de Contribución

¡Gracias por contribuir al repositorio del curso de AI Fundamentals! Esta guía te ayudará a enviar tus soluciones y contribuciones de manera efectiva.

## � Estructura del Repositorio

```
AI-Fundamentals-Guayerd-IBM/
├── recursos/                  # Recursos comunes del curso
│   ├── datasets/             # Conjuntos de datos
│   ├── presentaciones/       # Material de presentación
│   ├── codigo/              # Código de ejemplo
│   └── templates/           # Plantillas para ejercicios
│
└── sprint-[número]/          # Carpeta de cada sprint
    ├── ejercicios/          # Ejercicios de la clase
    └── soluciones/          # Soluciones de los estudiantes
        └── [tu-usuario]/     # Ej: wigsdev
            └── clase-[número]/
                ├── ejercicio1.ipynb
                ├── ejercicio2.py
                └── README.md
```

## 📝 Proceso de Contribución

### 1. Preparación
1. Haz fork del repositorio a tu cuenta de GitHub
2. Clona tu fork localmente: `git clone https://github.com/[tu-usuario]/AI-Fundamentals-Guayerd-IBM.git`
3. Añade el repositorio original como remoto: `git remote add upstream https://github.com/wigsdev/AI-Fundamentals-Guayerd-IBM.git`

### 2. Creación de tu Solución
1. Actualiza tu rama main: `git pull upstream main`
2. Crea una rama con tu nombre de usuario: `git checkout -b respuesta-juan`
3. Ubica la carpeta del sprint correspondiente
4. Dentro de `soluciones/`, crea una carpeta con tu nombre de usuario (por ejemplo: `wigsdev`)
5. Copia los notebooks de ejercicios y completa tus respuestas

### 3. Completar los Ejercicios
- Los ejercicios están en notebooks de Jupyter dentro de la carpeta `ejercicios/` de cada sprint
- Completa tus respuestas en las celdas designadas
- No modifiques las celdas de enunciados o tests
- Asegúrate de que tus soluciones pasen los tests incluidos

### 4. Envío de tu Solución
1. Haz commit con tus cambios: `git commit -m "Agregadas mis soluciones"`
2. Sube tus cambios: `git push origin soluciones-wilmer`
3. Crea un Pull Request desde GitHub
4. Espera la revisión de los mentores

## ⚠️ Importante

- No modifiques archivos fuera de tu carpeta de respuestas
- No incluyas archivos grandes (>50MB) ni datos sensibles
- Mantén un código limpio y bien documentado
- Sigue las convenciones de nombres establecidas

## � Proceso de Revisión

1. Los mentores revisarán tu código
2. Puedes recibir sugerencias de mejora
3. Realiza los cambios solicitados si es necesario
4. Una vez aprobado, se fusionará con la rama principal

## 🙋‍♂️ Ayuda y Soporte

- Revisa los [ejemplos](recursos/codigo/ejemplos/)
- Usa las [Issues](../../issues) para preguntas generales
- Menciona a los mentores en tu PR para revisión
- Consulta el [canal de Discord](https://discord.gg/curso-ia) para dudas