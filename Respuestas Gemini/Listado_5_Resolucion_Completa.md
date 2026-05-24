# Guía de Estudio y Resolución Formal: Listado 5 - Álgebra
**Asignatura:** Álgebra (DCEX0007)  
**Temática:** Lógica Proposicional y Teoría de Conjuntos  
**Origen:** Universidad San Sebastián (2026-1)  
**Resolución:** Gemini Academic Assistant (Estándar de Oro Pedagógico)  

---

## Introducción Conceptual
Esta guía ha sido reestructurada bajo un estándar docente premium. El objetivo no es solo presentar el resultado final, sino desglosar el razonamiento analítico detrás de cada paso lógico y demostración algebraica. Cada sección cuenta con justificaciones explícitas, uso formal de la notación matemática en LaTeX y la aplicación estricta de las leyes de la lógica y la teoría de conjuntos enseñadas en el curso.

---

## I. Ejercicios de Desarrollo

### 1. Análisis de Veracidad de Afirmaciones
> **Justificación Pedagógica:** Una proposición matemática es un enunciado declarativo que posee un valor de verdad unívoco (Verdadero o Falso). Las expresiones con variables libres no son proposiciones a menos que estén vinculadas por cuantificadores o se defina una igualdad.

*   **a) "x - 11" es una proposición. (Falso)**  
    *Desarrollo:* La expresión $x - 11$ es un término algebraico o función proposicional abierta, pero no es una proposición, ya que no afirma nada de lo cual se pueda dictaminar veracidad o falsedad. Para serlo, debería estar expresada como una ecuación o inecuación (ej. $x - 11 = 5$).
    
*   **b) Si la proposición $5 < 9$ es verdadera y $9 < 7$ es falsa, entonces la proposición compuesta $(5 < 9) \land (9 < 7)$ es verdadera. (Falso)**  
    *Desarrollo:* Definamos $p: 5 < 9 \equiv V$ y $q: 9 < 7 \equiv F$. Por definición de la conjunción ($\land$), la proposición compuesta $p \land q$ es verdadera **únicamente** cuando ambos componentes son verdaderos. Evaluando:  
    $$V \land F \equiv \mathbf{F}$$
    
*   **c) La negación de la proposición $(5 < 9) \land (9 < 7)$ es verdadera. (Verdadero)**  
    *Desarrollo:* Usando el resultado de la afirmación anterior, sabemos que $[(5 < 9) \land (9 < 7)] \equiv F$. Al aplicar el operador de negación ($\neg$):  
    $$\neg(F) \equiv \mathbf{V}$$
    
*   **d) La proposición compuesta $(5 < 9) \lor [\neg(9 < 7) \land (5 < 7)]$ es verdadera. (Verdadero)**  
    *Desarrollo:* Asignemos variables lógicas: $p: 5 < 9 \equiv V$, $q: 9 < 7 \equiv F$, $r: 5 < 7 \equiv V$. La expresión formal es:  
    $$p \lor (\neg q \land r) \equiv V \lor (\neg F \land V) \equiv V \lor (V \land V) \equiv V \lor V \equiv \mathbf{V}$$  
    *Nota:* Por Ley de Dominación, dado que el primer término de la disyunción inclusiva ($\lor$) es $V$, toda la expresión se evalúa inmediatamente como verdadera.

*   **e) La proposición $0 > 1 \iff 2 > 1$ es verdadera. (Falso)**  
    *Desarrollo:* Definamos $p: 0 > 1 \equiv F$ y $q: 2 > 1 \equiv V$. El bicondicional ($\iff$) establece que la relación es verdadera si y solo si ambas proposiciones tienen el **mismo** valor de verdad. Evaluando:  
    $$F \iff V \equiv \mathbf{F}$$

*   **f) La conjunción de dos proposiciones es falsa solo si ambas son falsas. (Falso)**  
    *Desarrollo:* La conjunción ($p \land q$) es falsa si **al menos una** de las proposiciones que la componen es falsa. Por lo tanto, es falsa en los casos $(V \land F)$, $(F \land V)$ y $(F \land F)$.

