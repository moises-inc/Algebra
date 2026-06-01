---
id: "20260524-nmeros-complejos-lgenra"
title: "Números complejos - Álgenra"
project: "Estudios_Universidad"
date: "2026-05-24T12:29:05"
last_modified: "2026-05-30T19:03:58"
type: "academic-note"
status: "completed"
priority: "medium"
tags: ["#status/completed", "#project/Estudios_Universidad", "#course/lgebra"]
---

## **INFORMACIÓN RELEVANTE:**

## NOTAS**:**

# Números complejos

— Se llama unidad imaginaria, denotada por i, al símbolo que cumple

$$i²=-1$$

- Donde $i$, se llama un$i$dad $i$mag$i$nar$i$a.
— Así, se pueden satisfacer ecuaciones que no tengan solución en los $\R$. Además, se puede construir el conjunto:

$$\mathbb{C} = \{  a+bi:a,b\in\R \land i²=-1 \} \\\R \subseteq \mathbb{C}$$

- Donde ***a*** se llama parte real y $b \cdot i$ parte imaginaria.
- Además, se define como $z=a+bi $ como **forma binomial**.
## Conjugado de un número complejo

— Dado el número complejo *z*, su conjugado está definido por $\overline{z} =a-bi$

— Se tiene las siguientes propiedades:

# Representación geometría de un complejo

## Plano complejo

## Forma polar (o trigonométrica) de un complejo

— Luego, el número complejo se puede representar como: 

$$z= a+bi = |z| \cos \Phi + |z|\sin \Phi \\ = |z|(\cos \Phi + i\sin \Phi)  \\ =|z| \cdot\text{cis } \Phi$$

- Recordando que: 
- Además, notar que el valor de $\Phi$ se puede sacar por:
— Por lo tanto, se define como $\color{red} \text{cis } \Phi$ a $\color{red} \cos \Phi + i\sin \Phi$

### Argumento de *z*.

— El ángulo $\Phi$, se llama argumento de *z* (número complejo) y se denota como $\Phi$ = \arg (z). 

— Sin embargo, dada la periodicidad de las funciones $\sin \land \cos$, el $\arg (z)$ puede tomar infinitos valores dados por:

$$\arg(z) = \Phi +2k\pi, k \in \Z$$

— Por otro lado, para evitar infinitas soluciones, se restringe el valor de $\Phi $  al intervalo $[0, 2\pi[$, donde dicho intervalo se llamará argumento principal de *z*, denotado por $\color{red}   \text{Arg}(z)$.

# Operaciones entre complejos

## Operaciones entre complejos dada su forma binomial

— Dado dos números complejos en su forma binomial, $z_1 = a+bi \land z_2 = c+di$, se definen las siguientes operaciones:

### Suma y resta de complejos

$$z_1\pm z_2=(a+bi) \pm (c+di)= (a\pm c)+(b \pm d)i$$

- “Parte real con parte real y parte imaginaria con parte imaginaria”.
- Ejemplo:
$$\text{Dado } z_1 = 3-2i \land 5+3i \\ z_1 + z_2 = (3+5) + (-2+3)i \\ \therefore z_1 + z_2 = 8+i$$

$$z_1 \times z_2= (a+bi)(c+di)=(ac-bd)+(ad+bc)i$$

### Multiplicación entre complejos

— Notar que además los números complejos son un campo no ordenado.

### Inverso multiplicativo de un complejo

— Dado  $z (z\ne 0) = a+bi$, el inverso multiplicativo de $z, z^{-1}$, se debería cumplir que $z\cdot z^{-1}= 1$.

— Donde el inverso de *z*, está dado por: 

$$z^{-1}= \frac{a}{a²+b²} - \frac{bi}{a²+b²}$$

— Donde, además, se comprueba que:

$$z^{-1} = \frac1z= \frac{1}{a+bi} \cdot \frac{a-bi}{a-bi} = \frac{a-bi}{a²+b²} = \frac{a}{a²+b²} - \frac{b}{a²+b²}$$

- **Observar** que $a-bi $ se llama conjugado de *z* y se denota por $ \overline{z}$. 
### División de complejos

— Dado $z_1, z_2 \in \mathbb{C}, \land \, z_2 \ne 0$, se define división de complejos como:

$$\frac{z_1}{z_2} :=z_1 \cdot z_2^{-1} \iff z_1 \cdot \overline{z_2}$$

## Potenc$i$as de $i$

— Las potenc$i$as de $i$ están dadas por:

## Operaciones entre complejos dada su forma polar

— Dado dos complejos no nulos, en su forma polar, definidos como:

$$z=|z| (\cos\Phi + i \sin \Phi) \\ w = |w|(\cos \alpha + \sin \alpha)$$

### Multiplicación entre complejos

— La multiplicación entre *z* y *w* está dada por:

$$z \cdot w = |z \cdot w| \cdot[\cos(\Phi + \alpha) + i \sin (\Phi + \alpha) ]$$

- Donde:
### División entre complejos

— Por otra parte, la división de *z* y *w*, está dada por: 

$$\frac{z}{w} = \left | \frac{z}{w} \right | [\cos (\Phi - \alpha) + i \sin (\Phi - \alpha)]$$

- Recordando: 
## Potencias de un complejo

### Teorema De Moivre

— Para todo complejo de la forma $z = |z| \cdot \text{cis } \Phi$ y para cada $n \in \N$, se tiene que:

$$z^n=|z|^n \cdot \text{cis} (n \cdot \Phi)$$

— Ejemplo: 

$$\text{Primero, calcular } |z| \\ |z| = \sqrt{(\sqrt{3})^2 + (1)²} \\ = 2$$

$$\text{Luego, dado la } \tan \Phi = \frac{1}{\sqrt{3}} , \text{ se tiene que } \Phi = \frac{\pi}{6}$$

$$\text{Así, } z = 2 \cdot \text{cis} \frac{\pi}{6}$$

$$\text{Por De Moivre, se tiene que } \\ z^{8} = 2^{8} \cdot \text{cis} \left ( 8 \cdot \frac{\pi}{6}  \right ) \\ = 256 \cdot \text{cis} \left( \frac{4 \pi}{3}\right) \\ = 256 \cdot \left[ \cos \left( \frac{4 \pi}{3}\right) + i \sin \left( \frac{4 \pi}{3}\right) \right] \\ = 256 \cdot \left( -\frac{1}{2} - \frac{\sqrt{3}}{2} i \right) \\ \color{red} = - 128 - 128 \cdot \sqrt{3} i $$