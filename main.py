# =============================================================================
# HOMEWORK 3 - ANALYSE ROTORDYNAMIQUE AVEC ROSS
# Arbre flexible avec deux disques et paliers anisotropes
# =============================================================================

import ross as rs
import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# ÉTAPE 1: DÉFINITION DU MATÉRIAU ET DES PARAMÈTRES
# =============================================================================

steel = rs.Material(
    name="Steel",
    rho=7800,      # kg/m³
    E=210e9,       # Pa (210 GPa)
    G_s=81e9,      # Pa (81 GPa)
    color="grey"
)

# Paramètres géométriques
shaft_diameter = 0.05  # m
shaft_length = 2.0     # m
n_elements = 10        # Nombre d'éléments de poutre
element_length = shaft_length / n_elements  # 0.2 m par élément

print("="*70)
print("PARAMÈTRES DU SYSTÈME")
print("="*70)
print(f"Longueur totale de l'arbre: {shaft_length} m")
print(f"Diamètre de l'arbre: {shaft_diameter*1000} mm")
print(f"Nombre d'éléments: {n_elements}")
print(f"Longueur d'un élément: {element_length} m")
print(f"Matériau: {steel.name}, E={steel.E/1e9} GPa, G={steel.G_s/1e9} GPa")

# =============================================================================
# ÉTAPE 2: CRÉATION DES ÉLÉMENTS D'ARBRE (SHAFT ELEMENTS)
# =============================================================================

shaft_elements = []
for i in range(n_elements):
    shaft = rs.ShaftElement(
        L=element_length,
        idl=0,                    # Diamètre intérieur gauche (arbre plein)
        odl=shaft_diameter,       # Diamètre extérieur gauche
        idr=0,                    # Diamètre intérieur droit
        odr=shaft_diameter,       # Diamètre extérieur droit
        material=steel,
        shear_effects=True,       # Effets de cisaillement (Timoshenko)
        rotary_inertia=True,      # Inertie de rotation
        gyroscopic=True,          # Effets gyroscopiques
        n=i                       # Numéro du nœud gauche
    )
    shaft_elements.append(shaft)

print(f"\n{n_elements} éléments d'arbre créés avec succès")

# =============================================================================
# ÉTAPE 3: CRÉATION DES DISQUES
# =============================================================================

# Disque gauche à 0.8m → nœud 4 (0.8/0.2 = 4)
disk_left_thickness = 0.07    # m
disk_left_diameter = 0.30     # m
disk_left_node = 4

# Calcul des moments d'inertie du disque gauche
m_left = steel.rho * np.pi * (disk_left_diameter/2)**2 * disk_left_thickness
Id_left = 0.25 * m_left * (disk_left_diameter/2)**2  # Moment polaire
Ip_left = 0.5 * m_left * (disk_left_diameter/2)**2   # Moment axial

disk_left = rs.DiskElement(
    n=disk_left_node,
    m=m_left,
    Id=Id_left,
    Ip=Ip_left,
    tag="Disk_Left"
)

# Disque droit à 1.4m → nœud 7 (1.4/0.2 = 7)
disk_right_thickness = 0.07   # m
disk_right_diameter = 0.35    # m
disk_right_node = 7

# Calcul des moments d'inertie du disque droit
m_right = steel.rho * np.pi * (disk_right_diameter/2)**2 * disk_right_thickness
Id_right = 0.25 * m_right * (disk_right_diameter/2)**2
Ip_right = 0.5 * m_right * (disk_right_diameter/2)**2

disk_right = rs.DiskElement(
    n=disk_right_node,
    m=m_right,
    Id=Id_right,
    Ip=Ip_right,
    tag="Disk_Right"
)

disk_elements = [disk_left, disk_right]

print("\n" + "="*70)
print("DISQUES")
print("="*70)
print(f"Disque gauche - Nœud: {disk_left_node}, Position: 0.8m")
print(f"  Masse: {m_left:.2f} kg")
print(f"  Diamètre: {disk_left_diameter*1000} mm")
print(f"  Id: {Id_left:.4f} kg.m², Ip: {Ip_left:.4f} kg.m²")
print(f"\nDisque droit - Nœud: {disk_right_node}, Position: 1.4m")
print(f"  Masse: {m_right:.2f} kg")
print(f"  Diamètre: {disk_right_diameter*1000} mm")
print(f"  Id: {Id_right:.4f} kg.m², Ip: {Ip_right:.4f} kg.m²")

# =============================================================================
# ÉTAPE 4: CRÉATION DES PALIERS ANISOTROPES
# =============================================================================

# Rigidités des paliers
kxx = 1e6       # N/m (horizontal)
kyy = 1.5e6     # N/m (vertical)
cxx = 0         # Pas d'amortissement spécifié
cyy = 0

# Palier gauche (nœud 0)
bearing_left = rs.BearingElement(
    n=0,
    kxx=kxx,
    kyy=kyy,
    cxx=cxx,
    cyy=cyy,
    tag="Bearing_Left"
)

