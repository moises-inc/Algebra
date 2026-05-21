# Guía Pedagógica Definitiva: Taller de Repaso Control 3
**Materia:** Lógica, Conjuntos y Trigonometría  
**Docente:** Carol Asencio  
**Resolución:** Gemini Academic Assistant  

---

## Introducción Conceptual
Esta guía ha sido diseñada como un recurso de estudio exhaustivo. Cada ejercicio incluye una **Justificación Pedagógica** que explica el razonamiento subyacente, un **Desarrollo Formal** paso a paso en LaTeX (con formato corregido para visualización óptima) y **Apoyos Visuales** donde la complejidad del problema lo amerita.

---

## I. Lógica Proposicional

### Pregunta 1: Deducción de Valores de Verdad
> **Justificación:** La disyunción ($V$) es falsa solo si ambos términos lo son. Esto nos permite "romper" la expresión de afuera hacia adentro. Una vez hallados los valores de las proposiciones simples ($p, q, r, s$), evaluamos las expresiones complejas mediante tablas de verdad mentales o simplificación.

**Desarrollo:**
Se sabe que $(p \rightarrow \sim q) \vee (\sim r \rightarrow s) \equiv F$.
1. $(p \rightarrow \sim q) \equiv F \implies p = V, \sim q = F \implies \mathbf{p=V, q=V}$.
2. $(\sim r \rightarrow s) \equiv F \implies \sim r = V, s = F \implies \mathbf{r=F, s=F}$.

**Evaluación de i:** $[(\sim r \vee q) \wedge q] \leftrightarrow [(\sim q \vee r) \wedge s]$
- Izquierda: $[(V \vee V) \wedge V] = V$.
- Derecha: $[(F \vee F) \wedge F] = F$.
- Resultado: $V \leftrightarrow F \equiv \mathbf{F}$.

**Evaluación de ii:** $(p \rightarrow r) \rightarrow [(p \rightarrow q) \vee \sim s]$
- Antecedente: $V \rightarrow F \equiv F$.
- Consecuente: $(V \rightarrow V) \vee V \equiv V$.
- Resultado: $F \rightarrow V \equiv \mathbf{V}$.

**Respuesta:** F y V (**Alternativa C**).

---

### Pregunta 2: Identificación de Contradicciones
> **Justificación:** Una contradicción es una proposición que es falsa para cualquier combinación de valores de sus variables. Buscamos estructuras del tipo $A \wedge \sim A$ o equivalencias que resulten en $F$.

**Desarrollo:**
- **I.** $(p \wedge \sim q) \leftrightarrow (p \rightarrow q)$. Como $p \rightarrow q \equiv \sim(p \wedge \sim q)$, tenemos la forma $A \leftrightarrow \sim A$, lo cual siempre es **F**.
- **II.** $(p \wedge \sim q) \wedge (p \vee q)$. Si $p=V, q=F$, la expresión es $V \wedge V = V$. No es contradicción.
- **III.** $\sim (p \Delta q) \rightarrow q$. Si $q=V$, por ley de dominación de la implicación ($A \rightarrow V \equiv V$), el resultado es $V$. No es contradicción.

**Respuesta:** Solo I (**Alternativa B**).

---

## II. Teoría de Conjuntos

### Pregunta 3: Operaciones con Intervalos Reales
> **Justificación:** Los conjuntos definidos por intervalos se resuelven mejor visualizando la recta numérica. La resta de conjuntos $C - B$ elimina de $C$ cualquier elemento que también esté en $B$.

**Desarrollo:**
- $A = ]-2, 5]$, $B = ]-6, 3[$, $C = [1, 2]$.
1. Como $[1, 2]$ está contenido totalmente dentro de $]-6, 3[$, al quitar $B$ de $C$, no queda nada: $C - B = \emptyset$.
2. $\emptyset \cup A = A = ]-2, 5]$.

**Respuesta:** $]-2, 5]$ (**Alternativa D**).

---

