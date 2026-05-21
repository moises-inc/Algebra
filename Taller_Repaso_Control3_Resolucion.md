# Resolución Formal: Taller de Repaso Control 3 - Álgebra
**Materia:** Lógica, Conjuntos y Trigonometría  
**Docente:** Carol Asencio  
**Resolución:** Gemini Academic Assistant  

---

## Pregunta 1: Lógica Proposicional - Valores de Verdad
**Enunciado:** Se sabe que $(p \rightarrow \sim q) \vee (\sim r \rightarrow s)$ es falsa. Determinar el valor de verdad de:
i. $[(\sim r \vee q) \wedge q] \leftrightarrow [(\sim q \vee r) \wedge s]$
ii. $(p \rightarrow r) \rightarrow [(p \rightarrow q) \vee \sim s]$

**Desarrollo:**
Una disyunción ($A \vee B$) es falsa únicamente si ambos componentes son falsos.
1. $(p \rightarrow \sim q) \equiv F \implies p = V$ y $\sim q = F \implies \mathbf{q = V}$.
2. $(\sim r \rightarrow s) \equiv F \implies \sim r = V$ y $s = F \implies \mathbf{r = F, s = F}$.

Valores encontrados: $p=V, q=V, r=F, s=F$.

**Evaluación i:**
- Lado izquierdo: $[(\sim F \vee V) \wedge V] = [(V \vee V) \wedge V] = V \wedge V = V$.
- Lado derecho: $[(\sim V \vee F) \wedge F] = [(F \vee F) \wedge F] = F \wedge F = F$.
- $V \leftrightarrow F = \mathbf{F}$.

**Evaluación ii:**
- Antecedente: $p \rightarrow r = V \rightarrow F = F$.
- Consecuente: $(V \rightarrow V) \vee \sim F = V \vee V = V$.
- $F \rightarrow V = \mathbf{V}$.

**Respuesta:** F y V (**Alternativa C**).

---

## Pregunta 2: Lógica Proposicional - Contradicciones
**Enunciado:** ¿Cuál de las siguientes proposiciones es una contradicción (siempre falsa)?
I. $(p \wedge \sim q) \leftrightarrow (p \rightarrow q)$
II. $(p \wedge \sim q) \wedge (p \vee q)$
III. $\sim (p \Delta q) \rightarrow q$

**Desarrollo:**
I. Sabemos que $p \rightarrow q \equiv \sim p \vee q$. Su negación es $\neg(p \rightarrow q) \equiv p \wedge \sim q$. La expresión es de la forma $A \leftrightarrow \sim A$, lo cual es una **contradicción**.
II. Si $p=V, q=F$, entonces $(V \wedge \sim F) \wedge (V \vee F) = V \wedge V = V$. No es siempre falsa.
III. Si $p=V, q=V$, entonces $\sim (V \Delta V) \rightarrow V = \sim F \rightarrow V = V \rightarrow V = V$. No es siempre falsa.

**Respuesta:** Solo I (**Alternativa B**).

---

## Pregunta 3: Conjuntos en los Reales
**Enunciado:** $A = ]-2, 5]$, $B = ]-6, 3[$ y $C = [1, 2]$. Hallar $(C - B) \cup A$.

**Desarrollo:**
1. **Calcular $C - B$:** Son los elementos de $C$ que no están en $B$. Dado que $[1, 2] \subset ]-6, 3[$, todos los elementos de $C$ pertenecen a $B$. Por lo tanto, $C - B = \emptyset$.
2. **Unión con A:** $\emptyset \cup A = A = ]-2, 5]$.

**Respuesta:** $]-2, 5]$ (**Alternativa D**).

---

## Pregunta 4: Problema de Conjuntos (Encuesta)
**Enunciado:** Encuesta a 60 personas. 50 consumen al menos uno.
- 6 consumen F y C, pero no P.
- 3 consumen P y C, pero no F.
- 11 consumen P y F.
¿Cuántos consumen solamente un producto?

**Desarrollo:**
Definimos $x$ como el número de personas que consumen los tres productos ($P \cap F \cap C$).
- $P \cap F \setminus C = 11 - x$.
- Suma de regiones con 2 o 3 productos: $6 (FC) + 3 (PC) + (11 - x) (PF) + x (PFC) = 20$.
- Personas que consumen al menos uno = (Solo 1) + (Suma regiones 2 o 3).
- $50 = (\text{Solo 1}) + 20 \implies \text{Solo 1} = 30$.

