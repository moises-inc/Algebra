import pandas as pd
import os

# 1. Configuración de rutas
directorio_actual = os.path.dirname(os.path.abspath(__file__))

archivo_tmax = os.path.join(directorio_actual, 'tmax_cr2met_day.csv')
archivo_tmin = os.path.join(directorio_actual, 'tmin_cr2met_day.csv')
# Ya no buscamos archivo_tmean

codigo_estacion = '4314002' 

print("Cargando archivos CSV de T_max y T_min...")
df_tmax = pd.read_csv(archivo_tmax)
df_tmin = pd.read_csv(archivo_tmin)

# 2. Filtrar y renombrar
df_tmax = df_tmax[['date', codigo_estacion]].rename(columns={codigo_estacion: 'T_max'})
df_tmin = df_tmin[['date', codigo_estacion]].rename(columns={codigo_estacion: 'T_min'})

# 3. Unificar datos por fecha
print("Unificando datos...")
df_unificado = pd.merge(df_tmax, df_tmin, on='date')

# 4. CALCULAR LA TEMPERATURA PROMEDIO (T_mean)
print("Calculando Temperatura Promedio diaria...")
df_unificado['T_mean'] = (df_unificado['T_max'] + df_unificado['T_min']) / 2

# 5. Filtrar los últimos 5 años
df_unificado['date'] = pd.to_datetime(df_unificado['date'])
anio_maximo = df_unificado['date'].dt.year.max()
anio_minimo = anio_maximo - 4 

print(f"Filtrando datos para el quinquenio: {anio_minimo} - {anio_maximo}...")
df_5_anios = df_unificado[df_unificado['date'].dt.year >= anio_minimo].copy()
df_5_anios.dropna(inplace=True)

# 6. Guardar el archivo listo para la Parte 2
archivo_salida = os.path.join(directorio_actual, f'datos_consolidados_{codigo_estacion}_5anios.csv')
df_5_anios.to_csv(archivo_salida, index=False)
print(f"¡Proceso completado! Archivo guardado con éxito como: datos_consolidados_{codigo_estacion}_5anios.csv")