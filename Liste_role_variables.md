# 🧾 Variables du convertisseur de bases numériques (V4.x)

Ce document a pour objectif de servir de **référence pédagogique** pour ton programme
de conversion de bases numériques. Il est pensé pour :
- t’aider à retrouver rapidement le rôle de chaque variable ;
- comprendre **où** elle est utilisée (globale ou locale) ;
- faciliter l’évolution du code (ajout de fonctionnalités, refactorisation, etc.) ;
- servir de support pour d’autres programmeurs ou étudiants.

> 💡 N’hésite pas à compléter / corriger ce fichier au fur et à mesure.

---

## 1. Variables globales principales

Ces variables sont définies au niveau du module (en dehors des fonctions) et sont
utilisées dans plusieurs parties du programme.

| Nom de la variable        | Type / Widget   | Rôle / Description                                                                 | Où elle est définie              | Remarques                          |
|---------------------------|-----------------|-------------------------------------------------------------------------------------|----------------------------------|------------------------------------|
| `VERSION`                 | `str`           | Numéro de version du programme (ex. `"4.3-dev"`). Affichée dans le titre et l’À propos. | En haut du script                | À mettre à jour à chaque version.  |
| `BASE_DIR`                | `Path`          | Dossier racine du script. Sert de base pour construire les chemins (`Langues/`, `Aides/`, etc.). | En haut du script (section imports) | Utile pour compatibilité .exe.     |
| `fenetre`                 | `tk.Tk`         | Fenêtre principale de l’application.                                               | Dans l’initialisation de l’UI    | Racine de toute l’interface Tkinter. |
| `langue_actuelle`         | `str`           | Code de langue courant (`"fr"`, `"en"`, …).                                        | Initialisée au début du script   | Modifiée par `changer_langue()`.   |
| `textes_langues`          | `dict`          | Dictionnaire contenant tous les textes UI pour la langue actuelle (chargé depuis `.json`). | Juste après `langue_actuelle`    | Alimenté par `charger_traductions()`. |
| `zone_texte_aide`         | `tk.Text` \| `None` | Widget qui affiche le texte d’aide. `None` tant que l’aide n’a pas été ouverte. | Global + dans `afficher_aide()`  | Mis à jour par `charger_fichier_aide()`. |
| `panneau_aide`            | `tk.LabelFrame` \| `None` | Conteneur (frame / labelframe) qui entoure la zone d’aide.                        | Global + dans `afficher_aide()`  | Son titre change avec la langue.   |
| `bouton_fermer_aide`      | `tk.Button` \| `None` | Bouton “Fermer” de la zone d’aide.                                                 | Global + dans `afficher_aide()`  | Le texte change avec la langue.    |
| `zone_texte_contexte`     | `tk.Text` \| `None` | Widget qui affiche le texte de contexte.                                           | Global + dans `afficher_contexte()` | Même logique que l’aide.        |
| `panneau_contexte`        | `tk.LabelFrame` \| `None` | Conteneur pour la zone de contexte.                                                | Global + dans `afficher_contexte()` | Titre mis à jour sur changement de langue. |
| `bouton_fermer_contexte`  | `tk.Button` \| `None` | Bouton “Fermer” pour le panneau de contexte.                                       | Global + dans `afficher_contexte()` | Texte mis à jour par `changer_langue()`. |
| `binaire_brut_var`        | `tk.StringVar`  | Contient la valeur brute affichée dans la zone binaire.                            | Zone d’initialisation des widgets | Utilisée pour l’affichage dynamique. |
| `hexadecimal_brut_var`    | `tk.StringVar`  | Contient la valeur brute affichée dans la zone hexadécimale.                       | Idem                              |                                    |
| `format_binaire_var`      | `tk.StringVar`  | Choix du format d’affichage binaire (brut, 4 bits, 8 bits, etc.).                  | Idem                              | Texte initial = `textes_langues["brut"]`. |
| `format_hexadecimal_var`  | `tk.StringVar`  | Choix du format d’affichage hexadécimal.                                           | Idem                              | Même logique que pour le binaire. |

> ℹ️ Tu peux compléter ce tableau avec toutes les autres variables globales
> que tu ajoutes (icônes, couleurs, polices, etc.).

---

## 2. Variables par fonction

Dans cette section, chaque fonction importante du programme a son propre petit tableau
pour lister **ses paramètres** et **ses variables locales**.

L’idée est pédagogique : comprendre ce qui “vit” **à l’intérieur** de chaque fonction,
par opposition aux variables globales ci-dessus.

> 💡 Astuce : tu peux plier/déplier les fonctions dans VS Code (`Ctrl + K, Ctrl + 1`)
> pour naviguer facilement dans le fichier Python pendant que tu complètes ce document.

---

### 2.1. `changer_langue(nouvelle_langue)`

**Rôle de la fonction :**  
Met à jour la langue de l’interface (textes, menus, labels) en fonction du code passé
(`"fr"`, `"en"`, …), recharge les traductions et met à jour les panneaux d’aide et de contexte
s’ils sont ouverts.

**Paramètres :**

| Nom             | Type | Rôle                                                      |
|-----------------|------|-----------------------------------------------------------|
| `nouvelle_langue` | `str` | Code de langue demandé (`"fr"`, `"en"`, etc.).        |

**Variables utilisées dans la fonction :**

