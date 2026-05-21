import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# =========================================
# 1. PARÁMETROS DEL BRAZO ROBÓTICO (USS)
# =========================================
L1 = 80  # Longitud del Segmento 1 (cm)
L2 = 70  # Longitud del Segmento 2 (cm)

# Punto objetivo a alcanzar (P)
Px = 60
Py = 90

# =========================================
# 2. CÁLCULO CINEMÁTICO INVERSO (Algebraico)
# =========================================
# Distancia d (Hipotenusa)
d = np.hypot(Px, Py)

# Ángulo interno del codo (Beta)
cos_beta = (L1**2 + L2**2 - d**2) / (2 * L1 * L2)
beta_rad = np.arccos(cos_beta)
beta_deg = np.degrees(beta_rad)

# Ángulo de elevación (Alpha)
gamma_rad = np.arctan2(Py, Px)
cos_delta = (L1**2 + d**2 - L2**2) / (2 * L1 * d)
delta_rad = np.arccos(cos_delta)
alpha_rad = gamma_rad + delta_rad # Configuración "codo hacia arriba"
alpha_deg = np.degrees(alpha_rad)

# Coordenadas de la articulación del codo (C)
codo_x = L1 * np.cos(alpha_rad)
codo_y = L1 * np.sin(alpha_rad)

# =========================================
# 3. VERIFICACIÓN COMPUTACIONAL (Cinemática Directa)
# =========================================
# Calculamos la posición del efector final usando los ángulos obtenidos
vector_L2_rad = alpha_rad + (beta_rad - np.pi)
x_final = codo_x + L2 * np.cos(vector_L2_rad)
y_final = codo_y + L2 * np.sin(vector_L2_rad)

# =========================================
# 4. DISEÑO VISUAL CORREGIDO (Beta Interno)
# =========================================
fig, ax = plt.subplots(figsize=(10, 10))
# Estilo formal académico
plt.style.use('seaborn-v0_8-white')

# 4.1. Trazar la hipotenusa primero (Fondo)
ax.plot([0, Px], [0, Py], 'r--', alpha=0.6, linewidth=2, label='Distancia $d$ al objetivo', zorder=1)

# 4.2. DIBUJO Y SOMBREADO DE ÁNGULOS RESALTADOS (zorder=2)
# --- Ángulo Alpha (Base) ---
r_arc_base = 25
alpha_shading = patches.Wedge((0, 0), r_arc_base, 0, alpha_deg, color='blue', alpha=0.15, zorder=2)
alpha_arc_line = patches.Arc((0, 0), r_arc_base*2, r_arc_base*2, angle=0, theta1=0, theta2=alpha_deg, color='blue', linewidth=2.5, zorder=3)
ax.add_patch(alpha_shading)
ax.add_patch(alpha_arc_line)

# --- Ángulo Beta (Codo) - CORRECCIÓN AL INTERIOR ---
# Calculamos los ángulos absolutos desde el Codo hacia Base y hacia P
vector_C_to_B_rad = np.arctan2(-codo_y, -codo_x)
vector_C_to_P_rad = np.arctan2(Py - codo_y, Px - codo_x)

# Convertir a grados absolutos (0-360)
start_angle_beta_deg = np.degrees(vector_C_to_B_rad) % 360
end_angle_beta_deg = np.degrees(vector_C_to_P_rad) % 360

# Asegurar que dibujamos el ángulo menor interno, no el wrap exterior CCW
if start_angle_beta_deg > end_angle_beta_deg:
    if start_angle_beta_deg - end_angle_beta_deg < 180:
        # Dibujamos de start a end
        pass
    else:
        # El ángulo interno cruza el 360, ajustamos
        end_angle_beta_deg += 360
else:
    if end_angle_beta_deg - start_angle_beta_deg < 180:
        # Dibujamos de start a end
        pass
    else:
         # El ángulo interno cruza el 360, ajustamos
         start_angle_beta_deg += 360

r_arc_elbow = 20
# Shading suave verde (alpha=0.15, zorder=2)
beta_shading = patches.Wedge((codo_x, codo_y), r_arc_elbow, start_angle_beta_deg, end_angle_beta_deg, color='green', alpha=0.15, zorder=2)
# Borde sólido verde del arco (zorder=3)
beta_arc_line = patches.Arc((codo_x, codo_y), r_arc_elbow*2, r_arc_elbow*2, angle=0, theta1=start_angle_beta_deg, theta2=end_angle_beta_deg, color='green', linewidth=2.5, zorder=3)
ax.add_patch(beta_shading)
ax.add_patch(beta_arc_line)

# 4.3. Trazar Segmentos sobre los sombreados (zorder=4)
ax.plot([0, codo_x], [0, codo_y], 'b-', linewidth=6, label=f'Segmento 1 ($L_1$={L1} cm)', zorder=4)
ax.plot([codo_x, Px], [codo_y, Py], 'g-', linewidth=6, label=f'Segmento 2 ($L_2$={L2} cm)', zorder=4)

# 4.4. Marcar los Nodos encima de todo (zorder=5)
ax.plot(0, 0, 'ks', markersize=14, label='Base B(0,0)', zorder=5)
ax.plot(codo_x, codo_y, 'ko', markersize=12, zorder=5)
ax.plot(Px, Py, 'ro', markersize=16, label=f'Objetivo P({Px},{Py})', zorder=5)

# 4.5. Textos Numéricos (Pushed outside arcs, size 16)
# Texto Alpha
ax.text(r_arc_base * 1.35 * np.cos(np.radians(alpha_deg/2)), 
        r_arc_base * 1.35 * np.sin(np.radians(alpha_deg/2)), 
        r'$\alpha \approx {:.1f}^\circ$'.format(alpha_deg), 
        fontsize=16, color='darkblue', fontweight='bold', ha='center', va='center')

# Texto Beta - CORRECCIÓN DE POSICIÓN
# Usamos el punto medio exacto del arco interno dibujado
mid_angle_beta_draw_rad = np.radians((start_angle_beta_deg + end_angle_beta_deg) / 2)
ax.text(codo_x + r_arc_elbow * 1.45 * np.cos(mid_angle_beta_draw_rad), 
        codo_y + r_arc_elbow * 1.45 * np.sin(mid_angle_beta_draw_rad), 
        r'$\beta \approx {:.1f}^\circ$'.format(beta_deg), 
        fontsize=16, color='darkgreen', fontweight='bold', ha='center', va='center')

# Etiquetas de vértices
ax.text(-8, -8, 'B', fontsize=18, fontweight='bold', color='black')
ax.text(codo_x - 10, codo_y + 10, 'C (Codo)', fontsize=16, fontweight='bold', color='black')
ax.text(Px + 4, Py + 4, 'P', fontsize=20, fontweight='bold', color='black')

# 4.6. Configuraciones Generales Académicas
ax.set_xlim(-20, 160)
ax.set_ylim(-20, 160)
ax.set_aspect('equal')
ax.axhline(0, color='black', linewidth=1.5)
ax.axvline(0, color='black', linewidth=1.5)

ax.set_title("Modelamiento Digital y Verificación Cinemática", fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel("Eje X (cm)", fontsize=16)
ax.set_ylabel("Eje Y (cm)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=14)
ax.grid(True, linestyle=':', alpha=0.5)
ax.legend(loc='lower right', fontsize=14, frameon=True, shadow=True, borderpad=1)

# Guardar
output_filename = "Modelamiento_Brazo_Verificado_Corregido.png"
plt.savefig(output_filename, dpi=300, bbox_inches='tight')
print(f"✅ Diseño visual formal corregido generado y guardado como '{output_filename}'.")
# plt.show()