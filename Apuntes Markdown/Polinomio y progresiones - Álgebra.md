--- 
title: Polinomio y progresiones - Álgebra
origin: Notion
---

## **INFORMACIÓN RELEVANTE:**

## NOTAS**:**

# Polinomios

— Dado un polinomio de variable *x*, sobre $\mathbb{K}$ (donde $\mathbb{K}$ = \R \lor $\mathbb{K}$ = \mathbb{C}), es una expresión de la forma:

$$p(x)=a_n  \cdot x^n + a_{n-1} \cdot x^{n-1} + \dots + a_1 \cdot x + a_0, n \in \N$$

- Do$n$de si $a_$n$ \$n$e 0$, se dice que $p(x)$ tie$n$e **grado** y está dado por $n$ (\text{gr}(p)=$n$).
- Donde $\mathbb{K}$, con variable x \in $\mathbb{K}$, se define como:
$$p(x)= \sum^{n}_{i=0} a_i \cdot x^i$$

- Donde, $\forall \, k= n : a_i \in \mathbb{K} \land n \in \N$
— Si $a_n \not= 0$, entonces, el polinomio tiene grado “*n*”.

— La notación: $$\mathbb{K}$_{[x]}$, se usa para denotar el conjunto de todos los polinomios en la variable *x* con coeficiente en $\mathbb{K}$.

— Dado $p(x) = cte \not=0$, también es polinomio y tiene grado 0.

# Teorema del resto

— El resto de dividir un polinomio $p(x) $ con otro de la forma $(x-a)$ es igual a $p(a)$

# Raíces de un polinomio

— Se define como raíz de un polinomio a $C \in \mathbb{K}$,  de un polinomio $p(x) \in \mathbb{K}$ si $p(c) = 0$

— **Observación**, $c \in \mathbb{K}$ es raíz de $$$p(x)$$ \iff (x-c)$ es factor de $$p(x)$$ , donde $$p(x)$$ se puede escribir como $$p(x)$$ = (x-2) \cdot h(x).

## Herramienta para encontrar raíces racionales

— Sea $p(x) = a_n \cdot x^n + \dots + a_0$ un polinomio con coeficientes $\in \Z$. Si $\frac{a}{b} \in \mathbb{Q}$, es irreductible es raíz de $p(x) \Longrightarrow a | a_0 \land b | a_n$

— Observar que, el teorema **solo entrega los posibles candidatos para ser una raíz**, además, **los posibles candidatos tienen la forma**: 

$$\frac{\text{Div}(a_0)}{\text{Div} (an)}$$

## Segunda herramienta

— Sea $$p(x)$, \text{con coeficientes en } \color{red} \R$, entonces, si $z$ es raí$z$ de *p*, implica que  \overline{$z$} también es raí$z$ de $p(x)$.

# Multiplicidad de una raíz

— Se define a $c \in \R$, como una raíz de multiplicidad si se repite más de 1 vez, donde se puede escribir como:

$$p(x) = (x-c)^k \cdot (s)$$

# Teorema fundamental del Álgebra

— Todo polinomio $p(x) \in \R_{[x]} \lor \in $\mathbb{C}$_{[x]}$ de grado $n \geq 0$, tiene exactamente n raíces en $\mathbb{C}$.

# Polinomios reducibles e irreducibles

— Un polinomio es irreductible cuando no se puede factorizar en el mundo que se está trabajando.

— Por otro lado, se dices que un polinomio es reductible si se puede factorizar en el mundo que se está trabajando.

# Función racional

— Dada una función *f*, de la forma: 

$$ f(x) = \frac{p(x)}{g(x)}, \, g (x) \ne0 $$

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

— Recordando, que, para que dos polinomios sean iguales, tiene que pasar que **deben tener mismo grado e índice. **

$$ A+B = 5 \\  6A-B+C = 15 \\ 9A-12B-4C = 7$$

— Luego, todo se basa en resolver el sistema de ecuaciones, donde, se debería llegar a que: 

$$A= 3 \\ B= 2 \\ C= -1$$

— Por último, la fracción racional quedaría expresada como: 

$$f(x) = \frac{3}{x+4} + \frac{2}{x+3} - \frac{1}{(x+3)^2}$$

### Caso 2, $gr(p(x)) \geq gr(g(x))$

— Primero, recordar que una fracción impropia se puede escribir como: 

$$\text{cociente }+ \frac{\text{resto}}{\text{divisor}}$$

- Donde la fracción $\frac{\text{resto}}{\text{divisor}}$, siempre será una fracción propia.
— Entonces, cuando se tenga una fracción impropia, se tienen que dividir los polinomios para generar una fracción propia.

— Por lo tanto, queda repetir el mismo procedimiento para una función propia.