*   **g) La proposición compuesta $(p \land \neg q) \lor (p \Rightarrow q)$ es siempre verdadera. (Verdadero)**  
    *Desarrollo:* Demostremos mediante equivalencia lógica formal:
    1.  Definición de implicación: $p \Rightarrow q \equiv \neg p \lor q$
    2.  Sustituyendo: $(p \land \neg q) \lor (\neg p \lor q)$
    3.  Por Ley de De Morgan, notamos que $\neg(p \land \neg q) \equiv \neg p \lor \neg(\neg q) \equiv \neg p \lor q$.
    4.  Por tanto, la expresión tiene la estructura formal:  
        $$A \lor \neg A \equiv \mathbf{V} \quad \text{(Ley del Tercero Excluido)}$$
    La proposición es una tautología.

*   **h) El valor de verdad de $(p \land q) \lor p$ depende de los valores de verdad de $p$ y $q$. (Falso)**  
    *Desarrollo:* Aplicando la **Ley de Absorción** de la lógica proposicional:  
    $$(p \land q) \lor p \equiv p$$  
    La expresión se reduce algebraicamente de forma exclusiva a la variable $p$. Por ende, su valor de verdad depende únicamente de $p$ y es completamente independiente de $q$.

*   **i) Si la proposición $(p \land q) \lor p$ es falsa, entonces la proposición $q$ es falsa. (Falso)**  
    *Desarrollo:* Dado que $(p \land q) \lor p \equiv p$, si el enunciado es falso, implica directamente que $p \equiv F$. Bajo este escenario, si evaluamos la expresión original con $p=F$ y $q=V$:  
    $$(F \land V) \lor F \equiv F \lor F \equiv F$$  
    Vemos que la proposición sigue siendo falsa incluso si $q$ es verdadera. Por lo tanto, $q$ puede tomar cualquier valor de verdad.

*   **j) En lógica de predicados, de una afirmación universal se puede deducir una afirmación particular. (Verdadero)**  
    *Desarrollo:* En un dominio de discurso no vacío, si una propiedad se cumple para todos los elementos ($\forall x, P(x)$), por instanciación universal se garantiza que se cumple para al menos un elemento particular ($\exists x, P(x)$).

*   **k) De la afirmación "existe un elemento que cumple la propiedad", se puede deducir que dicho elemento es único. (Falso)**  
    *Desarrollo:* El cuantificador existencial estándar ($\exists x$) asegura la existencia de **al menos uno**, pero no restringe la cantidad superior. Para asegurar unicidad, se requiere el cuantificador de unicidad ($\exists! x$).

*   **l) La proposición $[(p \Rightarrow q) \land (\neg q \Rightarrow \neg p)] \Rightarrow (p \Rightarrow q)$ es verdadera. (Verdadero)**  
    *Desarrollo:* Analicemos la estructura: por la ley de contraposición, sabemos que $(\neg q \Rightarrow \neg p) \equiv (p \Rightarrow q)$. Sustituyendo, la proposición compuesta es:  
    $$[(p \Rightarrow q) \land (p \Rightarrow q)] \Rightarrow (p \Rightarrow q)$$  
    Por Ley de Idempotencia:  
    $$(p \Rightarrow q) \Rightarrow (p \Rightarrow q)$$  
    Cualquier proposición que se implique a sí misma ($A \Rightarrow A$) es una tautología, por lo tanto, siempre es **Verdadera**.

*   **m) El valor de verdad de $p \iff V$ es el mismo que el valor de verdad de $p$. (Verdadero)**  
    *Desarrollo:* Analicemos por casos:
    - Si $p \equiv V \implies V \iff V \equiv V$.
    - Si $p \equiv F \implies F \iff V \equiv F$.  
    En ambos casos, el valor resultante es idéntico al de $p$.

*   **n) Para demostrar que una afirmación universal es falsa, basta con encontrar un contraejemplo. (Verdadero)**  
    *Desarrollo:* La negación de una proposición universal es una existencial: $\neg[\forall x, P(x)] \equiv \exists x, \neg P(x)$. Por ende, exhibir un único elemento $x_0$ para el cual la propiedad $P(x_0)$ sea falsa (contraejemplo) refuta la universalidad.

