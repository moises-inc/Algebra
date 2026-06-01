---
id: "20260524-listado-5-resolucion-completa"
title: "Listado 5 resolucion completa"
project: "Estudios_Universidad"
date: "2026-05-24T12:30:20"
last_modified: "2026-05-30T19:03:58"
type: "academic-note"
status: "completed"
priority: "medium"
tags: ["#status/completed", "#project/Estudios_Universidad", "#course/lgebra"]
---

# Guía de Estudio y Resolución Formal: Listado 5 - Álgebra
**Asignatura:** Álgebra (DCEX0007)  
**Temática:** Lógica Proposicional y Teoría de Conjuntos  
**Origen:** Universidad San Sebastián (2026-1)  
**Resolución:** Revisor Matemático (Estándar de Oro Académico)  

---

## Introducción Conceptual
Esta guía ha sido revisada minuciosamente y corregida bajo un estándar académico de excelencia docente. Cada sección cuenta con justificaciones formales y la aplicación estricta de las leyes lógicas y de teoría de conjuntos dictadas en el curso. 

En cumplimiento estricto con las directrices del curso, **no se utilizan herramientas de cálculo infinitesimal** (límites, derivadas, integrales). Todos los razonamientos se fundamentan exclusivamente en la lógica proposicional, de predicados y en el álgebra de conjuntos.

---

## I. Ejercicios de Desarrollo

### 1. Análisis de Veracidad de Afirmaciones
> **Justificación Pedagógica:** Una proposición matemática es un enunciado declarativo que posee un valor de verdad unívoco (Verdadero o Falso). Las expresiones con variables libres no son proposiciones a menos que estén cuantificadas o tengan valores de verdad fijos asignados en el dominio.

*   **a) “x – 11” corresponde a una proposición lógica, si se reemplaza el x por un número. (Falso)**  
    *Desarrollo:* La expresión $x - 11$ es un término algebraico (función). Si se reemplaza $x$ por un número (por ejemplo, $x = 15$), se obtiene $15 - 11 = 4$, el cual sigue siendo un número y no un enunciado declarativo. Para ser una proposición, debería ser una igualdad o desigualdad (ej. $x - 11 = 0$, que al reemplazar $x$ sí puede evaluarse como verdadera o falsa).

*   **b) $5 < 9$ y $9 < 7$. (Falso)**  
    *Desarrollo:* Definamos las proposiciones simples $p: 5 < 9$ (Verdadera, $\mathbf{V}$) y $q: 9 < 7$ (Falsa, $\mathbf{F}$). La conjunción $p \land q$ es verdadera únicamente cuando ambos componentes son verdaderos. Evaluando:  
    $$\mathbf{V} \land \mathbf{F} \equiv \mathbf{F}$$

*   **c) No es cierto que ($5 < 9$ y $9 < 7$). (Verdadero)**  
    *Desarrollo:* A partir del resultado del ejercicio anterior, sabemos que la conjunción $(5 < 9) \land (9 < 7)$ es falsa ($\mathbf{F}$). Al aplicar la negación externa $\neg(p \land q)$:  
    $$\neg(\mathbf{F}) \equiv \mathbf{V}$$

*   **d) $5 < 9$ o no es cierto que ($9 < 7$) y ($5 < 7$). (Verdadero)**  
    *Desarrollo:* Sean $p: 5 < 9 \equiv \mathbf{V}$, $q: 9 < 7 \equiv \mathbf{F}$ y $r: 5 < 7 \equiv \mathbf{V}$. La expresión formal es:  
    $$p \lor (\neg q \land r)$$  
    Sustituyendo los valores de verdad:  
    $$\mathbf{V} \lor (\neg\mathbf{F} \land \mathbf{V}) \equiv \mathbf{V} \lor (\mathbf{V} \land \mathbf{V}) \equiv \mathbf{V} \lor \mathbf{V} \equiv \mathbf{V}$$  
    *(Nota: Por ley de dominación de la disyunción, dado que el primer término $p$ es verdadero, toda la proposición es inmediatamente verdadera).*

*   **e) $0 > 1$ sí, y sólo si, $2 > 1$. (Falso)**  
    *Desarrollo:* Sean $p: 0 > 1 \equiv \mathbf{F}$ y $q: 2 > 1 \equiv \mathbf{V}$. El bicondicional ($p \iff q$) es verdadero únicamente cuando ambas proposiciones tienen el mismo valor de verdad. Como una es falsa y la otra verdadera:  
    $$\mathbf{F} \iff \mathbf{V} \equiv \mathbf{F}$$

*   **f) La proposición $p \land q$ es falsa si y solo si $p$ y $q$ son falsas. (Falso)**  
    *Desarrollo:* Por definición del conector de conjunción ($\land$), $p \land q$ es falsa siempre que **al menos una** de las proposiciones simples sea falsa. Es decir, es falsa si $p \equiv \mathbf{F}$ y $q \equiv \mathbf{V}$, o si $p \equiv \mathbf{V}$ y $q \equiv \mathbf{F}$, o si ambas son falsas. Por ende, no requiere de forma exclusiva que ambas sean falsas.

