import math

def calcular_distancia_euclidiana(punto_base, punto_objetivo):
    """
    Calcula la distancia euclidiana entre dos puntos en un plano 2D.
    Utiliza math.hypot que implementa el Teorema de Pitágoras de forma segura.
    """
    # Extraemos las coordenadas
    x1, y1 = punto_base
    x2, y2 = punto_objetivo
    
    # Calculamos los deltas (diferencias)
    delta_x = x2 - x1
    delta_y = y2 - y1
    
    # math.hypot(x, y) es equivalente a math.sqrt(x**2 + y**2)
    distancia = math.hypot(delta_x, delta_y)
    
    return distancia

# ==========================================
# EJECUCIÓN Y VALIDACIÓN
# ==========================================
if __name__ == "__main__":
    # Definición de las coordenadas dadas en el problema
    B = (0, 0)   # Base del brazo robótico
    P = (60, 90) # Punto objetivo a alcanzar
    
    print("=== VERIFICACIÓN CINEMÁTICA: DISTANCIA EUCLIDIANA ===")
    print(f"-> Coordenada Base (B): {B}")
    print(f"-> Coordenada Objetivo (P): {P}")
    
    # Ejecutamos la función
    d_exacta = calcular_distancia_euclidiana(B, P)
    d_redondeada = round(d_exacta, 2)
    
    print("-" * 50)
    print(f"Cálculo interno: √({P[0]}^2 + {P[1]}^2) = √{P[0]**2 + P[1]**2}")
    print(f"Distancia decimal completa : {d_exacta:.6f} cm")
    print(f"Distancia redondeada final : {d_redondeada} cm")
    print("-" * 50)
    
    # Comprobación de integridad lógica
    if d_redondeada == 108.17:
        print("✅ VALIDACIÓN EXITOSA: El cálculo analítico manual coincide con el computacional.")
    else:
        print("❌ ADVERTENCIA: Discrepancia en los cálculos.")