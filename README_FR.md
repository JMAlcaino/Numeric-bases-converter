# 🧮 Convertisseur de Bases Numériques — Interface Tkinter

**Auteur :** Jean‑Marc (Jean)  
**Assistant :** Pylo 🧙‍♂️  
**Dernière mise à jour :** 2025‑04‑18  
**Langage :** Python 3 + Tkinter  
**Licence :** Open source – usage personnel et éducatif
**Version :** 4.1.1

---

## 📖 Sommaire
- [🎯 Objectifs](#-objectifs)
- [✅ Fonctionnalités actuelles](#-fonctionnalités-actuelles)
- [⚙️ Installation et exécution](#️-installation-et-exécution)
- [📘 Documentation](#-documentation)
- [🔜 Évolutions prévues](#-évolutions-prévues)
- [👤 Auteur](#-auteur)
- [📜 Licence](#-licence)

---

## 🎯 Objectifs
- Créer un outil graphique complet pour convertir des valeurs numériques entre différentes bases.  
- Offrir une interface ergonomique, pédagogique et extensible.  
- Intégrer un panneau d’aide et un affichage formaté (groupes de bits/digits).  
- Servir de base et de modèle pour d’autres projets Tkinter.

---

## ✅ Fonctionnalités actuelles
- Interface graphique réalisée avec **Tkinter** (`LabelFrame`, `Entry`, `Label`, `Button`…)  
- Choix de la base d’entrée : décimale (10), binaire (2), octale (8) ou hexadécimale (16)  
- Conversion automatique vers les quatre bases  
- Menus déroulants pour formatage : blocs de 2, 4, 8 caractères ou brut  
- Labels dynamiquement redimensionnables selon la longueur du résultat  
- Copie des résultats par bouton 📋 ou clic droit  
- Collage dans le champ d’entrée via clic droit  
- Gestion des entiers négatifs avec message d’avertissement  
- Fenêtre « À propos » (`Toplevel`) centrée automatiquement  
- Panneau d’aide latéral (`LabelFrame`) :  
  - Texte issu du fichier externe `aide.txt`  
  - Zone `Text` défilable avec barre de défilement et molette souris  
  - Bouton de fermeture dédié  
- Code structuré, commenté et orienté apprentissage

---

## ⚙️ Installation et exécution

### 🧩 Prérequis
- **Python 3.10+**
- Module standard : `tkinter` (installé par défaut avec Python)

### ▶️ Lancer l’application
```bash
python conv_num_gui.py
```

### 💡 Astuce
Pour générer un exécutable :
```bash
pyinstaller --onefile conv_num_gui.py
```

---

## 📘 Documentation

### 🇫🇷 Fiches mémo (français)
- [🧭 Fiche 1 – Raccourcis clavier et gestion des événements](./Documentation/Fiche_memo_Tkinter_raccourcis.md)  
- [🧭 Fiche 2 – Menus et événements souris](./Documentation/Fiche_memo_Tkinter_menus_souris.md)  
- [🧭 Fiche 3 – Widgets essentiels & Internationalisation (i18n)](./Documentation/Fiche_memo_Tkinter_widgets_i18n.md)

### 🇬🇧 Memo Sheets (English)
- [🧭 Memo 1 – Tkinter Keyboard Shortcuts](./Documentation/Tkinter_shortcuts_memo_EN.md)  
- [🧭 Memo 2 – Tkinter Menus & Mouse Events](./Documentation/Tkinter_menus_mouse_memo_EN.md)  
- [🧭 Memo 3 – Tkinter Widgets & Internationalization (i18n)](./Documentation/Tkinter_widgets_i18n_memo_EN.md)

---

## 🔜 Évolutions prévues
- Animation latérale du panneau d’aide  
- Module de calculs binaires / hexadécimaux  
- Module de logique booléenne (AND, OR, XOR, NOT…)  
- Export des résultats dans un fichier texte  
- Version exécutable multi‑plateforme  
- Publication GitHub complète avec exemples et captures

---

## 👤 Auteur
Développé par **Jean‑Marc (Jean)**  
Avec l’assistance fidèle de **Pylo**, compagnon magique du code 🧙‍♂️

---

## 📜 Licence
Projet **open source** destiné à un usage personnel et éducatif.  
Reproduction et réutilisation autorisées avec mention de l’auteur.