*   **g) El valor de verdad de $(p \land \neg q) \lor (p \Rightarrow q)$ puede ser falso. (Falso)**  
    *Desarrollo:* Demostremos analíticamente que la expresión es una tautología (siempre verdadera):  
    1.  Definición de condicional: $p \Rightarrow q \equiv \neg p \lor q$  
    2.  Sustituyendo: $(p \land \neg q) \lor (\neg p \lor q)$  
    3.  Por la ley de De Morgan, notamos que $\neg(p \land \neg q) \equiv \neg p \lor q$.  
    4.  Sustituyendo esto, la expresión original se reduce a la estructura clásica del Tercero Excluido:  
        $$A \lor \neg A \equiv \mathbf{V}$$  
    Al ser una tautología, su valor de verdad es **siempre verdadero** y jamás puede ser falso.

*   **h) La proposición $(p \land q) \lor p$ es verdadera sólo cuando $q$ es verdadera. (Falso)**  
    *Desarrollo:* Aplicando la **Ley de Absorción** de la lógica proposicional:  
    $$(p \land q) \lor p \equiv p$$  
    La expresión depende única y exclusivamente de la proposición $p$. Si $p$ es verdadera, toda la proposición es verdadera sin importar si $q$ es verdadera o falsa (por ejemplo, si $p \equiv \mathbf{V}$ y $q \equiv \mathbf{F}$, la expresión se evalúa como verdadera).

*   **i) Si la proposición $(p \land q) \lor p$ es falsa, necesariamente $q$ es falsa. (Falso)**  
    *Desarrollo:* Por absorción, $(p \land q) \lor p \equiv p$. Si la expresión es falsa, significa que $p \equiv \mathbf{F}$. Bajo este escenario, si evaluamos la expresión con $p \equiv \mathbf{F}$ y $q \equiv \mathbf{V}$:  
    $$(\mathbf{F} \land \mathbf{V}) \lor \mathbf{F} \equiv \mathbf{F} \lor \mathbf{F} \equiv \mathbf{F}$$  
    Vemos que la proposición sigue siendo falsa aunque $q$ sea verdadera. Por lo tanto, $q$ no es necesariamente falsa.

*   **j) Si la proposición $(\forall x)p(x)$ es verdadera, entonces la proposición $(\exists x)p(x)$ es también verdadera. (Verdadero)**  
    *Desarrollo:* En un dominio de discurso no vacío (estándar en lógica de primer orden), si una propiedad $p(x)$ es verdadera para **todos** los elementos del conjunto, se garantiza por instanciación universal que se cumple para al menos un elemento particular. Por lo tanto, existirá al menos un elemento que cumpla con la propiedad.

*   **k) Es siempre cierto que si la proposición $(\exists x)p(x)$ es verdadera, entonces la proposición $(\exists! x)p(x)$ es verdadera. (Falso)**  
    *Desarrollo:* El cuantificador existencial estándar ($\exists x$) asegura la existencia de **al menos uno** (uno o más), mientras que el cuantificador de existencia única ($\exists! x$) exige que exista **exactamente uno**. Si la propiedad la cumplen dos o más elementos, la proposición existencial es verdadera pero la de unicidad es falsa.

*   **l) La proposición $((\neg q \Rightarrow \neg p) \land (q \Rightarrow r)) \Rightarrow (\neg r \Rightarrow \neg p)$ es una tautología. (Verdadero)**  
    *Desarrollo:* Simplifiquemos la implicación utilizando la Ley de Contraposición:  
    1.  $\neg q \Rightarrow \neg p \equiv p \Rightarrow q$  
    2.  $\neg r \Rightarrow \neg p \equiv p \Rightarrow r$  
    Sustituyendo estos términos equivalentes, la proposición se transforma en:  
    $$((p \Rightarrow q) \land (q \Rightarrow r)) \Rightarrow (p \Rightarrow r)$$  
    Esta estructura formal corresponde exactamente a la regla del **Silogismo Hipotético** (transitividad del condicional), la cual es una tautología clásica de la lógica proposicional.

*   **m) La proposición $(p \iff \mathbf{V})$ tiene siempre el mismo valor de verdad que $p$. (Verdadero)**  
    *Desarrollo:* Analicemos por tabla de verdad o casos:  
    - Si $p \equiv \mathbf{V} \implies \mathbf{V} \iff \mathbf{V} \equiv \mathbf{V}$.  
    - Si $p \equiv \mathbf{F} \implies \mathbf{F} \iff \mathbf{V} \equiv \mathbf{F}$.  
    En ambos casos, el valor resultante es idéntico al valor original de $p$.

*   **n) Si $p(x)$ es una función proposicional y $x_0$ es tal que $p(x_0)$ es falsa, entonces la proposición cuantificada $(\forall x)p(x)$ es falsa. (Verdadero)**  
    *Desarrollo:* Por leyes de cuantificadores, la negación de una afirmación universal es una existencial: $\neg(\forall x)p(x) \equiv (\exists x)\neg p(x)$. Si encontramos un contraejemplo $x_0$ tal que $p(x_0) \equiv \mathbf{F}$, demostramos que $(\exists x)\neg p(x)$ es verdadera, lo que invalida y hace falsa la universal $(\forall x)p(x)$.

