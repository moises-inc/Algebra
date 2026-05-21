import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# =========================================
# 1. PARÁMETROS DEL BRAZO ROBÓTICO
# =========================================
L1 = 80  # Longitud del Segmento 1 (cm)
L2 = 70  # Longitud del Segmento 2 (cm)

# Punto objetivo a alcanzar (P)
Px = 60
Py = 90

# =========================================
# 2. CÁLCULO CINEMÁTICO (Oculto, solo para renderizado)
# =========================================
# Distancia hipotenusa (d)
d = np.hypot(Px, Py)

# Ángulo interno del codo (Beta)
cos_beta = (L1**2 + L2**2 - d**2) / (2 * L1 * L2)
beta_rad = np.arccos(cos_beta)
beta_deg = np.degrees(beta_rad)

# Ángulo de elevación (Alpha)
gamma_rad = np.arctan2(Py, Px)
cos_delta = (L1**2 + d**2 - L2**2) / (2 * L1 * d)
delta_rad = np.arccos(cos_delta)
alpha_rad = gamma_rad + delta_rad
alpha_deg = np.degrees(alpha_rad)

# Coordenadas de la articulación del codo (C)
codo_x = L1 * np.cos(alpha_rad)
codo_y = L1 * np.sin(alpha_rad)

# =========================================
# 3. DISEÑO VISUAL REPRESENTATIVO
# =========================================
fig, ax = plt.subplots(figsize=(10, 10))
plt.style.use('seaborn-v0_8-white')

# 3.1. Trazar la hipotenusa primero (al fondo)
ax.plot([0, Px], [0, Py], 'r--', alpha=0.6, linewidth=2, label='Distancia $d$ al objetivo', zorder=1)

# 3.2. DIBUJO DE LAS ÁREAS SOMBREADAS (zorder=2)
# --- Ángulo Alpha (Base) ---
r_arc_base = 25
alpha_shading = patches.Wedge((0, 0), r_arc_base, 0, alpha_deg, color='blue', alpha=0.15, zorder=2)
alpha_arc_line = patches.Arc((0, 0), r_arc_base*2, r_arc_base*2, angle=0, theta1=0, theta2=alpha_deg, color='blue', linewidth=2.5, zorder=3)
ax.add_patch(alpha_shading)
ax.add_patch(alpha_arc_line)

# --- Ángulo Beta (Codo) ---
theta_C_to_B = np.degrees(np.arctan2(-codo_y, -codo_x)) % 360
theta_C_to_P = np.degrees(np.arctan2(Py - codo_y, Px - codo_x)) % 360

start_angle = min(theta_C_to_B, theta_C_to_P)
end_angle = max(theta_C_to_B, theta_C_to_P)
if end_angle - start_angle > 180:
    start_angle, end_angle = end_angle, start_angle + 360

r_arc_elbow = 22
beta_shading = patches.Wedge((codo_x, codo_y), r_arc_elbow, start_angle, end_angle, color='green', alpha=0.15, zorder=2)
beta_arc_line = patches.Arc((codo_x, codo_y), r_arc_elbow*2, r_arc_elbow*2, angle=0, theta1=start_angle, theta2=end_angle, color='green', linewidth=2.5, zorder=3)
ax.add_patch(beta_shading)
ax.add_patch(beta_arc_line)

# 3.3. Trazar Segmentos sobre los sombreados (zorder=4)
ax.plot([0, codo_x], [0, codo_y], 'b-', linewidth=6, label=f'Segmento 1 ($L_1$={L1} cm)', zorder=4)
ax.plot([codo_x, Px], [codo_y, Py], 'g-', linewidth=6, label=f'Segmento 2 ($L_2$={L2} cm)', zorder=4)

# 3.4. Marcar los Nodos encima de todo (zorder=5)
ax.plot(0, 0, 'ks', markersize=14, label='Base B(0,0)', zorder=5)
ax.plot(codo_x, codo_y, 'ko', markersize=12, zorder=5)
ax.plot(Px, Py, 'ro', markersize=16, label=f'Objetivo P({Px},{Py})', zorder=5)

# 3.5. Textos y Etiquetas ajustados (Simbología Teórica)
# Texto Alpha (Solo la incógnita)
ax.text(r_arc_base * 1.35 * np.cos(np.radians(alpha_deg/2)), 
        r_arc_base * 1.35 * np.sin(np.radians(alpha_deg/2)), 
        r'$\alpha$', 
        fontsize=20, color='darkblue', fontweight='bold', ha='center', va='center')

# Texto Beta (Solo la incógnita)
mid_angle_beta = np.radians((start_angle + end_angle) / 2)
ax.text(codo_x + r_arc_elbow * 1.4 * np.cos(mid_angle_beta), 
        codo_y + r_arc_elbow * 1.4 * np.sin(mid_angle_beta), 
        r'$\beta$', 
        fontsize=20, color='darkgreen', fontweight='bold', ha='center', va='center')

# Etiquetas de vértices
ax.text(-8, -8, 'B', fontsize=18, fontweight='bold', color='black')
ax.text(codo_x - 5, codo_y + 8, 'C (Codo)', fontsize=16, fontweight='bold', color='black')
ax.text(Px + 4, Py + 4, 'P', fontsize=20, fontweight='bold', color='black')

# 3.6. Configuraciones Generales
ax.set_xlim(-20, 160)
ax.set_ylim(-20, 160)
ax.set_aspect('equal')
ax.axhline(0, color='black', linewidth=1.5)
ax.axvline(0, color='black', linewidth=1.5)

ax.set_title("Diseño Visual Representativo: Cinemática de Brazo Robótico", fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel("Eje X (cm)", fontsize=16)
ax.set_ylabel("Eje Y (cm)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=14)
ax.grid(True, linestyle=':', alpha=0.5)
ax.legend(loc='lower right', fontsize=14, frameon=True, shadow=True, borderpad=1)

# Guardar
output_filename = "Diseno_Brazo_Robotico_Teorico.png"
plt.savefig(output_filename, dpi=300, bbox_inches='tight')
print(f"✅ Diseño visual teórico generado y guardado como '{output_filename}'.")
plt.show()