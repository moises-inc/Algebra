# Guía de Estudio y Resolución Formal: Listado 6 - Álgebra
**Asignatura:** Álgebra (DCEX0007)  
**Temática:** Trigonometría Plana y Ecuaciones Trigonométricas  
**Origen:** Universidad San Sebastián (2026-1)  
**Resolución:** Gemini Academic Assistant (Estándar de Oro Pedagógico)  

---

## Introducción Conceptual
La trigonometría es la rama de las matemáticas que estudia las relaciones entre los lados y los ángulos de los triángulos. En el ámbito de la ingeniería, es la base analítica para el modelamiento de estructuras espaciales y cinemática mecatrónica (como brazos robóticos). 

Esta guía detalla la resolución formal del **Listado 6** siguiendo la **Directiva Crítica de no emplear herramientas de cálculo infinitesimal** (límites, derivadas, integrales). Todos los desarrollos se fundamentan de forma rigurosa en identidades algebraicas, relaciones trigonométricas de triángulos rectángulos y oblicuángulos, y el análisis explícito de los dominios y recorridos de las funciones circulares.

---

## 1. Conversión de Unidades Angulares
> **Justificación Pedagógica:** La medida de un ángulo representa la amplitud de rotación de un segmento. Se puede expresar en grados sexagesimales ($^\circ$) o en radianes ($\text{rad}$). El factor de conversión fundamental se basa en la equivalencia de una semicircunferencia:  
> $$\pi \text{ rad} = 180^\circ$$
> Para convertir de grados a radianes multiplicamos por $\frac{\pi}{180^\circ}$, y de radianes a grados multiplicamos por $\frac{180^\circ}{\pi}$.

*   **a) Convertir $20^\circ$ a radianes:**  
    *Desarrollo:*  
    $$\theta = 20^\circ \cdot \frac{\pi \text{ rad}}{180^\circ} = \frac{20}{180} \pi \text{ rad} = \mathbf{\frac{\pi}{9} \text{ rad}}$$

*   **b) Convertir $\frac{7\pi}{6} \text{ rad}$ a grados sexagesimales:**  
    *Desarrollo:*  
    $$\theta = \frac{7\pi}{6} \cdot \frac{180^\circ}{\pi \text{ rad}} = \frac{7 \cdot 180^\circ}{6} = 7 \cdot 30^\circ = \mathbf{210^\circ}$$  
    *Explicación:* Un ángulo de $210^\circ$ se ubica en el tercer cuadrante del plano cartesiano, superando al ángulo llano ($180^\circ$).

*   **c) Convertir $15^\circ$ a radianes:**  
    *Desarrollo:*  
    $$\theta = 15^\circ \cdot \frac{\pi \text{ rad}}{180^\circ} = \frac{15}{180} \pi \text{ rad} = \mathbf{\frac{\pi}{12} \text{ rad}}$$

*   **d) Convertir $\frac{2\pi}{5} \text{ rad}$ a grados sexagesimales:**  
    *Desarrollo:*  
    $$\theta = \frac{2\pi}{5} \cdot \frac{180^\circ}{\pi \text{ rad}} = \frac{2 \cdot 180^\circ}{5} = 2 \cdot 36^\circ = \mathbf{72^\circ}$$

*   **e) Convertir $-120^\circ$ a radianes:**  
    *Desarrollo:*  
    $$\theta = -120^\circ \cdot \frac{\pi \text{ rad}}{180^\circ} = -\frac{120}{180} \pi \text{ rad} = \mathbf{-\frac{2\pi}{3} \text{ rad}}$$  
    *Explicación:* El signo negativo indica una rotación en sentido horario (a favor de las manecillas del reloj) partiendo desde el eje horizontal positivo.

*   **f) Convertir $-250^\circ$ a radianes:**  
    *Desarrollo:*  
    $$\theta = -250^\circ \cdot \frac{\pi \text{ rad}}{180^\circ} = -\frac{250}{180} \pi \text{ rad} = \mathbf{-\frac{25\pi}{18} \text{ rad}}$$

*   **g) Convertir $-90^\circ$ a radianes:**  
    *Desarrollo:*  
    $$\theta = -90^\circ \cdot \frac{\pi \text{ rad}}{180^\circ} = -\frac{90}{180} \pi \text{ rad} = \mathbf{-\frac{\pi}{2} \text{ rad}}$$

---