*   **o) Si la proposición $q \Rightarrow r$ es verdadera y $q$ también lo es, necesariamente $r$ es verdadera. (Verdadero)**  
    *Desarrollo:* Corresponde directamente a la regla fundamental de inferencia del **Modus Ponendo Ponens**. En un condicional verdadero con antecedente verdadero, el consecuente está obligado a ser verdadero.

*   **p) “¿Podrás venir mañana?” es una proposición lógica. (Falso)**  
    *Desarrollo:* Es una oración interrogativa. Las oraciones exclamativas, preguntas o mandatos no son enunciados declarativos y no poseen un valor de verdad (Verdadero o Falso). Por lo tanto, no son proposiciones lógicas.

*   **q) “$25 - 11 < 0$” corresponde a una proposición lógica. (Verdadero)**  
    *Desarrollo:* Es un enunciado declarativo matemático que afirma una relación cuantitativa. Aunque es falsa ($14 < 0$ es falso), al poder asignársele un valor de verdad inequívoco, cumple formalmente con la definición de proposición.

*   **r) Existe una proposición lógica $p$ tal que $(p \land q)$ es siempre verdadera, sin importar el valor de verdad de $q$. (Falso)**  
    *Desarrollo:* Para que una conjunción $p \land q$ sea verdadera, ambos operandos deben ser verdaderos simultáneamente. Si $q$ toma el valor de verdad falso ($\mathbf{F}$), no existe ningún valor de $p$ que pueda hacer que la conjunción sea verdadera, ya que $\mathbf{T} \land \mathbf{F} \equiv \mathbf{F}$.

---

### 2. Formalización de Proposiciones con p y q
Definiciones de las variables proposicionales:
*   $p$: Conduces a más de 100 km por hora.
*   $q$: Te multan por exceso de velocidad.

*   **a) No conduces a más de 100 km por hora.**  
    *Formalización:* $\neg p$
*   **b) Conduces a más de 100 km por hora, pero no te multan por exceso de velocidad.**  
    *Formalización:* $p \land \neg q$  
    *(Nota: En lógica formal, el conector "pero" tiene la función semántica de una conjunción $\land$).*
*   **c) Te multarán por exceso de velocidad siempre que conduces a más de 100 km por hora.**  
    *Formalización:* $p \Rightarrow q$  
    *Explicación:* "Siempre que" introduce el antecedente o condición suficiente, de modo que $p$ implica $q$.
*   **d) Si no conduces a más de 100 km por hora no te multarán por exceso de velocidad.**  
    *Formalización:* $\neg p \Rightarrow \neg q$
*   **e) Conducir a más de 100 km por hora es suficiente para que te multen por exceso de velocidad.**  
    *Formalización:* $p \Rightarrow q$  
    *Explicación:* La condición "suficiente" define el antecedente de la implicación.
*   **f) Te multan por exceso de velocidad pero no conduces a más de 100 km por hora.**  
    *Formalización:* $q \land \neg p$
*   **g) Siempre que te multan por exceso de velocidad conduces a más de 100 km por hora.**  
    *Formalización:* $q \Rightarrow p$  
    *Explicación:* La frase "siempre que" introduce la condición antecedente, la cual en este caso es "te multan por exceso de velocidad" ($q$), por lo tanto $q$ implica $p$.

---

### 3. Formalización de Proposiciones Compuestas Complejas
*   **a) No es cierto que no me guste estudiar.**  
    *Definición:* $p$: Me gusta estudiar.  
    *Formalización:* $\neg(\neg p) \equiv p$ (Por ley de doble negación).
*   **b) José y Juan no son estudiosos.**  
    *Definición:* $p$: José es estudioso. $q$: Juan es estudioso.  
    *Formalización:* $\neg p \land \neg q$
*   **c) No es cierto que José y Juan son estudiosos.**  
    *Definición:* $p$: José es estudioso. $q$: Juan es estudioso.  
    *Formalización:* $\neg(p \land q)$  
    *(Nota: Por leyes de De Morgan, equivale a decir "José no es estudioso o Juan no es estudioso", $\neg p \lor \neg q$).*
*   **d) Es necesario lavar el coche del jefe para ascender.**  
    *Definición:* $p$: Ascender. $q$: Lavar el coche del jefe.  
    *Formalización:* $p \Rightarrow q$  
    *Explicación:* La condición "necesaria" siempre se coloca en el consecuente de la implicación.
*   **e) Viento del sur implica deshielo en primavera.**  
    *Definición:* $p$: Viento del sur. $q$: Deshielo en primavera.  
    *Formalización:* $p \Rightarrow q$
*   **f) Una condición suficiente para que la garantía sea válida (p) es que hayas comprado el ordenador hace menos de un año (q).**  
    *Formalización:* $q \Rightarrow p$  
    *Explicación:* Dado que "haber comprado el ordenador hace menos de un año" ($q$) es la condición suficiente, actúa como el antecedente de la implicación.