| Nom                    | Portée   | Rôle / Description                                              |
|------------------------|----------|-----------------------------------------------------------------|
| `langue_actuelle`      | globale  | Mise à jour avec `nouvelle_langue`.                            |
| `textes_langues`       | globale  | Rechargé via `charger_traductions(...)`.                       |
| `zone_texte_aide`      | globale  | Si non `None`, le texte est rechargé via `charger_fichier_aide()`. |
| `panneau_aide`         | globale  | Son titre est mis à jour avec `textes_langues["titre_aide"]`.  |
| `bouton_fermer_aide`   | globale  | Son texte est mis à jour avec `textes_langues["fermer"]`.      |
| `zone_texte_contexte`  | globale  | Idem pour la zone de contexte (si ouverte).                    |
| `panneau_contexte`     | globale  | Titre mis à jour selon la langue.                              |
| `bouton_fermer_contexte` | globale | Texte mis à jour pour le bouton “Fermer” du contexte.         |

> ✏️ À compléter : d’autres labels, menus, boutons mis à jour dans cette fonction.

---

### 2.2. `afficher_aide()`

**Rôle de la fonction :**  
Crée (ou affiche) le panneau d’aide dans la fenêtre principale, initialise la zone
de texte d’aide et charge le contenu depuis le fichier d’aide correspondant à la langue.

**Variables locales et globales utilisées :**

| Nom                   | Portée   | Rôle / Description                                             |
|-----------------------|----------|----------------------------------------------------------------|
| `panneau_aide`        | globale  | Frame / LabelFrame principal de la section aide.              |
| `zone_texte_aide`     | globale  | Widget `Text` qui contient le texte d’aide.                   |
| `bouton_fermer_aide`  | globale  | Bouton pour fermer le panneau d’aide.                         |
| `textes_langues`      | globale  | Récupère les traductions du titre d’aide et des boutons.      |
| `fenetre`             | globale  | Parent du panneau d’aide.                                     |

> ✏️ Tu peux noter ici les paramètres visuels : largeur/hauteur, scrollbars, etc.

---

### 2.3. `charger_fichier_aide()`

**Rôle de la fonction :**  
Lire le fichier texte d’aide (`Aides/aide_<langue>.txt`) correspondant à `langue_actuelle`
et l’afficher dans `zone_texte_aide` (en lecture seule).

**Variables :**

| Nom               | Portée   | Rôle / Description                                             |
|-------------------|----------|----------------------------------------------------------------|
| `zone_texte_aide` | globale  | Widget `Text` à remplir.                                       |
| `langue_actuelle` | globale  | Sert à construire le nom du fichier d’aide.                   |
| `BASE_DIR`        | globale  | Sert à construire un chemin robuste vers le fichier texte.    |
| `chemin`          | locale   | Chemin complet vers le fichier `aide_<langue>.txt`.           |
| `contenu`         | locale   | Texte lu dans le fichier d’aide.                              |

> 🧠 Rappel : le passage en `state="normal"` puis `state="disabled"` permet de modifier
> le widget tout en le laissant non-éditable pour l’utilisateur.

---

### 2.4. `afficher_contexte()`

*(À compléter selon ta version exacte du code)*

**Rôle de la fonction :**  
Afficher un panneau de “Contexte” expliquant les bases numériques, le but pédagogique
du programme, et éventuellement quelques notions de cryptographie / informatique.

**Variables à documenter :**

| Nom                      | Portée   | Rôle / Description                                      |
|--------------------------|----------|---------------------------------------------------------|
| `panneau_contexte`       | globale  | Frame / LabelFrame pour le contexte.                    |
| `zone_texte_contexte`    | globale  | Zone de texte pour afficher le contenu de contexte.     |
| `bouton_fermer_contexte` | globale  | Bouton pour fermer ce panneau.                          |
| `textes_langues`         | globale  | Titre, texte du bouton, etc.                            |

---

### 2.5. `afficher_a_propos()`

**Rôle de la fonction :**  
Afficher une petite fenêtre popup “À propos” avec le nom du programme, la version,
tes informations d’auteur et un lien vers le dépôt GitHub.

**Variables typiques :**

| Nom              | Portée   | Rôle / Description                                                |
|------------------|----------|-------------------------------------------------------------------|
| `popup_a_propos` | locale   | Fenêtre `Toplevel` pour le “À propos”.                           |
| `couleur`        | locale   | Couleur de fond choisie aléatoirement.                           |
| `largeur`/`hauteur` | locales | Dimensions de la fenêtre popup.                               |
| `x`, `y`         | locales  | Coordonnées pour centrer la fenêtre sur l’écran.                 |
| `texte_principal`| locale   | Texte principal pris dans `textes_langues["a_propos_texte"]`.    |
| `VERSION`        | globale  | Injectée dans l’affichage de la version.                         |

> ✏️ Tu peux ajouter aussi les labels, le bouton “Fermer”, et la fonction interne
> `ouvrir_github()` si tu l’as définie dedans.

---

## 3. Modèle à réutiliser pour d’autres fonctions

Tu peux copier/coller ce modèle pour documenter n’importe quelle fonction de ton
programme :

```markdown
### 2.x. `nom_de_la_fonction(param1, param2, ... )`

**Rôle de la fonction :**  
(Explique en une ou deux phrases ce que fait la fonction.)

**Paramètres :**

| Nom   | Type | Rôle |
|-------|------|------|
|       |      |      |

**Variables utilisées dans la fonction :**

| Nom      | Portée   | Rôle / Description |
|----------|----------|--------------------|
|          | locale   |                    |
|          | globale  |                    |
