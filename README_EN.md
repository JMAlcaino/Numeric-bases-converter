# Project: Numeric Base Converter with Interactive Help

**Author:** Jean-Marc (Jean)  
**Assistant:** Pylo 🧙‍♂️  
**Last updated:** 2025-04-18  
**Language:** Python 3 + Tkinter

---

## 🎯 Goals
- Build a complete graphical tool to convert numbers between different bases.
- Offer a user-friendly, educational, and extensible interface.
- Include an integrated help panel and useful formatting options.
- Serve as a reference base for future Tkinter projects.

---

## ✅ Current Features

- GUI using Tkinter: `LabelFrame`, `Entry`, `Label`, `Button`
- Choose input base (decimal, binary, octal, hexadecimal)
- Full conversion to binary, octal, decimal, hexadecimal
- Dropdown menus to format output into blocks of 2, 4, 8 characters or raw
- Dynamic label resizing based on output
- Copy results via 📋 button or right-click
- Paste into input field using right-click
- Basic support for negative integers with warning message
- “About” popup using a centered `Toplevel` window
- Help panel (LabelFrame) with:
  - Text loaded from external file `aide.txt`
  - Scrollable `Text` widget with scrollbar and mouse wheel support
  - Close button
- Clean and well-commented code

---

## 🛠️ Example function: `charger_aide()`

```python
def charger_aide(zone_texte):
    try:
        with open("aide.txt", "r", encoding="utf-8") as f:
            content = f.read()
            zone_texte.delete("1.0", tk.END)
            zone_texte.insert(tk.END, content)
    except FileNotFoundError:
        zone_texte.insert(tk.END, "⚠️ Help file not found.")
```

---

## 🔜 Planned Features
- Animated sliding help panel
- Export results to text file
- Create a multi-platform executable version
- GitHub release with full documentation

---

## 👤 Author

Developed by **Jean-Marc (Jean)**  
With the magical guidance of **Pylo**, code companion 🧙‍♂️

---

## 📜 License

Open source – for personal and educational use.
