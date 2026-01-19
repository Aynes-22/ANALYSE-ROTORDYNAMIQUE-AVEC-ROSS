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