*   **o) La proposición $[(q \Rightarrow r) \land q] \Rightarrow r$ es siempre verdadera. (Verdadero)**  
    *Desarrollo:* Esta estructura corresponde a la regla de inferencia fundamental clásica conocida como **Modus Ponendo Ponens** (Modus Ponens). Su tabla de verdad arroja únicamente valores verdaderos, siendo una tautología.

*   **p) La expresión "¿Cómo estás hoy?" es una proposición. (Falso)**  
    *Desarrollo:* Las oraciones exclamativas, interrogativas u órdenes no son declarativas y carecen de valor de verdad.

*   **q) La expresión $3 + 5 = 12$ es una proposición. (Verdadero)**  
    *Desarrollo:* Es un enunciado declarativo matemático que puede evaluarse inequívocamente como **Falso**. Al poder asignársele un valor de verdad, es una proposición.

*   **r) Si la proposición $p \land q$ es siempre verdadera, entonces $p$ es siempre verdadera y $q$ puede ser falsa. (Falso)**  
    *Desarrollo:* Para que la conjunción $p \land q$ sea verdadera, es condición necesaria y suficiente que **ambas** proposiciones simples sean verdaderas simultáneamente. Si $q$ fuese falsa, la conjunción sería falsa.

---

### 2. Formalización de Proposiciones con p y q
> **Justificación Pedagógica:** La formalización traduce el lenguaje natural al lenguaje formal de la lógica matemática. Es clave identificar el rol del antecedente y consecuente en estructuras condicionales (como "es necesario", "es suficiente", "siempre que").

Definiciones de variables lógicas:
*   $p$: Conduces a más de 100 km/h.
*   $q$: Te multan por exceso de velocidad.

*   **a) No conduces a más de 100 km/h.**  
    *Formalización:* $\neg p$
*   **b) Conduces a más de 100 km/h pero no te multan por exceso de velocidad.**  
    *Formalización:* $p \land \neg q$  
    *Nota:* La palabra "pero" actúa semánticamente como una conjunción lógica ($\land$).
*   **c) Si conduces a más de 100 km/h, te multarán por exceso de velocidad.**  
    *Formalización:* $p \Rightarrow q$
*   **d) Si no conduces a más de 100 km/h, no te multarán por exceso de velocidad.**  
    *Formalización:* $\neg p \Rightarrow \neg q$
*   **e) Conducir a más de 100 km/h es suficiente para que te multen por exceso de velocidad.**  
    *Formalización:* $p \Rightarrow q$  
    *Explicación:* Que ocurra $p$ basta para garantizar $q$. El término "suficiente" señala el antecedente.
*   **f) Te multan por exceso de velocidad, pero no conduces a más de 100 km/h.**  
    *Formalización:* $q \land \neg p$
*   **g) Te multarán por exceso de velocidad siempre que conduzcas a más de 100 km/h.**  
    *Formalización:* $p \Rightarrow q$  
    *Explicación:* "Siempre que" introduce la condición bajo la cual ocurre el evento, es decir, el antecedente. Por lo tanto, $p$ implica $q$.

---

### 3. Formalización de Proposiciones Compuestas Complejas
*   **a) No es verdad que no me guste estudiar.**  
    *Definición:* $p$: Me gusta estudiar.  
    *Formalización:* $\neg(\neg p) \equiv p$ (Por ley de doble negación, equivale a "Me gusta estudiar").
*   **b) Ni José ni Juan son estudiosos.**  
    *Definición:* $p$: José es estudioso. $q$: Juan es estudioso.  
    *Formalización:* $\neg p \land \neg q$ (Equivalente por De Morgan a $\neg(p \lor q)$).
*   **c) No ocurre que: haga calor y no llueva.**  
    *Definición:* $p$: Hace calor. $q$: Llueve.  
    *Formalización:* $\neg(p \land \neg q)$
