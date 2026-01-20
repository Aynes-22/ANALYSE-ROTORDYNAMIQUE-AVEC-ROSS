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

### Configuration du Modèle
- **11 nœuds** numérotés de 0 à 10
- **10 éléments d'arbre** uniformes
- **2 éléments disques** positionnés asymétriquement
- **2 éléments paliers** aux extrémités

<img width="1200" height="600" alt="newplot" src="https://github.com/user-attachments/assets/93fdb8b0-5744-41e8-9e54-568f48044d97" />

**Figure 1: Visualisation du système rotor avec disques (rouge) et paliers (bleu)**
***Le modèle par éléments finis du rotor a été créé avec ROSS***

Le modèle de Timoshenko inclut les effets de cisaillement, l'inertie de rotation et les effets gyroscopiques. Le placement asymétrique des disques (40% et 70% de la longueur) influence les formes modales.

---

## 2. FRÉQUENCES NATURELLES ET MODES PROPRES (0-5000 RPM)

### 2.1 Résultats de l'Analyse Modale

Les fréquences naturelles ont été calculées à quatre vitesses de rotation différentes:

| Vitesse | Mode 1 | Mode 2 | Mode 3 | Mode 4 | Mode 5 | Mode 6 |
|---------|--------|--------|--------|--------|--------|--------|
| **0 RPM** | 9.57 Hz | 9.93 Hz | 34.74 Hz | 37.42 Hz | 85.91 Hz | 87.97 Hz |
| **1000 RPM** | 9.56 Hz | 9.93 Hz | 34.66 Hz | 37.49 Hz | 85.91 Hz | 87.46 Hz |
| **2500 RPM** | 9.53 Hz | 9.96 Hz | 34.28 Hz | 37.82 Hz | 85.03 Hz | 85.91 Hz |
| **5000 RPM** | 9.43 Hz | 10.04 Hz | 33.28 Hz | 38.63 Hz | 78.40 Hz | 85.91 Hz |

### Observations

**À 0 RPM:** Les modes se présentent par paires proches (9.57/9.93 Hz, 34.74/37.42 Hz, 85.91/87.97 Hz) en raison de l'anisotropie des paliers (kxx ≠ kyy). Chaque paire correspond aux modes horizontal et vertical d'une même forme de flexion.

**Évolution avec la vitesse:** 
- Les modes 1-2 (premiers modes de flexion) montrent une séparation croissante: l'écart passe de 0.36 Hz (0 RPM) à 0.61 Hz (5000 RPM)
- Les modes 3-4 montrent également une séparation accrue: de 2.68 Hz à 5.35 Hz
- Les modes 5-6 convergent avec la vitesse: écart de 2.06 Hz à 0 RPM, réduction significative à 5000 RPM

Cette séparation croissante illustre le **couplage gyroscopique** qui différencie les modes forward et backward.

---

## 3. INVESTIGATION DE LA DYNAMIQUE À 0 ET 5000 RPM

### 3.1 Comparaison entre 0 RPM et 5000 RPM

**À 0 RPM (statique):**
- 1ère fréquence: **9.57 Hz**
- 2ème fréquence: **9.93 Hz**
- Modes de flexion purs, pas de couplage gyroscopique

**À 5000 RPM (opérationnel):**
- 1ère fréquence: **9.43 Hz** (variation: **-0.14 Hz**)
- 2ème fréquence: **10.04 Hz** (variation: **+0.12 Hz**)
- Effets gyroscopiques présents avec séparation des modes

### Interprétation Physique

**Mode 1 (diminution):** Le mode backward voit sa fréquence diminuer avec la vitesse. L'effet gyroscopique crée un "ramollissement" pour la précession rétrograde.

**Mode 2 (augmentation):** Le mode forward voit sa fréquence augmenter. L'effet gyroscopique rigidifie le système pour la précession directe.

