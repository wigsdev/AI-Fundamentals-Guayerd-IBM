# 📘 Clase 2 – Fundamentos del Dato y Pensamiento Computacional

## 🧾 1. Dato, Información e Insight

| Concepto      | Definición                                     | Ejemplo                             |
| :------------ | :--------------------------------------------- | :---------------------------------- |
| **Dato**      | Hecho o cifra sin procesar, sin significado.   | 25, 33, 46 (edades sin contexto)    |
| **Información** | Datos procesados y organizados que dan sentido. | Ventas del último mes por categoría |
| **Insight**   | Comprensión profunda derivada del análisis.    | Ventas aumentan por promociones o estacionalidad |

👉 Dato = materia prima del conocimiento.

## 🔢 2. Tipos de datos

| Tipo          | Descripción                       | Ejemplo                  |
| :------------ | :-------------------------------- | :----------------------- |
| **Cuantitativos** | Representan cantidades numéricas. | Precio, edad, peso       |
| **Cualitativos**  | Representan categorías o cualidades. | País, color, producto    |

**Subtipos:**
- **Cuantitativos** → Discretos (número de hijos) / Continuos (altura).
- **Cualitativos** → Nominales (sin orden) / Ordinales (con orden).

## 🧩 3. Calidad de los datos
**Criterios principales:**
- **Exactitud:** datos correctos
- **Completitud:** sin faltantes
- **Consistencia:** mismo formato
- **Actualidad:** vigentes
- **Relevancia:** útiles para el objetivo

## 🔁 4. Ciclo de vida del dato
1.  **Captura:** recolección (formularios, sensores)
2.  **Almacenamiento:** guardar (bases de datos)
3.  **Preparación:** limpieza y transformación (`Python`, `Excel`)
4.  **Análisis:** búsqueda de patrones
5.  **Comunicación:** visualización (`Power BI`, `Looker`)
6.  **Decisión:** acción basada en resultados
7.  **Retroalimentación:** medición y mejora continua

## 📊 5. Escalas de medición

| Escala     | Tipo                    | Ejemplo                 |
| :--------- | :---------------------- | :---------------------- |
| **Nominal**  | Categórica sin orden    | Género, país            |
| **Ordinal**  | Categórica con orden    | Nivel de satisfacción   |
| **Intervalo**| Numérica sin cero real  | Temperatura, fechas     |
| **Razón**    | Numérica con cero absoluto | Ingreso, ventas         |

## 🧱 6. Estructuras básicas de datos
-   **Campos (columnas):** atributos o características.
-   **Registros (filas):** instancias únicas.
-   **Tabla:** agrupación de registros bajo los mismos campos.

**Claves:**
-   `PK` (Primary Key): identifica de forma única un registro.
-   `FK` (Foreign Key): vincula registros de distintas tablas.

## 📐 7. Modelo lógico y tipos de tablas

| Tipo de tabla | Descripción                   | Ejemplo                 |
| :------------ | :---------------------------- | :---------------------- |
| **Hechos**    | Eventos medibles              | Ventas, transacciones   |
| **Dimensiones** | Atributos que describen el hecho | Cliente, producto       |
| **Puente**      | Relaciones muchos a muchos    | Productos–proveedores   |

**📍 Ejemplo correcto:**
La tabla B (Producto–Mes–Ventas) es la correcta para análisis, ya que cada fila representa una observación individual.

---

# 💻 Pensamiento Computacional

## 🧮 1. Conceptos clave
Habilidad para resolver problemas que pueden ser entendidos y ejecutados por humanos o computadoras.

| Elemento    | Descripción                             | Ejemplo                 |
| :---------- | :-------------------------------------- | :---------------------- |
| **Secuencia** | Pasos en orden lógico                   | Calcular promedio       |
| **Condición** | Si ocurre algo, entonces…               | Si `pago` = `aprobado`  |
| **Bucle**     | Repetir mientras se cumpla una condición | Contar pedidos aprobados |

## 🧠 2. Descomposición de problemas
Dividir un problema grande en partes más simples.

**Pasos:**
1.  Definir objetivo
2.  Listar subtareas
3.  Definir entradas/salidas
4.  Identificar reglas y excepciones
5.  Priorizar lo crítico

---

## 🧩 Ejercicios resueltos

### Ejercicio 1 – “Lupa logística”
**Problema:** Contar cuántos pedidos fueron enviados.

**Datos:**
| ID    | Pago      | Stock |
| :---- | :-------- | :---- |
| O-502 | Aprobado  | Sí    |
| O-506 | Pendiente | No    |
| O-501 | Aprobado  | No    |
| O-505 | Anulado   | Sí    |
| O-503 | Pendiente | Sí    |
| O-504 | Aprobado  | No    |
| O-508 | Aprobado  | No    |
| O-507 | Aprobado  | Sí    |

**Pseudocódigo:**
```
contador = 0
lista_enviados = []
para cada fila en tabla:
    si fila.Pago == "Aprobado" y fila.Stock == "Sí":
        contador = contador + 1
        lista_enviados.append(fila.ID)
```

**✅ Resultado:** Pedidos enviados = 2 (`O-502`, `O-507`)

### Ejercicio 2 – “Despacho inteligente”
**Reglas:**
-   Si `Pago` = `Anulado` → `Estado` = `Anulado`
-   Si `Pago` ≠ `Aprobado` → `Estado` = `Pendiente`
-   Si `Pago` = `Aprobado` y `Stock` = `No` → `Estado` = `Enviado`
-   Si `Pago` = `Aprobado` y `Stock` = `Sí` →
    -   **Moto** → si `Destino` = `Capital` y `Peso` ≤ 5
    -   **Correo** → si `Destino` = `Interior` y `Peso` ≤ 10
    -   **Expreso** → cualquier otro caso

**Pseudocódigo:**
```
para cada pedido en tabla:
    si pago == "Anulado":
        estado = "Anulado"
    sino si pago != "Aprobado":
        estado = "Pendiente"
    sino si pago == "Aprobado" y stock == "No":
        estado = "Enviado"
    sino si pago == "Aprobado" y stock == "Sí":
        estado = "Enviado"
        si destino == "Capital" y peso <= 5:
            metodo = "Moto"
        sino si destino == "Interior" y peso <= 10:
            metodo = "Correo"
        sino:
            metodo = "Expreso"
```

**Ejemplo de salida simplificada:**
| ID    | Estado    | Método  |
| :---- | :-------- | :------ |
| O-702 | Pendiente | —       |
| O-708 | Enviado   | Correo  |
| O-705 | Enviado   | —       |
| O-701 | Enviado   | Moto    |
| O-703 | Enviado   | Correo  |
| O-707 | Enviado   | Expreso |
| O-704 | Enviado   | Expreso |
| O-706 | Anulado   | —       |

## ⚙️ 3. Automatización
Proceso para que tareas repetitivas se ejecuten solas.

**Ejemplos:**
-   **Python:** limpiar y preparar datos automáticamente.
-   **Power BI:** actualizar dashboards sin intervención manual.