## 2. Determinación de Ángulos $\theta$ en Radianes
> **Justificación Pedagógica:** Resolver la ecuación $f(\theta) = c$ requiere el uso de funciones trigonométricas inversas (como el arcoseno, arcocoseno o arcotangente). Sin embargo, estas funciones inversas en calculadora devuelven únicamente el valor principal de su dominio restringido (valor de la rama principal). Para determinar la totalidad de las soluciones dentro de una circunferencia completa ($[0, 2\pi[$), es indispensable emplear la simetría de los cuadrantes del círculo unitario.

*   **a) $\sin \theta = 0.8$ en el primer cuadrante:**  
    *Desarrollo:* Aplicamos la función inversa del seno (arcoseno) directamente:  
    $$\theta = \arcsin(0.8) \approx \mathbf{0.93 \text{ rad}}$$  
    *Nota:* Dado que la restricción explícita indica primer cuadrante ($0 \le \theta \le \pi/2 \approx 1.57 \text{ rad}$), esta corresponde a la única solución válida en este intervalo.

*   **b) $\tan \theta = 1$ en el primer cuadrante:**  
    *Desarrollo:*  
    $$\theta = \arctan(1) = \mathbf{\frac{\pi}{4} \text{ rad}}$$  
    *Explicación:* El ángulo notable cuyo cateto opuesto y adyacente son idénticos es $45^\circ$, equivalente a $\frac{\pi}{4}$ radianes.

