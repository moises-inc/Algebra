# Resolución Formal: Listado 5 - Álgebra
**Materia:** Lógica Proposicional y Teoría de Conjuntos  
**Origen:** Universidad San Sebastián (2026-1)  
**Resolución:** Gemini Academic Assistant  

---

## Parte I: Lógica Proposicional

### Ejercicio 1: Simplificación de Proposiciones
**Enunciado:** Simplifique la siguiente proposición utilizando leyes de la lógica:
$$[(p \rightarrow q) \land \neg q] \rightarrow \neg p$$

**Resolución:**
Para simplificar la expresión, utilizaremos las equivalencias lógicas fundamentales.

1. **Definición de Condicional:** $A \rightarrow B \equiv \neg A \lor B$
   Aplicando al antecedente $(p \rightarrow q)$:
   $$[(\neg p \lor q) \land \neg q] \rightarrow \neg p$$

2. **Ley Distributiva:** $(A \lor B) \land C \equiv (A \land C) \lor (B \land C)$
   $$[(\neg p \land \neg q) \lor (q \land \neg q)] \rightarrow \neg p$$

3. **Ley de Contradicción:** $q \land \neg q \equiv \mathbf{F}$ (donde $\mathbf{F}$ es una contradicción)
   $$[(\neg p \land \neg q) \lor \mathbf{F}] \rightarrow \neg p$$

4. **Ley de Identidad:** $A \lor \mathbf{F} \equiv A$
   $$(\neg p \land \neg q) \rightarrow \neg p$$

5. **Definición de Condicional (nuevamente):**
   $$\neg(\neg p \land \neg q) \lor \neg p$$

6. **Ley de De Morgan:** $\neg(A \land B) \equiv \neg A \lor \neg B$
   $$(\neg \neg p \lor \neg \neg q) \lor \neg p$$

7. **Ley de Doble Negación:** $\neg \neg A \equiv A$
   $$(p \lor q) \lor \neg p$$

8. **Leyes Asociativa y Conmutativa:**
   $$(p \lor \neg p) \lor q$$

9. **Ley del Tercero Excluido:** $p \lor \neg p \equiv \mathbf{V}$ (donde $\mathbf{V}$ es una tautología)
   $$\mathbf{V} \lor q$$

10. **Ley de Dominación:** $\mathbf{V} \lor A \equiv \mathbf{V}$
    $$\mathbf{V}$$

**Conclusión:** La proposición original es una **tautología**.

---

## Parte II: Teoría de Conjuntos

### Ejercicio 2: Demostración de Igualdad de Conjuntos
**Enunciado:** Demuestre formalmente que $A \setminus (B \cup C) = (A \setminus B) \cap (A \setminus C)$.

**Resolución:**
Realizaremos la demostración mediante la definición de pertenencia ($\in$). Un elemento $x$ pertenece al conjunto del lado izquierdo si y solo si pertenece al del lado derecho.

$$x \in A \setminus (B \cup C)$$

1. **Definición de Diferencia:** $A \setminus B = \{x : x \in A \land x \notin B\}$
   $$x \in A \land \neg(x \in B \cup C)$$

2. **Definición de Unión:** $B \cup C = \{x : x \in B \lor x \in C\}$
   $$x \in A \land \neg(x \in B \lor x \in C)$$

3. **Ley de De Morgan (Lógica):** $\neg(p \lor q) \equiv \neg p \land \neg q$
   $$x \in A \land (x \notin B \land x \notin C)$$

4. **Ley de Idempotencia y Asociatividad:** (Podemos escribir $x \in A \equiv x \in A \land x \in A$)
   $$(x \in A \land x \notin B) \land (x \in A \land x \notin C)$$

5. **Definición de Diferencia (en ambos paréntesis):**
   $$x \in (A \setminus B) \land x \in (A \setminus C)$$

6. **Definición de Intersección:** $A \cap B = \{x : x \in A \land x \in B\}$
   $$x \in (A \setminus B) \cap (A \setminus C)$$

**Conclusión:** Por transitividad de las equivalencias, se ha demostrado que:
$$A \setminus (B \cup C) = (A \setminus B) \cap (A \setminus C)$$