**Anisotropie des paliers:** La différence kxx < kyy crée deux fréquences distinctes pour chaque forme modale, visible même à 0 RPM. À haute vitesse, les effets gyroscopiques amplifient cette séparation.

Le moment gyroscopique **M = Ip × Ω × ω** couple les directions orthogonales. Pour ce système avec deux disques significatifs (Ip totale ≈ 0.92 kg·m²), l'effet est mesurable mais modéré dans la plage 0-5000 RPM.

---

## 4. DIAGRAMME DE CAMPBELL ET EXPLICATION

![Diagramme de Campbell](https://github.com/user-attachments/assets/6f3c57a8-9d15-458f-91c5-62cef7b3f296)

**Figure 2:** Diagramme de Campbell (0-5500 RPM)

### Éléments du Diagramme

**Courbes observées:**
- **Modes forward (triangles):** Légère augmentation avec la vitesse (effet de rigidification gyroscopique)
- **Modes backward (triangles inversés):** Légère diminution avec la vitesse
- **Ligne 1X (bleue):** Fréquence d'excitation synchrone (balourd)
- **Points critiques (×):** Intersections indiquant les vitesses critiques

### Identification des Vitesses Critiques

D'après le diagramme, **deux vitesses critiques** principales sont visibles dans la plage 0-5000 RPM:

1. **1ère vitesse critique:** ~**570-600 RPM** (~9.5-10 Hz)
   - Intersection entre le premier mode forward et la ligne 1X
   - Correspond au premier mode de flexion

2. **2ème vitesse critique:** ~**2100-2250 RPM** (~35-37.5 Hz)
   - Intersection entre le deuxième mode forward et la ligne 1X
   - Correspond au deuxième mode de flexion

### Comportement Gyroscopique

Les courbes montrent:
- **Séparation modérée** entre forward et backward (système à moments d'inertie intermédiaires)
- **Stabilité générale** des fréquences (variations < 10% dans la plage analysée)
- **Effets anisotropes** visibles par le dédoublement de chaque famille modale

Les modes de haute fréquence (>80 Hz) restent quasiment constants car les effets gyroscopiques sont proportionnellement plus faibles.

---

## 5. CONCLUSIONS

### Résultats Principaux

1. **Modélisation:** Le système rotor-paliers a été modélisé avec succès via 10 éléments de Timoshenko incluant cisaillement, inertie rotationnelle et gyroscopie.

2. **Anisotropie dominante:** L'anisotropie des paliers (kyy = 1.5 × kxx) crée un dédoublement systématique des modes (horizontal/vertical) plus marqué que les effets gyroscopiques dans cette plage de vitesse.

3. **Vitesses critiques identifiées:**
   - **~600 RPM** (1er mode, ~9.5-10 Hz)
   - **~2200 RPM** (2ème mode, ~35-37.5 Hz)

4. **Effets gyroscopiques mesurables:** Variations des fréquences < 2 Hz entre 0 et 5000 RPM. L'effet est réel mais modéré comparé à l'anisotropie.

### Recommandations Opérationnelles

**Zones à éviter (±10% API):**
- 540-660 RPM autour de la 1ère critique
- 1980-2420 RPM autour de la 2ème critique

**Stratégies:**
- Fonctionnement **sous-critique** (< 540 RPM) pour éviter toute résonance
- Si fonctionnement > 600 RPM: **équilibrage précis** requis (grade G2.5)
- **Passage rapide** lors de la traversée des critiques au démarrage
- **Surveillance vibratoire** recommandée pour détecter tout balourd

### Caractérisation du Rotor

Ce rotor est **flexible** (1ère critique à ~600 RPM << 5000 RPM). Un équilibrage multi-plans sera nécessaire pour tout fonctionnement au-delà de 600 RPM.

L'anisotropie des paliers (ratio 1.5:1) domine le comportement dynamique et nécessite une attention particulière lors de l'équilibrage et du diagnostic vibratoire.
