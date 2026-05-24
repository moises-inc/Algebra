# Resolución Formal de Ejercicios Clave: Listado 5 - Álgebra
**Asignatura:** Álgebra (DCEX0007)  
**Materia:** Lógica Proposicional y Teoría de Conjuntos  
**Resolución:** Gemini Academic Assistant  

---

## Introducción Conceptual
Esta guía contiene las resoluciones detalladas paso a paso de los dos ejercicios teóricos y de demostración más importantes del **Listado 5**. Cada paso está acompañado de su correspondiente **Justificación Pedagógica** y de la explicitación de los teoremas y leyes de la lógica y la teoría de conjuntos que validan rigurosamente el desarrollo, alineándose con el estándar académico del curso.

---

## Parte I: Lógica Proposicional

### Ejercicio 1: Simplificación de Proposiciones Compuestas
**Enunciado:** Simplifique la siguiente proposición utilizando leyes de la lógica y demuestre si corresponde a una tautología, contradicción o contingencia:
$$[(p \rightarrow q) \land \neg q] \rightarrow \neg p$$

#### Justificación Pedagógica:
El condicional ($A \rightarrow B$) se puede reescribir lógicamente en términos de disyunción y negación ($\neg A \lor B$). Para simplificar la expresión completa, deconstruiremos el antecedente y aplicaremos leyes distributivas, de contradicción y de absorción lógicas para simplificar de adentro hacia afuera, demostrando de manera analítica el valor de verdad final sin necesidad de recurrir a tablas de verdad.

#### Desarrollo Formal Paso a Paso:
Queremos simplificar la expresión:  
$$E \equiv [(p \rightarrow q) \land \neg q] \rightarrow \neg p$$

1.  **Definición de Condicional:** Reemplazamos la implicación interna del antecedente $p \rightarrow q \equiv \neg p \lor q$:
    $$E \equiv [(\neg p \lor q) \land \neg q] \rightarrow \neg p$$

2.  **Ley Distributiva:** Distribuimos la conjunción exterior $\land \neg q$ sobre los elementos de la disyunción inclusiva interna:
    $$E \equiv [(\neg p \land \neg q) \lor (q \land \neg q)] \rightarrow \neg p$$

3.  **Ley de Contradicción:** Sabiendo que una proposición y su negación no pueden ser verdaderas simultáneamente, la expresión $q \land \neg q$ equivale a una falsedad absoluta ($\mathbf{F}$):
    $$E \equiv [(\neg p \land \neg q) \lor \mathbf{F}] \rightarrow \neg p$$

4.  **Ley de Identidad:** La disyunción de cualquier expresión con una falsedad absoluta equivale a la misma expresión original ($A \lor \mathbf{F} \equiv A$):
    $$E \equiv (\neg p \land \neg q) \rightarrow \neg p$$

5.  **Definición de Condicional (Principal):** Reescribimos la implicación principal usando la regla $A \rightarrow B \equiv \neg A \lor B$:
    $$E \equiv \neg(\neg p \land \neg q) \lor \neg p$$

6.  **Ley de De Morgan:** Aplicamos la negación sobre el producto lógico (conjunción) interior, lo que cambia la conjunción a disyunción e invierte el estado de cada proposición simple:
    $$E \equiv (\neg\neg p \lor \neg\neg q) \lor \neg p$$

7.  **Ley de Doble Negación:** La negación de una negación es lógicamente equivalente a la afirmación original ($\neg\neg A \equiv A$):
    $$E \equiv (p \lor q) \lor \neg p$$

8.  **Leyes Asociativa y Conmutativa:** Reorganizamos los términos de la disyunción para agrupar variables semejantes:
    $$E \equiv (p \lor \neg p) \lor q$$

9.  **Ley del Tercero Excluido:** Una proposición o bien es verdadera o bien es falsa, por lo que la disyunción $p \lor \neg p$ siempre equivale a una verdad absoluta o tautología ($\mathbf{V}$):
    $$E \equiv \mathbf{V} \lor q$$