*   **d) Lavar el coche es una condición necesaria para ascender.**  
    *Definición:* $p$: Ascender. $q$: Lavar el coche.  
    *Formalización:* $p \Rightarrow q$  
    *Explicación:* La condición "necesaria" siempre se ubica en el consecuente de la implicación. Si asciendes ($p$), obligatoriamente lavaste el coche ($q$).
*   **e) El viento del sur implica el deshielo.**  
    *Definición:* $p$: Viento del sur. $q$: Deshielo.  
    *Formalización:* $p \Rightarrow q$
*   **f) La garantía es válida solo si compraste el producto hace menos de un año.**  
    *Definición:* $p$: La garantía es válida. $q$: Compraste el producto hace menos de un año.  
    *Formalización:* $p \Rightarrow q$  
    *Explicación:* La estructura "$A$ solo si $B$" se formaliza algebraicamente como $A \Rightarrow B$.
*   **g) Si haces trampas serás pillado.**  
    *Definición:* $p$: Hacer trampas. $q$: Ser pillado.  
    *Formalización:* $p \Rightarrow q$
*   **h) Es necesario pagar la cuota para acceder a la web.**  
    *Definición:* $p$: Acceder a la web. $q$: Pagar la cuota.  
    *Formalización:* $p \Rightarrow q$ (Nuevamente, la necesidad se traduce en el consecuente).
*   **i) Conocer a la gente adecuada es suficiente para ser elegido.**  
    *Definición:* $p$: Conocer a la gente adecuada. $q$: Ser elegido.  
    *Formalización:* $p \Rightarrow q$ (La suficiencia señala al antecedente).
*   **j) Ganarás el concurso si y solo si tienes el número ganador.**  
    *Definición:* $p$: Ganar el concurso. $q$: Tener el número ganador.  
    *Formalización:* $p \iff q$
*   **k) Tomo el tren siempre y cuando llegue con retraso.**  
    *Definición:* $p$: Tomo el tren. $q$: El tren llega con retraso.  
    *Formalización:* $p \iff q$  
    *Explicación:* "Siempre y cuando" establece una equivalencia bicondicional estricta.

---

### 4. Deducción de Valor de Verdad con Condicional Falso
> **Justificación Pedagógica:** El operador de implicación ($p \Rightarrow q$) es falso en un único escenario: cuando el antecedente es verdadero ($V$) y el consecuente es falso ($F$). Esto nos provee el valor de verdad de las variables de forma inmediata para evaluar expresiones más complejas.

**Enunciado:** Si la proposición $p \Rightarrow q$ es falsa, determine el valor de verdad de la proposición compuesta:  
$$(p \lor q) \iff (q \land p)$$

**Desarrollo Paso a Paso:**
1.  Dado que $p \Rightarrow q \equiv F$, deducimos que:
    *   $p \equiv V$
    *   $q \equiv F$
2.  Sustituimos estos valores individuales en la expresión objetivo:
    *   Término izquierdo: $(p \lor q) \equiv (V \lor F) \equiv V$
    *   Término derecho: $(q \land p) \equiv (F \land V) \equiv F$
3.  Evaluamos el bicondicional central:
    $$(p \lor q) \iff (q \land p) \equiv V \iff F \equiv \mathbf{F}$$

**Conclusión:** La proposición compuesta es **Falsa**.

---

### 5. Deducción de Valor de Verdad con Conjunción Verdadera
> **Justificación Pedagógica:** El operador de conjunción ($p \land q$) es verdadero únicamente en un escenario: cuando ambos operandos son verdaderos simultáneamente.

**Enunciado:** Si la proposición $p \land q$ es verdadera, determine el valor de verdad de:  
$$(p \Rightarrow q) \iff (p \lor q)$$

**Desarrollo Paso a Paso:**
1.  Dado que $p \land q \equiv V$, deducimos directamente que:
    *   $p \equiv V$
    *   $q \equiv V$
2.  Sustituimos en la expresión:
    *   Término izquierdo: $(p \Rightarrow q) \equiv (V \Rightarrow V) \equiv V$
    *   Término derecho: $(p \lor q) \equiv (V \lor V) \equiv V$
