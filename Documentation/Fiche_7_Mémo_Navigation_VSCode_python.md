# Navigation et Productivité dans VS Code (Python)

Ce mémo rassemble les raccourcis et outils de navigation **indispensables** dans VS Code pour améliorer rapidement l’efficacité dans ton projet *Numeric Bases Converter* — en particulier pour explorer, comprendre et réorganiser le code.

---

# 🧭 1. Navigation dans le code

## ▶️ Aller à la définition
**F12**

Permet d’aller directement à l’endroit où une variable, fonction ou classe est définie.

Très utile pour :
- trouver l’origine d’une `StringVar()`
- suivre le parcours d’une fonction
- inspecter un menu Tkinter ou un callback

---

## ▶️ Rechercher toutes les références
**Shift + F12**

C’est l’outil le plus plus puissant pour comprendre un programme :

- liste *toutes* les lignes où un symbole apparaît  
- indique la fonction / section dans laquelle il est utilisé  
- affichage clair et cliquable  
- parfait pour nettoyer et refactorer

---

## ▶️ Aller à un symbole
**Ctrl + Shift + O**

Affiche une liste :
- de toutes les fonctions  
- de toutes les classes  
- des variables globales  
- des sections du code

Tu peux taper quelques lettres pour filtrer.

---

## ▶️ Rechercher un fichier
**Ctrl + P**

Permet d’ouvrir n’importe quel fichier du projet rapidement.

Très utile dans les projets structurés en dossiers (comme ton dossier /Documentation, /Langues, /src, etc.).

---

## ▶️ Rechercher dans un fichier
**Ctrl + F**

Recherche simple.

---

## ▶️ Rechercher dans tout le projet
**Ctrl + Shift + F**

Affiche toutes les occurrences dans tous les fichiers du projet.

Indispensable quand tu modifies :
- un texte
- une variable
- un nom de fonction
- une clé JSON de traduction

---

# 🔙 2. Navigation “comme un navigateur web”

## ▶️ Retour en arrière
**Alt + ←**

Reviens là où tu étais avant (comme un navigateur web).

## ▶️ Avancer
**Alt + →**

Refait le chemin inverse.

Super pratique quand tu explores une suite de fonctions.

---

# 🎯 3. Outils visuels de repérage

Grâce à ta configuration améliorée :

- la **ligne active** est surlignée  
- le **numéro de ligne actif** est en couleur jaune  
- les **occurrences des variables** sont mises en évidence  
- le thème se rafraîchit immédiatement

Cela rend beaucoup plus simple :
- le suivi d’une variable
- l’analyse de sections complexes
- la préparation au passage vers des classes

---

# 🔧 4. Astuces pratiques

### 📌 Sélectionner rapidement une ligne
Clique dans la marge gauche, ou utilise :
```
Ctrl + L
```

### 📌 Déplacer une ligne / un bloc
```
Alt + ↑
Alt + ↓
```

### 📌 Copier une ligne rapidement
```
Shift + Alt + ↓
```

### 📌 Formater le document (indentation propre)
```
Shift + Alt + F
```

---

# 🛠️ 5. Pour préparer le passage aux classes

Ces fonctions t’aideront énormément pour :
- repérer quelles fonctions doivent être regroupées
- isoler les variables globales à transformer en attributs
- comprendre les dépendances entre parties du code
- restructurer progressivement ton convertisseur

VS Code devient alors un **véritable outil d’analyse du code**.

---

# ✨ Conclusion

Avec ces raccourcis et outils :

- tu vas débugger plus vite  
- mieux comprendre la structure du code  
- éviter les erreurs lors des réorganisations  
- et préparer un passage propre vers une architecture orientée objets  

Ce mémo est pensé pour accompagner l’évolution de ton projet.

**Per Scientiam, ad Caelum ✈️**  
Ton copilote Pylo
