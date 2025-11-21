#  Fiche mémo — Création d’un exécutable avec PyInstaller

##  Objectif
Ce document explique comment créer un exécutable autonome de l’application **Numeric Bases Converter**
à l’aide de la bibliothèque **PyInstaller**.

---

##  Installation de PyInstaller

Avant toute chose, installer PyInstaller via pip :

```bash
pip install pyinstaller
```

Vérifier ensuite l’installation :
```bash
pyinstaller --version
```

---

##  Génération d’un exécutable simple

Dans le dossier où se trouve le fichier principal `conv_num_gui.py`, exécute :

```bash
pyinstaller --onefile conv_num_gui.py
```

 Cette commande crée un sous-dossier `dist/` contenant l'exécutable unique :  
`dist/conv_num_gui.exe` (ou sans extension sur Linux/Mac).

---

##  Inclure les ressources nécessaires

Pour que l'exécutable fonctionne correctement, il faut **inclure les fichiers externes** utilisés par le programme :

- Les traductions (`Langues/`)
- Les textes d’aide et de contexte (`Textes/`)
- Les images (bannières, icônes, drapeaux…)

### Sous **Windows** :
```bash
pyinstaller --onefile ^
--add-data "Langues;Langues" ^
--add-data "Textes;Textes" ^
--add-data "Documentation;Documentation" ^
conv_num_gui.py
```

### Sous **Linux / macOS** :
```bash
pyinstaller --onefile --add-data "Langues:Langues" --add-data "Textes:Textes" --add-data "Documentation:Documentation" conv_num_gui.py
```

 Syntaxe :
```
--add-data "source;destination"  (Windows)
--add-data "source:destination"  (Linux/Mac)
```

Cela indique à PyInstaller d’embarquer les dossiers tels quels dans le `.exe`.

---

##  Structure recommandée avant compilation

```
Numeric-bases-converter/
│
├── conv_num_gui.py
├── Langues/
├── Textes/
├── Documentation/
│   ├── Fiche_memo_PyInstaller.md
│   ├── README_FR.md
│   ├── README_EN.md
│   └── screenshots/
│
├── requirements.txt
└── README.md
```

---

##  Exécuter le programme compilé

Une fois la compilation terminée, l’exécutable se trouve ici :
```
dist/conv_num_gui.exe
```

On peut le déplacer n’importe où, il est **autonome**.
Cependant, pour qu’il trouve les fichiers inclus, utilise les chemins relatifs du projet.

---

##  Astuces utiles

- 🔹 Ajouter `--noconsole` pour cacher la fenêtre de terminal (programmes Tkinter).
  ```bash
  pyinstaller --onefile --noconsole conv_num_gui.py
  ```

- 🔹 Ajouter une **icône personnalisée** :
  ```bash
  pyinstaller --onefile --noconsole --icon=Documentation/icon.ico conv_num_gui.py
  ```

- 🔹 Nettoyer les anciens fichiers de build :
  ```bash
  pyinstaller --clean --onefile conv_num_gui.py
  ```

---

##  Exemple complet (Windows)

```bash
pyinstaller --onefile --noconsole ^
--icon=Documentation/icon.ico ^
--add-data "Langues;Langues" ^
--add-data "Textes;Textes" ^
--add-data "Documentation;Documentation" ^
conv_num_gui.py
```

### Résultat :
- Un exécutable propre et autonome
- Toutes les ressources internes embarquées
- Aucune dépendance à installer sur la machine cible

---

##  Vérification après compilation

- Lance `dist/conv_num_gui.exe` et vérifie :
  - que les traductions fonctionnent,
  - que l’aide et le contexte s’affichent,
  - que les icônes et drapeaux apparaissent correctement.

---

##  Références

- [Documentation officielle PyInstaller](https://pyinstaller.org/en/stable/)
- [Dépôt GitHub du projet Numeric Bases Converter](https://github.com/JMAlcaino/Numeric-bases-converter)

---

 **Rédigé par Jean-Marc Alcaïno **
 Version : 1.0 — Mars 2025