*   **g) A Guillermo siempre se le pilla cuando hace trampas.**  
    *Definición:* $p$: Se le pilla a Guillermo. $q$: Guillermo hace trampas.  
    *Formalización:* $q \Rightarrow p$  
    *Explicación:* "Cuando" funciona como condicional, estableciendo que hacer trampas es la condición que gatilla que lo pillen.
*   **h) Puedes acceder a la página web si pagas una cuota de suscripción.**  
    *Definición:* $p$: Puedes acceder a la página web. $q$: Pagas una cuota de suscripción.  
    *Formalización:* $q \Rightarrow p$  
    *Explicación:* La palabra "si" introduce la condición suficiente (antecedente).
*   **i) Ser elegido es consecuencia de conocer a la gente adecuada.**  
    *Definición:* $p$: Ser elegido. $q$: Conocer a la gente adecuada.  
    *Formalización:* $q \Rightarrow p$  
    *Explicación:* "Es consecuencia de" indica que $p$ es el resultado de la causa $q$, es decir, $q$ implica $p$.
*   **j) Para ganar el concurso es necesario y suficiente tener el número ganador.**  
    *Definición:* $p$: Ganar el concurso. $q$: Tener el número ganador.  
    *Formalización:* $p \iff q$
*   **k) El tren llega con retraso exactamente aquellos días que tengo que tomarlo.**  
    *Definición:* $p$: El tren llega con retraso. $q$: Tengo que tomar el tren.  
    *Formalización:* $p \iff q$  
    *Explicación:* "Exactamente aquellos días que" establece una relación bicondicional equivalente.

---

### 4. Deducción de Valor de Verdad con Condicional Falso
**Enunciado:** Si la proposición $p \Rightarrow q$ es falsa, determine el valor de verdad de la proposición compuesta:  
$$(p \lor q) \iff (q \land p)$$

**Desarrollo Paso a Paso:**
1.  Dado que $p \Rightarrow q \equiv \mathbf{F}$, deducimos por definición del condicional que:
    *   $p \equiv \mathbf{V}$
    *   $q \equiv \mathbf{F}$
2.  Sustituimos estos valores individuales en los términos del bicondicional:
    *   Término izquierdo: $(p \lor q) \equiv (\mathbf{V} \lor \mathbf{F}) \equiv \mathbf{V}$
    *   Término derecho: $(q \land p) \equiv (\mathbf{F} \land \mathbf{V}) \equiv \mathbf{F}$
3.  Evaluamos el conector central del bicondicional:
    $$\mathbf{V} \iff \mathbf{F} \equiv \mathbf{F}$$

**Conclusión:** La proposición compuesta es **Falsa**.

---

### 5. Deducción de Valor de Verdad con Conjunción Verdadera
**Enunciado:** Si la proposición $p \land q$ es verdadera, determine el valor de verdad de la proposición compuesta:  
$$(p \Rightarrow q) \iff (p \lor q)$$

**Desarrollo Paso a Paso:**
1.  Dado que $p \land q \equiv \mathbf{V}$, por definición de la conjunción deducimos de manera inequívoca que:
    *   $p \equiv \mathbf{V}$
    *   $q \equiv \mathbf{V}$
2.  Sustituimos en la expresión proposicional:
    *   Término izquierdo: $(p \Rightarrow q) \equiv (\mathbf{V} \Rightarrow \mathbf{V}) \equiv \mathbf{V}$
    *   Término derecho: $(p \lor q) \equiv (\mathbf{V} \lor \mathbf{V}) \equiv \mathbf{V}$
3.  Evaluamos el bicondicional:
    $$\mathbf{V} \iff \mathbf{V} \equiv \mathbf{V}$$

**Conclusión:** La proposición compuesta es **Verdadera**.

---

### 6. Demostración Formal sin usar Tablas de Verdad
> **Justificación Pedagógica:** Demostrar equivalencias lógicas utilizando álgebra proposicional consiste en simplificar el miembro izquierdo hasta transformarlo en el miembro derecho, justificando detalladamente cada paso mediante leyes lógicas axiomáticas.

*   **a) Demostrar: $(p \land \neg q) \Rightarrow r \equiv \neg p \lor (q \lor r)$**  
    *Demostración paso a paso:*
    1.  **Definición de Condicional:** Reescribimos la implicación principal $A \Rightarrow B \equiv \neg A \lor B$:  
        $$\equiv \neg(p \land \neg q) \lor r$$
    2.  **Ley de De Morgan:** Negamos la conjunción interior:  
        $$\equiv (\neg p \lor \neg(\neg q)) \lor r$$
    3.  **Ley de Doble Negación:** Simplificamos el término de la variable $q$:  
        $$\equiv (\neg p \lor q) \lor r$$
    4.  **Ley Asociativa de la Disyunción:** Agrupamos los elementos correspondientes al miembro derecho:  
        $$\equiv \neg p \lor (q \lor r)$$  
    *Queda demostrado formalmente.*

