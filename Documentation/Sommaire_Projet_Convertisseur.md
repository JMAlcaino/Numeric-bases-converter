# Projet : Convertisseur de bases numériques & Aide interactive

**Auteur :** Jean-Marc Alcaïno    
**Langage :** Python 3 + Tkinter

---

##  Objectifs
- Créer un outil graphique complet pour convertir des valeurs numériques entre bases.
- Offrir une interface ergonomique, pédagogique et extensible.
- Ajouter un panneau d’aide intégré et des fonctionnalités pratiques de visualisation.
- Servir de base/modèle pour d'autres projets Tkinter futurs.

---

##  Fonctionnalités actuelles

- Interface Tkinter avec `LabelFrame`, `Entry`, `Label`, `Button`
- Choix de la base d’entrée (10, 2, 8, 16)
- Conversion complète en binaire, octal, décimal, hexadécimal
- Menus déroulants pour format d’affichage : blocs de 2, 4, 8 ou brut
- Labels redimensionnables dynamiquement
- Copie possible par bouton 📋 ou clic droit
- Collage dans le champ d'entrée avec clic droit
- Gestion basique des entiers négatifs avec message d’information
- Pop-up “À propos” avec `Toplevel` centré dynamiquement
- Panneau latéral d’aide (LabelFrame), avec :
  - Texte issu d’un fichier `aide.txt`
  - Zone `Text` défilable avec Scrollbar et molette souris
  - Fermeture par bouton
- Code structuré, commenté et pédagogique

---

##  Exemple de fonction utilisée : `charger_aide()`

```python
def charger_aide(zone_texte):
    try:
        # Ouvre le fichier d'aide en lecture avec encodage UTF-8
        with open("aide.txt", "r", encoding="utf-8") as f:
            contenu = f.read()  # Lit tout le contenu du fichier
            zone_texte.delete("1.0", tk.END)  # Efface le texte existant
            zone_texte.insert(tk.END, contenu)  # Insère le texte lu
    except FileNotFoundError:
        # En cas de fichier manquant, affiche un message dans la zone
        zone_texte.insert(tk.END, "⚠️ Fichier d'aide introuvable.")
```

---

##  À venir
- Animation de panneau d’aide (déroulement latéral)
- Export des résultats dans un fichier texte
- Préparation de version exécutable multi-plateforme
- Publication GitHub et documentation enrichie

---

##  Auteur

Développé par **Jean-Marc Alcaïno**  
Assistant **Pylo**

---

##  Licence

Open source – usage personnel et éducatif.
