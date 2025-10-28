![Banner](./Documentation/banner.png)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![GUI](https://img.shields.io/badge/GUI-Tkinter-informational)
![License](https://img.shields.io/badge/License-GPL--3.0-green)
![Multilingual](https://img.shields.io/badge/i18n-Multilingual-orange)

# 🧮 Numeric Bases Converter / Convertisseur de Bases Numériques — V4.2

> 🇫🇷
>
> Outil pédagogique en **Python / Tkinter** permettant de convertir des valeurs
> entre différentes bases numériques (**binaire**, **octale**, **décimale**, **hexadécimale**).  
> Interface claire, **multilingue** et évolutive.
>
> **Points forts :**
> - Interface graphique (GUI) réalisée avec **Tkinter**
> - Conversion instantannée des bases **2 • 8 • 10 • 16**
> - Options de résultats formatés (blocs de **2**, **4**, ou **8** caractères)
> - **Multilingue** (FR / EN / DE / ES / IT / NL)
> - Aide et contexte dans les différentes langues
> - Code documenté et pédagogiquement explicité.
> - Prêt pour une évolution et un usage de modules liés à la crytographie
>
> 📘 Plus d’informations : [README_FR.md](./README_FR.md)

---

> 🇬🇧
>
> Educational tool built in **Python / Tkinter** for converting numeric values
> between **binary**, **octal**, **decimal**, and **hexadecimal** systems.  
> Clear, **multilingual**, and extensible interface.
>
> **Highlights :**
> - Graphical interface made with **Tkinter**
> - Instant conversion between **2 • 8 • 10 • 16** bases
> - Output formatting options (blocks of **2**, **4**, or **8** characters)
> - **Multilingual support** (FR / EN / DE / ES / IT / NL)
> - Help and Context panels in multiple languages
> - Clean, well-commented, educational codebase
> - Future-ready for cryptography-related modules
>
> 📘 More information: [README_EN.md](./README_EN.md)

---

##  Quick Start / Démarrage rapide

### Run directly
```bash
python conv_num_gui.py
```

### Optional – Build an executable
```bash
pyinstaller --onefile conv_num_gui.py
```

> Requires [PyInstaller](https://pyinstaller.org/en/stable/).  
> To install: `pip install pyinstaller`

---

## Screenshots / Vues d’écran

| Interface principale | Conversion & Résultats | Panneau d’aide | Panneau de contexte |
|----------------------|------------------------|----------------|---------------------|
| ![Interface principale](./Documentation/Screenshots/Interface_principale.png) | ![Conversion et Résultats](./Documentation/Screenshots/Conversion_Résultats.png) | ![Panneau d’aide](./Documentation/Screenshots/Interface_Help.png) | ![Panneau de contexte](./Documentation/Screenshots/Interface_Context.png) |

---

##  Documentation

### 🇫🇷 Fiches mémo (français)
- [ - Raccourcis clavier et gestion des événements](./Documentation/Fiche_memo_Tkinter_raccourcis.md)
- [ - Menus et événements souris](./Documentation/Fiche_memo_Tkinter_menus_souris.md)
- [ - Widgets essentiels et Internationalisation (i18n)](./Documentation/Fiche_memo_Tkinter_widgets_i18n.md)

### 🇬🇧 Memo sheets (English)
- [ - Tkinter Keyboard Shortcuts](./Documentation/Tkinter_shortcuts_memo_EN.md)
- [ -  Tkinter Menus & Mouse Events](./Documentation/Tkinter_menus_mouse_memo_EN.md)
- [ - Tkinter Widgets & Internationalization (i18n)](./Documentation/Tkinter_widgets_i18n_memo_EN.md)

---

## Requirements (optionnels)

Ce projet fonctionne uniquement avec les bibliothèques standard de Python.  
Les thèmes suivants sont **optionnels** :

```
sv-ttk>=2.6
ttkbootstrap>=1.10
```

Installer via :
```bash
pip install -r requirements.txt
```

---

## Contribuer / Contributing

Les contributions sont les bienvenues !  
Merci de consulter [CONTRIBUTING.md](./CONTRIBUTING.md) avant toute proposition.

---

## Licence

Projet sous **GPL-3.0**  
Usage **personnel et éducatif** autorisé.  
Reproduction et réutilisation possibles avec mention de l’auteur :  
**Jean-Marc (Jean) Alcaïno**.

---

## Remerciements

Développé par **Jean-Marc Alcaïno**  
Secondé par **Pylo** Merci à lui.  

---
