import pandas as pd
import os

# =============================================================================
# CONFIGURACIÓN DEL USUARIO
# Modifica exclusivamente las variables de este bloque para cada nueva estación.
# =============================================================================
codigo_estacion = '5427003' # Ejemplo: '1234567'
archivo_tmax_csv = 'tmax_cr2met_day.csv'   # Nombre del archivo de T. Máxima
archivo_tmin_csv = 'tmin_cr2met_day.csv'   # Nombre del archivo de T. Mínima
# =============================================================================

# 1. Configuración de rutas (Detecta automáticamente la carpeta de trabajo)
directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_tmax = os.path.join(directorio_actual, archivo_tmax_csv)
ruta_tmin = os.path.join(directorio_actual, archivo_tmin_csv)

print(f"Iniciando procesamiento para la estación {codigo_estacion}...")

try:
    # 2. Cargar los datos desde los archivos CSV
    df_tmax = pd.read_csv(ruta_tmax)
    df_tmin = pd.read_csv(ruta_tmin)
except FileNotFoundError as e:
    print(f"Error: No se encontró uno de los archivos. Asegúrate de que estén en la misma carpeta.\nDetalle: {e}")
    exit()

# 3. Extraer solo las columnas necesarias (Fecha y los datos de la estación) y renombrarlas
df_tmax = df_tmax[['date', codigo_estacion]].rename(columns={codigo_estacion: 'T_max'})
df_tmin = df_tmin[['date', codigo_estacion]].rename(columns={codigo_estacion: 'T_min'})

# 4. Unificar las tablas utilizando la fecha exacta como punto de coincidencia
df_unificado = pd.merge(df_tmax, df_tmin, on='date')

# 5. Calcular matemáticamente la Temperatura Promedio (T_mean)
df_unificado['T_mean'] = (df_unificado['T_max'] + df_unificado['T_min']) / 2

# 6. Transformar la columna de fechas para poder operar con los años
df_unificado['date'] = pd.to_datetime(df_unificado['date'])

# 7. Identificar el año más reciente registrado y calcular el límite de los 5 años (quinquenio)
anio_maximo = df_unificado['date'].dt.year.max()
anio_minimo = anio_maximo - 4 

# 8. Filtrar el DataFrame para conservar únicamente el periodo requerido
df_5_anios = df_unificado[df_unificado['date'].dt.year >= anio_minimo].copy()

# Eliminar cualquier fila que contenga datos nulos/vacíos en ese periodo para evitar errores estadísticos
df_5_anios.dropna(inplace=True)

# 9. Guardar los datos limpios en un nuevo archivo CSV
archivo_salida = os.path.join(directorio_actual, f'datos_consolidados_{codigo_estacion}_5anios.csv')
df_5_anios.to_csv(archivo_salida, index=False)

print(f"Proceso finalizado. Se han filtrado datos desde {anio_minimo} hasta {anio_maximo}.")
print(f"Archivo guardado como: datos_consolidados_{codigo_estacion}_5anios.csv\n")