**Respuesta:** 30 (**Alternativa A**).

---

## Pregunta 5: Porcentajes y Conjuntos (Diabetes)
**Enunciado:** T=59%, H=45%, D=49%. Padecen las tres=5%. T e H=17%. H y D=18%. Solo T=18%.
¿Qué porcentaje presenta alguna patología distinta a las tres?

**Desarrollo:**
1. $T \cap H \setminus D = 17 - 5 = 12\%$.
2. $H \cap D \setminus T = 18 - 5 = 13\%$.
3. Usando $T = \text{Solo T} + (TH \setminus D) + (TD \setminus H) + THD$:
   $59 = 18 + 12 + (TD \setminus H) + 5 \implies TD \setminus H = 24\%$.
4. $n(T \cup H \cup D) = \text{Solo T} + \text{Solo H} + \text{Solo D} + (TH \setminus D) + (HD \setminus T) + (TD \setminus H) + THD$.
   Primero hallamos Solo H: $45 - (12+13+5) = 15\%$.
   Hallamos Solo D: $49 - (24+13+5) = 7\%$.
5. Total Unión = $18 + 15 + 7 + 12 + 13 + 24 + 5 = 94\%$.
6. Exterior = $100\% - 94\% = 6\%$.

**Respuesta:** 6% (**Alternativa C**).

---

## Preguntas 6 a 8: Recetas Médicas
**Datos extraídos:**
- $A \cap B \setminus C = 20$
- Solo A = 40
- $A \setminus B = 55 \implies AC \setminus B = 55 - 40 = 15$
- Total A = 100 $\implies ABC = 100 - (40+20+15) = 25$
- Solo B = 50
- $B \cap C = 60 \implies BC \setminus A = 60 - 25 = 35$
- Total C = 80 $\implies \text{Solo C} = 80 - (15+35+25) = 5$

**Resultados:**
6. $B \cap C \setminus A = 35$ (**Alternativa B**).
7. $(A \cup C) \setminus B = \text{Solo A} + \text{Solo C} + (AC \setminus B) = 40 + 5 + 15 = 60$ (**Alternativa D**).
8. Total = $40+50+5+20+15+35+25 = 190$ (**Alternativa A**).

---

## Pregunta 9: Lógica - Implicación Falsa
**Enunciado:** $p \implies (q \vee r)$ es falsa. Determinar $p \vee (q \wedge \sim r)$.

**Desarrollo:**
Para que la implicación sea falsa: $p=V$ y $(q \vee r)=F$. Por lo tanto, $q=F$ y $r=F$.
- $V \vee (F \wedge \sim F) = V \vee (F \wedge V) = V \vee F = \mathbf{V}$.

**Respuesta:** Es Verdadera (**Alternativa C**).

---

## Pregunta 10: Lógica - Conjunción Verdadera
**Enunciado:** $p \wedge \sim (q \vee r)$ es verdadera. Determinar $p \implies (\sim q \wedge r)$.

**Desarrollo:**
Para que sea verdadera: $p=V$ y $\sim (q \vee r)=V \implies q \vee r = F \implies q=F, r=F$.
- $V \implies (\sim F \wedge F) = V \implies (V \wedge F) = V \implies F = \mathbf{F}$.

**Respuesta:** Es Falsa (**Alternativa D**).

---

## Pregunta 11: Problema de Salud (Venn)
**Enunciado:** $A=600, B=480, R=510$. $R \cap B=120, A \cap B=270, R \cap A=199, A \cap B \cap R=100$.
¿Bronquitis y Amigdalitis, pero no Rinofaringitis?

**Desarrollo:**
Se busca el conjunto $B \cap A \setminus R$.
- $(A \cap B) - (A \cap B \cap R) = 270 - 100 = 170$.

**Respuesta:** 170 niños (**Alternativa B**).

---

## Pregunta 12 y 13: Diagramas de Venn
12. El área coloreada cubre la unión de A y B, pero excluye el círculo C.
    **Respuesta:** $(A \cup B) - C$ (**Alternativa C**).
13. El área coloreada es la intersección de A y B, pero excluye la zona que pertenece a C.
    **Respuesta:** $(A \cap B) - C$ (**Alternativa D**).

---

