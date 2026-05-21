import pandas as pd
import os

# =============================================================================
# CONFIGURACIÓN DEL USUARIO
# Modifica estas variables según la estación que estés analizando ahora.
# =============================================================================
codigo_estacion = '5427003' # Mismo código usado en el Script 1
zona_geografica = 'Centro'   # Ejemplo: 'Norte', 'Centro' o 'Sur'
# =============================================================================

# 1. Configuración de rutas para abrir el archivo consolidado generado previamente
directorio_actual = os.path.dirname(os.path.abspath(__file__))
nombre_archivo = f'datos_consolidados_{codigo_estacion}_5anios.csv'
ruta_datos = os.path.join(directorio_actual, nombre_archivo)

print(f"Analizando conjuntos para la estación {codigo_estacion} (Zona {zona_geografica})...")

try:
    df = pd.read_csv(ruta_datos)
except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{nombre_archivo}'. Ejecuta el Script 1 primero.")
    exit()

# 2. Definición matemática de los conjuntos (Condiciones Booleanas)
condicion_A = df['T_max'] > 30                                 # Conjunto A
condicion_B = df['T_min'] < 10                                 # Conjunto B
condicion_C = (df['T_mean'] >= 18) & (df['T_mean'] <= 22)      # Conjunto C

# 3. Creación de un diccionario con los cálculos de cardinalidad requeridos por la pauta
# La función .sum() cuenta cuántos registros cumplen la condición (True = 1)
resultados = {
    "Estación": codigo_estacion,
    "Zona": zona_geografica,
    "A": condicion_A.sum(),
    "B": condicion_B.sum(),
    "C": condicion_C.sum(),
    "AnB": (condicion_A & condicion_B).sum(),                  # Intersección A y B
    "AnC": (condicion_A & condicion_C).sum(),                  # Intersección A y C
    "BnC": (condicion_B & condicion_C).sum(),                  # Intersección B y C
    "AnBnC": (condicion_A & condicion_B & condicion_C).sum()   # Intersección de los tres conjuntos
}

# 4. Imprimir resultados en consola para revisión rápida
print("-" * 50)
print(f" RESULTADOS DE CARDINALIDAD: ESTACIÓN {codigo_estacion} ")
print("-" * 50)
for clave, valor in resultados.items():
    print(f"{clave:<10}: {valor}")
print("-" * 50)

# 5. Exportar los resultados a formato CSV para incorporarlos al informe
df_resultados = pd.DataFrame([resultados])
nombre_salida_csv = f'resultados_cardinalidad_{codigo_estacion}.csv'
ruta_salida = os.path.join(directorio_actual, nombre_salida_csv)

df_resultados.to_csv(ruta_salida, index=False)
print(f"Tabla exportada exitosamente en: {nombre_salida_csv}\n")