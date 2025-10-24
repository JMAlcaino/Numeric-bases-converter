# 🧭 Memo Sheet — Tkinter: Essential Widgets & Internationalization (i18n)

This sheet combines the fundamentals for creating modern, multilingual Tkinter interfaces:  
🎨 **Essential widgets** and 🌍 **language management (i18n)**.

---

## 🎨 1) Essential Tkinter Widgets

Tkinter provides simple and lightweight widgets for building user interfaces.

| Widget | Description | Example |
|:--|:--|:--|
| `Label` | Displays text or an image. | `tk.Label(fenetre, text="Bonjour")` |
| `Button` | Clickable button triggering a command. | `tk.Button(fenetre, text="OK", command=action)` |
| `Entry` | Single-line text input field. | `tk.Entry(fenetre)` |
| `Text` | Multi-line text area. | `tk.Text(fenetre, height=10, width=40)` |
| `LabelFrame` | Container with a labeled frame. | `tk.LabelFrame(fenetre, text="Options")` |
| `Frame` | Base container for layout. | `tk.Frame(fenetre)` |
| `Checkbutton` | Boolean checkbox. | `tk.Checkbutton(fenetre, text="Activer", variable=etat)` |
| `Radiobutton` | Single-choice button. | `tk.Radiobutton(fenetre, text="Option A", variable=choix, value=1)` |
| `OptionMenu` | Simple dropdown menu. | `tk.OptionMenu(fenetre, var, *options)` |
| `Scrollbar` | Scroll bar (vertical or horizontal). | `tk.Scrollbar(zone)` |

---

### 🧩 2) Widget Layout Systems

| Method | Description | Example |
|:--|:--|:--|
| `.pack()` | Stacks widgets vertically or horizontally. | `label.pack(padx=10, pady=5)` |
| `.grid()` | Grid layout (rows and columns). | `bouton.grid(row=0, column=1)` |
| `.place()` | Absolute positioning (in pixels). | `widget.place(x=50, y=20)` |

💡 **Tips:**
- Never mix `pack()` and `grid()` in the same container.
- Use `Frame` and `LabelFrame` to structure the layout.
- Use `expand=True` and `fill='both'` for responsive resizing.

---

### 🪟 3) Dynamic Window Resizing

```python
fenetre.update_idletasks()
fenetre.geometry("")              # Auto adjust size
fenetre.minsize(width, height)    # Set a minimum size
```

Ideal when resizing after a language change or text update.

---

## 🌍 4) Internationalization (i18n)

### 📁 Recommended Folder Structure
```
/lang/
 ├── lang_fr.json
 ├── lang_en.json
 └── lang_es.json
```

Each file contains interface translations for a given language.

**Example `lang_fr.json`**
```json
{
  "titre": "Convertisseur de bases numériques",
  "btn_convertir": "Convertir",
  "btn_effacer": "Effacer",
  "btn_quitter": "Quitter",
  "menu_fichier": "Fichier",
  "menu_aide": "Aide",
  "menu_langue": "Langue"
}
```

**Example `lang_en.json`**
```json
{
  "titre": "Numeric base converter",
  "btn_convertir": "Convert",
  "btn_effacer": "Clear",
  "btn_quitter": "Quit",
  "menu_fichier": "File",
  "menu_aide": "Help",
  "menu_langue": "Language"
}
```

---

### 🔄 Loading Language Files

```python
import json

def charger_traductions(fichier):
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"titre": "Erreur : fichier de langue introuvable"}
```

---

### 🗣️ Updating the Interface

```python
def mettre_a_jour_interface():
    fenetre.title(textes_langues["titre"])
    bouton_convertir.config(text=textes_langues["btn_convertir"])
    bouton_effacer.config(text=textes_langues["btn_effacer"])
    bouton_quitter.config(text=textes_langues["btn_quitter"])
```

---

### 🚩 Switching Language Dynamically

```python
def changer_langue(nouvelle_langue):
    global langue_actuelle, textes_langues
    langue_actuelle = nouvelle_langue
    nom_fichier = f"lang_{nouvelle_langue}.json"
    textes_langues = charger_traductions(nom_fichier)
    mettre_a_jour_interface()
    fenetre.update_idletasks()
    fenetre.geometry("")
```

💡 Place this function in the `command=` of your language flag buttons.

---

### 🧠 Best Practices for i18n

✅ Store each language in separate `.json` files.  
✅ Encode files in **UTF-8** (for accented characters).  
✅ Always call `update_idletasks()` after switching languages.  
✅ Avoid hard-coded strings — always use `textes_langues["key"]`.  
✅ Use clear, consistent key names (`btn_*`, `menu_*`, `titre_*`).

---

### ✨ Minimal Example

```python
import tkinter as tk, json

# Default load
def charger_traductions(fichier):
    with open(fichier, "r", encoding="utf-8") as f:
        return json.load(f)

textes_langues = charger_traductions("lang_fr.json")

# Window
fenetre = tk.Tk()
fenetre.title(textes_langues["titre"])

# Widgets
label = tk.Label(fenetre, text=textes_langues["titre"])
bouton_convertir = tk.Button(fenetre, text=textes_langues["btn_convertir"])
label.pack(pady=10)
bouton_convertir.pack(pady=5)

# Language switch
def changer_langue(nouvelle_langue):
    global textes_langues
    textes_langues = charger_traductions(f"lang_{nouvelle_langue}.json")
    fenetre.title(textes_langues["titre"])
    label.config(text=textes_langues["titre"])
    bouton_convertir.config(text=textes_langues["btn_convertir"])

# Language buttons
tk.Button(fenetre, text="FR", command=lambda: changer_langue("fr")).pack(side="left", padx=10)
tk.Button(fenetre, text="EN", command=lambda: changer_langue("en")).pack(side="left", padx=10)

fenetre.mainloop()
```

---

### 📚 Final Checklist
- [x] Create a `lang/` folder with `.json` files  
- [x] Load language at startup using `charger_traductions()`  
- [x] Update text dynamically with `mettre_a_jour_interface()`  
- [x] Provide a menu or buttons to switch languages  
- [x] Verify UTF-8 encoding for accented text  
- [x] Avoid any hard-coded strings in the UI  

---

✨ *Happy coding, Commandant Jean! You now have a solid base to build elegant, educational, multilingual Tkinter interfaces.* 🇫🇷🇬🇧🇪🇸
