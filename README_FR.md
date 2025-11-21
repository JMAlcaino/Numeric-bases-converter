# 🧮 Convertisseur de Bases Numériques — Interface Tkinter

**Auteur :** Jean‑Marc (Jean) ALCAÏNO

**Assistant :** Pylo 

**Dernière mise à jour :** 20/11/2025

**Langage :** Python 3 + Tkinter

**Licence :** Open source – usage personnel et éducatif

**Version :** 4.3.1

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
- Panneaux d’aide et de contexte latéraux (`LabelFrame`) :  
  - Textes issu de fichiers externes 
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
- [🧭 Fiche 1 – Raccourcis clavier et gestion des événements](./Documentation/Fiche_1_memo_Tkinter_raccourcis.md)  
- [🧭 Fiche 2 – Menus et événements souris](./Documentation/Fiche_2_memo_Tkinter_menus_souris.md)  
- [🧭 Fiche 3 – Widgets essentiels & Internationalisation (i18n)](./Documentation/Fiche_3_memo_Tkinter_widgets_i18n.md)
- [🧭 Fiche 4 – PyInstaller](./Documentation/Fiche_4_memo_PyInstaller.md)
- [🧭 Fiche 5 – Bouton actions Tkinter](./Documentation/Fiche_5_Mémo_bouton_actions_Tkinter_FR.md)
- [🧭 Fiche 6 – Rappels des mises à jour de /main par /dev dans GitHUb](./Documentation/Fiche_6_git_convertisseur.md)
- [🧭 Fiche 7 – Navigation et raccourcis clavier utiles dans VSCode](./Documentation/Fiche_7_Mémo_Navigation_VSCode_python.md)
- [🧭 Fiche 8 – Problématique des widgets détruits dans Tkinter](./Documentation/Fiche_8_Mémo_widgets_detruits.md)

### 🇬🇧 Memo Sheets (English)
- [🧭 Memo 1 – Tkinter Keyboard Shortcuts](./Documentation/Memo_1_EN_Tkinter_shortcuts.md)  
- [🧭 Memo 2 – Tkinter Menus & Mouse Events](./Documentation/Memo_2_Tkinter_menus_mouse.md)
- [🧭 Memo 3 – Tkinter Widgets & Internationalization (i18n)](./Documentation/Memo_3_Tkinter_widgets_i18n.md)
- [🧭 Memo 4 – PyInstaller](./Documentation/Memo_4_PyInstaller_EN.md)
- [🧭 Memo 5 – Tkinter Button actions](./Documentation/Memo_5_Tkinter_Button_Actions.md)
- [🧭 Memo 6 – GitHub /main update from /dev](./Documentation\Memo_6_EN_git_convertisseur.md)
- [🧭 Memo 7 – VSCode navigation and shortkeys](./Documentation\Memo_7_EN_Navigation_VSCode_python.md)
- [🧭 Memo 8 – Destructed widgets problems in Tkinter](./Documentation/Memo_8_EN_Destructed_widgets_.md)

---

## 🔜 Évolutions prévues  
- Module de calculs binaires / hexadécimaux  
- Module de logique booléenne (AND, OR, XOR, NOT…)  
- Export des résultats dans un fichier texte  
- Version exécutable multi‑plateforme  
- Publication GitHub complète avec exemples et captures d'écran
- Intégration dans un projet pédagogique plus large de découverte et pratique de cryptographie.

---

## 👤 Auteur
Développé par **Jean‑Marc (Jean) Alcaïno**  
Avec l’assistance fidèle de **Pylo**

---

## 📜 Licence
Projet **open source** destiné à un usage personnel et éducatif.  
Reproduction et réutilisation autorisées avec mention de l’auteur.
