# 🧭 Memo Sheet — Tkinter: Menus & Mouse Events

This memo complements the one on keyboard shortcuts.  
It explains how to create menus, context menus, and manage mouse events in Tkinter — all while keeping your French variable names.

---

## 🍔 1) Application Menus (Menu Bar)

```python
menu_principal = tk.Menu(fenetre)

# File Menu
menu_fichier = tk.Menu(menu_principal, tearoff=0, postcommand=None)
menu_fichier.add_command(label="Nouveau", command=nouveau_fichier)
menu_fichier.add_separator()
menu_fichier.add_command(label="Quitter", accelerator="Ctrl+Q", command=fenetre.destroy)
menu_principal.add_cascade(label="Fichier", menu=menu_fichier)

# Tools Menu (e.g., modules)
menu_outils = tk.Menu(menu_principal, tearoff=0)
menu_outils.add_command(label="Calculs bin./hex.", command=ouvrir_module_calculs)
menu_outils.add_command(label="Opérations logiques", command=ouvrir_module_logique)
menu_principal.add_cascade(label="Outils", menu=menu_outils)

# Help Menu
menu_aide = tk.Menu(menu_principal, tearoff=0)
menu_aide.add_command(label="Aide", accelerator="F1", command=afficher_aide)
menu_aide.add_command(label="Contexte", command=afficher_contexte)
menu_principal.add_cascade(label="Aide", menu=menu_aide)

fenetre.config(menu=menu_principal)
```

**Notes:**
- `tearoff=0` removes the dotted line at the top of menus.
- `postcommand=` allows you to execute a function **just before the menu opens** (useful for enabling/disabling items dynamically).

---

## 🔘 2) Special Menu Elements

```python
etat_son = tk.BooleanVar(value=True)
mode_vue = tk.StringVar(value="hexa")

menu_options = tk.Menu(menu_principal, tearoff=0)
menu_options.add_checkbutton(label="Activer le son", onvalue=True, offvalue=False, variable=etat_son)
menu_options.add_radiobutton(label="Affichage binaire", value="bin", variable=mode_vue)
menu_options.add_radiobutton(label="Affichage hexadécimal", value="hexa", variable=mode_vue)

# Enable/disable a menu item by its index
menu_options.entryconfig(0, state="disabled")
menu_options.entryconfig(0, state="normal")
```

**Remember:**
- `add_checkbutton` and `add_radiobutton` automatically link to Tkinter variables.
- `entryconfig(index, state=...)` enables or disables menu entries dynamically.

---

## 📜 3) Context Menu (Right-click)

```python
class MenuContextuel:
    def __init__(self, parent):
        self.menu = tk.Menu(parent, tearoff=0)
        self.menu.add_command(label="Copier", command=self.copier)
        self.menu.add_command(label="Coller", command=self.coller)

    def afficher(self, event):
        try:
            self.menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.menu.grab_release()

    def copier(self): ...
    def coller(self): ...

# Usage
ctx = MenuContextuel(fenetre)
fenetre.bind("<Button-3>", ctx.afficher)
```

**Platform Differences:**
- Windows/Linux: right-click → `<Button-3>`  
- macOS: right-click may be `<Button-2>`  
  ```python
  widget.bind("<Button-2>", ctx.afficher)
  widget.bind("<Button-3>", ctx.afficher)
  ```

---

## 🖱️ 4) Common Mouse Events

| Pattern | Meaning |
|:--|:--|
| `<Button-1>` | Left-click (press) |
| `<ButtonRelease-1>` | Left-click release |
| `<Double-Button-1>` | Double-click |
| `<B1-Motion>` | Drag while holding left button |
| `<Enter>` / `<Leave>` | Mouse enters / leaves the widget |
| `<Motion>` | Mouse moves over widget |
| `<MouseWheel>` | Scroll wheel (Windows/Linux) |
| `<Button-4>` / `<Button-5>` | Scroll wheel (X11) |

**Examples:**
```python
def on_click(e): print("Clic en:", e.x, e.y)
def on_drag(e): print("Drag:", e.x, e.y)

zone.bind("<Button-1>", on_click)
zone.bind("<B1-Motion>", on_drag)
```

---

## 🔄 5) Mouse Wheel — Platform Differences

### Windows / Linux
```python
def on_wheel(e):
    if e.delta > 0:
        print("Scroll up")
    else:
        print("Scroll down")

fenetre.bind_all("<MouseWheel>", on_wheel)
```

### X11 Compatibility
```python
def on_wheel_up(e): print("Scroll up")
def on_wheel_down(e): print("Scroll down")
fenetre.bind_all("<Button-4>", on_wheel_up)
fenetre.bind_all("<Button-5>", on_wheel_down)
```

### macOS
- `<MouseWheel>` usually works, but `e.delta` values may vary (±1 or ±120).

---

## 🎯 6) Event Coordinates and Information

```python
def on_double_click(e):
    print("Widget:", e.widget, "/ xy:", e.x, e.y, "/ root:", e.x_root, e.y_root)

liste.bind("<Double-Button-1>", on_double_click)
```

**Useful attributes:**
- `e.x`, `e.y`: widget-relative coordinates  
- `e.x_root`, `e.y_root`: screen coordinates  
- `e.widget`: event source widget  
- `e.state`: modifier keys (Ctrl, Shift, etc.)  

---

## 🧼 7) Binding Scope: Widget vs Global

- `widget.bind("<Button-1>", cb)` → only applies to that widget  
- `fenetre.bind_all("<Button-1>", cb)` → applies globally

**Best Practices:**
- Use `bind` for local interactions.  
- Use `bind_all` for global actions (shortcuts, app-wide commands).

---

## 🧪 8) Example: Entry + Context Menu

```python
def copier_selection(entry):
    try:
        selection = entry.selection_get()
        entry.clipboard_clear()
        entry.clipboard_append(selection)
    except tk.TclError:
        pass

def coller_clipboard(entry):
    try:
        entry.insert(tk.INSERT, entry.clipboard_get())
    except tk.TclError:
        pass

def build_context_menu(entry):
    m = tk.Menu(entry, tearoff=0)
    m.add_command(label="Copier", command=lambda: copier_selection(entry))
    m.add_command(label="Coller", command=lambda: coller_clipboard(entry))

    def popup(e):
        try:
            m.tk_popup(e.x_root, e.y_root)
        finally:
            m.grab_release()

    entry.bind("<Button-3>", popup)
    entry.bind("<Button-2>", popup)
    return m

entree = tk.Entry(fenetre)
entree.pack(padx=10, pady=10, fill="x")
build_context_menu(entree)
```

---

## ✅ 9) Quick Checklist (Menus & Mouse)

- [ ] `tearoff=0` on all menus  
- [ ] Use `postcommand=` for dynamic item activation  
- [ ] Use `add_checkbutton` / `add_radiobutton` when needed  
- [ ] Support right-click (`<Button-3>` + `<Button-2>`)  
- [ ] Add scroll wheel compatibility (`<MouseWheel>` + `<Button-4/5>`)  
- [ ] Use `x_root/y_root` for menu popup positioning  
- [ ] Avoid excessive use of `bind_all`

---

Cheers to the developer’s red Chimay! 🍺😄