3.  Evaluamos el conector principal:
    $$(p \Rightarrow q) \iff (p \lor q) \equiv V \iff V \equiv \mathbf{V}$$

**Conclusión:** La proposición compuesta es **Verdadera**.

---

### 6. Demostración mediante Tablas de Verdad
> **Justificación Pedagógica:** Para demostrar que dos proposiciones compuestas son lógicamente equivalentes, se construyen sus tablas de verdad. Si las columnas resultantes para ambas expresiones son idénticas en todas las combinaciones posibles, las expresiones son equivalentes.

**Enunciado:** Demuestre mediante tablas de verdad la equivalencia:  
$$(p \land \neg q) \Rightarrow r \equiv \neg p \lor (q \lor r)$$

**Tabla de Verdad Estructurada:**

| $p$ | $q$ | $r$ | $\neg q$ | $p \land \neg q$ | $(p \land \neg q) \Rightarrow r$ | $q \lor r$ | $\neg p$ | $\neg p \lor (q \lor r)$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|  V  |  V  |  V  |    F   |        F         |                **V**             |     V      |    F     |          **V**           |
|  V  |  V  |  F  |    F   |        F         |                **V**             |     V      |    F     |          **V**           |
|  V  |  F  |  V  |    V   |        V         |                **V**             |     V      |    F     |          **V**           |
|  V  |  F  |  F  |    V   |        V         |                **F**             |     F      |    F     |          **F**           |
|  F  |  V  |  V  |    F   |        F         |                **V**             |     V      |     V    |          **V**           |
|  F  |  V  |  F  |    F   |        F         |                **V**             |     V      |     V    |          **V**           |
|  F  |  F  |  V  |    V   |        F         |                **V**             |     V      |     V    |          **V**           |
|  F  |  F  |  F  |    V   |        F         |                **V**             |     F      |     V    |          **V**           |

**Conclusión:** Como las columnas correspondientes a $(p \land \neg q) \Rightarrow r$ y $\neg p \lor (q \lor r)$ son idénticas en todas sus filas, queda formalmente demostrado que las proposiciones son lógicamente equivalentes.

---

### 7. Simplificación Algebraico-Formal de Proposiciones
> **Justificación Pedagógica:** La simplificación consiste en aplicar consecutivamente leyes lógicas fundamentales demostradas para reducir la complejidad de una proposición, evitando el uso de tablas de verdad. Se debe explicitar el nombre de cada ley en cada transición.

*   **a) $p \land (q \land \neg p)$**  
    1.  $p \land (\neg p \land q)$ — *Ley Conmutativa*
    2.  $(p \land \neg p) \land q$ — *Ley Asociativa*
    3.  $F \land q$ — *Ley de Contradicción* (ya que $p \land \neg p \equiv F$)
    4.  $\mathbf{F}$ — *Ley de Dominación*  

*   **b) $(p \land q) \lor p$**  
    1.  $\mathbf{p}$ — *Ley de Absorción* (Directo, puesto que $A \lor (A \land B) \equiv A$).

*   **c) $(p \Rightarrow q) \lor \neg p$**  
    1.  $(\neg p \lor q) \lor \neg p$ — *Definición de Implicación*
    2.  $(\neg p \lor \neg p) \lor q$ — *Leyes Conmutativa y Asociativa*
    3.  $\neg p \lor q$ — *Ley de Idempotencia* ($\neg p \lor \neg p \equiv \neg p$)
    4.  $\mathbf{p \Rightarrow q}$ — *Definición de Implicación*

*   **d) $(p \Rightarrow q) \lor p$**  
    1.  $(\neg p \lor q) \lor p$ — *Definición de Implicación*
    2.  $(p \lor \neg p) \lor q$ — *Leyes Conmutativa y Asociativa*
    3.  $V \lor q$ — *Ley del Tercero Excluido* ($p \lor \neg p \equiv V$)
    4.  $\mathbf{V}$ — *Ley de Dominación* (Tautología)

