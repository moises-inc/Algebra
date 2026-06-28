# Directivas de Organización y Estructura del Proyecto de Álgebra (DCEX0007)

Este documento establece las directrices de organización, estructura de carpetas, nomenclatura de archivos y estilo matemático para el proyecto de **Álgebra**. El objetivo es que cualquier agente o chat del ecosistema que opere en este repositorio mantenga la consistencia y la calidad de los apuntes y resoluciones.

---

## 📂 1. Estructura de Directorios del Proyecto

El repositorio de Álgebra está organizado de la siguiente manera:

*   **`Teoria/`**: Contiene los archivos PDF oficiales con la materia del curso, organizados por unidades, y los planes de estudio.
*   **`Apuntes/`**: Resúmenes, síntesis y apuntes conceptuales redactados en Markdown. Están estructurados para ser importados a Notion y enlazados en Obsidian.
*   **`Taller/`**:
    *   `Listados/`: Archivos PDF con las guías de ejercicios y talleres prácticos oficiales del curso.
    *   `Respuestas Oficiales/`: Archivos PDF con los solucionarios provistos por la cátedra.
*   **`Guias_Resueltas/`**: Resoluciones formales paso a paso de guías y talleres, generadas por la IA para guiar el estudio práctico. Contiene además la carpeta `assets/` para recursos gráficos.
*   **`Evaluaciones/`**:
    *   `Controles/`: Enunciados y pautas de controles periódicos.
    *   `Solemnes/`: Enunciados y pautas de certámenes solemnes.
    *   `Trabajos/`: Proyectos prácticos o grupales evaluados (ej. `Solemne 2` que incluye Casos de estudio e Informes).
*   **`README.md`**: Guía ética del repositorio, licencias y citación académica bajo la norma APA 7ma Edición.

---

## 🏷️ 2. Nomenclatura y Metadatos de Archivos

### 2.1 Archivos en `Apuntes/`
Deben nombrarse usando minúsculas sin acentos, reemplazando espacios y caracteres especiales por guiones bajos (e.g., `Logica_y_conjuntos.md`, `Numeros_complejos.md`).
Cada apunte debe comenzar con el siguiente bloque de metadatos YAML (frontmatter) y finalizar con el enlace `[[Álgebra]]`:

```yaml
---
id: "[Fecha-Tema-Identificador]"
title: "[Título Limpio]"
project: "Estudios_Universidad"
date: "YYYY-MM-DDTHH:MM:SS"
last_modified: "YYYY-MM-DDTHH:MM:SS"
type: "academic-note"
status: "completed" # o "in-progress"
priority: "medium"
tags: ["#status/completed", "#project/Estudios_Universidad", "#course/lgebra"]
---
```

### 2.2 Archivos en `Guias_Resueltas/`
Deben nombrarse con el formato: `Listado_[Número]_Resolucion_Completa.md` o `Taller_Repaso_Control[N]_Resolucion.md`.
Al igual que los apuntes, deben llevar el frontmatter YAML y terminar con el enlace `[[Álgebra]]` para mantener la consistencia en el grafo de conocimiento.

---

## ✍️ 3. Pautas de Redacción y Estilo Matemático (Compatibilidad Notion/Obsidian)

Para garantizar la correcta importación en Notion y visualización en Obsidian, los archivos Markdown deben seguir estas reglas estrictas de formato matemático:

1.  **Prohibición de Símbolo de Dólar Sencillo (`$`) para Expresiones en Línea:**
    *   Notion tiende a romper las expresiones matemáticas fluidas en varias líneas si se usa `$formula$`.
    *   **Solución:** Para términos simples, variables o conjuntos dentro de la lectura fluida, se debe emplear **tipografía matemática Unicode enriquecida y negrita-cursiva**.
        *   *Ejemplos:*
            *   Variables o funciones: ***x***, ***y***, ***p(x)***, ***gr(p)***, ***α***, ***z̄***.
            *   Cuerpos y conjuntos: **𝕂**, **ℝ**, **ℂ**, **ℚ**, **ℤ**, **ℕ**, **ℕ₀**.
            *   Operadores o símbolos lógicos: ∈, ∉, ∧, ∨, ⊕, →, ↔, ≡, ⟳, ∴, ∵, ∄, ∃, ∀.
2.  **Uso de Doble Dólar (`$$`) para Bloques de Ecuaciones:**
    *   Para ecuaciones principales, sistemas de ecuaciones o desarrollos paso a paso largos, se debe usar bloques de ecuaciones centrados de doble signo de dólar.
    *   *Ejemplo:*
        $$p(x) = \sum^{n}_{i=0} a_i x^i$$
3.  **Rigor Matemático Académico:**
    *   El curso de Álgebra prescinde estrictamente de conceptos infinitesimales (límites, derivadas, integrales). Todos los desarrollos deben fundamentarse de forma rigurosa en el álgebra clásica.
4.  **Justificación de Pasos:**
    *   Cada paso de una demostración o simplificación lógica/algebraica debe estar justificado indicando explícitamente la ley, axioma o teorema aplicado (ej. *Ley de De Morgan*, *Teorema del Factor*, *Propiedad Conmutativa*).

---

## 🗓️ 4. Directivas de Sincronización del Ecosistema de Estudio

Cualquier propuesta de trabajo, estudio o actualización en este repositorio debe respetar el marco general de planificación establecido por el usuario:

*   **Google Calendar (Notion Calendar):** No se deben proponer ni agendar sesiones de estudio sobre bloques de clases fijas (eventos regulares). Únicamente se utilizarán los bloques marcados con **"(taller)"** o **"(Taller)"** o espacios libres en el Time Blocking.
*   **Tiempos de Descanso:** Se deben resguardar estrictamente las horas de comida (desayuno y almuerzo) y rampa de sueño.
*   **Orden de Prioridad de Asignaturas:**
    1.  Introducción al Cálculo (Prioridad Máxima - Teórico)
    2.  Taller de Programación I (Desarrollo y Proyecto Grupal)
    3.  **Álgebra (Prioridad Media - Práctico/Fórmulas)**
    4.  Taller de Aptitudes Lógicas y Matemáticas (Razonamiento)
    5.  Introducción a la Ingeniería Informática (Vinculación con el Medio)

---

> [!IMPORTANT]
> **Aviso para Agentes de IA:** Si vas a crear, editar o complementar resoluciones o apuntes dentro de este repositorio, lee y aplica estas pautas en su totalidad. No uses placeholders en las resoluciones; cada desarrollo debe ser completo y autocontenido.