*   **c) $\sin \theta = \frac{1}{2}$ en el intervalo $[0, 2\pi[$:**  
    *Desarrollo:* El seno es positivo en el primer y segundo cuadrante.
    1.  **Solución en I Cuadrante:** $\theta_1 = \arcsin(\frac{1}{2}) = \mathbf{\frac{\pi}{6} \text{ rad}}$ (ángulo notable de $30^\circ$).
    2.  **Solución en II Cuadrante:** Por simetría horizontal, $\theta_2 = \pi - \theta_1 = \pi - \frac{\pi}{6} = \mathbf{\frac{5\pi}{6} \text{ rad}}$ ($150^\circ$).
    *Conjunto Solución:* $S = \{\frac{\pi}{6}, \frac{5\pi}{6}\}$

*   **d) $\sin \theta = \frac{\sqrt{2}}{2}$ en el intervalo $[0, 2\pi[$:**  
    *Desarrollo:* El seno es positivo en I y II Cuadrante.
    1.  **Solución en I Cuadrante:** $\theta_1 = \arcsin(\frac{\sqrt{2}}{2}) = \mathbf{\frac{\pi}{4} \text{ rad}}$ ($45^\circ$).
    2.  **Solución en II Cuadrante:** $\theta_2 = \pi - \theta_1 = \pi - \frac{\pi}{4} = \mathbf{\frac{3\pi}{4} \text{ rad}}$ ($135^\circ$).
    *Conjunto Solución:* $S = \{\frac{\pi}{4}, \frac{3\pi}{4}\}$

*   **e) $\tan \theta = \sqrt{3}$ en el intervalo $[0, 2\pi[$:**  
    *Desarrollo:* La función tangente es positiva en el primer y tercer cuadrante.
    1.  **Solución en I Cuadrante:** $\theta_1 = \arctan(\sqrt{3}) = \mathbf{\frac{\pi}{3} \text{ rad}}$ ($60^\circ$).
    2.  **Solución en III Cuadrante:** Por simetría antipodal (periodicidad de la tangente de $\pi$), $\theta_2 = \theta_1 + \pi = \frac{\pi}{3} + \pi = \mathbf{\frac{4\pi}{3} \text{ rad}}$ ($240^\circ$).
    *Conjunto Solución:* $S = \{\frac{\pi}{3}, \frac{4\pi}{3}\}$

*   **f) $\cos \theta = \frac{1}{2}$ en el intervalo $[0, 2\pi[$:**  
    *Desarrollo:* El coseno es positivo en el primer y cuarto cuadrante.
    1.  **Solución en I Cuadrante:** $\theta_1 = \arccos(\frac{1}{2}) = \mathbf{\frac{\pi}{3} \text{ rad}}$ ($60^\circ$).
    2.  **Solución en IV Cuadrante:** Por simetría vertical, $\theta_2 = 2\pi - \theta_1 = 2\pi - \frac{\pi}{3} = \mathbf{\frac{5\pi}{3} \text{ rad}}$ ($300^\circ$).
    *Conjunto Solución:* $S = \{\frac{\pi}{3}, \frac{5\pi}{3}\}$

---

## 3. Resolución de Triángulos Rectángulos
> **Justificación Pedagógica:** En un triángulo rectángulo, las funciones trigonométricas se definen de manera directa mediante razones geométricas entre sus lados:  
> $$\sin(\theta) = \frac{\text{Cateto Opuesto}}{\text{Hipotenusa}}, \quad \cos(\theta) = \frac{\text{Cateto Adyacente}}{\text{Hipotenusa}}, \quad \tan(\theta) = \frac{\text{Cateto Opuesto}}{\text{Cateto Adyacente}}$$
> Conociendo un ángulo agudo y la longitud de un lado, podemos despejar algebraicamente cualquier variable geométrica faltante.

*   **a) Hallar el cateto opuesto $y$ sabiendo que la hipotenusa es $18$ y el ángulo opuesto a $y$ es $60^\circ$:**  
    *Desarrollo:* Planteamos la razón del seno:  
    $$\sin(60^\circ) = \frac{y}{18} \implies y = 18 \cdot \sin(60^\circ)$$  
    Sustituyendo el valor notable de $\sin(60^\circ) = \frac{\sqrt{3}}{2}$:  
    $$y = 18 \cdot \frac{\sqrt{3}}{2} = \mathbf{9\sqrt{3}} \approx 15.59$$

*   **b) Hallar el cateto adyacente $x$ sabiendo que el cateto opuesto es $30$ y el ángulo agudo opuesto es $30^\circ$:**  
    *Desarrollo:* Planteamos la razón de la tangente:  
    $$\tan(30^\circ) = \frac{30}{x} \implies x = \frac{30}{\tan(30^\circ)}$$  
    Sustituyendo el valor notable de $\tan(30^\circ) = \frac{1}{\sqrt{3}}$ (o $\frac{\sqrt{3}}{3}$):  
    $$x = \frac{30}{1/\sqrt{3}} = \mathbf{30\sqrt{3}} \approx 51.96$$

*   **c) Hallar el cateto adyacente $x$ sabiendo que el cateto opuesto es $32$ y el ángulo adyacente a $x$ es $60^\circ$:**  
    *Desarrollo:* Dado que el ángulo de $60^\circ$ es adyacente a $x$ y el lado opuesto es $32$, planteamos la relación de la tangente:  
    $$\tan(60^\circ) = \frac{32}{x} \implies x = \frac{32}{\tan(60^\circ)}$$  
    Sustituyendo el valor notable de $\tan(60^\circ) = \sqrt{3}$:  
    $$x = \frac{32}{\sqrt{3}}$$  
    Racionalizando el denominador (multiplicando por $\frac{\sqrt{3}}{\sqrt{3}}$):  
    $$x = \mathbf{\frac{32\sqrt{3}}{3}} \approx 18.48$$

*   **d) Hallar la hipotenusa $r$ sabiendo que el cateto opuesto a un ángulo de $45^\circ$ mide $20$:**  
    *Desarrollo:* Planteamos la razón del seno:  
    $$\sin(45^\circ) = \frac{20}{r} \implies r = \frac{20}{\sin(45^\circ)}$$  
    Sustituyendo el valor notable de $\sin(45^\circ) = \frac{\sqrt{2}}{2}$:  
    $$r = \frac{20}{\frac{\sqrt{2}}{2}} = \frac{40}{\sqrt{2}}$$  
    Racionalizando:  
    $$r = \frac{40\sqrt{2}}{2} = \mathbf{20\sqrt{2}} \approx 28.28$$

---

## 18. Simplificación de Expresiones Trigonométricas
> **Justificación Pedagógica:** La simplificación de expresiones algebraicas trigonométricas complejas consiste en reescribirlas a su mínima expresión utilizando identidades fundamentales. La estrategia analítica estándar es convertir todas las funciones secundarias ($\tan, \sec, \csc, \cot$) a expresiones basadas exclusivamente en $\sin x$ y $\cos x$, para luego operar algebraicamente utilizando fracciones y la identidad pitagórica fundamental:  
> $$\sin^2 x + \cos^2 x = 1$$

*   **a) Simplificar la expresión:**  
    $$E = \frac{1}{1 + \cos x} + \frac{1}{1 - \cos x}$$  
    *Desarrollo Paso a Paso:*
    1.  **Suma de Fracciones:** Encontramos el común denominador multiplicando los denominadores individuales:  
        $$E = \frac{(1 - \cos x) + (1 + \cos x)}{(1 + \cos x)(1 - \cos x)}$$
    2.  **Operación en el Numerador:** Los términos con coseno se cancelan mutuamente:  
        $$\text{Numerador} = 1 - \cos x + 1 + \cos x = 2$$
    3.  **Operación en el Denominador:** Se multiplica como una suma por su diferencia:  
        $$\text{Denominador} = (1 + \cos x)(1 - \cos x) = 1 - \cos^2 x$$
    4.  **Aplicación de Identidad Pitagórica:** Sabiendo que $\sin^2 x + \cos^2 x = 1 \implies 1 - \cos^2 x = \sin^2 x$:  
        $$E = \frac{2}{\sin^2 x}$$
    5.  **Conversión a cosecante:** Por identidad recíproca, $\frac{1}{\sin x} = \csc x$:  
        $$E = \mathbf{2\csc^2 x}$$