*   **e) $(q \Rightarrow p) \Rightarrow p$**  
    1.  $\neg(q \Rightarrow p) \lor p$ — *Definición de Implicación*
    2.  $\neg(\neg q \lor p) \lor p$ — *Definición de Implicación*
    3.  $(\neg \neg q \land \neg p) \lor p$ — *Ley de De Morgan*
    4.  $(q \land \neg p) \lor p$ — *Ley de Doble Negación*
    5.  $p \lor (q \land \neg p)$ — *Ley Conmutativa*
    6.  $(p \lor q) \land (p \lor \neg p)$ — *Ley Distributiva*
    7.  $(p \lor q) \land V$ — *Ley del Tercero Excluido*
    8.  $\mathbf{p \lor q}$ — *Ley de Identidad*

*   **f) $(p \Rightarrow q) \Rightarrow p$**  
    1.  $\neg(p \Rightarrow q) \lor p$ — *Definición de Implicación*
    2.  $\neg(\neg p \lor q) \lor p$ — *Definición de Implicación*
    3.  $(\neg \neg p \land \neg q) \lor p$ — *Ley de De Morgan*
    4.  $(p \land \neg q) \lor p$ — *Ley de Doble Negación*
    5.  $\mathbf{p}$ — *Ley de Absorción* (ya que $p \lor (p \land A) \equiv p$)

*   **g) $p \land \neg(q \Rightarrow p)$**  
    1.  $p \land \neg(\neg q \lor p)$ — *Definición de Implicación*
    2.  $p \land (\neg \neg q \land \neg p)$ — *Ley de De Morgan*
    3.  $p \land (q \land \neg p)$ — *Ley de Doble Negación*
    4.  $p \land (\neg p \land q)$ — *Ley Conmutativa*
    5.  $(p \land \neg p) \land q$ — *Ley Asociativa*
    6.  $F \land q$ — *Ley de Contradicción*
    7.  $\mathbf{F}$ — *Ley de Dominación*

---

### 8. Valor de Verdad con Cuantificadores en $A = \{1, 2, 3, 4\}$
> **Justificación Pedagógica:** Los cuantificadores determinan la extensión en la que una proposición abierta es válida en un conjunto dado. $\forall$ exige cumplimiento absoluto en cada elemento, mientras que $\exists$ requiere que al menos un elemento verifique la condición.

*   **a) $\forall x \in A : x + 3 < 6$ (Falso)**  
    *Desarrollo:* Evaluemos para cada elemento de $A$:
    - Si $x=1 \implies 4 < 6$ (V)
    - Si $x=2 \implies 5 < 6$ (V)
    - Si $x=3 \implies 6 < 6$ (F).  
    Dado que existe un contraejemplo ($x=3$ y $x=4$ no cumplen), la afirmación universal es falsa.

*   **b) $\forall x \in A : x^2 - 10 \le 8$ (Verdadero)**  
    *Desarrollo:* Evaluemos para el elemento más crítico, el máximo valor de $A$ ($x=4$):  
    $$4^2 - 10 = 16 - 10 = 6 \le 8 \quad (V)$$  
    Dado que se cumple para el elemento más grande del conjunto, es directo verificar que para $x=1,2,3$ el término $x^2-10$ será aún menor y, por tanto, menor o igual a 8.

*   **c) $\exists x \in A : 2x^2 + x = 15$ (Falso)**  
    *Desarrollo:* Resolvamos algebraicamente la ecuación cuadrática $2x^2 + x - 15 = 0$:  
    $$(2x - 5)(x + 3) = 0 \implies x = \frac{5}{2} \lor x = -3$$  
    Ninguno de los dos valores reales resultantes ($\frac{5}{2}, -3$) pertenece al conjunto $A$. En consecuencia, no existe ningún elemento en $A$ que cumpla la igualdad.

*   **d) $\exists x \in A : x^2 > 1 \Rightarrow x + 2 = 0$ (Verdadero)**  
    *Desarrollo:* Evaluemos la implicación para $x=1$:
    - Antecedente: $1^2 > 1 \equiv 1 > 1 \equiv F$
    - Consecuente: $1 + 2 = 0 \equiv 3 = 0 \equiv F$  
    Evaluando el condicional para $x=1$: $F \Rightarrow F \equiv V$. Al encontrar al menos un elemento que hace verdadera la implicación, la afirmación existencial es verdadera.

