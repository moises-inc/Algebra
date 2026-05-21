# Solucionario Integral: Taller de Repaso Control 3 - Álgebra
**Materia:** Lógica, Conjuntos y Trigonometría  
**Docente:** Carol Asencio  
**Resolución:** Gemini Academic Assistant  

---

## Pregunta 1: Lógica Proposicional
**Enunciado:** Se sabe que $(p \rightarrow \sim q) \vee (\sim r \rightarrow s)$ es falsa. Determinar el valor de verdad de:
i. $[(\sim r \vee q) \wedge q] \leftrightarrow [(\sim q \vee r) \wedge s]$
ii. $(p \rightarrow r) \rightarrow [(p \rightarrow q) \vee \sim s]$

**Desarrollo:**
1. $(p \rightarrow \sim q) \equiv F \implies p = V, q = V$.
2. $(\sim r \rightarrow s) \equiv F \implies r = F, s = F$.
- **Evaluación i:** $[(V \vee V) \wedge V] \leftrightarrow [(F \vee F) \wedge F] \equiv V \leftrightarrow F = \mathbf{F}$.
- **Evaluación ii:** $(V \rightarrow F) \rightarrow [(V \rightarrow V) \vee V] \equiv F \rightarrow V = \mathbf{V}$.

**Respuesta:** F y V (**Alternativa C**).

---

## Pregunta 2: Contradicciones Lógicas
I. $(p \wedge \sim q) \leftrightarrow (p \rightarrow q) \equiv \neg(p \rightarrow q) \leftrightarrow (p \rightarrow q) \equiv \mathbf{F}$ (**Contradicción**).
II. $(p \wedge \sim q) \wedge (p \vee q)$: Si $p=V, q=F \implies V \wedge V = V$ (No es contradicción).
III. $\sim (p \Delta q) \rightarrow q$: Si $q=V \implies V$ (No es contradicción).

**Respuesta:** Solo I (**Alternativa B**).

---

## Pregunta 3: Operaciones con Conjuntos
$A = ]-2, 5]$, $B = ]-6, 3[$, $C = [1, 2]$.
1. $C - B = \emptyset$ (ya que $C \subset B$).
2. $(C - B) \cup A = \emptyset \cup ]-2, 5] = ]-2, 5]$.

**Respuesta:** $]-2, 5]$ (**Alternativa D**).

---

## Pregunta 4: Problema de Encuestas (Venn)
- $n(\text{Unión}) = 50$.
- $n(F \cap C \setminus P) = 6$.
- $n(P \cap C \setminus F) = 3$.
- $n(P \cap F) = 11$.
1. Suma regiones intersección: $6 + 3 + 11 = 20$.
2. $n(\text{Solo 1}) = 50 - 20 = 30$.

**Respuesta:** 30 (**Alternativa A**).

---

## Pregunta 5: Porcentajes de Patologías
- $T=59, H=45, D=49, (T \cap H \cap D)=5$.
- $(T \cap H)=17 \implies (T \cap H \setminus D)=12$.
- $(H \cap D)=18 \implies (H \cap D \setminus T)=13$.
- Solo $T=18 \implies (T \cap D \setminus H) = 59 - (18+12+5) = 24$.
- Solo $H = 45 - (12+13+5) = 15$.
- Solo $D = 49 - (24+13+5) = 7$.
- Total Unión = $18+15+7+12+13+24+5 = 94\%$.
- Exterior = $100\% - 94\% = 6\%$.

**Respuesta:** 6% (**Alternativa C**).

---

## Pregunta 6, 7 y 8: Recetas Médicas
- $n(A \cap B \setminus C) = 20$.
- $n(\text{Solo } A) = 40$.
- $n(A \setminus B) = 55 \implies n(A \cap C \setminus B) = 55 - 40 = 15$.
- $n(A) = 100 \implies n(A \cap B \cap C) = 100 - (40+20+15) = 25$.
- $n(\text{Solo } B) = 50$.
- $n(B \cap C) = 60 \implies n(B \cap C \setminus A) = 60 - 25 = 35$.
- $n(C) = 80 \implies n(\text{Solo } C) = 80 - (15+35+25) = 5$.

6. $B \cap C \setminus A = \mathbf{3 5}$ (**Alternativa B**).
7. $(A \cup C) \setminus B = 40 + 15 + 5 = \mathbf{6 0}$ (**Alternativa D**).
8. Total = $100 + 50 + 5 + 35 = \mathbf{190}$ (**Alternativa A**).

---

## Pregunta 9: Valor de Verdad
$p \implies (q \vee r) \equiv F \implies p=V, q=F, r=F$.
- $p \vee (q \wedge \sim r) \equiv V \vee (F \wedge V) \equiv V \vee F = \mathbf{V}$.

**Respuesta:** Es Verdadera (**Alternativa C**).

---