*   **b) Demostrar: $[(p \land q) \lor r] \land \neg q \equiv (r \land \neg q)$**  
    *Demostración paso a paso:*
    1.  **Ley Conmutativa:** Reorganizamos los términos de la conjunción:  
        $$\equiv \neg q \land [(p \land q) \lor r]$$
    2.  **Ley Distributiva:** Distribuimos la conjunción $\neg q \land$ sobre la disyunción interior:  
        $$\equiv (\neg q \land (p \land q)) \lor (\neg q \land r)$$
    3.  **Leyes Asociativa y Conmutativa:** Reagrupamos las variables semejantes en el primer paréntesis:  
        $$\equiv ((\neg q \land q) \land p) \lor (\neg q \land r)$$
    4.  **Ley de Contradicción:** Como un elemento y su negación no pueden coexistir bajo conjunción:  
        $$\equiv (\mathbf{F} \land p) \lor (\neg q \land r)$$
    5.  **Ley de Dominación:** La conjunción de cualquier término con una falsedad absoluta da falso:  
        $$\equiv \mathbf{F} \lor (\neg q \land r)$$
    6.  **Ley de Identidad:** La disyunción con una falsedad absoluta no altera el término:  
        $$\equiv \neg q \land r$$
    7.  **Ley Conmutativa:** Expresamos en el orden final requerido:  
        $$\equiv r \land \neg q$$  
    *Queda demostrado formalmente.*

*   **c) Demostrar: $p \Rightarrow [p \land \neg(q \lor r)] \equiv \neg p \lor (\neg q \land \neg r)$**  
    *Demostración paso a paso:*
    1.  **Definición de Condicional:** Reemplazamos la implicación principal:  
        $$\equiv \neg p \lor [p \land \neg(q \lor r)]$$
    2.  **Ley Distributiva:** Distribuimos la disyunción exterior sobre la conjunción interior:  
        $$\equiv (\neg p \lor p) \land (\neg p \lor \neg(q \lor r))$$
    3.  **Ley del Tercero Excluido:** Sabiendo que $p \lor \neg p$ es siempre una tautología:  
        $$\equiv \mathbf{V} \land (\neg p \lor \neg(q \lor r))$$
    4.  **Ley de Identidad:** La conjunción de una tautología con cualquier término equivale al término:  
        $$\equiv \neg p \lor \neg(q \lor r)$$
    5.  **Ley de De Morgan:** Aplicamos la negación en el segundo paréntesis para obtener la forma simplificada:  
        $$\equiv \neg p \lor (\neg q \land \neg r)$$  
    *Queda demostrado formalmente.*

---

### 7. Simplificación Algebraico-Formal de Proposiciones
*   **a) $p \land (q \land \neg p)$**  
    1.  $p \land (\neg p \land q)$ — *Ley Conmutativa*
    2.  $(p \land \neg p) \land q$ — *Ley Asociativa*
    3.  $\mathbf{F} \land q$ — *Ley de Contradicción*
    4.  $\mathbf{\mathbf{F}}$ — *Ley de Dominación*

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
    3.  $\mathbf{V} \lor q$ — *Ley del Tercero Excluido*
    4.  $\mathbf{\mathbf{V}}$ — *Ley de Dominación* (Tautología)

*   **e) $(q \Rightarrow p) \Rightarrow p$**  
    1.  $\neg(q \Rightarrow p) \lor p$ — *Definición de Implicación*
    2.  $\neg(\neg q \lor p) \lor p$ — *Definición de Implicación*
    3.  $(\neg\neg q \land \neg p) \lor p$ — *Ley de De Morgan*
    4.  $(q \land \neg p) \lor p$ — *Ley de Doble Negación*
    5.  $p \lor (q \land \neg p)$ — *Ley Conmutativa*
    6.  $(p \lor q) \land (p \lor \neg p)$ — *Ley Distributiva*
    7.  $(p \lor q) \land \mathbf{V}$ — *Ley del Tercero Excluido*
    8.  $\mathbf{p \lor q}$ — *Ley de Identidad*

*   **f) $(p \Rightarrow q) \Rightarrow p$**  
    1.  $\neg(p \Rightarrow q) \lor p$ — *Definición de Implicación*
    2.  $\neg(\neg p \lor q) \lor p$ — *Definición de Implicación*
    3.  $(\neg\neg p \land \neg q) \lor p$ — *Ley de De Morgan*
    4.  $(p \land \neg q) \lor p$ — *Ley de Doble Negación*
    5.  $\mathbf{p}$ — *Ley de Absorción*

*   **g) $p \land \neg(q \Rightarrow p)$**  
    1.  $p \land \neg(\neg q \lor p)$ — *Definición de Implicación*
    2.  $p \land (\neg\neg q \land \neg p)$ — *Ley de De Morgan*
    3.  $p \land (q \land \neg p)$ — *Ley de Doble Negación*
    4.  $p \land (\neg p \land q)$ — *Ley Conmutativa*
    5.  $(p \land \neg p) \land q$ — *Ley Asociativa*
    6.  $\mathbf{F} \land q$ — *Ley de Contradicción*
    7.  $\mathbf{\mathbf{F}}$ — *Ley de Dominación*

---