*   **e) $\exists! x \in A : x^2 > 1 \iff x + 2 = 0$ (Verdadero)**  
    *Desarrollo:* Analicemos el bicondicional para cada elemento de $A$:
    - Para $x=1$: $1^2 > 1 \iff 1+2=0 \equiv F \iff F \equiv \mathbf{V}$ (Verdadero).
    - Para $x=2$: $4 > 1 \iff 4=0 \equiv V \iff F \equiv \mathbf{F}$ (Falso).
    - Para $x=3$: $9 > 1 \iff 5=0 \equiv V \iff F \equiv \mathbf{F}$ (Falso).
    - Para $x=4$: $16 > 1 \iff 6=0 \equiv V \iff F \equiv \mathbf{F}$ (Falso).  
    El único elemento de $A$ que cumple la condición es $x=1$. Al ser única la solución, la afirmación de existencia y unicidad ($\exists!$) es verdadera.

---

### 9. Valor de Verdad con Cuantificadores en $A = \{0, 1, 2, 3, 4, 5\}$
*   **a) $\exists x \in A / x^2 = x$ (Verdadero)**  
    *Desarrollo:* La ecuación $x(x-1) = 0$ tiene soluciones $x=0$ y $x=1$. Ambos elementos pertenecen al conjunto $A$. Al existir al menos uno, el enunciado es verdadero.

*   **b) $\exists x \in A / \forall y \in A, xy \ge 0$ (Verdadero)**  
    *Desarrollo:* Evaluemos si existe un elemento que al multiplicarse por cualquier otro dé mayor o igual a cero. Seleccionemos $x=0 \in A$:  
    $$0 \cdot y = 0 \ge 0 \quad \forall y \in A$$  
    La proposición se cumple (de hecho, para cualquier $x$ del conjunto se cumpliría pues no hay elementos negativos en $A$).

*   **c) $\forall x \in A, \exists y \in A / x + 2 = y$ (Falso)**  
    *Desarrollo:* Evaluemos para $x=4 \in A$:  
    $$4 + 2 = 6$$  
    Dado que $6 \notin A$, no existe ningún elemento $y \in A$ tal que se verifique la igualdad para $x=4$ (y lo mismo ocurre para $x=5$).

*   **d) $\exists x \in A / \forall y \in A, x + y$ es par. (Falso)**  
    *Desarrollo:* Para cualquier número entero $x$ elegido en $A$, la suma $x+y$ alternará necesariamente entre par e impar dependiendo de la paridad de $y$. Si $x$ es par, basta elegir $y$ impar (ej. $y=1$) para que la suma sea impar. Si $x$ es impar, elegimos $y$ par (ej. $y=0$) para obtener una suma impar. Por lo tanto, no existe tal $x$.

---

### 10. Negación Formal de Proposiciones Cuantificadas
> **Justificación Pedagógica:** La negación de cuantificadores se rige por las leyes de equivalencia: $\neg[\forall x, P(x)] \equiv \exists x, \neg P(x)$ y $\neg[\exists x, P(x)] \equiv \forall x, \neg P(x)$. Además, se debe negar formalmente la función proposicional interna.

*   **a) $\exists x \in A / x^2 = x$**  
    *Negación:* $\forall x \in A, x^2 \neq x$
*   **b) $\forall x \exists y (x + y = 5 \lor y = -x)$**  
    *Negación:* $\exists x \forall y \neg(x + y = 5 \lor y = -x) \equiv \exists x \forall y (x + y \neq 5 \land y \neq -x)$
*   **c) $\forall x \forall y (x + y \text{ es par} \lor x \text{ es impar} \lor y \text{ es impar})$**  
    *Negación:* $\exists x \exists y (x + y \text{ es impar} \land x \text{ es par} \land y \text{ es par})$
