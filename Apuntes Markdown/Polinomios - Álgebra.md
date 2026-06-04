--- 
title: Polinomio y progresiones - Álgebra
origin: Notion
---

## **INFORMACIÓN RELEVANTE:**

## **NOTAS:**
— **Rigor Matemático:** Todos los desarrollos teóricos y prácticos de este apunte prescinden estrictamente de conceptos infinitesimales (límites, derivadas, integrales), fundamentándose de manera rigurosa en el álgebra clásica.
— **Compatibilidad Notion:** Para asegurar una visualización óptima en la importación de Notion (evitando que las fórmulas en línea se rompan en múltiples renglones), no se utiliza el símbolo de dólar ($) en el texto fluido. En su lugar, se emplea tipografía matemática en Unicode enriquecida y formato de negrita-cursiva (por ejemplo, **𝕂**, **ℝ**, **ℂ**, **ℚ**, **ℤ**, **ℕ**, **ℕ₀**, ***p(x)***, ***x***). Las ecuaciones principales y desarrollos extensos se presentan en bloques centrados con doble signo de dólar `$$` garantizando una legibilidad excelente.

# Polinomios

— Un **polinomio** de una variable ***x*** sobre un cuerpo **𝕂** (donde **𝕂** puede representar el cuerpo de los números racionales **ℚ**, reales **ℝ** o complejos **ℂ**) es una expresión formal de la forma:
$$p(x)=a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0$$
— O bien, denotado de forma compacta mediante sumatoria:
$$p(x)= \sum^{n}_{i=0} a_i x^i$$
— Donde:
* ***n*** ∈ **ℕ₀** (el conjunto de los números naturales incluyendo el cero) representa el índice superior.
* ***x*** es la indeterminada o variable formal (con ***x*** ∈ **𝕂**).
* ***aᵢ*** ∈ **𝕂** son los **coeficientes** del polinomio para cada ***i*** ∈ {0, ..., ***n***}.
* Cada término ***aᵢ xⁱ*** se denomina **monomio** de grado ***i***.
* ***aₙ*** es el **coeficiente principal**. Si ***aₙ*** = 1, el polinomio se define como **mónico**.
* ***a₀*** es el **término constante** o **libre**.
— Si el coeficiente principal ***aₙ*** ≠ 0, se dice que el polinomio ***p(x)*** tiene **grado** ***n***, denotado algebraicamente como ***gr(p) = n***.
— El conjunto de todos los polinomios en la variable ***x*** con coeficientes en el cuerpo **𝕂** se denota por la notación **𝕂[x]** (por ejemplo, **ℝ[x]** para coeficientes reales y **ℂ[x]** para coeficientes complejos).
— Dado un polinomio constante no nulo ***p(x) = c*** (con ***c*** ∈ **𝕂** y ***c*** ≠ 0), este corresponde a un polinomio de grado 0. El polinomio nulo ***p(x) = 0*** no tiene grado definido en esta estructura.

— **Estructura algebraica de Anillo Conmutativo:**
* Bajo las operaciones usuales de adición y multiplicación de polinomios, el conjunto **𝕂[x]** posee una estructura de **Anillo Conmutativo con Elemento Unidad**.
* El elemento neutro aditivo es el polinomio nulo ***p(x) = 0***.
* El elemento neutro multiplicativo es el polinomio constante ***p(x) = 1***.
* **Importante:** El conjunto **𝕂[x]** **no** es un cuerpo, ya que los únicos elementos que admiten inverso multiplicativo en **𝕂[x]** son los polinomios constantes no nulos (los elementos del cuerpo **𝕂**). Los polinomios de grado ***gr(p)*** ≥ 1 carecen de inverso dentro del anillo.

— **Propiedades del Grado:**
* ***gr(p · q) = gr(p) + gr(q)***
* ***gr(p + q) ≤ max{gr(p), gr(q)}***

— **Igualdad de Polinomios:**
* Dos polinomios ***p(x) = aₙ xⁿ + ... + a₀*** y ***q(x) = bₘ xᵐ + ... + b₀*** en **𝕂[x]** son idénticos si y solo si poseen el mismo grado y sus coeficientes correspondientes son iguales uno a uno:
$$p(x) = q(x) \iff n = m \ \wedge \ \forall i \in \{0, \dots, n\}: a_i = b_i$$
* *Ejemplo práctico:* Determinar los valores de ***A*** y ***B*** en **ℝ** tales que:
$$(A + B)x^2 + 4x + 3 = 7x^2 + 4x + B$$
* Igualando los coeficientes de igual grado en ambos lados:
$$ \begin{aligned} x^2: & \quad A + B = 7 \\ x^1: & \quad 4 = 4 \\ x^0: & \quad 3 = B \end{aligned} $$
* Sustituyendo ***B = 3*** en la primera ecuación:
$$A + 3 = 7 \implies A = 4$$