10. **Ley de Dominación:** Dado que la disyunción inclusiva requiere que al menos uno de sus componentes sea verdadero para ser verdadera, la presencia de una tautología domina y simplifica todo el término:
    $$E \equiv \mathbf{V}$$

#### Conclusión:
La proposición original $[(p \rightarrow q) \land \neg q] \rightarrow \neg p$ se reduce a una verdad absoluta ($\mathbf{V}$). Por lo tanto, queda formalmente demostrado que es una **Tautología** (también conocida como la regla de inferencia del *Modus Tollendo Tollens*).

---

## Parte II: Teoría de Conjuntos

### Ejercicio 2: Demostración Formal de Igualdad de Conjuntos
**Enunciado:** Demuestre formalmente utilizando lógica de pertenencia y leyes de conjuntos la siguiente igualdad de conjuntos (Leyes de De Morgan para Conjuntos):
$$A \setminus (B \cup C) = (A \setminus B) \cap (A \setminus C)$$

#### Justificación Pedagógica:
Para demostrar la igualdad de dos conjuntos, se debe probar que un elemento genérico $x$ pertenece al conjunto del miembro izquierdo si y solo si pertenece al conjunto del miembro derecho ($x \in \text{MI} \iff x \in \text{MD}$). Traduciremos la pertenencia de conjuntos a conectores de la lógica proposicional clásica, resolveremos la simplificación mediante leyes lógicas y revertiremos el proceso de vuelta a la notación de conjuntos.

#### Desarrollo Formal Paso a Paso:
Sea $x$ un elemento arbitrario del universo de discurso.

1.  **Definición de pertenencia en la diferencia de conjuntos:**  
    Por definición, la diferencia de conjuntos $X \setminus Y = \{x : x \in X \land x \notin Y\}$. Aplicado a nuestro miembro izquierdo:
    $$x \in A \setminus (B \cup C) \iff x \in A \land x \notin (B \cup C)$$

2.  **Negación de pertenencia en una unión:**  
    Sabemos que la unión se define mediante una disyunción ($x \in B \cup C \iff x \in B \lor x \in C$). Por ende, la no pertenencia corresponde a negar dicha disyunción:
    $$\iff x \in A \land \neg(x \in B \lor x \in C)$$

3.  **Ley de De Morgan (Lógica):**  
    Aplicando la equivalencia lógica $\neg(p \lor q) \equiv \neg p \land \neg q$ sobre el miembro derecho de nuestra conjunción:
    $$\iff x \in A \land (x \notin B \land x \notin C)$$

4.  **Ley de Idempotencia y Asociatividad de la Conjunción:**  
    Por idempotencia, la proposición simple $x \in A$ equivale lógicamente a $(x \in A \land x \in A)$. Reemplazamos y reorganizamos los términos mediante asociatividad:
    $$\iff (x \in A \land x \in A) \land (x \notin B \land x \notin C)$$
    $$\iff (x \in A \land x \notin B) \land (x \in A \land x \notin C)$$

5.  **Definición de diferencia de conjuntos (en sentido inverso):**  
    Traducimos la conjunción de pertenencia y no pertenencia en cada uno de los paréntesis de vuelta a la notación clásica de diferencia:
    $$\iff x \in (A \setminus B) \land x \in (A \setminus C)$$

6.  **Definición de Intersección de Conjuntos:**  
    La conjunción lógica ($\land$) entre dos condiciones de pertenencia se traduce en la intersección de ambos conjuntos por definición ($x \in X \land x \in Y \iff x \in X \cap Y$):
    $$\iff x \in (A \setminus B) \cap (A \setminus C)$$

#### Conclusión:
Dado que se ha establecido una cadena continua de equivalencias lógicas bicondicionales ($\iff$) desde el miembro izquierdo al derecho, queda formalmente demostrado que:
$$A \setminus (B \cup C) = (A \setminus B) \cap (A \setminus C)$$