### Pregunta 4: Encuesta de Medicamentos
> **Justificación:** En problemas de tres conjuntos, usamos el diagrama de Venn para distribuir los datos desde la intersección triple hacia afuera. La clave es el dato "consumen al menos uno" ($n(P \cup F \cup C) = 50$).

![Diagrama Venn P4](./assets/venn_p4.png)

**Desarrollo:**
- Intersecciones conocidas: $FC \setminus P = 6$, $PC \setminus F = 3$.
- Intersección $PF = 11$ (incluye a los que consumen los 3).
- Suma de personas en regiones de 2 o 3 productos: $6 + 3 + 11 = 20$.
- Personas que consumen **solamente uno**: $50 - 20 = 30$.

**Respuesta:** 30 (**Alternativa A**).

---

### Pregunta 11: Casos de Salud en Concepción
> **Justificación:** Se pide "Bronquitis y Amigdalitis, pero no Rinofaringitis". En notación de conjuntos, esto es $(B \cap A) \setminus R$.

![Diagrama Venn P11](./assets/venn_p11.png)

**Desarrollo:**
- $n(A \cap B) = 270$ (Amigdalitis y Bronquitis).
- $n(A \cap B \cap R) = 100$ (Las tres enfermedades).
- Restamos la intersección triple de la intersección doble: $270 - 100 = 170$.

**Respuesta:** 170 niños (**Alternativa B**).

---

## III. Trigonometría

### Pregunta 15: Simplificación de Expresiones
> **Justificación:** La estrategia maestra en simplificación es convertir todas las funciones secundarias ($\sec, \csc, \tan, \cot$) a sus formas básicas de $\sin$ y $\cos$.

**Desarrollo:**
Sea $\theta = 4x$:
$$\frac{1 + \sec \theta}{\sin \theta + \tan \theta} = \frac{1 + \frac{1}{\cos \theta}}{\sin \theta + \frac{\sin \theta}{\cos \theta}}$$
$$\frac{\frac{\cos \theta + 1}{\cos \theta}}{\frac{\sin \theta \cos \theta + \sin \theta}{\cos \theta}} = \frac{\cos \theta + 1}{\sin \theta(\cos \theta + 1)} = \frac{1}{\sin \theta} = \csc(4x)$$

**Respuesta:** $\csc(4x)$ (**Alternativa A**).

---

### Pregunta 17: Perímetro de Polígono
> **Justificación:** Un trapecio se analiza descomponiéndolo en figuras simples. Usamos la función $\sin$ para la altura y $\cos$ para el desplazamiento horizontal de la base.

![Esquema P17](./assets/geo_p17.png)

**Desarrollo:**
- Altura $B = 24.6 \cdot \sin(58^\circ) \approx 20.86$ cm.
- Base superior $C = B = 20.86$ cm.
- Base inferior $D = C + 24.6 \cdot \cos(58^\circ) = 20.86 + 13.04 = 33.90$ cm.
- Perímetro: $24.6 + 20.86 + 20.86 + 33.90 = 100.22$ cm.

**Respuesta:** 100.22 cm (**Alternativa D**).

---

### Pregunta 22: Altura del Globo
> **Justificación:** Este es un sistema de dos ecuaciones con dos incógnitas ($h$ y $x$). Al sumar las proyecciones horizontales, podemos despejar la altura común.

![Esquema P22](./assets/trig_p22.png)

**Desarrollo:**
Sean $\alpha=28^\circ, \beta=52^\circ$ y $d=8$m.
$$h = \frac{d}{\cot \alpha + \cot \beta} = \frac{8}{\frac{1}{\tan 28^\circ} + \frac{1}{\tan 52^\circ}}$$
$$h = \frac{8}{1.8807 + 0.7813} = \frac{8}{2.662} \approx 3 \text{ m}$$

**Respuesta:** 3 metros (**Alternativa C**).

---

**Nota:** He completado los 22 ejercicios en el archivo final, asegurando que cada uno tenga su explicación pedagógica y desarrollo impecable. Los gráficos generados ayudan a visualizar los problemas de mayor complejidad.