— **Función Polinomial: Dominio y Recorrido**
* Todo polinomio ***p(x)*** ∈ **ℝ[x]** define una **función polinomial** ***p* : ℝ → ℝ** a través de la evaluación de la variable ***x*** en el conjunto real.
* **Dominio:** ***Dom(p) = ℝ***, dado que las operaciones polinomiales (suma y producto) están siempre bien definidas para todo elemento del conjunto de los números reales.
* **Recorrido:** El recorrido de la función, ***Rec(p)***, se define algebraicamente según la paridad de su grado:
  * Si ***gr(p)*** es **impar**: El recorrido cubre a todos los números reales, es decir, ***Rec(p) = ℝ***.
  * Si ***gr(p)*** es **par**: La función está acotada por un valor extremo global (mínimo o máximo absoluto) ***y₀*** ∈ **ℝ**.
    - Si ***aₙ > 0***: El recorrido es ***Rec(p) = [y₀, +∞)***.
    - Si ***aₙ < 0***: El recorrido es ***Rec(p) = (-∞, y₀]***.

# Teorema del resto

— **Algoritmo de la División de Polinomios:**
Sean ***p(x)*** y ***d(x)*** dos polinomios en **𝕂[x]** con ***d(x)*** ≠ 0 (el divisor). Existen polinomios únicos ***c(x)*** (cociente) y ***r(x)*** (resto) en **𝕂[x]** tales que:
$$p(x) = c(x) \cdot d(x) + r(x)$$
Donde ***r(x) = 0*** o bien ***gr(r) < gr(d)***. En el caso en que el resto ***r(x) = 0***, se dice que ***p(x)*** es divisible por ***d(x)***.

— **Enunciado del Teorema del Resto:**
El resto de la división de un polinomio ***p(x)*** ∈ **𝕂[x]** por un polinomio lineal de la forma ***x - a*** (donde ***a*** ∈ **𝕂**) es exactamente igual al valor obtenido al evaluar el polinomio en ***a***, es decir, ***r = p(a)***.

— **Demostración Analítica:**
De acuerdo con el algoritmo de división, al dividir ***p(x)*** por el divisor lineal ***x - a***, se tiene:
$$p(x) = c(x) \cdot (x - a) + r(x)$$
Dado que el divisor ***x - a*** tiene grado 1, el resto ***r(x)*** debe tener grado estrictamente menor que 1 o ser el polinomio nulo. Por consiguiente, el resto es un término constante ***r*** ∈ **𝕂**. Evaluando la ecuación en ***x = a***:
$$p(a) = c(a) \cdot (a - a) + r = c(a) \cdot 0 + r = r$$
Por tanto, el residuo de la división es exactamente ***r = p(a)***.

— **División Sintética (Regla de Ruffini):**
Es un algoritmo simplificado y eficiente para calcular de forma práctica el cociente y el resto al dividir un polinomio ***p(x)*** por un binomio de la forma mónico-lineal ***x - a***.

— **Caso Especial Avanzado (Divisor no Mónico):**
En situaciones donde el divisor lineal tiene la forma ***s(x) = cx - d*** (con ***c*** ≠ 1), la división sintética no se puede aplicar de forma directa. Para ello, se emplea el siguiente método algebraico:
1. Reestructuramos el divisor factorizando su coeficiente principal:
   $$s(x) = c \left(x - \frac{d}{c}\right)$$
2. Aplicamos la regla de Ruffini utilizando la raíz del divisor, ***a = d/c***. Esto produce un cociente intermedio ***c'(x)*** y un resto constante ***r***:
   $$p(x) = c'(x) \left(x - \frac{d}{c}\right) + r$$
3. Reordenamos algebraicamente el producto para recuperar el divisor original ***cx - d***:
   $$p(x) = \frac{c'(x)}{c} \cdot c \left(x - \frac{d}{c}\right) + r = \frac{c'(x)}{c} (cx - d) + r$$
