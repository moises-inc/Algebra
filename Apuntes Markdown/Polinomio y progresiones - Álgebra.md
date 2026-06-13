---
id: "20260605-polinomio-y-progresiones-lgebra"
title: "Polinomio y progresiones - Álgebra"
project: "Estudios_Universidad"
date: "2026-06-05T11:30:00"
last_modified: "2026-06-05T11:30:00"
type: "academic-note"
status: "in-progress"
priority: "medium"
tags: ["#status/in-progress", "#project/Estudios_Universidad", "#course/lgebra"]
---

## **INFORMACIÓN RELEVANTE:**

## NOTAS**:**

# Polinomios

— Dado un polinomio de variable *x*, sobre $\mathbb{K}$ (donde $\mathbb{K}$ = \R \lor $\mathbb{K}$ = \mathbb{C}), es una expresión de la forma:

$$p(x)=a_n  \cdot x^n + a_{n-1} \cdot x^{n-1} + \dots + a_1 \cdot x + a_0, n \in \N$$

- Do$n$de si $a_$n$ \$n$e 0$, se dice que $p(x)$ tie$n$e **grado** y está dado por $n$ (\text{gr}(p)=$n$).
- Donde $\mathbb{K}$, con variable x \in $\mathbb{K}$, se define como:
$$p(x)= \sum^{n}_{i=0} a_i \cdot x^i$$

— Donde:

- ***$n ∈ ℕ₀$*** (el conjunto de los números naturales incluyendo el cero) representa el índice superior.
- ***$x$*** es la indeterminada o variable formal (con $x$ ∈ 𝕂).
- ***$aᵢ ∈ 𝕂$*** son los **coeficientes** del polinomio para cada $i ∈ {0, ..., n}$.
- Cada término ***aᵢ xⁱ*** se denomina **monomio** de grado $i.$
- ***$aₙ$*** es el **coeficiente principal**. Si $aₙ$ = 1, el polinomio se define como **mónico**.
- ***$a₀$*** es el **término constante** o **libre**.
— Si el coeficiente principal $aₙ ≠ 0$, se dice que el polinomio ***p(x)*** tiene **grado** ***n***, denotado algebraicamente como $gr(p) = n.$

— La notación: $$\mathbb{K}$_{[x]}$, se usa para denotar el conjunto de todos los polinomios en la variable *x* con coeficiente en $\mathbb{K}$.

— Dado $p(x) = cte \not=0$, también es polinomio y tiene grado 0.

$$p(x)=a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0$$

$$p(x)= \sum^{n}_{i=0} a_i x^i$$

# Teorema del resto

— El resto de dividir un polinomio $p(x)$ con otro de la forma $(x-a)$ es igual a $p(a)$.

## **Algoritmo de la División de Polinomios**

— Sean ***$p(x) $***y ***$d(x)$*** dos polinomios en **$$𝕂[x]$$** con ***$d(x)$ ≠ 0*** (el divisor). Existen polinomios únicos ***$c(x)$*** (cociente) y ***$r(x)$*** (resto) en **$$𝕂[x]$$** tales que:

$$p(x) = c(x) \cdot d(x) + r(x)$$

- Donde ***$r(x) = 0$*** o bien ***$gr(r) < gr(d)$***. 
## **Enunciado del Teorema del Resto**

— El resto de l$a$ división de un polinomio ***$p(x) ∈ 𝕂[x]$*** por un polinomio line$a$l de l$a$ form$a$ ***$x - $a$$*** (donde ***$$a$ ∈ 𝕂$***) es ex$a$ct$a$mente igu$a$l $a$l v$a$lor obtenido $a$l ev$a$lu$a$r el polinomio en ***$a$***, es decir, r = p($a$).

### **Demostración Analítica**

— De acuerdo con el algoritmo de división, al dividir ***$p(x)$*** por el divisor lineal ***$x - a,$*** se tiene:

$$p(x) = c(x) \cdot (x - a) + r(x)$$

— Dado que el divisor ***$x - a$*** tiene grado 1, el resto ***$r(x)$*** debe tener grado estrictamente menor que 1 o ser el polinomio nulo. Por consiguiente, el resto es un término constante ***$r ∈ 𝕂.$*** Evaluando la ecuación en ***x = a***:

$$p(a) = c(a) \cdot (a - a) + r \\ = c(a) \cdot 0 + r = r$$

— Por tanto, el residuo de la división es exactamente$ r = p(a)$.

## **División Sintética (Regla de Ruffini)**

— Es un algoritmo simplificado y eficiente para calcular de forma práctica el cociente y el resto al dividir un polinomio ***$p(x)$*** por un binomio de la forma mónico-lineal ***$x - a.$***

### **Caso Especial Avanzado (Divisor no Mónico):**

— En situaciones donde el divisor lineal tiene la forma ***$s(x) = cx - d (con c ≠ 1)$***, la división sintética no se puede aplicar de forma directa. Para ello, se emplea el siguiente método algebraico:

1. Reestructuramos el divisor factorizando su coeficiente principal:
1. Aplicamos la regla de Ruffini utilizando la raíz del divisor, ***a = d/c***. Esto produce un cociente intermedio ***c'(x)*** y un resto constante ***r***:
1. Reordenamos algebraicamente el producto para recuperar el divisor original ***cx - d***:
1. De este modo, concluimos que el cociente verdadero de la división es ***c(x) = c'(x) / c***, mientras que el resto definitivo es exactamente ***r*** (permaneciendo inalterado).
# Raíces de un polinomio

— Se define como raíz de un polinomio a $C \in \mathbb{K}$,  de un polinomio $p(x) \in \mathbb{K}$ si $p(c) = 0$