*   **b) Simplificar la expresión:**  
    $$E = \frac{\cos x}{1 + \sin x} + \frac{1 + \sin x}{\cos x}$$  
    *Desarrollo Paso a Paso:*
    1.  **Suma de Fracciones (Multiplicación Cruzada):**  
        $$E = \frac{\cos^2 x + (1 + \sin x)^2}{\cos x(1 + \sin x)}$$
    2.  **Desarrollo del Cuadrado del Binomio:**  
        $$E = \frac{\cos^2 x + (1 + 2\sin x + \sin^2 x)}{\cos x(1 + \sin x)}$$
    3.  **Agrupación Término Pitagórico:** Reorganizamos asociativamente el numerador:  
        $$E = \frac{(\cos^2 x + \sin^2 x) + 1 + 2\sin x}{\cos x(1 + \sin x)}$$
    4.  **Sustitución Pitagórica:** Como $\cos^2 x + \sin^2 x = 1$:  
        $$E = \frac{1 + 1 + 2\sin x}{\cos x(1 + \sin x)} = \frac{2 + 2\sin x}{\cos x(1 + \sin x)}$$
    5.  **Factorización por Factor Común:** Factorizamos el número 2 en el numerador:  
        $$E = \frac{2(1 + \sin x)}{\cos x(1 + \sin x)}$$
    6.  **Simplificación de Términos Comunes:** Cancelamos el binomio $(1 + \sin x)$ presente tanto en numerador como en denominador:  
        $$E = \frac{2}{\cos x}$$
    7.  **Conversión a secante:** Por identidad recíproca, $\frac{1}{\cos x} = \sec x$:  
        $$E = \mathbf{2\sec x}$$

*   **c) Simplificar la expresión:**  
    $$E = \tan x + \frac{\cos x}{1 + \sin x}$$  
    *Desarrollo Paso a Paso:*
    1.  **Conversión a Funciones Básicas:** Convertimos la tangente $\tan x = \frac{\sin x}{\cos x}$:  
        $$E = \frac{\sin x}{\cos x} + \frac{\cos x}{1 + \sin x}$$
    2.  **Suma de Fracciones:**  
        $$E = \frac{\sin x(1 + \sin x) + \cos^2 x}{\cos x(1 + \sin x)}$$
    3.  **Distribución en el Numerador:**  
        $$E = \frac{\sin x + \sin^2 x + \cos^2 x}{\cos x(1 + \sin x)}$$
    4.  **Sustitución de Identidad Pitagórica:** Sabiendo que $\sin^2 x + \cos^2 x = 1$:  
        $$E = \frac{\sin x + 1}{\cos x(1 + \sin x)}$$
    5.  **Simplificación:** El binomio $(\sin x + 1)$ es conmutativamente equivalente a $(1 + \sin x)$. Cancelamos en ambos miembros:  
        $$E = \frac{1}{\cos x}$$
    6.  **Conversión Recíproca:**  
        $$E = \mathbf{\sec x}$$

---

## 20. Resolución de Ecuaciones Trigonométricas en el Intervalo $[0, 2\pi[$
> **Justificación Pedagógica:** Una ecuación trigonométrica es una igualdad donde la variable independiente se encuentra bajo el efecto de una función circular. Para resolverlas se emplean técnicas algebraicas estándar (factorización, fórmula cuadrática, sustitución de variables), pero se debe considerar estrictamente el **recorrido formal** de las funciones circulares (ej. $\cos x$ y $\sin x$ tienen recorrido $[-1, 1]$ en el campo real). Cualquier ecuación que resulte en un valor absoluto mayor a 1 no posee soluciones reales.