## Pregunta 10: Implicación Lógica
$p \wedge \sim (q \vee r) \equiv V \implies p=V, q=F, r=F$.
- $p \implies (\sim q \wedge r) \equiv V \rightarrow (V \wedge F) \equiv V \rightarrow F = \mathbf{F}$.

**Respuesta:** Es Falsa (**Alternativa D**).

---

## Pregunta 11: Problema de Salud
$n(A \cap B \setminus R) = n(A \cap B) - n(A \cap B \cap R) = 270 - 100 = 170$.

**Respuesta:** 170 niños (**Alternativa B**).

---

## Pregunta 12 y 13: Diagramas de Venn
12. Área sombreada: $(A \cup B) - C$ (**Alternativa C**).
13. Área sombreada: $(A \cap B) - C$ (**Alternativa D**).

---

## Pregunta 14: Conjuntos con Valor Absoluto
- $A = ]1, 2] \cup \{3\}$.
- $B = \{x : |x-1| < 1\} = ]0, 2[$.
- $C = \{x : -2 \le x < 1\} = [-2, 1[$.
1. $B - C = ]0, 2[ \setminus [-2, 1[ = [1, 2[$.
2. $(B - C) \cup A = [1, 2[ \cup (]1, 2] \cup \{3\}) = [1, 2] \cup \{3\}$.

**Respuesta:** $[1, 2] \cup \{3\}$ (**Alternativa B**).

---

## Pregunta 15: Simplificación Trigonométrica
$$\frac{1 + \sec(4x)}{\sin(4x) + \tan(4x)} = \frac{1 + \frac{1}{\cos(4x)}}{\sin(4x) + \frac{\sin(4x)}{\cos(4x)}} = \frac{\frac{\cos(4x) + 1}{\cos(4x)}}{\frac{\sin(4x) \cos(4x) + \sin(4x)}{\cos(4x)}} = \frac{\cos(4x) + 1}{\sin(4x) (\cos(4x) + 1)} = \frac{1}{\sin(4x)} = \csc(4x)$$

**Respuesta:** $\csc(4x)$ (**Alternativa A**).

---

## Pregunta 16: Ecuación Trigonométrica
$2 \cos^2(x) - \cos(x) = 0 \implies \cos(x)(2\cos(x) - 1) = 0$.
1. $\cos(x) = 0 \implies x = \pi/2, 3\pi/2$.
2. $\cos(x) = 1/2 \implies x = \pi/3, 5\pi/3$.

**Respuesta:** $\{\pi/3, \pi/2, 3\pi/2, 5\pi/3\}$ (**Alternativa C**).

---

## Pregunta 17: Perímetro de Polígono
1. Altura $B = 24.6 \cdot \sin(58^\circ) = 20.86$.
2. Base $C = B = 20.86$.
3. Base $D = 20.86 + 24.6 \cdot \cos(58^\circ) = 33.90$.
4. $P = 24.6 + 20.86 + 20.86 + 33.90 = 100.22$.

**Respuesta:** 100.22 cm (**Alternativa D**).

---

## Pregunta 18: Ecuaciones sin Solución
I. $2 \cos^2 \theta + 5 \cos \theta + 2 = 0 \implies \cos \theta = -1/2$.
II. $\tan(\theta/4) = -\sqrt{3} \implies \theta/4 = -\pi/3 + k\pi$.
III. $2 \sin \theta - 1 = 3 \implies \sin \theta = 2$ (**Imposible**, $|\sin \theta| \le 1$).

**Respuesta:** Solo la III (**Alternativa B**).

---

## Pregunta 19: Identidades
$\sin(2x) \cos x - 2 \sin^3 x = 0 \implies 2 \sin x \cos^2 x - 2 \sin^3 x = 0 \implies 2 \sin x \cos(2x) = 0$.
1. $\sin x = 0 \implies 0, \pi, 2\pi$.
2. $\cos(2x) = 0 \implies \pi/4, 3\pi/4, 5\pi/4, 7\pi/4$.

**Respuesta:** Unión de soluciones (**Alternativa C**).

---

## Pregunta 20: Aplicación Pitágoras
$d = \sqrt{4^2 + 3^2} = \sqrt{25} = 5$.

**Respuesta:** 5 metros (**Alternativa B**).

---

## Pregunta 21: Teorema del Coseno
$c = \sqrt{450^2 + 550^2 - 2(450)(550) \cos(69^\circ)} \approx \sqrt{327592} \approx 572$.

**Respuesta:** 572 m (**Alternativa D**).

---

## Pregunta 22: Altura del Globo
$h = \frac{8}{\frac{1}{\tan(28^\circ)} + \frac{1}{\tan(52^\circ)}} = \frac{8}{1.8807 + 0.7813} = \frac{8}{2.662} \approx 3$.

**Respuesta:** 3 metros (**Alternativa C**).
