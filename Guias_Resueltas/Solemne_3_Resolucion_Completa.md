---
id: "2026-06-13-solemne-3-resolucion"
title: "Resolución Completa Solemne 3 Álgebra 2025-1"
project: "Estudios_Universidad"
date: "2026-06-13T13:20:00"
last_modified: "2026-06-13T13:20:00"
type: "academic-note"
status: "completed"
priority: "medium"
tags: ["#status/completed", "#project/Estudios_Universidad", "#course/lgebra"]
---

# Resolución Completa: Solemne 3A - Álgebra (2025-1)
**Asignatura:** Álgebra (DCEX0007)  
**Resolución:** OpenCode & Antigravity Hibrid Core  

---

## Parte I: VERDADERO O FALSO

### Ejercicio I.1: Triangulación y Ley del Coseno
*   **Enunciado:** Un piloto de avión observa dos embarcaciones. Una se encuentra a 7 km de distancia del avión en el aire y la otra a 4 km. La distancia entre las embarcaciones es de 8 km. El piloto afirma que el ángulo formado por sus líneas visuales es de 100°.
*   **Desarrollo:**  
    Sean los vértices del triángulo ***A*** (avión), ***B*** (embarcación 1) y ***C*** (embarcación 2). Las longitudes de los lados son ***c*** = 7, ***b*** = 4 y ***a*** = 8.
    Aplicamos la Ley del Coseno para obtener el ángulo del vértice ***A*** (***α***):
    $$a^2 = b^2 + c^2 - 2bc \cos(\alpha)$$
    Sustituyendo los valores conocidos:
    $$8^2 = 4^2 + 7^2 - 2(4)(7) \cos(\alpha)$$
    $$64 = 16 + 49 - 56 \cos(\alpha)$$
    $$64 = 65 - 56 \cos(\alpha)$$
    $$-1 = -56 \cos(\alpha) \implies \cos(\alpha) = \frac{1}{56}$$
    Dado que ***cos(α)*** = 1/56 \> 0, el ángulo ***α*** debe encontrarse necesariamente en el primer cuadrante (es decir, 0 \< ***α*** \< 90°).
    Calculando el ángulo exacto:
    $$\alpha = \arccos\left(\frac{1}{56}\right) \approx 88.98^\circ$$
    Dado que el ángulo calculado de aproximadamente 88.98° es agudo, la afirmación del piloto de que el ángulo es de 100° (ángulo obtuso) es falsa.
*   **Resultado:** **F** (Falsa).

---

### Ejercicio I.2: Operación con Complejos (De Moivre)
*   **Enunciado:** Un estudiante resuelve la potencia (***i*** - 1)⁶ y comete errores en su procedimiento.
*   **Desarrollo:**  
    Analizando los pasos del estudiante:
    *   **Paso 1:** Escribe 1 + ***i*** = \sqrt{2} (\cos(3\pi/4) + ***i***\sin(3\pi/4)). Aquí comete el primer error: el número a evaluar es ***i*** - 1 = -1 + ***i***. Escribió 1 + ***i*** (cuyo argumento es \pi/4, no 3\pi/4), generando una igualdad inválida.
    *   **Paso 5:** A partir de 2³ (\cos(9\pi/2) + ***i***\sin(9\pi/2)), concluye que la forma binómica es -8***i***. Evaluando analíticamente:
        $$\cos(9\pi/2) = \cos(\pi/2 + 4\pi) = \cos(\pi/2) = 0$$
        $$\sin(9\pi/2) = \sin(\pi/2 + 4\pi) = \sin(\pi/2) = 1$$
        Por tanto, la potencia correcta es 8(0 + ***i***) = 8***i***. El estudiante concluye erróneamente -8***i*** por un error de signo.
    Como el estudiante posee efectivamente dos errores en su procedimiento, la afirmación de que "El estudiante tiene un error en su desarrollo" es verdadera.
*   **Resultado:** **V** (Verdadera).

---