### 8. Valor de Verdad con Cuantificadores en $A = \{1, 2, 3, 4\}$
*   **a) $\forall x \in A : x + 3 < 6$ (Falso)**  
    *Desarrollo:* Evaluamos los elementos de $A$:
    - Para $x=3 \implies 3+3=6 \not< 6$. Se encuentra un contraejemplo, lo cual invalida la universalidad.

*   **b) $\forall x \in A : x^2 - 10 \le 8$ (Verdadero)**  
    *Desarrollo:* Evaluamos para el elemento más crítico (el más grande, $x=4$):  
    $$4^2 - 10 = 16 - 10 = 6 \le 8 \quad (\mathbf{V})$$  
    Dado que se cumple para el máximo, es directo verificar que para los demás valores menores se cumple holgadamente.

*   **c) $\exists x \in A : 2x^2 + x = 15$ (Falso)**  
    *Desarrollo:* Resolvemos la ecuación cuadrática en los reales:  
    $$2x^2 + x - 15 = 0 \implies (2x - 5)(x + 3) = 0 \implies x = \frac{5}{2} \lor x = -3$$  
    Ninguna de estas raíces pertenece al conjunto $A$. Por lo tanto, no existe tal elemento.

*   **d) $\exists x \in A : x^2 > 1 \Rightarrow x + 2 = 0$ (Verdadero)**  
    *Desarrollo:* Evaluamos la implicación con el elemento $x=1$:
    - Antecedente: $1^2 > 1 \equiv 1 > 1 \equiv \mathbf{F}$
    - Consecuente: $1 + 2 = 0 \equiv 3 = 0 \equiv \mathbf{F}$  
    Por definición de implicación, $\mathbf{F} \Rightarrow \mathbf{F} \equiv \mathbf{V}$. Dado que existe al menos un elemento que satisface el condicional, la proposición existencial es verdadera.

*   **e) $\exists! x \in A : x^2 > 1 \iff x + 2 = 0$ (Verdadero)**  
    *Desarrollo:* Evaluamos el bicondicional para cada elemento de $A$:
    - Para $x=1$: $1^2 > 1 \iff 1+2=0 \equiv \mathbf{F} \iff \mathbf{F} \equiv \mathbf{V}$ (Se cumple).
    - Para $x=2$: $4 > 1 \iff 4=0 \equiv \mathbf{V} \iff \mathbf{F} \equiv \mathbf{F}$ (No cumple).
    - Para $x=3$: $9 > 1 \iff 5=0 \equiv \mathbf{V} \iff \mathbf{F} \equiv \mathbf{F}$ (No cumple).
    - Para $x=4$: $16 > 1 \iff 6=0 \equiv \mathbf{V} \iff \mathbf{F} \equiv \mathbf{F}$ (No cumple).  
    El único elemento del conjunto $A$ que satisface la condición del bicondicional es $x=1$. Al ser único, el enunciado existencial único es verdadero.

---

### 9. Valor de Verdad con Cuantificadores en $A = \{0, 1, 2, 3, 4, 5\}$
*   **a) $\exists x \in A / x^2 = x$ (Verdadero)**  
    *Desarrollo:* Para $x=0$ o $x=1$ se cumple que $0^2 = 0$ y $1^2 = 1$. Ambos pertenecen a $A$.

*   **b) $\exists x \in A / \forall y \in A, xy \ge 0$ (Verdadero)**  
    *Desarrollo:* Si elegimos $x=0 \in A$, tenemos que $0 \cdot y = 0 \ge 0$ para todo $y \in A$. De hecho, dado que no hay números negativos en $A$, el producto de cualquier par de elementos es no negativo.

*   **c) $\forall x \in A, \exists y \in A / x + 2 = y$ (Falso)**  
    *Desarrollo:* Si tomamos $x=4 \in A$, requerimos que $y = 6 \in A$, pero $6 \notin A$. Lo mismo ocurre para $x=5$.

*   **d) $\exists x \in A / \forall y \in A, x + y$ es par. (Falso)**  
    *Desarrollo:* Para cualquier entero $x$ fijo, la suma $x+y$ alternará necesariamente entre par e impar a medida que $y$ varíe. Si elegimos $x$ par (ej. $2$), al tomar $y$ impar (ej. $1$), la suma es impar. Si elegimos $x$ impar, basta tomar $y$ par para que la suma sea impar.

---

### 10. Negación Formal de Proposiciones Cuantificadas
*   **a) $\exists x \in A / x^2 = x$**  
    *Negación:* $\forall x \in A, x^2 \neq x$
*   **b) $\forall x \exists y (x + y = 5 \Rightarrow y = -x)$**  
    *Negación:* $\exists x \forall y \neg(x + y = 5 \Rightarrow y = -x) \equiv \exists x \forall y (x + y = 5 \land y \neq -x)$  
    *(Nota: Se aplicó la negación del condicional, $\neg(A \Rightarrow B) \equiv A \land \neg B$).*
*   **c) $\forall x \forall y [(x + y \text{ es impar}) \Rightarrow (x \text{ es impar} \lor y \text{ es impar})]$**  
    *Negación:* $\exists x \exists y [(x + y \text{ es impar}) \land (x \text{ es par} \land y \text{ es par})]$
