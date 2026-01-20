# Homework 3 - Analyse Rotordynamique avec ROSS
**Module: Dynamique des Machines Tournantes**  

# Projet : Analyse rotordynamique avec ROSS

## Exécution en ligne du notebook

Vous pouvez exécuter le notebook directement dans votre navigateur via Binder.  
Cliquez sur le badge ci-dessous ou directement sur ce lien : [**Cliquez ici pour lancer le notebook sur Binder**](https://mybinder.org/v2/gh/Aynes-22/ANALYSE-ROTORDYNAMIQUE-AVEC-ROSS.git/HEAD?urlpath=%2Ftree%2Fproject.ipynb)

[![Launch Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Aynes-22/ANALYSE-ROTORDYNAMIQUE-AVEC-ROSS.git/HEAD?urlpath=%2Ftree%2Fproject.ipynb)

---

Le notebook `project.ipynb` contient le code et les explications étape par étape.  
Vous pouvez exécuter les cellules une par une, visualiser les plots et vérifier les résultats facilement.

---

## INTRODUCTION

Ce rapport présente une analyse rotordynamique complète d'un système d'arbre flexible de 2 mètres supportant deux disques par des paliers anisotropes. À l'aide de la bibliothèque ROSS (Rotordynamic Open-Source Software), un modèle par éléments finis a été développé avec 10 éléments de poutre de Timoshenko pour investiguer le comportement dynamique du rotor dans la plage opérationnelle de 0 à 5000 RPM.

---

## SPÉCIFICATIONS DU SYSTÈME

### Paramètres de l'Arbre
- **Longueur totale:** 2.0 m
- **Diamètre:** 0.05 m (50 mm)
- **Matériau:** Acier
  - Densité (ρ): 7800 kg/m³
  - Module de Young (E): 210 GPa
  - Module de cisaillement (G): 81 GPa
- **Discrétisation:** 10 éléments de poutre de Timoshenko
- **Longueur d'élément:** 0.2 m chacun
- **Amortissement interne:** Aucun

### Configuration des Disques

**Disque Gauche (à 0.8 m de l'extrémité gauche - Nœud 4):**
- Épaisseur: 0.07 m
- Diamètre: 0.30 m
- Masse: 30.91 kg
- Moment d'inertie diamétral (Id): 0.1737 kg·m²
- Moment d'inertie polaire (Ip): 0.3474 kg·m²

**Disque Droit (à 1.4 m de l'extrémité gauche - Nœud 7):**
- Épaisseur: 0.07 m
- Diamètre: 0.35 m
- Masse: 42.16 kg
- Moment d'inertie diamétral (Id): 0.2879 kg·m²
- Moment d'inertie polaire (Ip): 0.5758 kg·m²

### Propriétés des Paliers

Les deux paliers (aux nœuds 0 et 10) présentent une rigidité anisotrope:
- **Rigidité horizontale (kxx):** 1.0 × 10⁶ N/m
- **Rigidité verticale (kyy):** 1.5 × 10⁶ N/m
- **Amortissement:** 0 N·s/m

Cette anisotropie crée une dépendance directionnelle dans la réponse dynamique du système.

---

## 1. DESSIN DU SYSTÈME MODÉLISÉ

Le modèle par éléments finis du rotor a été créé avec ROSS :
<img width="1200" height="600" alt="newplot" src="https://github.com/user-attachments/assets/93fdb8b0-5744-41e8-9e54-568f48044d97" />

### Configuration du Modèle
- **11 nœuds** numérotés de 0 à 10
- **10 éléments d'arbre** de longueur égale (0.2 m)
- **2 éléments disques** positionnés aux nœuds 4 et 7
- **2 éléments paliers** aux extrémités (nœuds 0 et 10)

### Visualisation du Système

La représentation graphique du rotor modélisé montre:

1. **Géométrie:** Un arbre horizontal de 2 mètres avec deux disques positionnés asymétriquement
2. **Localisation des disques:** 
   - Disque gauche à 0.8 m (40% de la longueur totale)
   - Disque droit à 1.4 m (70% de la longueur totale)
3. **Conditions d'appui:** Configuration simplement appuyée avec paliers aux deux extrémités
4. **Système de coordonnées:** Directions horizontale (X) et verticale (Y) clairement définies

### Caractéristiques du Modèle de Timoshenko

Le modèle utilise la théorie de poutre de Timoshenko qui prend en compte:
- **Déformation de cisaillement** (importante pour les poutres courtes/épaisses)
- **Inertie de rotation** des sections transversales de l'arbre
- **Effets gyroscopiques** dus à la rotation des disques

**Observation clé:** Le placement asymétrique des disques crée une distribution de masse déséquilibrée qui influencera les formes modales et les vitesses critiques.

---

## 2. FRÉQUENCES NATURELLES ET MODES PROPRES (0-5000 RPM)

### 2.1 Résultats de l'Analyse Modale

Les fréquences naturelles ont été calculées à quatre vitesses de rotation différentes:

#### **À 0 RPM (Condition statique):**
**Fréquences naturelles (Hz):**
  Mode 1: wd = 9.57 Hz, wn = 9.57 Hz
  Mode 2: wd = 9.93 Hz, wn = 9.93 Hz
  Mode 3: wd = 34.74 Hz, wn = 34.74 Hz
  Mode 4: wd = 37.42 Hz, wn = 37.42 Hz
  Mode 5: wd = 85.91 Hz, wn = 85.91 Hz
  Mode 6: wd = 87.97 Hz, wn = 87.97 Hz

#### **À 1000 RPM:**
**Fréquences naturelles (Hz):**
  Mode 1: wd = 9.56 Hz, wn = 9.56 Hz
  Mode 2: wd = 9.93 Hz, wn = 9.93 Hz
  Mode 3: wd = 34.66 Hz, wn = 34.66 Hz
  Mode 4: wd = 37.49 Hz, wn = 37.49 Hz
  Mode 5: wd = 85.91 Hz, wn = 85.91 Hz
  Mode 6: wd = 87.46 Hz, wn = 87.46 Hz

#### **À 2500 RPM:**
**Fréquences naturelles (Hz):**
  Mode 1: wd = 9.53 Hz, wn = 9.53 Hz
  Mode 2: wd = 9.96 Hz, wn = 9.96 Hz
  Mode 3: wd = 34.28 Hz, wn = 34.28 Hz
  Mode 4: wd = 37.82 Hz, wn = 37.82 Hz
  Mode 5: wd = 85.03 Hz, wn = 85.03 Hz
  Mode 6: wd = 85.91 Hz, wn = 85.91 Hz

#### **À 5000 RPM:**
**Fréquences naturelles (Hz):**
  Mode 1: wd = 9.43 Hz, wn = 9.43 Hz
  Mode 2: wd = 10.04 Hz, wn = 10.04 Hz
  Mode 3: wd = 33.28 Hz, wn = 33.28 Hz
  Mode 4: wd = 38.63 Hz, wn = 38.63 Hz
  Mode 5: wd = 78.40 Hz, wn = 78.40 Hz
  Mode 6: wd = 85.91 Hz, wn = 85.91 Hz

---

## 3. INVESTIGATION DE LA DYNAMIQUE À 0 ET 5000 RPM

### 3.1 Comparaison entre 0 RPM et 5000 RPM

#### **À 0 RPM (Condition non-rotative):**
1ère fréquence naturelle: 9.57 Hz
2ème fréquence naturelle: 9.93 Hz
Effets gyroscopiques: Aucun (vitesse nulle)

#### **À 5000 RPM (Condition opérationnelle):**
1ère fréquence naturelle: 9.43 Hz
2ème fréquence naturelle: 10.04 Hz
Effets gyroscopiques: Présents (séparation des modes)

### 3.2 Variation des Fréquences
Mode 1: -0.14 Hz
Mode 2: +0.12 Hz

---

## 4. DIAGRAMME DE CAMPBELL ET EXPLICATION

### 4.1 Description du Diagramme de Campbell

Le diagramme de Campbell trace les fréquences naturelles (Hz) en fonction de la vitesse de rotation (RPM) sur la plage 0-5500 RPM. Il constitue un outil fondamental en rotordynamique pour identifier les vitesses critiques.
<img width="1200" height="800" alt="newplot (1)" src="https://github.com/user-attachments/assets/6f3c57a8-9d15-458f-91c5-62cef7b3f296" />