*   **d) $\exists x \forall y (x < y \land x^2 \ge y)$**  
    *Negación:* $\forall x \exists y \neg(x < y \land x^2 \ge y) \equiv \forall x \exists y (x \ge y \lor x^2 < y)$

---

## II. Selección Múltiple

### 1. Respuesta Correcta: C
*   **Enunciado:** Si $p$ es falsa, $q$ verdadera y $r$ falsa. Evaluar $(q \Rightarrow p) \Rightarrow r$.
*   **Desarrollo:**  
    $$(V \Rightarrow F) \Rightarrow F \equiv F \Rightarrow F \equiv \mathbf{V}$$

### 2. Respuesta Correcta: A
*   **Enunciado:** Si $(p \land \neg q) \Rightarrow (r \Rightarrow \neg s)$ es falsa. Determinar el orden de verdad para $q, p, r, s$.
*   **Desarrollo:**  
    Para que una implicación sea falsa, el antecedente debe ser verdadero y el consecuente falso:
    1.  $p \land \neg q \equiv V \implies \mathbf{p = V, q = F}$.
    2.  $r \Rightarrow \neg s \equiv F \implies \mathbf{r = V, \neg s = F \implies s = V}$.
    3.  Orden $q, p, r, s$: $F, V, V, V$.

### 3. Respuesta Correcta: B
*   **Enunciado:** Evaluar expresiones con $p=V, q=V, r=F, s=F$.
*   **Desarrollo:** Al sustituir directamente en los condicionales y conjunciones, se comprueba que únicamente las combinaciones de la alternativa B resultan consistentes con todas las variables dadas.

### 4. Respuesta Correcta: C
*   **Enunciado:** Analizar cuantificadores en $A = \{1, 2, 3\}$.
*   **Desarrollo:** 
    *   i) $\forall x \in A, x+3<6 \lor x^2-10 \le 8$ (Verdadero, pues todos cumplen al menos una de las dos condiciones).
    *   ii) $\exists x \in A / 2x^2+x=15 \lor x^2>1 \Rightarrow x+2=0$ (Verdadero, se verifica para $x=1$).
    *   iii) $\exists! x \in A / x^2 > 1 \iff x+7=0$ (Falso, ningún elemento satisface la inecuación de manera unívoca).

### 5. Respuesta Correcta: C
*   **Enunciado:** Negar la proposición $p \iff q$.
*   **Desarrollo:**  
    $$\neg(p \iff q) \equiv \neg[(p \Rightarrow q) \land (q \Rightarrow p)] \equiv (p \land \neg q) \lor (q \land \neg p)$$  
    Esto representa exactamente la disyunción exclusiva (o excluyente) de $p$ y $q$.

### 6. Respuesta Correcta: A
*   **Enunciado:** Si $s=V$ y $s \Rightarrow \neg(p \lor q) \equiv V$.
*   **Desarrollo:**  
    Dado que el antecedente $s$ es verdadero y la implicación es verdadera, el consecuente debe ser verdadero: $\neg(p \lor q) \equiv V \implies p \lor q \equiv F \implies \mathbf{p=F, q=F}$. Al evaluar, se verifica que todas las sub-expresiones de la alternativa A son verdaderas.

### 7. Respuesta Correcta: A
*   **Enunciado:** Si $(p \Rightarrow \neg q) \lor (\neg r \Rightarrow s)$ es falsa.
*   **Desarrollo:**  
    La disyunción es falsa si ambos términos son falsos:
    1.  $p \Rightarrow \neg q \equiv F \implies \mathbf{p = V, \neg q = F \implies q = V}$.
    2.  $\neg r \Rightarrow s \equiv F \implies \mathbf{\neg r = V \implies r = F, s = F}$.
    Por ende: $p=V, q=V, r=F, s=F$.

### 8. Respuesta Correcta: A
*   **Enunciado:** Formalizar "Para que ocurra B es suficiente que ocurra A".
*   **Desarrollo:**  
    La suficiencia señala al antecedente de la implicación, por lo tanto se traduce como $A \Rightarrow B$. Sustituyendo los enunciados correspondientes del ejercicio, la forma correcta es $(q \land p) \Rightarrow r$.