*   **d) $\exists x \forall y (x < y \land x^2 \ge y)$**  
    *Negación:* $\forall x \exists y \neg(x < y \land x^2 \ge y) \equiv \forall x \exists y (x \ge y \lor x^2 < y)$

---

## II. Selección Múltiple

### 1. Respuesta Correcta: C
*   **Enunciado:** Cuál proposición compuesta es una tautología (verdadera), conociendo las proposiciones simples $p$, $q$ y $r$:
    - $p$: "Una tautología puede ser falsa" ($\equiv \mathbf{F}$)
    - $q$: "2 es un número primo" ($\equiv \mathbf{V}$)
    - $r$: "$x > 5$ es una proposición simple" ($\equiv \mathbf{F}$)
*   **Desarrollo:** Evaluemos las alternativas con estos valores fijos:
    - **A)** $(p \lor q) \Rightarrow r \equiv (\mathbf{F} \lor \mathbf{V}) \Rightarrow \mathbf{F} \equiv \mathbf{V} \Rightarrow \mathbf{F} \equiv \mathbf{F}$.
    - **B)** $(\neg p \land q) \iff r \equiv (\mathbf{V} \land \mathbf{V}) \iff \mathbf{F} \equiv \mathbf{V} \iff \mathbf{F} \equiv \mathbf{F}$.
    - **C)** $(q \Rightarrow p) \Rightarrow r \equiv (\mathbf{V} \Rightarrow \mathbf{F}) \Rightarrow \mathbf{F} \equiv \mathbf{F} \Rightarrow \mathbf{F} \equiv \mathbf{V}$.  
    Por ende, el enunciado **C** se evalúa como una proposición verdadera.

### 2. Respuesta Correcta: A
*   **Enunciado:** Si la proposición $(p \land \neg q) \Rightarrow (r \Rightarrow \neg s)$ es falsa, el valor de verdad de $q, p, r, s$ en ese orden es:
*   **Desarrollo:** Para que una implicación sea falsa, es mandatorio que el antecedente sea verdadero y el consecuente falso:
    1.  Antecedente: $p \land \neg q \equiv \mathbf{V} \implies p \equiv \mathbf{V}$ y $\neg q \equiv \mathbf{V} \implies q \equiv \mathbf{F}$.
    2.  Consecuente: $r \Rightarrow \neg s \equiv \mathbf{F} \implies r \equiv \mathbf{V}$ y $\neg s \equiv \mathbf{F} \implies s \equiv \mathbf{V}$.
    3.  Orden solicitado $q, p, r, s$: **F, V, V, V** (que se corresponde con la opción A).

### 3. Respuesta Correcta: B
*   **Enunciado:** Si $p = \mathbf{V}, q = \mathbf{V}, r = \mathbf{F}, s = \mathbf{F}$. Deduzca el valor de verdad de las siguientes proposiciones compuestas:
    - i. $(\neg p \land \neg q) \lor \neg q$
    - ii. $(\neg r \lor q) \iff [(\neg q \lor r) \land s]$
    - iii. $(p \Rightarrow q) \Rightarrow [(p \lor q) \land \neg q]$
*   **Desarrollo:**
    - **i.** $(\neg\mathbf{V} \land \neg\mathbf{V}) \lor \neg\mathbf{V} \equiv (\mathbf{F} \land \mathbf{F}) \lor \mathbf{F} \equiv \mathbf{F} \lor \mathbf{F} \equiv \mathbf{F}$.
    - **ii.** $(\neg\mathbf{F} \lor \mathbf{V}) \iff [(\neg\mathbf{V} \lor \mathbf{F}) \land \mathbf{F}] \equiv (\mathbf{V} \lor \mathbf{V}) \iff [(\mathbf{F} \lor \mathbf{F}) \land \mathbf{F}] \equiv \mathbf{V} \iff [\mathbf{F} \land \mathbf{F}] \equiv \mathbf{V} \iff \mathbf{F} \equiv \mathbf{F}$.
    - **iii.** $(\mathbf{V} \Rightarrow \mathbf{V}) \Rightarrow [(\mathbf{V} \lor \mathbf{V}) \land \neg\mathbf{V}] \equiv \mathbf{V} \Rightarrow [\mathbf{V} \land \mathbf{F}] \equiv \mathbf{V} \Rightarrow \mathbf{F} \equiv \mathbf{F}$.
*   El trío de resultados es **F, F, F**, lo cual corresponde a la opción **B**.

### 4. Respuesta Correcta: C
*   **Enunciado:** Sea $A = \{1, 2, 3, 4, 5\}$, hallar el valor de verdad de los siguientes enunciados:
    - i. $(\forall x \in A)[(x + 3 < 10) \lor (x \text{ es par})]$
    - ii. $(\exists x \in A)(x^2 - 3x + 2 = 0)$
    - iii. $(\exists x \in A)[(x + 3 = 10) \land (x < 6)]$
