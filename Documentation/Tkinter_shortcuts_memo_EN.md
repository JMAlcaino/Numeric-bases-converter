# 🧭 Memo Sheet — Tkinter: Keyboard Shortcuts & Key Event Management

This memo summarizes how to create and manage keyboard shortcuts in Tkinter, making your interface more fluid and professional while keeping your code clear.

---

## 🎹 1. Adding a Keyboard Shortcut (menu display only)

> This option only *displays the shortcut text in the menu*  
> It does **not** make the shortcut functional on its own.

```python
menu_fichier.add_command(
    label="Quitter",
    accelerator="Ctrl+Q",   # Text displayed on the right side of the menu
    command=fenetre.destroy
)
```

**Display:**
```
Quitter       Ctrl+Q
```

---

## ⌨️ 2. Making the Shortcut Functional (bind_all / bind)

> Associates a key combination with a Python action  
> `bind_all` → active in the entire application  
> `bind` → active only on a specific widget

```python
fenetre.bind_all("<Control-q>", lambda e: fenetre.destroy())  # Quit
fenetre.bind_all("<F1>", lambda e: afficher_aide())           # Open help
```

---

## 🧩 3. Common Key Syntaxes

| Syntax | Action |
|:--|:--|
| `<Control-q>` | Ctrl + Q |
| `<Control-Shift-s>` | Ctrl + Shift + S |
| `<Alt-F4>` | Alt + F4 |
| `<F1>` to `<F12>` | Function keys |
| `<Escape>` | Escape |
| `<Return>` | Enter |
| `<space>` | Space bar |
| `<Tab>` | Tab |
| `<BackSpace>` | Backspace |
| `<Delete>` | Delete |
| `<Up>`, `<Down>`, `<Left>`, `<Right>` | Arrow keys |
| `<KeyPress-a>` | Pressing key “a” (lowercase) |
| `<KeyRelease-A>` | Releasing key “A” (uppercase) |

---

## 🧠 4. The “event” Object (e)

When a shortcut is bound, the called function receives an **`event` object** containing information about the pressed key.

```python
def touche_appuyee(e):
    print(f"Touche : {e.keysym}  |  Code : {e.keycode}")

fenetre.bind_all("<Key>", touche_appuyee)
```

💬 Example output:
```
Touche : a  |  Code : 65
```

---

## 🧰 5. Useful Tips and Tricks

- **Combine display + action:**
  ```python
  menu_fichier.add_command(label="Quitter", accelerator="Ctrl+Q", command=fenetre.destroy)
  fenetre.bind_all("<Control-q>", lambda e: fenetre.destroy())
  ```
  👉 perfect consistency between menu and shortcut.

- **Restrict a shortcut to a specific widget:**
  ```python
  entree.bind("<Return>", lambda e: convertir())
  ```
  Pressing “Enter” will trigger conversion without clicking the button.

- **Temporarily disable a shortcut:**
  ```python
  fenetre.unbind_all("<Control-q>")
  ```

---

## 💡 6. Best Practices

✅ Always show keyboard shortcuts in menus (`accelerator=`).  
✅ Group your `bind_all` commands in a dedicated section after window creation.  
✅ Use `lambda e:` when the `event` parameter isn’t needed.  
✅ For complex actions, define a proper function with `(event)` as an argument.  

---

## ✨ Complete Example

```python
# Menu
menu_fichier.add_command(label="Quitter", accelerator="Ctrl+Q", command=fenetre.destroy)
menu_aide.add_command(label="Aide", accelerator="F1", command=afficher_aide)

# Bindings
fenetre.bind_all("<Control-q>", lambda e: fenetre.destroy())
fenetre.bind_all("<F1>", lambda e: afficher_aide())
fenetre.bind_all("<Control-e>", lambda e: effacer())
fenetre.bind_all("<Control-r>", lambda e: convertir())
```

---

💾 **Bonus Tip for Your Converter:**
You could display a small message such as:  
> “Tip: Use **Ctrl+R** to convert quickly or **F1** to open help.”

…in your message zone or side panel, for a more educational and friendly feel 😉

