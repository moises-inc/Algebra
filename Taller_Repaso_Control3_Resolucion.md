# Guía Pedagógica: Resolución Taller de Repaso Control 3
**Materia:** Lógica, Conjuntos y Trigonometría  
**Objetivo:** Preparación Integral para Control 3 - Álgebra (USS)  
**Estándar:** Rigor Algebraico Formal y Justificación Conceptual  

---

## Introducción Conceptual
Esta guía no es solo un solucionario; es un mapa de razonamiento. Cada ejercicio se aborda desde sus **Axiomas** y **Leyes Fundamentales**, evitando el cálculo mecánico y priorizando la comprensión del lenguaje matemático.

---

## I. Lógica Proposicional: La Estructura del Pensamiento

### Pregunta 1: Análisis de Valores de Verdad
> **Justificación Lógica:** En lógica proposicional, la **Disyunción ($A \lor B$)** tiene un comportamiento "inclusivo", pero es extremadamente restrictiva cuando es falsa: **ambas proposiciones deben ser falsas simultáneamente**.

**Paso 1: Deducción de Atómicos**
Se sabe que $(p \rightarrow \sim q) \vee (\sim r \rightarrow s) \equiv F$.
- De $(p \rightarrow \sim q) \equiv F$, deducimos: $p = V$ y $\sim q = F \implies q = V$.
- De $(\sim r \rightarrow s) \equiv F$, deducimos: $\sim r = V \implies r = F$ y $s = F$.

**Paso 2: Evaluación**
i. $[(\sim r \vee q) \wedge q] \leftrightarrow [(\sim q \vee r) \wedge s] \equiv [(V \vee V) \wedge V] \leftrightarrow [(F \vee F) \wedge F] \equiv V \leftrightarrow F \equiv \mathbf{F}$.
ii. $(p \rightarrow r) \rightarrow [(p \rightarrow q) \vee \sim s] \equiv (V \rightarrow F) \rightarrow [(V \rightarrow V) \vee V] \equiv F \rightarrow V \equiv \mathbf{V}$.

**Respuesta:** F y V (**Alternativa C**).

---

## II. Teoría de Conjuntos: Cardinalidad y Regiones

### Pregunta 4: Análisis de Intersecciones
> **Estrategia Pedagógica:** El error común es sumar directamente los datos. Debemos usar el principio de **Inclusión-Exclusión**. La clave es que "50 personas consumen al menos uno", lo que define el universo de nuestra unión $n(P \cup F \cup C) = 50$.

![Diagrama de Venn P4](./assets/venn_p4.png)

**Desarrollo Formal:**
1. Definimos las regiones de intersección pura: $n(F \cap C \setminus P) = 6$ y $n(P \cap C \setminus F) = 3$.
2. Sea $x$ la intersección triple $n(P \cap F \cap C)$. Entonces $n(P \cap F \setminus C) = 11 - x$.
3. La suma de todas las regiones de intersección (2 o 3 productos) es:
$$6 + 3 + (11 - x) + x = 20$$
4. Dado que $n(\text{Unión}) = n(\text{Solo 1}) + n(\text{Intersecciones})$:
$$50 = n(\text{Solo 1}) + 20 \implies n(\text{Solo 1}) = \mathbf{3 0}$$

**Respuesta:** 30 personas (**Alternativa A**).

---

## III. Trigonometría: Identidades y Ecuaciones

### Pregunta 15: Simplificación Algebraica
> **Justificación Conceptual:** El método más robusto es **reducir todo a Seno y Coseno**, lo que permite cancelaciones algebraicas directas.

**Desarrollo Paso a Paso:**
Sea $\alpha = 4x$:
$$\frac{1 + \sec \alpha}{\sin \alpha + \tan \alpha} = \frac{1 + \frac{1}{\cos \alpha}}{\sin \alpha + \frac{\sin \alpha}{\cos \alpha}} = \frac{\frac{\cos \alpha + 1}{\cos \alpha}}{\frac{\sin \alpha \cos \alpha + \sin \alpha}{\cos \alpha}} = \frac{\cos \alpha + 1}{\sin \alpha (\cos \alpha + 1)} = \csc \alpha$$

**Respuesta:** $\csc(4x)$ (**Alternativa A**).

---