# Palier droit (nœud 10)
bearing_right = rs.BearingElement(
    n=n_elements,  # Dernier nœud
    kxx=kxx,
    kyy=kyy,
    cxx=cxx,
    cyy=cyy,
    tag="Bearing_Right"
)

bearing_elements = [bearing_left, bearing_right]

print("\n" + "="*70)
print("PALIERS ANISOTROPES")
print("="*70)
print(f"Palier gauche - Nœud: 0")
print(f"  kxx (horizontal): {kxx/1e6} MN/m")
print(f"  kyy (vertical): {kyy/1e6} MN/m")
print(f"\nPalier droit - Nœud: {n_elements}")
print(f"  kxx (horizontal): {kxx/1e6} MN/m")
print(f"  kyy (vertical): {kyy/1e6} MN/m")

# =============================================================================
# ÉTAPE 5: ASSEMBLAGE DU ROTOR
# =============================================================================

rotor = rs.Rotor(
    shaft_elements=shaft_elements,
    disk_elements=disk_elements,
    bearing_elements=bearing_elements,
    tag="Flexible_Rotor_System"
)

print("\n" + "="*70)
print("ROTOR ASSEMBLÉ")
print("="*70)
print(f"Nombre total de nœuds: {n_elements + 1}")
print(f"Nombre d'éléments d'arbre: {len(shaft_elements)}")
print(f"Nombre de disques: {len(disk_elements)}")
print(f"Nombre de paliers: {len(bearing_elements)}")

# =============================================================================
# QUESTION 1: DESSINER LE SYSTÈME MODÉLISÉ
# =============================================================================
print("\n" + "="*70)
print("QUESTION 1: VISUALISATION DU SYSTÈME")
print("="*70)

fig1 = rotor.plot_rotor()
fig1.update_layout(
    title="Modèle du Rotor avec Disques et Paliers",
    width=1200,    # CORRECTION: en pixels (entier)
    height=600     # CORRECTION: en pixels (entier)
)
fig1.show()

# =============================================================================
# QUESTION 2: FRÉQUENCES NATURELLES ET MODES PROPRES (0-5000 RPM)
# =============================================================================
print("\n" + "="*70)
print("QUESTION 2: ANALYSE MODALE")
print("="*70)

# Analyse modale à différentes vitesses
speeds = [0, 1000, 2500, 5000]  # rpm

for speed_rpm in speeds:
    speed_rad_s = speed_rpm * 2 * np.pi / 60
    
    modal = rotor.run_modal(speed=speed_rad_s)
    
    print(f"\n--- Vitesse: {speed_rpm} RPM ---")
    print(f"Fréquences naturelles (Hz):")
    for i, (wd, wn) in enumerate(zip(modal.wd[:6], modal.wn[:6])):
        print(f"  Mode {i+1}: wd = {wd/(2*np.pi):.2f} Hz, wn = {wn/(2*np.pi):.2f} Hz")
        
# Visualisation des modes propres à 0 RPM
print("\nGénération des formes modales à 0 RPM...")
modal_0 = rotor.run_modal(speed=0)

# Premier mode (Mode 0)
fig2 = modal_0.plot_mode_2d(mode=0)
fig2.update_layout(
    title="Premier Mode Propre (0 RPM)",
    width=1000,
    height=500
)
fig2.show()

# Deuxième mode (Mode 1)
fig3 = modal_0.plot_mode_2d(mode=1)
fig3.update_layout(
    title="Deuxième Mode Propre (0 RPM)",
    width=1000,
    height=500
)
fig3.show()

# =============================================================================
# QUESTION 3: DYNAMIQUE À 0 ET 5000 RPM
# =============================================================================

print("\n" + "="*70)
print("QUESTION 3: ANALYSE DYNAMIQUE À 0 ET 5000 RPM")
print("="*70)

# À 0 RPM
modal_0rpm = rotor.run_modal(speed=0)
print("\nÀ 0 RPM:")
print(f"  1ère fréquence naturelle: {modal_0rpm.wn[0]/(2*np.pi):.2f} Hz")
print(f"  2ème fréquence naturelle: {modal_0rpm.wn[1]/(2*np.pi):.2f} Hz")
print(f"  Effets gyroscopiques: Aucun (vitesse nulle)")

# À 5000 RPM
speed_5000_rad = 5000 * 2 * np.pi / 60
modal_5000rpm = rotor.run_modal(speed=speed_5000_rad)
print("\nÀ 5000 RPM:")
print(f"  1ère fréquence naturelle: {modal_5000rpm.wn[0]/(2*np.pi):.2f} Hz")
print(f"  2ème fréquence naturelle: {modal_5000rpm.wn[1]/(2*np.pi):.2f} Hz")
print(f"  Effets gyroscopiques: Présents (séparation des modes)")

# Comparaison
delta_f1 = modal_5000rpm.wn[0]/(2*np.pi) - modal_0rpm.wn[0]/(2*np.pi)
delta_f2 = modal_5000rpm.wn[1]/(2*np.pi) - modal_0rpm.wn[1]/(2*np.pi)
print(f"\nVariation des fréquences:")
print(f"  Mode 1: {delta_f1:+.2f} Hz")
print(f"  Mode 2: {delta_f2:+.2f} Hz")