*   **a) $-\csc x = 1$**  
    *Desarrollo Paso a Paso:*
    1.  Multiplicamos por $-1$:  
        $$\csc x = -1$$
    2.  Aplicamos la definición de cosecante ($\csc x = \frac{1}{\sin x}$):  
        $$\frac{1}{\sin x} = -1 \implies \sin x = -1$$
    3.  Buscamos el ángulo dentro del intervalo $[0, 2\pi[$ cuya ordenada en el círculo unitario sea $-1$. El único punto de intersección es el extremo inferior del eje vertical:  
        $$x = \mathbf{\frac{3\pi}{2} \text{ rad}} \quad (270^\circ)$$  
    *Conjunto Solución:* $S = \{\frac{3\pi}{2}\}$

*   **e) $2\cos^2 x - 3\cos x - 2 = 0$**  
    *Desarrollo Paso a Paso:*
    1.  **Cambio de Variable:** Definamos una variable auxiliar $u = \cos x$. Esto transforma la ecuación a una forma cuadrática estándar de segundo grado:  
        $$2u^2 - 3u - 2 = 0$$
    2.  **Factorización de la Ecuación Cuadrática:**  
        $$2u^2 - 4u + u - 2 = 0 \implies 2u(u - 2) + 1(u - 2) = 0 \implies (2u + 1)(u - 2) = 0$$
    3.  **Determinación de Raíces para $u$:**
        -   **Caso 1:** $2u + 1 = 0 \implies u = -1/2$
        -   **Caso 2:** $u - 2 = 0 \implies u = 2$
    4.  **Retorno a la Variable Original e Imposición de Restricciones:**
        -   **Análisis del Caso 2:** $\cos x = 2$. Dado que el recorrido formal de la función coseno está restringido estrictamente al intervalo $[-1, 1]$ para soluciones reales, la ecuación $\cos x = 2$ no tiene soluciones reales (absurdo matemático).
        -   **Análisis del Caso 1:** $\cos x = -1/2$. El coseno es negativo en el segundo y tercer cuadrante.
            *   Ángulo de referencia notable en el I cuadrante: $x_{\text{ref}} = \arccos(1/2) = \frac{\pi}{3}$ ($60^\circ$).
            *   Solución en II Cuadrante: $x_1 = \pi - \frac{\pi}{3} = \mathbf{\frac{2\pi}{3} \text{ rad}}$ ($120^\circ$).
            *   Solución en III Cuadrante: $x_2 = \pi + \frac{\pi}{3} = \mathbf{\frac{4\pi}{3} \text{ rad}}$ ($240^\circ$).
    *Conjunto Solución:* $S = \{\frac{2\pi}{3}, \frac{4\pi}{3}\}$

*   **h) $\sin 2x + \sin x = 0$**  
    *Desarrollo Paso a Paso:*
    1.  **Homogeneización de Ángulos:** La ecuación posee dos ángulos distintos ($2x$ y $x$). Aplicamos la identidad de ángulo doble para el seno, $\sin(2x) = 2\sin x \cos x$, para homogeneizar la expresión:  
        $$2\sin x \cos x + \sin x = 0$$
    2.  **Factorización por Factor Común:** Factorizamos por el término $\sin x$:  
        $$\sin x(2\cos x + 1) = 0$$
    3.  **Determinación de Ecuaciones Simples:**
        -   **Caso 1:** $\sin x = 0$
        -   **Caso 2:** $2\cos x + 1 = 0 \implies \cos x = -1/2$
    4.  **Búsqueda de Soluciones en el Intervalo $[0, 2\pi[$:**
        -   **Resolución Caso 1 ($\sin x = 0$):** Los ángulos sobre el círculo unitario cuya ordenada es cero corresponden al eje horizontal positivo y negativo:  
            $$x = \mathbf{0 \text{ rad}}, \quad x = \mathbf{\pi \text{ rad}}$$  
            *Nota:* Aunque $2\pi$ también cumple la condición, está excluido por el intervalo abierto por la derecha $[0, 2\pi[$.
        -   **Resolución Caso 2 ($\cos x = -1/2$):** Como demostramos en el ejercicio (e) anterior, los valores correspondientes son:  
            $$x = \mathbf{\frac{2\pi}{3} \text{ rad}}, \quad x = \mathbf{\frac{4\pi}{3} \text{ rad}}$$
    5.  **Unión de Conjuntos Solución:** Reunimos todas las soluciones ordenadas ascendentemente:  
        $$S = \{0, \frac{2\pi}{3}, \pi, \frac{4\pi}{3}\}$$
