#  Memo Sheet — Creating an Executable with PyInstaller

##  Purpose
This document explains how to create a standalone executable of the **Numeric Bases Converter** application  
using the **PyInstaller** library.

---

##  Installing PyInstaller

First, install PyInstaller via pip:

```bash
pip install pyinstaller
```

Check the installation:
```bash
pyinstaller --version
```

---

##  Building a Simple Executable

In the folder containing your main file `conv_num_gui.py`, run:

```bash
pyinstaller --onefile conv_num_gui.py
```

 This command creates a `dist/` subfolder containing your single executable:  
`dist/conv_num_gui.exe` (or without extension on Linux/Mac).

---

##  Including Required Resources

To make your executable fully functional, you must **include all external resources** used by your program:

- Translation files (`Langues/`)
- Help and Context texts (`Textes/`)
- Images (banners, icons, flags, etc.)

### On **Windows**:
```bash
pyinstaller --onefile ^
--add-data "Langues;Langues" ^
--add-data "Textes;Textes" ^
--add-data "Documentation;Documentation" ^
conv_num_gui.py
```

### On **Linux / macOS**:
```bash
pyinstaller --onefile --add-data "Langues:Langues" --add-data "Textes:Textes" --add-data "Documentation:Documentation" conv_num_gui.py
```

 Syntax:
```
--add-data "source;destination"  (Windows)
--add-data "source:destination"  (Linux/Mac)
```

This tells PyInstaller to bundle these folders inside the final executable.

---

##  Recommended Folder Structure Before Compilation

```
Numeric-bases-converter/
│
├── conv_num_gui.py
├── Langues/
├── Textes/
├── Documentation/
│   ├── Memo_PyInstaller_EN.md
│   ├── README_FR.md
│   ├── README_EN.md
│   └── screenshots/
│
├── requirements.txt
└── README.md
```

---

##  Running the Compiled Program

After building, the executable can be found here:
```
dist/conv_num_gui.exe
```

You can move it anywhere; it is **fully standalone**.  
However, it will use the embedded folders you specified during compilation.

---

##  Useful Options

- 🔹 Add `--noconsole` to hide the terminal window (for Tkinter apps):
  ```bash
  pyinstaller --onefile --noconsole conv_num_gui.py
  ```

- 🔹 Add a **custom icon**:
  ```bash
  pyinstaller --onefile --noconsole --icon=Documentation/icon.ico conv_num_gui.py
  ```

- 🔹 Clean previous build files:
  ```bash
  pyinstaller --clean --onefile conv_num_gui.py
  ```

---

##  Complete Example (Windows)

```bash
pyinstaller --onefile --noconsole ^
--icon=Documentation/icon.ico ^
--add-data "Langues;Langues" ^
--add-data "Textes;Textes" ^
--add-data "Documentation;Documentation" ^
conv_num_gui.py
```

### Result:
- A clean and standalone executable  
- All internal resources embedded  
- No external dependencies required on the target machine

---

##  Post-Build Checklist

- Run `dist/conv_num_gui.exe` and check:
  - Translations work correctly  
  - Help and Context panels open properly  
  - Icons and flags display as expected

---

## 📚 9️⃣ References

- [Official PyInstaller Documentation](https://pyinstaller.org/en/stable/)
- [Numeric Bases Converter GitHub Repository](https://github.com/JMAlcaino/Numeric-bases-converter)

---

 **Written by Jean-Marc Alcaïno **  
 Version: 1.0 — March 2025