### Ejercicio I.3: Raíces y Factorización de Polinomios
*   **Enunciado:** El polinomio ***p(x)*** = ***x***⁴ - 6***x***³ + 12***x***² - 8***x*** tiene raíz ***a*** = +2 con multiplicidad 3 y su factorización completa es ***p(x)*** = ***x***(***x*** - 2)³.
*   **Desarrollo:**  
    Factorizando el polinomio extraemos primero el factor común ***x***:
    $$p(x) = x(x^3 - 6x^2 + 12x - 8)$$
    El término cúbico ***x***³ - 6***x***² + 12***x*** - 8 corresponde de manera exacta al desarrollo notable del cubo de un binomio (***x*** - 2)³:
    $$(x - 2)^3 = x^3 - 6x^2 + 12x - 8$$
    Sustituyendo, obtenemos la factorización final:
    $$p(x) = x(x - 2)^3$$
    Esto nos indica que las raíces del polinomio son ***x*** = 0 (multiplicidad 1) y ***x*** = 2 (multiplicidad 3). La afirmación es correcta.
*   **Resultado:** **V** (Verdadera).

---

## Parte II: SELECCIÓN MÚLTIPLE

### Ejercicio II.1: Simplificación Trigonométrica
*   **Pregunta:** Simplificar la expresión \sin(***x***)/\csc(***x***) + \cos(***x***)/\sec(***x***).
*   **Desarrollo:**  
    Aplicamos las identidades trigonométricas recíprocas:
    $$\csc(x) = \frac{1}{\sin(x)}, \quad \sec(x) = \frac{1}{\cos(x)}$$
    Sustituyendo en la fracción:
    $$\frac{\sin(x)}{\frac{1}{\sin(x)}} + \frac{\cos(x)}{\frac{1}{\cos(x)}} = \sin^2(x) + \cos^2(x)$$
    Por la identidad pitagórica fundamental, \sin²(***x***) + \cos²(***x***) = 1.
*   **Resultado:** Alternativa **a) 1**.

---

### Ejercicio II.2: División de Números Complejos
*   **Pregunta:** Calcular 3cis(60°)/(-\sqrt{3}/2 + 1/2***i***).
*   **Desarrollo:**  
    1. Numerador en forma polar: ***z₁*** = 3cis(60°).
    2. Denominador ***z₂*** = -\sqrt{3}/2 + 1/2***i*** a forma polar:
       * Módulo: ***r₂*** = \sqrt{(-\sqrt{3}/2)^2 + (1/2)^2} = \sqrt{3/4 + 1/4} = 1.
       * Argumento: Dado que la parte real es negativa y la imaginaria es positiva, se encuentra en el segundo cuadrante: ***θ₂*** = 180° - \arcsin(1/2) = 180° - 30° = 150°.
       * Por tanto, ***z₂*** = 1cis(150°).
    3. Efectuamos la división polar restando los argumentos:
       $$\frac{z_1}{z_2} = \frac{3\text{cis}(60^\circ)}{1\text{cis}(150^\circ)} = 3\text{cis}(60^\circ - 150^\circ) = 3\text{cis}(-90^\circ)$$
    4. Pasando a forma binómica:
       $$3\text{cis}(-90^\circ) = 3(\cos(-90^\circ) + i\sin(-90^\circ)) = 3(0 + i(-1)) = -3i$$
*   **Resultado:** Alternativa **c) -3***i***.

---

### Ejercicio II.3: Teorema del Resto
*   **Pregunta:** Hallar el valor de ***a*** para que el resto de la división de ***x***⁴ + 3***x***³ + (***a*** + 1)***x***² - ***x*** + ***a*** por ***x*** + 1 sea 32.
*   **Desarrollo:**  
    Por el Teorema del Resto, al dividir por ***x*** - ***c***, el resto es ***P(c)***. Aquí el divisor es ***x*** + 1 = ***x*** - (-1), por lo que evaluamos en ***c*** = -1:
    $$P(-1) = (-1)^4 + 3(-1)^3 + (a + 1)(-1)^2 - (-1) + a$$
    $$P(-1) = 1 - 3 + (a + 1) + 1 + a = 2a$$
    Igualando al resto requerido:
    $$2a = 32 \implies a = 16$$