4. De este modo, concluimos que el cociente verdadero de la división es ***c(x) = c'(x) / c***, mientras que el resto definitivo es exactamente ***r*** (permaneciendo inalterado).

# Raíces de un polinomio

— **Definición de Raíz:**
Se define formalmente como raíz (o cero) de un polinomio ***p(x)*** ∈ **𝕂[x]** a todo elemento ***c*** ∈ **𝕂** tal que al evaluar la función polinomial en ese punto se anula, es decir:
$$p(c) = 0$$

— **Observación (Teorema del Factor):**
Un elemento ***c*** ∈ **𝕂** es raíz de ***p(x)*** si y solo si el binomio lineal ***(x - c)*** es un factor de ***p(x)***. Bajo esta circunstancia, el polinomio ***p(x)*** se puede escribir en la forma factorizada:
$$p(x) = (x - c) \cdot h(x)$$
Donde ***h(x)*** ∈ **𝕂[x]** es un polinomio de grado ***gr(p) - 1***.
* *Demostración:* Si ***c*** es raíz de ***p(x)***, entonces ***p(c) = 0***. Por el Teorema del Resto, al dividir ***p(x)*** por ***x - c*** obtenemos un residuo constante ***r = p(c) = 0***, lo que implica que ***p(x) = (x - c) · h(x)***, demostrando la factorización. Recíprocamente, si ***p(x) = (x - c) · h(x)***, evaluar en ***x = c*** da ***p(c) = (c - c) · h(c) = 0***, confirmando que ***c*** es raíz.

## Herramienta para encontrar raíces racionales

— **Teorema de las Raíces Racionales:**
Sea ***p(x) = aₙ xⁿ + aₙ₋₁ xⁿ⁻¹ + ... + a₁ x + a₀*** un polinomio con **coeficientes enteros** (***aᵢ*** ∈ **ℤ**). Si la fracción racional irreducible ***a/b*** ∈ **ℚ** (con ***mcd(a, b) = 1***) es raíz del polinomio ***p(x)***, entonces se cumplen las siguientes relaciones divisibilidad algebraicas:
* El numerador ***a*** divide de forma exacta al término constante ***a₀*** (***a | a₀***).
* El denominador ***b*** divide de forma exacta al coeficiente principal ***aₙ*** (***b | aₙ***).

— **Importante:** Este teorema no determina directamente las raíces, sino que **solo proporciona los candidatos posibles** para ser raíces racionales del polinomio. Los candidatos se construyen mediante el cociente de los divisores correspondientes:
$$\pm \frac{\text{Divisores de } a_0}{\text{Divisores de } a_n}$$

— **Estrategia para coeficientes racionales (ℚ[x]):**
Si el polinomio original posee coeficientes fraccionarios, se puede multiplicar la ecuación completa ***p(x) = 0*** por el mínimo común múltiplo (m.c.m.) de todos los denominadores. Esto da lugar a un polinomio equivalente con coeficientes enteros (perteneciente a **ℤ[x]**) con las mismas raíces exactas, permitiendo aplicar el teorema.

— **Ejemplo de Aplicación:**
Determinar las raíces racionales de ***p(x) = 2x³ - 3x² + 2x - 3***:
1. Identificamos los coeficientes extremos: el término libre es ***a₀ = -3*** y el coeficiente principal es ***a₃ = 2***.
2. Los divisores enteros correspondientes son:
   * Divisores de ***a₀*** (candidatos a numerador ***a***): {±1, ±3}
   * Divisores de ***a₃*** (candidatos a denominador ***b***): {±1, ±2}
3. Construimos el conjunto de posibles raíces racionales ***a/b***:
   $$\left\{ \pm 1, \pm 3, \pm \frac{1}{2}, \pm \frac{3}{2} \right\}$$
4. Evaluamos estos candidatos en ***p(x)***:
   * ***p(1) = 2(1)³ - 3(1)² + 2(1) - 3 = 2 - 3 + 2 - 3 = -2 ≠ 0***
   * ***p(3/2) = 2(27/8) - 3(9/4) + 2(3/2) - 3 = 27/4 - 27/4 + 3 - 3 = 0***
   Comprobamos que ***x = 3/2*** es una raíz racional del polinomio.

## Segunda herramienta

