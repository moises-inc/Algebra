import pandas as pd
import os

# 1. Configuración de rutas seguras
directorio_actual = os.path.dirname(os.path.abspath(__file__))
# Nombre exacto del archivo que generó el script anterior
archivo_datos = os.path.join(directorio_actual, 'datos_consolidados_4314002_5anios.csv')

print("Cargando datos consolidados...")
try:
    df = pd.read_csv(archivo_datos)
except FileNotFoundError:
    print(f"Error: No se encontró el archivo. Verifica que el script 1 se haya ejecutado correctamente.")
    exit()

print(f"Analizando un total de {len(df)} días registrados...\n")

# 2. Definir las condiciones booleanas para cada conjunto
# Conjunto A: T_max > 30°C
condicion_A = df['T_max'] > 30

# Conjunto B: T_min < 10°C
condicion_B = df['T_min'] < 10

# Conjunto C: 18°C <= T_mean <= 22°C
condicion_C = (df['T_mean'] >= 18) & (df['T_mean'] <= 22)

# 3. Calcular la cardinalidad (cantidad de días) sumando los valores True
card_A = condicion_A.sum()
card_B = condicion_B.sum()
card_C = condicion_C.sum()

# 4. Calcular las intersecciones exigidas en la pauta
card_A_int_B = (condicion_A & condicion_B).sum()
card_A_int_C = (condicion_A & condicion_C).sum()
card_B_int_C = (condicion_B & condicion_C).sum()
card_A_int_B_int_C = (condicion_A & condicion_B & condicion_C).sum()

# 5. Mostrar los resultados en la terminal para el informe
print("-" * 45)
print("CARDINALIDADES DE LOS CONJUNTOS")
print("-" * 45)
print(f"Conjunto A (T_max > 30°C): {card_A} días")
print(f"Conjunto B (T_min < 10°C): {card_B} días")
print(f"Conjunto C (18°C <= T_promedio <= 22°C): {card_C} días")

print("\n" + "-" * 45)
print("INTERSECCIONES")
print("-" * 45)
print(f"A ∩ B (T_max > 30°C Y T_min < 10°C): {card_A_int_B} días")
print(f"A ∩ C (T_max > 30°C Y T_promedio 18-22°C): {card_A_int_C} días")
print(f"B ∩ C (T_min < 10°C Y T_promedio 18-22°C): {card_B_int_C} días")
print(f"A ∩ B ∩ C (Todas las condiciones): {card_A_int_B_int_C} días")
print("-" * 45) 