*   **Desarrollo:**
    - **i.** Notemos que para el elemento más desfavorable, $x=5$, se tiene $5+3 = 8 < 10$ ($\mathbf{V}$). Dado que para todo $x \in A$ se cumple $x+3 < 10$, la primera disyuntiva es verdadera para todos. Por lo tanto, el enunciado universal es **Verdadero** ($\mathbf{V}$).
    - **ii.** Las soluciones de la ecuación cuadrática $x^2 - 3x + 2 = 0$ son $x=1$ y $x=2$. Dado que ambos números están en el conjunto $A$, el enunciado existencial es **Verdadero** ($\mathbf{V}$).
    - **iii.** La ecuación $x+3 = 10 \implies x = 7$. Sin embargo, $7 \notin A$. Por tanto, no existe ningún elemento en $A$ que cumpla con la primera condición de la conjunción. El enunciado es **Falso** ($\mathbf{F}$).
*   Los valores son **V, V, F**, correspondientes a la opción **C**.

### 5. Respuesta Correcta: C
*   **Enunciado:** La negación de la proposición $(p \Rightarrow q) \land (q \Rightarrow p)$ es:
*   **Desarrollo:** La proposición original representa la definición del bicondicional: $(p \iff q)$.
    1.  Negando la expresión por ley de De Morgan:  
        $$\neg[(p \Rightarrow q) \land (q \Rightarrow p)] \equiv \neg(p \Rightarrow q) \lor \neg(q \Rightarrow p)$$
    2.  Aplicando la regla de negación del condicional, $\neg(A \Rightarrow B) \equiv A \land \neg B$:  
        $$\equiv (p \land \neg q) \lor (q \land \neg p)$$  
    Esto corresponde exactamente con la alternativa **C** (y representa algebraicamente la disyunción exclusiva).

### 6. Respuesta Correcta: A
*   **Enunciado:** Si $s$ y la proposición $s \Rightarrow \neg(p \lor q)$ son verdaderas, indique los valores de verdad de las expresiones:
    - i. $\neg(p \land \neg q)$
    - ii. $(p \Rightarrow q) \lor \neg s$
    - iii. $s \lor (q \Rightarrow p)$
*   **Desarrollo:**
    1.  Dado que $s \equiv \mathbf{V}$ y $s \Rightarrow \neg(p \lor q) \equiv \mathbf{V}$, el consecuente debe ser verdadero: $\neg(p \lor q) \equiv \mathbf{V} \implies p \lor q \equiv \mathbf{F}$.
    2.  Para que una disyunción sea falsa, ambos términos son falsos: $p \equiv \mathbf{F}$ y $q \equiv \mathbf{F}$.
    3.  Ahora evaluamos cada caso:
        - **i.** $\neg(p \land \neg q) \equiv \neg(\mathbf{F} \land \neg\mathbf{F}) \equiv \neg(\mathbf{F} \land \mathbf{V}) \equiv \neg(\mathbf{F}) \equiv \mathbf{V}$.
        - **ii.** $(p \Rightarrow q) \lor \neg s \equiv (\mathbf{F} \Rightarrow \mathbf{F}) \lor \neg\mathbf{V} \equiv \mathbf{V} \lor \mathbf{F} \equiv \mathbf{V}$.
        - **iii.** $s \lor (q \Rightarrow p) \equiv \mathbf{V} \lor (\mathbf{F} \Rightarrow \mathbf{F}) \equiv \mathbf{V} \lor \mathbf{V} \equiv \mathbf{V}$.
*   Los tres valores de verdad son **V, V, V**, correspondientes a la opción **A**.

### 7. Respuesta Correcta: A
*   **Enunciado:** Si la proposición $(p \Rightarrow \neg q) \lor (\neg r \Rightarrow s)$ es falsa, el valor de verdad de $p, q, r, s$ en ese orden es:
*   **Desarrollo:** Una disyunción ($\lor$) es falsa únicamente cuando ambos miembros son falsos de forma simultánea:
    1.  Primer miembro: $p \Rightarrow \neg q \equiv \mathbf{F} \implies p \equiv \mathbf{V}$ y $\neg q \equiv \mathbf{F} \implies q \equiv \mathbf{V}$.
    2.  Segundo miembro: $\neg r \Rightarrow s \equiv \mathbf{F} \implies \neg r \equiv \mathbf{V} \implies r \equiv \mathbf{F}$ y $s \equiv \mathbf{F}$.
    3.  El orden solicitado $p, q, r, s$ es **V, V, F, F**, lo cual corresponde a la opción **A**.

### 8. Respuesta Correcta: A
*   **Enunciado:** Simbolización de la proposición compuesta: “Para estar saludable es suficiente comer sano y hacer deporte”, conociendo:
    - $p$: Hacer deporte
    - $q$: Comer sano
    - $r$: Estar saludable
*   **Desarrollo:** El enunciado establece una relación de suficiencia: "comer sano y hacer deporte" es la condición suficiente para "estar saludable".
    1.  La condición de suficiencia define de forma directa al antecedente de la implicación.
    2.  Antecedente (comer sano y hacer deporte): $q \land p$.
    3.  Consecuente (estar saludable): $r$.
    4.  Formalización final: $(q \land p) \Rightarrow r$. Esto corresponde a la opción **A**.