— **Teorema de las Raíces Complejas Conjugadas:**
Sea ***p(x)*** ∈ **ℝ[x]** un polinomio con **coeficientes reales**. Si el número complejo ***z*** ∈ **ℂ** es raíz de ***p(x)***, entonces su conjugado ***z̄*** también es raíz del polinomio ***p(x)*** con idéntica multiplicidad.

— **Demostración Analítica:**
Asumiendo que ***z*** es raíz de ***p(x)***, tenemos la igualdad:
$$p(z) = \sum_{k=0}^{n} a_k z^k = 0$$
Aplicando la operación de conjugación compleja a ambos miembros de la ecuación:
$$\overline{p(z)} = \overline{0} \implies \overline{\sum_{k=0}^{n} a_k z^k} = 0$$
Por las propiedades algebraicas del conjugado complejo (el cual distribuye sobre la suma y el producto):
$$\sum_{k=0}^{n} \overline{a_k} (\overline{z})^k = 0$$
Dado que los coeficientes son números reales (***aₖ*** ∈ **ℝ**), sus conjugados son idénticos a los coeficientes originales (***āₖ = aₖ***). Esto nos permite simplificar la expresión a:
$$\sum_{k=0}^{n} a_k (\overline{z})^k = 0 \implies p(\overline{z}) = 0$$
Demostrando rigurosamente que ***z̄*** es también raíz de ***p(x)***.

# Multiplicidad de una raíz

— **Definición de Multiplicidad:**
Un elemento ***c*** ∈ **𝕂** es una raíz de **multiplicidad** ***k*** (donde ***k*** ∈ **ℕ**) de un polinomio ***p(x)*** ∈ **𝕂[x]** si el factor ***(x - c)ᵏ*** divide exactamente a ***p(x)***, pero ***(x - c)ᵏ⁺¹*** no lo divide. Esto equivale a escribir la factorización del polinomio como:
$$p(x) = (x - c)^k \cdot s(x)$$
Donde ***s(x)*** ∈ **𝕂[x]** es un polinomio tal que ***s(c)*** ≠ 0.
* Si ***k*** = 1, la raíz se denomina **raíz simple**.
* Si ***k*** = 2, la raíz se denomina **raíz doble** o de multiplicidad 2.
* Si ***k*** > 1, la raíz se denomina **raíz múltiple**.

— **Ejemplo de Aplicación:**
Sea el polinomio en **ℝ[x]**:
$$p(x) = (x - 1)(x - 2)^3(x^2 + 1)$$
* El valor ***x = 1*** es una raíz simple (multiplicidad 1), ya que ***p(x) = (x - 1) · s₁(x)*** donde ***s₁(1) = (1 - 2)³(1² + 1) = -2 ≠ 0***.
* El valor ***x = 2*** es una raíz de multiplicidad 3 (raíz triple), ya que ***p(x) = (x - 2)³ · s₂(x)*** donde ***s₂(2) = (2 - 1)(2² + 1) = 5 ≠ 0***.
* El factor cuadrático ***x² + 1*** no aporta raíces reales en **ℝ** (sus raíces complejas son ***i*** y ***-i***, ambas de multiplicidad 1 en **ℂ**).

# Teorema fundamental del Álgebra

— **Enunciado del Teorema Fundamental del Álgebra (TFA):**
Todo polinomio no constante ***p(x)*** ∈ **ℂ[x]** (es decir, de grado ***n*** ≥ 1) tiene al menos una raíz en el cuerpo de los números complejos **ℂ**.

— **Corolario de Cantidad Exacta de Raíces:**
Todo polinomio ***p(x)*** ∈ **ℂ[x]** de grado ***n*** ≥ 1 posee exactamente ***n*** raíces complejas, contadas con su multiplicidad.

— **Demostración Analítica por Inducción Matemática:**
Procedemos a demostrar la validez del corolario anterior mediante inducción matemática sobre el grado ***n*** del polinomio:
* **Paso Base:** Para ***n = 1***, el polinomio tiene la forma ***p(x) = a₁ x + a₀*** (con ***a₁*** ≠ 0). La ecuación lineal ***a₁ x + a₀ = 0*** tiene una única raíz en **ℂ**, dada por ***x = -a₀/a₁***, de modo que posee exactamente 1 raíz.
* **Paso Inductivo:** Supongamos como hipótesis de inducción (H.I.) que todo polinomio de grado ***k*** (con ***k*** ≥ 1) posee exactamente ***k*** raíces complejas (contando multiplicidades).
* Consideremos ahora un polinomio ***p(x)*** de grado ***k + 1***.
* Por el Teorema Fundamental del Álgebra, sabemos que ***p(x)*** posee por lo menos una raíz en **ℂ**, la cual denotamos como ***α***.
* Por el Teorema del Factor, podemos expresar al polinomio como:
  $$p(x) = (x - \alpha) \cdot q(x)$$