*   **Resultado:** Alternativa **d) 16**.

---

## Parte III: DESARROLLO

### Ejercicio III.1: Descomposición en Fracciones Parciales
*   **Enunciado:** Encuentra la descomposición en sumas de fracciones parciales de:
    $$\frac{x^3 - 3x^2 - 3x - 5}{x^2 - 4}$$
*   **Desarrollo:**  
    1. **División Polinomial:** Dado que el grado del numerador (3) es mayor que el del denominador (2), dividimos:
       $$(x^3 - 3x^2 - 3x - 5) \div (x^2 - 4)$$
       Obtenemos un cociente de ***x*** - 3 y un residuo de ***x*** - 17. Reescribimos:
       $$\frac{x^3 - 3x^2 - 3x - 5}{x^2 - 4} = x - 3 + \frac{x - 17}{x^2 - 4}$$
    2. **Fracciones Parciales:** Factorizamos el denominador ***x***² - 4 = (***x*** - 2)(***x*** + 2) y planteamos:
       $$\frac{x - 17}{(x - 2)(x + 2)} = \frac{A}{x - 2} + \frac{B}{x + 2}$$
       Multiplicando por el denominador común:
       $$x - 17 = A(x + 2) + B(x - 2)$$
    3. **Constantes:**
       * Evaluando en ***x*** = 2: -15 = 4***A*** \implies ***A*** = -15/4.
       * Evaluando en ***x*** = -2: -19 = -4***B*** \implies ***B*** = 19/4.
    4. **Resultado final:**
       $$\frac{x^3 - 3x^2 - 3x - 5}{x^2 - 4} = x - 3 - \frac{15}{4(x - 2)} + \frac{19}{4(x + 2)}$$

---

### Ejercicio III.2: Raíces Cúbicas de un Número Complejo
*   **Enunciado:** Calcule las raíces cúbicas de: ***z*** = 15 + 8***i***.
*   **Desarrollo:**  
    1. **Forma Polar:**
       * Módulo: ***r*** = |***z***| = \sqrt{15^2 + 8^2} = \sqrt{289} = 17.
       * Argumento: ***θ*** = \arctan(8/15) (primer cuadrante).
    2. **Fórmula de De Moivre:** Las raíces cúbicas ***w_k*** son:
       $$w_k = \sqrt[3]{17} \left( \cos\left(\frac{\theta + 2k\pi}{3}\right) + i \sin\left(\frac{\theta + 2k\pi}{3}\right) \right), \quad k \in \{0, 1, 2\}$$
       * **Para ***k*** = 0:**
         $$w_0 = \sqrt[3]{17} \left( \cos\left(\frac{\arctan(8/15)}{3}\right) + i \sin\left(\frac{\arctan(8/15)}{3}\right) \right)$$
       * **Para ***k*** = 1:**
         $$w_1 = \sqrt[3]{17} \left( \cos\left(\frac{\arctan(8/15) + 2\pi}{3}\right) + i \sin\left(\frac{\arctan(8/15) + 2\pi}{3}\right) \right)$$
       * **Para ***k*** = 2:**
         $$w_2 = \sqrt[3]{17} \left( \cos\left(\frac{\arctan(8/15) + 4\pi}{3}\right) + i \sin\left(\frac{\arctan(8/15) + 4\pi}{3}\right) \right)$$
    3. **Aproximación Decimal:**
       Con ***θ*** \approx 28.07° y \sqrt[3]{17} \approx 2.571:
       * ***w₀*** \approx 2.571(\cos(9.36°) + ***i***\sin(9.36°)) \approx 2.537 + 0.418***i***
       * ***w₁*** \approx 2.571(\cos(129.36°) + ***i***\sin(129.36°)) \approx -1.631 + 1.988***i***
       * ***w₂*** \approx 2.571(\cos(249.36°) + ***i***\sin(249.36°)) \approx -0.906 - 2.406***i***

[[Álgebra]]
