---
title: Polinomios y Progresiones - Álgebra
origin: Notion
---

## **INFORMACIÓN RELEVANTE:**
— **Materia:** Álgebra Universitaria (Unidad 4).
— **Objetivo:** Estudio riguroso y profundo de polinomios, fracciones parciales, y progresiones aritméticas/geométricas.
— **Metodología:** Mapeo de conceptos teóricos complejos de la USS y la UdeC, enriquecido con ejercicios avanzados del listado práctico.

## **NOTAS:**
— **Rigor Matemático:** Todos los desarrollos teóricos y prácticos de este apunte prescinden estrictamente de conceptos infinitesimales (límites, derivadas, integrales).
— **Compatibilidad Notion:** Se han removido las ecuaciones inline con símbolo de dólar ($) debido a que el importador de Notion las rompe en múltiples líneas. Se utiliza tipografía matemática Unicode enriquecida (**𝕂, ℝ, ℂ, ℚ, ℤ, ℕ**, subíndices/superíndices y cursiva negrita) para el texto fluido, y bloques `$$` centrados para ecuaciones complejas, garantizando una importación perfecta y estética.

# Parte I: Teoría de Polinomios en una Variable

# 1. Definición y Estructura Algebraica

## Definición de Polinomio
— Sea **𝕂** un cuerpo (como los racionales **ℚ**, los reales **ℝ** o los complejos **ℂ**). Un **polinomio de una variable** con coeficientes en **𝕂** es una expresión formal de la forma:
$$p(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0$$
— Donde:
  * ***n*** ∈ **ℕ₀** es un entero no negativo.
  * ***x*** es una variable o indeterminada (símbolo formal).
  * ***aₖ*** ∈ **𝕂** son los **coeficientes** del polinomio.
  * Cada término ***aₖ xᵏ*** es un **monomio** de grado ***k***.
  * ***aₙ*** es el **coeficiente principal**. Si ***aₙ* = 1**, el polinomio se define como **mónico**.
  * ***a₀*** es el **término libre** o término constante.
— El conjunto de todos los polinomios en la variable ***x*** con coeficientes en el cuerpo **𝕂** se denota por **𝕂[x]**. 

## Estructura de Anillo Conmutativo
— Bajo las operaciones usuales de suma y producto, el conjunto **𝕂[x]** tiene estructura algebraica de **Anillo Conmutativo con Unidad**:
  - El elemento neutro aditivo es el **polinomio nulo** ***p(x)* = 0**.
  - El elemento neutro multiplicativo es el polinomio constante ***p(x)* = 1**.
  - **Importante:** **𝕂[x]** **no** es un cuerpo, ya que los únicos elementos con inverso multiplicativo en **𝕂[x]** son los polinomios constantes no nulos (los elementos del cuerpo de coeficientes **𝕂**). Los polinomios de grado ≥ 1 no tienen inverso multiplicativo dentro de **𝕂[x]**.

## Grado de un Polinomio
— Dado ***p(x)*** ∈ **𝕂[x]** tal que ***p(x)* ≠ 0**, el **grado** de ***p***, denotado por **gr(***p***)**, se define como el máximo exponente ***k*** tal que ***aₖ* ≠ 0**:
$$\text{gr}(p) = \max\{k \in \mathbb{N}_0 : a_k \neq 0\}$$
  - **Propiedad del producto:** **gr(***p* · *q***) = gr(***p***) + gr(***q***)**
  - **Propiedad de la suma:** **gr(***p* + *q***) ≤ max{gr(***p***), gr(***q***)}**
  - **Nota:** No se define grado para el polinomio nulo (***p(x)* = 0**).

## Igualdad de Polinomios
— Dos polinomios ***p(x)* = aₙ xⁿ + ... + a₀** y ***q(x)* = bₘ xᵐ + ... + b₀** son iguales si y solo si sus grados son idénticos y sus coeficientes homólogos son iguales uno a uno:
$$p(x) = q(x) \iff n = m \ \wedge \ \forall k \in \{0, \dots, n\}: a_k = b_k$$

— **Ejemplo de Aplicación (Igualdad):** Determinar ***A, B*** ∈ **ℝ** tales que:
$$(A + B)x^2 + 4x + 3 = 7x^2 + 4x + B$$
— Por definición de igualdad de polinomios, igualamos los coeficientes de igual grado:
$$ \begin{aligned} x^2: & \quad A + B = 7 \\ x^1: & \quad 4 = 4 \\ x^0: & \quad 3 = B \end{aligned} $$
— Sustituyendo ***B* = 3** en la primera ecuación:
$$ A + 3 = 7 \implies \color{red}A = 4 $$

## Función Polinomial: Dominio y Recorrido
— Todo polinomio ***p(x)*** ∈ **ℝ[x]** induce una **función polinomial** ***p* : ℝ → ℝ** mediante la regla de asignación de evaluar la indeterminada ***x*** en un número real.
— **Dominio:** **Dom(***p***) = ℝ**, ya que las operaciones de suma y multiplicación son cerradas y están definidas para cualquier número real.
— **Recorrido:** El conjunto imagen o recorrido **Rec(***p***)** está determinado algebraicamente por la paridad del grado:
  * Si **gr(***p***)** es **impar**: El recorrido es todo el conjunto real, es decir, **Rec(***p***) = ℝ**.
  * Si **gr(***p***)** es **par**: La función está acotada por un extremo global (máximo o mínimo) ***y₀*** ∈ **ℝ**.
    - Si ***aₙ* > 0**, entonces **Rec(***p***) = [y₀, +∞)**.
    - Si ***aₙ* < 0**, entonces **Rec(***p***) = (-∞, y₀]**.

---

# 2. Algoritmos de División

## Algoritmo de la División de Polinomios
— Sean ***p(x), d(x)*** ∈ **𝕂[x]** con ***d(x)* ≠ 0** (el divisor). Existen polinomios únicos ***c(x)*** (cociente) y ***r(x)*** (resto) en **𝕂[x]** tales que:
$$p(x) = c(x)d(x) + r(x)$$
— Donde ***r(x)* = 0** o bien **gr(***r***) < gr(***d***)**. Si ***r(x)* = 0**, se dice que ***p(x)*** es divisible por ***d(x)***.

## Regla de Ruffini (División Sintética)
— Método abreviado para dividir un polinomio ***p(x)*** por un divisor de la forma lineal mónico ***d(x)* = x - a**.

## **Caso Especial Avanzado (Divisor no Mónico):** ¿Cómo aplicar Ruffini si el divisor es de la forma ***s(x)* = cx - d**?
— Si deseamos dividir ***p(x)*** por ***s(x)* = 3x - 2**:
  1. Reescribimos el divisor factorizando el coeficiente principal:
     $$s(x) = 3\left(x - \frac{2}{3}\right)$$
  2. Aplicamos la regla de Ruffini usando la raíz ***a* = 2/3**, lo que produce un cociente intermedio ***c'(x)*** y un resto ***r***:
     $$p(x) = c'(x)\left(x - \frac{2}{3}\right) + r$$
  3. Reordenamos algebraicamente para recuperar el divisor original ***3x - 2***:
     $$p(x) = \frac{c'(x)}{3}(3x - 2) + r$$
  4. Por lo tanto, el cociente real es $\color{red}c(x) = \frac{c'(x)}{3}$ y el resto definitivo de la división es exactamente $\color{red}r$.

---

# 3. Teoremas de Raíces y Factorización

## Teorema del Resto
— El resto de dividir un polinomio ***p(x)*** ∈ **𝕂[x]** por el término lineal ***x - a*** es exactamente el valor de evaluar el polinomio en ***a***: ***r* = p(a)**.
— **Demostración:** Por el algoritmo de división:
$$p(x) = c(x)(x - a) + r \quad (\text{con } \text{gr}(r) < 1 \implies r \text{ es constante})$$
— Evaluando la función en ***x = a***:
$$p(a) = c(a)(a - a) + r = c(a) \cdot 0 + r = \color{red}r$$

## Teorema del Factor
— Un valor ***a*** ∈ **𝕂** es raíz de ***p(x)*** si y solo si el binomio ***x - a*** es un factor de ***p(x)*** (es decir, ***p(x)*** es divisible por ***x - a***).

## Teorema de las Raíces Racionales
— Sea ***p(x)* = aₙ xⁿ + ... + a₀** ∈ **ℤ[x]** un polinomio con **coeficientes enteros**. Si ***p/s*** ∈ **ℚ** es una raíz racional irreducible de ***p(x)*** (donde **mcd(***p*, *s***) = 1**), entonces:
  * El numerador ***p*** es un divisor entero del término constante ***a₀***.
  * El denominador ***s*** es un divisor entero del coeficiente principal ***aₙ***.

## **Estrategia para coeficientes racionales (ℚ[x]):**
— Si el polinomio original pertenece a **ℚ[x]** (ej. coeficientes fraccionarios), multiplicamos la ecuación ***p(x)* = 0** por el mínimo común múltiplo (m.c.m.) de todos los denominadores. Esto produce un polinomio equivalente en **ℤ[x]** con idénticas raíces, permitiendo aplicar directamente el Teorema de las Raíces Racionales.

## Cantidad Exacta de Raíces (Corolario del TFA)
— **Teorema Fundamental del Álgebra:** Todo polinomio no constante en **ℂ[x]** posee al menos una raíz en **ℂ**.
— **Corolario:** Todo polinomio ***p(x)*** ∈ **ℂ[x]** de grado ***n* ≥ 1** tiene exactamente ***n*** raíces complejas (contadas con su multiplicidad).

## **Demostración Analítica por Inducción Matemática:**
  * *Paso Base:* Para ***n* = 1**, el polinomio es de la forma ***p(x)* = a₁ x + a₀**. La ecuación ***a₁ x + a₀* = 0** posee como solución única ***x* = -a₀/a₁**, cumpliéndose que tiene exactamente ***1*** raíz.
  * *Paso Inductivo:* Supongamos como hipótesis de inducción (H.I.) que todo polinomio de grado ***k*** posee exactamente ***k*** raíces complejas (contando multiplicidades).
  * Sea ***p(x)*** un polinomio de grado ***k* + 1**. Por el Teorema Fundamental del Álgebra, ***p(x)*** posee al menos una raíz compleja, denotémosla por ***α*** ∈ **ℂ**.
  * Por el Teorema del Resto, ***p(x)*** es divisible por ***x - α***:
    $$p(x) = (x - \alpha) \cdot q(x)$$
  * Dado que **gr(***p***) = k + 1** y el factor lineal tiene grado 1, el cociente ***q(x)*** tiene grado ***k***.
  * Por la H.I., el polinomio ***q(x)*** posee exactamente ***k*** raíces en **ℂ**.
  * Por ende, sumando la raíz ***α***, el polinomio ***p(x)*** posee exactamente ***k* + 1** raíces en **ℂ**.
  * Por el Principio de Inducción Matemática, el corolario queda formalmente demostrado.

## Teorema de las Raíces Complejas Conjugadas
— Sea ***p(x)*** ∈ **ℝ[x]** un polinomio con coeficientes reales. Si ***z*** ∈ **ℂ** es raíz de ***p(x)***, entonces su conjugado ***z̄*** también es raíz de ***p(x)*** con la misma multiplicidad.
— **Demostración:** Sea $$p(z) = \sum_{k=0}^n a_k z^k = 0$$ Aplicando conjugación compleja a ambos lados:
$$\overline{p(z)} = \overline{0} \implies \overline{\sum_{k=0}^n a_k z^k} = 0$$
— Por propiedades del conjugado (distribuye sobre la suma y producto):
$$\sum_{k=0}^n \overline{a_k} (\overline{z})^k = 0$$
— Dado que los coeficientes son reales (***aₖ*** ∈ **ℝ**), se cumple que $$\overline{a_k} = a_k$$. Así:
$$\sum_{k=0}^n a_k (\overline{z})^k = 0 \implies p(\overline{z}) = 0$$

## Reducibilidad e Irreducibilidad
— Un polinomio ***p(x)*** ∈ **𝕂[x]** de grado ≥ 1 es **reducible** en **𝕂[x]** si existen ***g(x), h(x)*** ∈ **𝕂[x]** de grado ≥ 1 tales que ***p(x)* = g(x)h(x)**. Si no existen tales factores, es **irreducible**.
  * **Criterio para grado 2 o 3:** Un polinomio de grado 2 o 3 es reducible en **𝕂[x]** si y solo si posee al menos una raíz en el cuerpo **𝕂**.
  * **Corolarios en los Reales:**
    - Todo polinomio en **ℝ[x]** de grado impar posee al menos una raíz real.
    - Todo polinomio en **ℝ[x]** de grado ≥ 3 es reducible en **ℝ[x]**. Los únicos irreducibles en **ℝ[x]** son los lineales y los cuadráticos con discriminante negativo (**Δ < 0**).

---

# 4. Descomposición en Fracciones Parciales

— Permite descomponer una fracción racional propia ***P(x) / Q(x)*** (donde **gr(***P***) < gr(***Q***)**) en una suma de fracciones algebraicas más simples. Si es impropia (**gr(***P***) ≥ gr(***Q***)**), primero realizamos la división polinomial.

## Los Cuatro Casos de Descomposición

### Caso 1: Factores lineales no repetidos en el denominador
— Si ***Q(x) = (x - c₁)(x - c₂)...(x - cₙ)*** con todos los ***cₖ*** distintos:
$$\frac{P(x)}{Q(x)} = \frac{A_1}{x - c_1} + \frac{A_2}{x - c_2} + \dots + \frac{A_n}{x - c_n}$$

### Caso 2: Factores lineales repetidos
— Si un factor lineal se repite, por ejemplo ***(x - c)ᵐ***:
$$\frac{P(x)}{(x - c)^m} = \frac{A_1}{x - c} + \frac{A_2}{(x - c)^2} + \dots + \frac{A_m}{(x - c)^m}$$

### Caso 3: Factores cuadráticos irreducibles distintos
— Si ***Q(x)*** contiene factores cuadráticos de la forma ***ax² + bx + c*** con **Δ < 0**:
$$\frac{P(x)}{ax^2 + bx + c} = \frac{Ax + B}{ax^2 + bx + c}$$

### Caso 4: Factores cuadráticos irreducibles repetidos
— Si el factor cuadrático irreducible se repite ***s*** veces, ***(ax² + bx + c)ˢ***:
$$\frac{P(x)}{(ax^2 + bx + c)^s} = \frac{A_1 x + B_1}{ax^2 + bx + c} + \frac{A_2 x + B_2}{(ax^2 + bx + c)^2} + \dots + \frac{A_s x + B_s}{(ax^2 + bx + c)^s}$$

## **Ejemplo de Aplicación (Fracción Impropia y Caso 1):**
— Descomponer en fracciones parciales la siguiente expresión racional (Listado 10, Ejercicio 19b):
$$f(x) = \frac{x^4 - 3x^3 - 19x^2 + 4x + 18}{x^2 - 3x - 18}$$
— **Paso 1: División polinomial por ser fracción impropia** (ya que **4 ≥ 2**):
  - Dividimos ***x⁴ - 3x³ - 19x² + 4x + 18*** por ***x² - 3x - 18***:
    1. Termino principal: ***x⁴ : x² = x²***. Multiplicamos y restamos:
       $$(x^4 - 3x^3 - 19x^2 + 4x + 18) - x^2(x^2 - 3x - 18) = -x^2 + 4x + 18$$
    2. Siguiente término: ***-x² : x² = -1***. Multiplicamos y restamos:
       $$(-x^2 + 4x + 18) - (-1)(x^2 - 3x - 18) = \color{red}x$$
  - Obtenemos el cociente ***c(x) = x² - 1*** y el resto ***r(x) = x***. Por lo tanto:
    $$f(x) = x^2 - 1 + \frac{x}{x^2 - 3x - 18}$$

— **Paso 2: Factorizar el denominador de la fracción propia**
  - Buscamos las raíces de ***x² - 3x - 18 = 0***. Mediante factorización directa:
    $$x^2 - 3x - 18 = (x - 6)(x + 3)$$

— **Paso 3: Plantear la descomposición en fracciones parciales (Caso 1)**
  $$\frac{x}{(x-6)(x+3)} = \frac{A}{x-6} + \frac{B}{x+3}$$
  - Multiplicamos por el denominador común:
    $$x = A(x + 3) + B(x - 6)$$
  - Evaluamos en los valores críticos (raíces) para despejar las constantes:
    * Si ***x* = 6**:
      $$6 = A(6 + 3) + B(0) \implies 9A = 6 \implies A = \frac{2}{3}$$
    * Si ***x* = -3**:
      $$-3 = A(0) + B(-3 - 6) \implies -9B = -3 \implies B = \frac{1}{3}$$

— **Paso 4: Escribir el resultado final**
  $$f(x) = \color{red}x^2 - 1 + \frac{2/3}{x-6} + \frac{1/3}{x+3}$$

***

# Parte II: Progresiones y Series (Álgebra y Sucesiones)

— Una **sucesión** en **ℝ** es una función con dominio en los números naturales **ℕ** y recorrido en **ℝ**. La suma de los términos de una sucesión se define como una **serie**.

# 5. Sucesiones y Series Aritméticas

## Definición de Progresión Aritmética (P.A.)
— Una progresión aritmética es una sucesión de números reales en la cual la diferencia entre dos términos consecutivos es constante. Esta constante se denomina **diferencia común** (***d***):
$$a_k - a_{k-1} = d, \quad \forall k \ge 2$$
— **Término General (***aₖ***):** El término ***k***-ésimo de una P.A. está dado por:
$$a_k = a_1 + (k - 1)d, \quad \text{para } k \in \mathbb{N}$$

## Serie Aritmética (Suma de términos)
— La suma de los primeros ***n*** términos de una progresión aritmética (***Sₙ***) se calcula algebraicamente mediante:
$$S_n = \frac{n(a_1 + a_n)}{2}$$

— **Ejemplo de Aplicación:** Calcular la suma de los 100 primeros números naturales (1, 2, 3, ..., 100).
— Los números naturales forman una P.A. con primer término ***a₁* = 1**, diferencia ***d* = 1** y término centésimo ***a₁₀₀* = 100**.
— Aplicando la fórmula:
$$S_{100} = \frac{100(1 + 100)}{2} = 50 \cdot 101 = \color{red}5050$$

---

# 6. Sucesiones y Series Geométricas

## Definición de Progresión Geométrica (P.G.)
— Sucesión de números reales en la cual cada término se obtiene multiplicando el término anterior por una constante no nula denominada **razón común** (***r***):
$$\frac{a_k}{a_{k-1}} = r, \quad \forall k \ge 2$$
— **Término General (***aₖ***):** El término ***k***-ésimo de una P.G. está dado por:
$$a_k = a_1 \cdot r^{k-1}, \quad \text{para } k \in \mathbb{N}$$

## Serie Geométrica (Suma de términos)
— La suma de los primeros ***n*** términos de una progresión geométrica (***Sₙ***), con ***r* ≠ 1**, está dada algebraicamente por:
$$S_n = a_1 \frac{1 - r^n}{1 - r}$$

## **Ejemplo de Aplicación (PDF Unidad 4):**
— En una progresión geométrica, el tercer término es 1 y el sexto término es 27. Determinar la razón (***r***), el primer término (***a₁***) y la suma de los primeros seis términos (***S₆***).
— **Paso 1: Planteamiento de las ecuaciones**
  $$ \begin{aligned} a_3: & \quad a_1 \cdot r^2 = 1 \\ a_6: & \quad a_1 \cdot r^5 = 27 \end{aligned} $$

— **Paso 2: Resolver el sistema algebraico**
  - Dividimos la segunda ecuación por la primera:
    $$\frac{a_1 \cdot r^5}{a_1 \cdot r^2} = \frac{27}{1} \implies r^3 = 27 \implies \color{red}r = 3$$
  - Sustituimos ***r* = 3** en la primera ecuación para hallar ***a₁***:
    $$a_1 \cdot 3^2 = 1 \implies 9a_1 = 1 \implies \color{red}a_1 = \frac{1}{9}$$

— **Paso 3: Calcular la suma ***S₆*****
  - Aplicamos la fórmula con ***a₁* = 1/9**, ***r* = 3** y ***n* = 6**:
    $$S_6 = \frac{1}{9} \left( \frac{1 - 3^6}{1 - 3} \right) = \frac{1}{9} \left( \frac{1 - 729}{-2} \right) = \frac{1}{9} \left( \frac{-728}{-2} \right) = \frac{364}{9}$$
  - Operando el cociente de enteros:
    $$S_6 = \color{red}\frac{364}{9}$$