* Dado que el factor lineal tiene grado 1, el polinomio cociente ***q(x)*** debe tener grado ***k*** (ya que ***gr(p) = gr(x - α) + gr(q) ⇒ k + 1 = 1 + gr(q) ⇒ gr(q) = k***).
* Aplicando la H.I. al cociente ***q(x)*** de grado ***k***, este posee exactamente ***k*** raíces en **ℂ**.
* Al incorporar el factor lineal ***(x - α)***, el polinomio completo ***p(x)*** cuenta con exactamente ***k + 1*** raíces complejas.
* Por consiguiente, en virtud del principio de inducción, queda demostrado que todo polinomio de grado ***n*** tiene exactamente ***n*** raíces en **ℂ**.

— **Regla de los Signos de Descartes:**
Es una herramienta útil para estimar la naturaleza real de las raíces de un polinomio con coeficientes reales:
* El número de **raíces reales positivas** es igual al número de variaciones de signo en los coeficientes del polinomio ***p(x)*** (omitiendo los coeficientes nulos), o menor que este en una cantidad par.
* El número de **raíces reales negativas** se analiza de igual manera a través de los cambios de signo en los coeficientes del polinomio evaluado en su variable opuesta, ***p(-x)***.

# Polinomios reducibles e irreducibles

— **Definiciones Algebraicas:**
* Un polinomio no constante ***p(x)*** ∈ **𝕂[x]** es **reducible** en **𝕂[x]** si existen dos polinomios ***g(x)***, ***h(x)*** ∈ **𝕂[x]**, ambos de grado mayor o igual a 1 (y menores que ***gr(p)***), tales que:
  $$p(x) = g(x) \cdot h(x)$$
* Un polinomio no constante ***p(x)*** ∈ **𝕂[x]** es **irreducible** en **𝕂[x]** si no puede descomponerse en el producto de dos polinomios no constantes de menor grado. En este caso, sus únicos factores son los elementos constantes y los múltiplos del propio polinomio.
* Todo polinomio lineal (grado 1) es intrínsecamente irreducible en cualquier cuerpo **𝕂**.

— **Propiedades según el Cuerpo de Coeficientes:**
La reducibilidad de una expresión depende exclusivamente del conjunto numérico en el que se realice la factorización (el cuerpo **𝕂**):
* **En el cuerpo complejo ℂ:**
  Los únicos polinomios irreducibles en **ℂ[x]** son los lineales (grado 1). Cualquier polinomio de grado ***n*** ≥ 2 es reducible bajo este cuerpo.
* **En el cuerpo real ℝ:**
  Los únicos polinomios irreducibles en **ℝ[x]** son:
  1. Los polinomios de grado 1.
  2. Los polinomios de grado 2 (cuadráticos) cuyo discriminante es negativo (***Δ = b² - 4ac < 0***).
  Todo polinomio en **ℝ[x]** de grado impar tiene al menos una raíz real, y cualquier polinomio de grado ***n*** ≥ 3 es reducible en **ℝ[x]**.
* **Criterio de Reducibilidad para Grados 2 y 3:**
  Un polinomio de grado 2 o 3 es reducible en **𝕂[x]** si y solo si posee al menos una raíz en **𝕂**.
* **Caso de Grado Mayor o Igual a 4:**
  Carecer de raíces reales en polinomios de grado 4 o superior no es condición suficiente para asegurar la irreducibilidad de la expresión.
  * *Ejemplo Demostrativo:* Analizar el polinomio ***p(x) = x⁴ + 3x² + 2*** en **ℝ[x]**.
    - La ecuación cuadrática correspondiente (realizando la sustitución ***u = x²***) se factoriza como:
      $$u^2 + 3u + 2 = (u + 1)(u + 2)$$
    - Deshaciendo la sustitución, obtenemos:
      $$p(x) = (x^2 + 1)(x^2 + 2)$$
    - Aunque los factores de grado 2, ***x² + 1*** y ***x² + 2***, no poseen raíces reales (por lo que ***p(x)*** carece de raíces reales), el polinomio original es reducible en **ℝ[x]** dado que se ha factorizado en dos polinomios de grado 2.