### Pregunta 17: Perímetro de Polígono
> **Justificación Conceptual:** Para hallar el perímetro de una figura irregular (trapecio), debemos descomponerla en un rectángulo y un triángulo rectángulo. Esto permite usar funciones trigonométricas básicas para encontrar los lados desconocidos.

**Desarrollo:**
Dados $\alpha = 58^\circ$, $A = 24.6$ cm, y la condición $B = C$ (lado vertical igual a base superior).
1. Hallamos la altura $B$: $B = A \cdot \sin(58^\circ) \approx 24.6 \cdot 0.848 = 20.86$ cm.
2. Por condición, la base superior $C = 20.86$ cm.
3. La base inferior $D$ se compone del cateto horizontal del triángulo más la base superior:
$$D = C + A \cdot \cos(58^\circ) = 20.86 + 24.6 \cdot 0.530 \approx 20.86 + 13.04 = 33.90 \text{ cm}$$
4. Perímetro $P = A + B + C + D = 24.6 + 20.86 + 20.86 + 33.90 = \mathbf{100.22} \text{ cm}$.

**Respuesta:** 100.22 cm (**Alternativa D**).

---

### Pregunta 19: Identidades de Ángulo Doble
> **Justificación Conceptual:** Al enfrentar ecuaciones con términos cúbicos y ángulos dobles, el primer paso es homogenizar los ángulos usando la identidad $\sin(2x) = 2 \sin x \cos x$.

**Desarrollo:**
$$\sin(2x) \cos x - 2 \sin^3 x = 0$$
$$(2 \sin x \cos x) \cos x - 2 \sin^3 x = 0$$
$$2 \sin x \cos^2 x - 2 \sin^3 x = 0$$
$$2 \sin x (\cos^2 x - \sin^2 x) = 0$$
Utilizando la identidad del coseno del ángulo doble $\cos(2x) = \cos^2 x - \sin^2 x$:
$$2 \sin x \cos(2x) = 0$$

**Soluciones en $[0, 2\pi]$:**
1. $\sin x = 0 \implies x \in \{0, \pi, 2\pi\}$.
2. $\cos(2x) = 0 \implies 2x \in \{\frac{\pi}{2}, \frac{3\pi}{2}, \frac{5\pi}{2}, \frac{7\pi}{2}\} \implies x \in \{\frac{\pi}{4}, \frac{3\pi}{4}, \frac{5\pi}{4}, \frac{7\pi}{4}\}$.

**Respuesta:** Unión de ambos conjuntos (**Alternativa C**).

---

### Pregunta 21: Teorema del Coseno (Geodesia)
> **Justificación Conceptual:** Cuando conocemos dos lados de un triángulo y el ángulo comprendido entre ellos, el **Teorema del Coseno** es la herramienta directa para hallar la distancia opuesta, actuando como una generalización de Pitágoras.

**Desarrollo:**
$$c^2 = a^2 + b^2 - 2ab \cos(C)$$
$$c^2 = 450^2 + 550^2 - 2(450)(550) \cos(69^\circ)$$
$$c^2 = 202500 + 302500 - 495000 \cdot 0.3584 \approx 327592$$
$$c = \sqrt{327592} \approx \mathbf{572} \text{ m}$$

**Respuesta:** 572 m (**Alternativa D**).

---

### Pregunta 22: Altura mediante Triangulación
> **Justificación Conceptual:** Este es un problema clásico de "dos estaciones". Planteamos un sistema de ecuaciones donde la altura $h$ es la variable común, relacionando las distancias horizontales mediante tangentes.

![Esquema Trig P22](./assets/trig_p22.png)

**Desarrollo:**
Sea $x$ la distancia desde A hasta la proyección del globo. La distancia desde B será $8 - x$.
1. $\tan(28^\circ) = \frac{h}{x} \implies x = \frac{h}{\tan(28^\circ)}$
2. $\tan(52^\circ) = \frac{h}{8-x} \implies 8 - x = \frac{h}{\tan(52^\circ)}$
Sumando ambas ecuaciones:
$$8 = h \left( \frac{1}{\tan(28^\circ)} + \frac{1}{\tan(52^\circ)} \right)$$
$$8 = h \cdot (1.8807 + 0.7813) \implies 8 = 2.662 \cdot h \implies h \approx \mathbf{3} \text{ m}$$

**Respuesta:** 3 metros (**Alternativa C**).
