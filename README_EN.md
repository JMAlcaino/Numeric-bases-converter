# 🧮 Numeric Base Converter — Tkinter GUI Application

**Author:** Jean‑Marc (Jean)  
**Assistant:** Pylo  
**Last updated:** 2025‑11‑20 
**Language:** Python 3 + Tkinter  
**License:** Open source – for personal and educational use

**Version:** 4.3.1


---

## 📖 Table of Contents
- [🎯 Goals](#-goals)
- [✅ Current Features](#-current-features)
- [⚙️ Installation & Execution](#️-installation--execution)
- [📘 Documentation](#-documentation)
- [🔜 Planned Improvements](#-planned-improvements)
- [👤 Author](#-author)
- [📜 License](#-license)

---

## 🎯 Goals
- Build a complete graphical tool to convert numbers between different bases.  
- Provide a user‑friendly, educational, and extensible interface.  
- Integrate a contextual help panel and output formatting options.  
- Serve as a learning base and template for future Tkinter projects.

---

## ✅ Current Features
- Graphical interface built with **Tkinter** (`LabelFrame`, `Entry`, `Label`, `Button`…)  
- Select input base: decimal (10), binary (2), octal (8), hexadecimal (16)  
- Automatic conversion to all four bases  
- Dropdown menus to format output in blocks of 2, 4, 8 characters or raw  
- Dynamic label resizing depending on content length  
- Copy results via 📋 button or right‑click  
- Paste into the input field via right‑click  
- Basic handling of negative integers with warning message  
- “About” popup (`Toplevel`) automatically centered  
- Lateral help panel (`LabelFrame`) with:  
  - Text loaded from `aide.txt` external file  
  - Scrollable `Text` widget with scrollbar and mouse‑wheel support  
  - Close button  
- Clean, structured, and well‑commented code

---

## ⚙️ Installation & Execution

### 🧩 Requirements
- **Python 3.10+**
- Standard module : `tkinter` (included by default)

### ▶️ Run the Application
```bash
python conv_num_gui.py
```

### 💡 Tip
To create an executable file :
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
- [🧭 Fiche 5 – Boutons actions Tkinter](./Documentation/Fiche_5_Mémo_bouton_actions_Tkinter_FR.md)
- [🧭 Fiche 6 – Rappels des mises à jour de /main par /dev dans GitHUb](./Documentation/Fiche_6_git_convertisseur.md)

### 🇬🇧 Memo Sheets (English)
- [🧭 Memo 1 – Tkinter Keyboard Shortcuts](./Documentation/Memo_1_EN_Tkinter_shortcuts.md)  
- [🧭 Memo 2 – Tkinter Menus & Mouse Events](./Documentation/Memo_2_Tkinter_menus_mouse.md)
- [🧭 Memo 3 – Tkinter Widgets & Internationalization (i18n)](./Documentation/Memo_3_Tkinter_widgets_i18n.md)
- [🧭 Memo 4 – PyInstaller](./Documentation/Memo_4_PyInstaller_EN.md)
- [🧭 Memo 5 – Tkinter Button actions](./Documentation/Memo_5_Tkinter_Button_Actions.md)
- [🧭 Memo 6 – GitHub /main update from /dev](./Documentation\Memo_6_EN_git_convertisseur.md)
---

## 🔜 Planned Improvements
- Sliding help‑panel animation  
- Binary / hexadecimal calculation module  
- Logic operation module (AND, OR, XOR, NOT…)  
- Export results to a text file  
- Multi‑platform executable version  
- GitHub release with examples and extended documentation
- Integration into a broader educational project on cryptography exploration and practice

---

## 👤 Author
Developed by **Jean‑Marc (Jean) Alcaïno**  
With the loyal guidance of **Pylo**

---

## 📜 License
**Open source** project for personal and educational use.  
Reuse and redistribution are allowed with proper credit.