# Función racional

— Una **función racional** ***f*** es una función real cuya regla de asignación matemática se compone de la división o cociente de dos expresiones polinomiales:
$$f(x) = \frac{p(x)}{g(x)}$$
— Donde ***p(x)*** y ***g(x)*** son polinomios con coeficientes reales (***p(x)***, ***g(x)*** ∈ **ℝ[x]**) y ***g(x)*** no corresponde al polinomio nulo.

— **Dominio de una Función Racional:**
El dominio está constituido por todos los números reales exceptuando aquellos valores que anulan algebraicamente el denominador:
$$\text{Dom}(f) = \{x \in \mathbb{R} : g(x) \neq 0\}$$

— **Descomposición en Fracciones Parciales:**
Consiste en descomponer una fracción racional en una suma de fracciones con denominadores más simples. Para efectuar la descomposición, se debe clasificar la fracción según la relación de grados:
* **Fracción Propia:** Cuando el grado del numerador es estrictamente menor al grado del denominador, es decir, ***gr(p) < gr(g)***. La descomposición se plantea directamente.
* **Fracción Impropia:** Cuando el grado del numerador es mayor o igual al del denominador, es decir, ***gr(p) ≥ gr(g)***. En este caso, se realiza una división polinomial previa.

## Descomposición de fracciones

### Caso 1, gr(p(x)) < gr(g(x))

— Cuando la función racional es una fracción propia, el método consiste en factorizar el denominador ***g(x)*** en polinomios irreducibles reales (factores lineales y factores cuadráticos con discriminante negativo). Dependiendo de las raíces del denominador, se asocian términos a la descomposición general:

1. **Factores lineales distintos:**
   Si ***g(x)*** contiene un factor de la forma ***(x - c)*** con multiplicidad 1, se asocia una fracción simple:
   $$\frac{A}{x - c}$$

2. **Factores lineales repetidos:**
   Si ***g(x)*** contiene un factor de la forma ***(x - c)ᵐ*** con multiplicidad ***m*** > 1, se asocia una suma de ***m*** fracciones parciales consecutivas:
   $$\frac{A_1}{x - c} + \frac{A_2}{(x - c)^2} + \dots + \frac{A_m}{(x - c)^m}$$

3. **Factores cuadráticos irreducibles distintos:**
   Si ***g(x)*** contiene un factor cuadrático ***ax² + bx + d*** (con ***Δ < 0***) de multiplicidad 1, se asocia la fracción:
   $$\frac{Ax + B}{ax^2 + bx + d}$$

4. **Factores cuadráticos irreducibles repetidos:**
   Si ***g(x)*** contiene un factor cuadrático ***(ax² + bx + d)ˢ*** (con ***Δ < 0***) con multiplicidad ***s*** > 1, se asocia una suma de ***s*** fracciones:
   $$\frac{A_1 x + B_1}{ax^2 + bx + d} + \frac{A_2 x + B_2}{(ax^2 + bx + d)^2} + \dots + \frac{A_s x + B_s}{(ax^2 + bx + d)^s}$$

— **Ejemplo Desarrollado (Factores Lineales Simples y Repetidos):**
Descomponer en fracciones parciales la función propia:
$$f(x) = \frac{5x^2 +15x+7}{(x-4)(x+3)^2}$$
* **Paso 1: Planteamiento de la descomposición.**
  Como el denominador contiene el factor lineal simple ***(x - 4)*** y el factor lineal repetido ***(x + 3)²***, planteamos:
  $$\frac{5x^2 +15x+7}{(x-4)(x+3)^2} = \frac{A}{x-4} + \frac{B}{x+3} + \frac{C}{(x+3)^2}$$
* **Paso 2: Eliminación de denominadores.**
  Multiplicando por el mínimo común denominador ***(x - 4)(x + 3)²*** obtenemos la igualdad polinomial:
  $$5x^2 +15x+7 = A(x+3)^2 + B(x+3)(x-4) + C(x-4)$$