— **Observación**, $c \in \mathbb{K}$ es raíz de $$$p(x)$$ \iff (x-c)$ es factor de $$p(x)$$ , donde $$p(x)$$ se puede escribir como $$p(x)$$ = (x-2) \cdot h(x).

## Herramienta para encontrar raíces racionales

— Sea $p(x) = a_n \cdot x^n + \dots + a_0$ un polinomio con coeficientes $\in \Z$. Si $\frac{a}{b} \in \mathbb{Q}$, es irreductible es raíz de $p(x) \Longrightarrow a | a_0 \land b | a_n$

— Observar que, el teorema **solo entrega los posibles candidatos para ser una raíz**, además, **los posibles candidatos tienen la forma**: 

$$\frac{\text{Div}(a_0)}{\text{Div} (an)}$$

## **Estrategia para coeficientes racionales ****$(ℚ[x])$**

— Si el polinomio original posee coeficientes fraccionarios, se puede multiplicar la ecuación completa ***$p(x) = 0$*** por el mínimo común múltiplo (m.c.m.) de todos los denominadores. Esto da lugar a un polinomio equivalente con coeficientes enteros (perteneciente a **$ℤ[x]$**) con las mismas raíces exactas, permitiendo aplicar el teorema.

### **Ejemplo de Aplicación**

— Determinar las raíces racionales de ***$p(x) = 2x³ - 3x² + 2x - 3$***:

1. Identificamos los coeficientes extremos: el término libre es ***a₀ = -3*** y el coeficiente principal es ***a₃ = 2***.
1. Los divisores enteros correspondientes son:
1. Construimos el conjunto de posibles raíces racionales ***a/b:\left\{ \pm 1, \pm 3, \pm \frac{1}{2}, \pm \frac{3}{2} \right\}***
1. Evaluamos estos candidatos en ***p(x)***:
— Comprobamos que ***$x = 3/2$*** es una raíz racional del polinomio.

## Segunda herramienta

— Sea $$p(x)$, \text{con coeficientes en } \color{red} \R$, entonces, si $z$ es raí$z$ de *p*, implica que  \overline{$z$} también es raí$z$ de $p(x)$.

# Multiplicidad de una raíz

— Se define a $c \in \R$, como una raíz de multiplicidad si se repite más de 1 vez, donde se puede escribir como:

$$p(x) = (x-c)^k \cdot s(x)$$

— Donde ***$s(x) ∈ 𝕂[x]$*** es un polinomio tal que ***$s(c) ≠ 0$***.

## **Ejemplo de Aplicación**

— Sea el polinomio en **$ℝ[x]$**:

$$p(x) = (x - 1)(x - 2)^3(x^2 + 1)$$

- El valor ***$x = 1$*** es una raíz simple (multiplicidad 1), ya que ***$p(x) = (x - 1) · s₁(x)$*** donde ***$s₁(1) = (1 - 2)³(1² + 1) = -2 ≠ 0.$***
- El valor ***$x = 2$*** es una raíz de multiplicidad 3 (raíz triple), ya que ***$p(x) = (x - 2)³ · s₂(x)$*** donde ***$s₂(2) = (2 - 1)(2² + 1) = 5 ≠ 0$***.
- El factor cuadrát$$i$$co ***$x² + 1$*** no aporta raíces reales en **$ℝ$** (sus raíces complejas son ***$$i$$*** y ***$$i$$***, ambas de mult$$i$$pl$$i$$c$$i$$dad 1 en **$ℂ$**).
# Teorema fundamental del Álgebra

— Todo polinomio $p(x) \in \R_{[x]} \lor \in $\mathbb{C}$_{[x]}$ de grado $n \geq 0$, tiene exactamente n raíces en $\mathbb{C}$.

# Polinomios reducibles e irreducibles

— Un polinomio es irreductible cuando no se puede factorizar en el mundo que se está trabajando.

— Por otro lado, se dices que un polinomio es reductible si se puede factorizar en el mundo que se está trabajando.

# Función racional

— Dada una función *f*, de la forma: 

$$f(x) = \frac{p(x)}{g(x)}, \, g (x) \ne0 $$

— Se llama función racional, donde *p*(*x*) y *g*(*x*) son polinomios $\in \R$. 

— Además, cuando: 

— La idea de la descomposición es, por ejemplo: 

$$f(x) = \frac{5x+7}{x^2+x-20} = \frac{5x+7}{(x+5)(x-4)} = \color{red} \frac{2}{x+5} + \frac{3}{x-4}$$

— La idea se basa en descomponer fracciones a formas “más simples”.

## Descomposición de fracciones

### Caso 1, $gr(p(x)) < gr(g(x))$

— Para el primer caso, la idea que se busca es que, dado una función racional, $f(x)$, descomponerla en tantas en suma de fracciones como polinomios en el denominador (siempre factorizados en $\R[x]$), en decir: 

- Ejemplos: 
— Dado: 

$$f(x) = \frac{5x^2 +15x+7}{(x-4)(x+3)^2} = \frac{A}{(x-4)} + \frac{B}{(x+3)} + \frac{C}{(x+3)^2}$$

— Si se multiplica todo por el denominador, $(x-4)(x+3)^2$, se tiene que:

$$5x^2 +15x+7 = A(x+3)^2+B(x+3)(x-4)+C(x-4)$$

— Resolviendo el lado derecho y luego agrupando según grados se tiene que:

$$5x^2 +15x+7 = (A+B)x^2+(6A - B+C)x+(9A-12B-4C)$$

$$A+B = 5 \\  6A-B+C = 15 \\ 9A-12B-4C = 7$$

[[Álgebra]]

---
🔗 [[Álgebra]]