## Pregunta 14: Conjuntos con Valor Absoluto
**Enunciado:** $A = ]1, 2] \cup \{3\}$, $B = \{x : |x-1| < 1\}$, $C = [-2, 1[$. Hallar $(B - C) \cup A$.

**Desarrollo:**
- $B = ]0, 2[$ (pues $|x-1| < 1 \iff 0 < x < 2$).
- $B - C = ]0, 2[ \setminus [-2, 1[ = [1, 2[$.
- $[1, 2[ \cup (]1, 2] \cup \{3\}) = [1, 2] \cup \{3\}$.

**Respuesta:** $[1, 2] \cup \{3\}$ (**Alternativa B**).

---

## Pregunta 15: Simplificación Trigonométrica
**Enunciado:** Simplifique $\frac{1 + \sec(4x)}{\sin(4x) + \tan(4x)}$.

**Desarrollo:**
Sea $\theta = 4x$.
$$\frac{1 + \frac{1}{\cos \theta}}{\sin \theta + \frac{\sin \theta}{\cos \theta}} = \frac{\frac{\cos \theta + 1}{\cos \theta}}{\frac{\sin \theta \cos \theta + \sin \theta}{\cos \theta}} = \frac{\cos \theta + 1}{\sin \theta (\cos \theta + 1)} = \frac{1}{\sin \theta} = \csc(4x)$$

**Respuesta:** $\csc(4x)$ (**Alternativa A**).

---

## Pregunta 16: Ecuación Trigonométrica
**Enunciado:** $2 \cos^2(x) - \cos(x) = 0$ en $[0, 2\pi]$.

**Desarrollo:**
Factoreando: $\cos(x)(2\cos(x) - 1) = 0$.
1. $\cos(x) = 0 \implies x = \pi/2, 3\pi/2$.
2. $\cos(x) = 1/2 \implies x = \pi/3, 5\pi/3$.

**Respuesta:** $\{\pi/3, \pi/2, 3\pi/2, 5\pi/3\}$ (**Alternativa C**).

---

## Pregunta 17: Perímetro de Polígono
**Datos:** $\alpha = 58^\circ, B=C, A=24.6$ cm.

**Desarrollo:**
- Altura $B = A \sin(58^\circ) \approx 20.86$.
- Base superior $C = B = 20.86$.
- Base inferior $D = C + A \cos(58^\circ) = 20.86 + 13.04 = 33.90$.
- Perímetro $= 24.6 + 20.86 + 20.86 + 33.90 = 100.22$.

**Respuesta:** 100.22 cm (**Alternativa D**).

---

## Pregunta 18: Ecuaciones sin Solución
I. $2 \cos^2 \theta + 5 \cos \theta + 2 = 0 \implies \cos \theta = -1/2$ (Tiene sol.).
II. $\tan(\theta/4) = -\sqrt{3}$ (Tiene sol.).
III. $2 \sin \theta = 4 \implies \sin \theta = 2$ (**No tiene solución real**).

**Respuesta:** Sólo la III (**Alternativa B**).

---

## Pregunta 19: Ecuación Trigonométrica con Identidades
**Enunciado:** $\sin(2x) \cos(x) - 2 \sin^3(x) = 0$.

**Desarrollo:**
$2 \sin x \cos^2 x - 2 \sin^3 x = 2 \sin x (\cos^2 x - \sin^2 x) = 2 \sin x \cos(2x) = 0$.
- $\sin x = 0 \implies x = 0, \pi, 2\pi$.
- $\cos(2x) = 0 \implies 2x = \pi/2, 3\pi/2, 5\pi/2, 7\pi/2 \implies x = \pi/4, 3\pi/4, 5\pi/4, 7\pi/4$.

**Respuesta:** Unión de ambos conjuntos (**Alternativa C**).

---

## Pregunta 20: Aplicación Pitágoras
- Altura = 4, Sombra = 3. Hipotenusa $= \sqrt{4^2 + 3^2} = 5$.
**Respuesta:** 5 metros (**Alternativa B**).

---

## Pregunta 21: Teorema del Coseno
$c^2 = 450^2 + 550^2 - 2(450)(550) \cos(69^\circ) \approx 327592$.
- $c \approx 572$.
**Respuesta:** 572 m (**Alternativa D**).

---

## Pregunta 22: Resolución de Triángulos (Altura Globo)
- $x = h / \tan(28^\circ)$ y $(8-x) = h / \tan(52^\circ)$.
- $h(1/\tan(28^\circ) + 1/\tan(52^\circ)) = 8$.
- $h = 8 / (1.8807 + 0.7813) \approx 3$.
**Respuesta:** 3 metros (**Alternativa C**).