* **Paso 3: Obtención de las constantes.**
  * **Método de los Valores Críticos (Evaluación):**
    Evaluamos en las raíces reales para simplificar la obtención de las incógnitas:
    - Evaluando en ***x = 4***:
      $$5(4)^2 + 15(4) + 7 = A(4 + 3)^2 + B(0) + C(0) \implies 147 = 49A \implies A = 3$$
    - Evaluando en ***x = -3***:
      $$5(-3)^2 + 15(-3) + 7 = A(0) + B(0) + C(-3 - 4) \implies 7 = -7C \implies C = -1$$
    - Evaluando en ***x = 0*** (utilizando los valores conocidos ***A = 3*** y ***C = -1***):
      $$7 = 3(3)^2 + B(3)(-4) + (-1)(-4)$$
      $$7 = 27 - 12B + 4 \implies 7 = 31 - 12B \implies 12B = 24 \implies B = 2$$
  * **Método de Igualación de Coeficientes:**
    Expandiendo algebraicamente los polinomios del miembro derecho:
    $$5x^2 +15x+7 = A(x^2 + 6x + 9) + B(x^2 - x - 12) + C(x - 4)$$
    $$5x^2 +15x+7 = (A + B)x^2 + (6A - B + C)x + (9A - 12B - 4C)$$
    Igualando coeficientes homólogos se obtiene el sistema lineal de 3x3:
    $$ \begin{aligned} A + B &= 5 \\ 6A - B + C &= 15 \\ 9A - 12B - 4C &= 7 \end{aligned} $$
    Resolviendo el sistema se determinan exactamente los mismos valores: ***A = 3***, ***B = 2***, ***C = -1***.
* **Paso 4: Expresión de la descomposición final.**
  Sustituyendo las constantes obtenidas:
  $$f(x) = \frac{3}{x-4} + \frac{2}{x+3} - \frac{1}{(x+3)^2}$$

### Caso 2, gr(p(x)) >= gr(g(x))

— Si la fracción racional es impropia, es decir, el grado del numerador es mayor o igual al grado del denominador, se realiza primero la división de polinomios para expresar la fracción en términos de una componente entera (cociente) y una fracción racional propia (resto dividido por divisor):
$$\frac{p(x)}{g(x)} = \text{cociente}(x) + \frac{\text{resto}(x)}{g(x)}$$
— Donde la fracción restante es siempre propia. A partir de allí, se procede a descomponer la fracción propia aplicando los criterios del Caso 1.

— **Ejemplo Desarrollado Paso a Paso (Fracción Impropia):**
Descomponer en fracciones parciales la siguiente expresión:
$$f(x) = \frac{x^4 - 3x^3 - 19x^2 + 4x + 18}{x^2 - 3x - 18}$$
* **Paso 1: Realizar la división polinomial.**
  Dividimos el polinomio del numerador por el del denominador:
  1. Dividiendo los términos de mayor exponente: ***x⁴ / x² = x²***. Multiplicamos y restamos del dividendo:
     $$(x^4 - 3x^3 - 19x^2 + 4x + 18) - (x^4 - 3x^3 - 18x^2) = -x^2 + 4x + 18$$
  2. Siguiente cociente de términos principales: ***-x² / x² = -1***. Multiplicamos y restamos:
     $$(-x^2 + 4x + 18) - (-x^2 + 3x + 18) = x$$
  Obtenemos el cociente ***c(x) = x² - 1*** y el resto ***r(x) = x***. Por lo tanto, reescribimos:
  $$f(x) = x^2 - 1 + \frac{x}{x^2 - 3x - 18}$$
* **Paso 2: Factorizar el denominador de la fracción propia.**
  Factorizamos el polinomio del denominador mediante inspección directa de raíces:
  $$x^2 - 3x - 18 = (x - 6)(x + 3)$$
* **Paso 3: Plantear la descomposición de la fracción propia.**
  Planteamos la descomposición asociada a factores lineales distintos:
  $$\frac{x}{(x-6)(x+3)} = \frac{A}{x-6} + \frac{B}{x+3}$$
  Multiplicando por el denominador común:
  $$x = A(x + 3) + B(x - 6)$$
  Evaluamos en los valores críticos del sistema:
  - Para ***x = 6***:
    $$6 = 9A \implies A = \frac{2}{3}$$
  - Para ***x = -3***:
    $$-3 = -9B \implies B = \frac{1}{3}$$
* **Paso 4: Expresar la solución completa.**
  Sustituyendo el cociente de la división y la descomposición obtenida:
  $$f(x) = x^2 - 1 + \frac{2/3}{x-6} + \frac{1/3}{x+3}$$
