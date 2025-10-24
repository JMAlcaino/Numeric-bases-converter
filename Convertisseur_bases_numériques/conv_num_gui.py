"""
############################################################################################################
 
 Filename     : conv_num_gui.py                                                                              
 Description  : A GUI numeric bases converter
 Author       : Alcaïno Jean-Marc                                                                          
 Modification : 2025/05/12                                                                            
 Version      : V 4.1.1

 GitHub       :     https://github.com/JMAlcaino/Numeric-bases-converter
 Author GitHub :    https://github.com/JMAlcaino

Ce petit logiciel a été conçu dans un but pédagogique, afin de mieux comprendre
la représentation des nombres dans différents systèmes de base utilisés en informatique.
 
 Notes de versions :
 V 3.6   : Ajout des menus et affichage de l'aide et du contexte du logiciel.
 V 4.0   : Internationalisation du logiciel avec l'ajout de boutons et d'un menu pour changer la langue de l'interface.
           Utilisation de fichiers de références linguistiques en .json afin de pouvoir modifier la langue de l'interface.
 V 4.1   : Mise en place de l'interface en allemand et en espagnol et des fichiers 'aide' et 'contexte'.
           Traduction des fichiers .json en allemand et en espagnol également.
 V 4.1.1 : Corrections de différents bugs. Affichage de l'à propos corrigé.

############################################################################################################
 
"""

# Importation des librairies
import tkinter as tk
import random
import json  # Importe la librairie de gestion des fichiers .json qui contiennent les différentes traductions des langues de l'interface.
from tkinter import PhotoImage  # Librairie qui gère les graphisme dans Tkinter utilisée pour afficher les petits drapeaux sur les boutons.


# Définitions des variables
panneau_aide_actif = None  # Variable globale servant à vérifier si un panneau d'aide est déjà ouvert afin d'éviter d'en ouvrir un autre à côté -> problèmes d'affichage.
panneau_contexte_actif = None  # Idem pour le panneau d'affichage du contexte.
langue_actuelle = "fr"  #  Variable de choix de langue (par défaut : français ).


# Définition des fonctions

def charger_traductions(fichier):  # Fonction qui charge le fichier contenant les différents textes_langues dans la langue sélectionnée.
    try:
        with open(fichier, "r", encoding="utf-8") as f:
                  return json.load(f)
    except FileNotFoundError:
        return {"titre": "Erreur : Fichier de langue introuvable"}



def mettre_a_jour_interface():
    fenetre.title(textes_langues["titre"])
    entree_labelframe.config(text=textes_langues["label_saisie"])
    resultats_labelframe.config(text=textes_langues["titre_resultats"])
    resultat_texte_binaire.config(text=textes_langues["texte_binaire"])
    resultat_texte_octal.config(text=textes_langues["texte_octal"])
    resultat_texte_entier.config(text=textes_langues["texte_decimal"])
    resultat_texte_hexadecimal.config(text=textes_langues["texte_hexadecimal"])
    bouton_convertir.config(text=textes_langues["btn_convertir"])
    bouton_effacer.config(text=textes_langues["btn_effacer"])
    bouton_quitter.config(text=textes_langues["btn_quitter"])
    erreur_labelframe.config(text=textes_langues["titre_message"])

    # Mise à jour du menu déroulant Binaire
    options_binaire = [
        textes_langues["brut"],
        textes_langues["blocs_4"],
        textes_langues["blocs_8"]
    ]
    menu_binaire = menu_format_binaire["menu"]
    menu_binaire.delete(0, "end")
    for option in options_binaire:
        menu_binaire.add_command(
            label=option,
            command=lambda val=option: (format_binaire_var.set(val), appliquer_format_binaire())
        )
    format_binaire_var.set(textes_langues["brut"])

    # Mise à jour du menu déroulant Hexadécimal
    options_hexa = [
        textes_langues["brut"],
        textes_langues["blocs_2"],
        textes_langues["blocs_4"],
        textes_langues["blocs_8"]
    ]
    menu_hexa = menu_format_hexadecimal["menu"]
    menu_hexa.delete(0, "end")
    for option in options_hexa:
     menu_hexa.add_command(
            label=option,
            command=lambda val=option: (format_hexadecimal_var.set(val), appliquer_format_hexadecimal())
        )
    format_hexadecimal_var.set(textes_langues["brut"])


def construire_menus():
    global menu_principal, menu_fichier, menu_aide, menu_langue

    # Supprimer le menu existant s’il y en a un
    fenetre.config(menu="")  # Réinitialise le menu

    # Nouveau menu principal
    menu_principal = tk.Menu(fenetre)

    # Menu Fichier
    menu_fichier = tk.Menu(menu_principal, tearoff=0)
    menu_fichier.add_command(label=textes_langues["a_propos_titre"], command=afficher_a_propos)
    menu_fichier.add_command(label=textes_langues["btn_quitter"], command=fenetre.destroy)
    menu_principal.add_cascade(label=textes_langues["menu_fichier"], menu=menu_fichier)

    # Menu Aide
    menu_aide = tk.Menu(menu_principal, tearoff=0)
    menu_aide.add_command(label=textes_langues["menu_aide"], command=afficher_aide)
    menu_aide.add_command(label=textes_langues["menu_contexte"], command=afficher_contexte)
    menu_principal.add_cascade(label=textes_langues["menu_aide"], menu=menu_aide)

    # Menu Langue
    menu_langue = tk.Menu(menu_principal, tearoff=0)
    menu_langue.add_command(label="Français", command=lambda: changer_langue("fr"))
    menu_langue.add_command(label="English", command=lambda: changer_langue("en"))
    menu_langue.add_command(label="Deutsch", command=lambda: changer_langue("de"))
    menu_langue.add_command(label="Espanol", command=lambda: changer_langue("es"))
    menu_principal.add_cascade(label=textes_langues["menu_langue"], menu=menu_langue)

    # Appliquer le menu à la fenêtre
    fenetre.config(menu=menu_principal)

# Création des boutons radio.
def mettre_a_jour_boutons_radio():
    # Suppression des anciens boutons s'ils existent
    for widget in boutons_base_frame.winfo_children():
        widget.destroy()

    # Création des nouveaux boutons en fonction de la langue
    bases = [
        textes_langues["texte_decimal"],
        textes_langues["texte_binaire"],
        textes_langues["texte_octal"],
        textes_langues["texte_hexadecimal"]
    ]

    for index, base in enumerate(bases):
        bouton = tk.Radiobutton(
            boutons_base_frame,
            text=base,
            variable=base_var,
            value=base,
            font=("arial", 9),
            anchor="w"
        )
        if index == 0:
            bouton.config(fg="#326565")
        elif index == 1:
            bouton.config(fg="#A83600")
        elif index == 2:
            bouton.config(fg="#5900B3")
        elif index == 3:
            bouton.config(fg="#C80430")
        bouton.grid(row=index, column=0, sticky="w", padx=5, pady=2)
    
    # Sélection par défaut "Décimal" dans la langue active
    base_var.set(textes_langues["texte_decimal"])


def changer_langue(nouvelle_langue):  # Fonction qui change la langue de l'interface en appelant la fonction 'mettre_a_jour_interface'. L'argument 'nouvelle_langue' est donné par appui sur le bouton du drapeau correspondant.
    global langue_actuelle, textes_langues

    # Sauvegarder d'abord la langue actuelle avant de la modifier
    ancienne_langue = langue_actuelle
    langue_actuelle = nouvelle_langue

    # Charger la nouvelle langue
    textes_langues = charger_traductions(f"lang_{langue_actuelle}.json")  # Appelle la fonction 'charger_traduction' pour ouvrir le fichier .json de la langue correspondante.

    # Re-traduction du message affiché dans erreur_label
    texte_actuel = erreur_label.cget("text")
    anciennes_traductions = charger_traductions(f"lang_{ancienne_langue}.json")

    for cle, texte in anciennes_traductions.items():
        if texte_actuel == texte and cle in textes_langues:
            erreur_label.config(text=textes_langues[cle])
            break
        
    mettre_a_jour_interface()  # Appelle la fonction qui va modifier tous les labels et autres textes_langues de l'interface dans la langue choisie.
    mettre_a_jour_boutons_radio() #Appelle la fonction de construction des boutons radio pour les mettre à jour selon la langue choisie.
    construire_menus()  # Appelle la fonction de construction des boutons pour les mettre dasn la langue choisie.
    fenetre.update_idletasks()  # Scrute la boucle d'affichage de la fenêtre principale.
    fenetre.geometry("")  # Calcule automatiquement la taille de la fenêtre pour s'ajuster aux éléments qu'elle contient.
    fenetre.minsize(fenetre.winfo_width(), fenetre.winfo_height())


def afficher_a_propos():  # Ouvre une petite fenêtre indépendante appelée par le menu 'aide' 'A propos' - Couleur de fond au hasard parmi 4 possibilités.
    bg_couleurs = ['#99CCCC', '#FFC5A8', '#D3A8FF', '#FDACBE']
    couleur = random.choice(bg_couleurs)
    popup_a_propos = tk.Toplevel(bg=couleur)
    popup_a_propos.title(textes_langues["a_propos_titre"])

    # Taille de la fenêtre popup
    largeur = 300
    hauteur = 200

    # Récupérer les dimensions de la fenêtre principale
    x_principal = fenetre.winfo_rootx()  # Position x de la fenêtre principale  .winfo... donne l'information d'une fenêtre (dimension, position...).
    y_principal = fenetre.winfo_rooty()  # Position y de la fenêtre principale.
    w_principal = fenetre.winfo_width()  # Largeur de la fenêtre principale.
    h_principal = fenetre.winfo_height()  # Hauteur de la fenêtre principale.

    # Calcul des coordonnées pour centrer la fentêtre 'popup'.
    x = x_principal + (w_principal // 2) - (largeur // 2)
    y = y_principal +(h_principal //2) - (hauteur //2)

    # Positionne la fenêtre popup
    popup_a_propos.geometry(f"{largeur}x{hauteur}+{x}+{y}")

    # Contenu de la fenêtre popup
    a_propos_label1 = tk.Label(popup_a_propos, text=textes_langues["a_propos_texte"], font=('arial', 10, 'bold'), fg='blue', bg=couleur)
    a_propos_label2 = tk.Label(popup_a_propos, text=textes_langues["a_propos_copyright"], font=('arial', 10), bg=couleur, justify='center')
    a_propos_bouton = tk.Button(popup_a_propos, text=textes_langues["fermer"], fg='green', command=popup_a_propos.destroy)
    a_propos_label1.pack(pady=10)
    a_propos_label2.pack(pady=5)
    a_propos_bouton.pack(pady=10)

def afficher_aide():
    global panneau_aide_actif  # Utilise la variable globale pour la vérification.

    # Vérifie si un panneau d'aide est déjà ouvert
    if panneau_aide_actif and panneau_aide_actif.winfo_exists():
        return
    
    # Affichage d'instructions dans le la bel des messages importants
    erreur_label.config(text=textes_langues["message_effacer"], font=('arial', 9), fg='black')

    # Conteneur principal de l’aide
    panneau_aide = tk.LabelFrame(conteneur_global, text=textes_langues["titre_aide"], font=('arial', 9), fg='blue')
    panneau_aide_actif = panneau_aide  # Signale que le panneau est bien existant

    # Conteneur vertical interne
    contenu_aide = tk.Frame(panneau_aide)
    contenu_aide.pack(fill='both', expand=True)

    # Conteneur horizontal pour le texte et la scrollbar
    bloc_texte = tk.Frame(contenu_aide)
    bloc_texte.pack(fill='both', expand=True)

    zone_texte_aide = tk.Text(bloc_texte, wrap='word', height=25, width=45)
    scroll = tk.Scrollbar(bloc_texte, command=zone_texte_aide.yview)
    zone_texte_aide.config(yscrollcommand=scroll.set)

    zone_texte_aide.pack(side='left', fill='both', expand=True)
    scroll.pack(side='right', fill='y')

    zone_texte_aide.bind("<MouseWheel>", lambda e: zone_texte_aide.yview_scroll(int(-1*(e.delta/120)), "units"))

    # Bouton de fermeture bien en dessous
    btn_fermer = tk.Button(contenu_aide, text=textes_langues["fermer"], font=('arial', 9), fg='green', command=lambda: panneau_aide.destroy())  # Autorise le scroll avec la roulette de la souris.
    btn_fermer.pack(pady=10)


    # Charger le texte d'aide
    charger_fichier_aide(zone_texte_aide)  # On passe la zone en argument à la fonction pour que le chargement du texte soit bien attibué au bon endroit.

    # Affichage
    panneau_aide.pack(side='right', fill='y', padx=10, pady=10)

def afficher_contexte():
    global panneau_contexte_actif  # Utilise la variable globla pour la vérification.

    # Vérifie si un panneau de contexte est déjà ouvert.
    if panneau_contexte_actif and panneau_contexte_actif.winfo_exists():
        return 

    # Conteneur principal du contexte
    panneau_contexte = tk.LabelFrame(conteneur_global, text=textes_langues["titre_contexte"], font=('arial', 9), fg='blue')
    panneau_contexte_actif = panneau_contexte  # Signale que le panneau est bien existant

    # Conteneur vertical interne
    contenu_contexte = tk.Frame(panneau_contexte)
    contenu_contexte.pack(fill='both', expand=True)

    # Conteneur horizontal pour le texte et la scrollbar
    bloc_texte = tk.Frame(contenu_contexte)
    bloc_texte.pack(fill='both', expand=True)

    zone_texte_contexte = tk.Text(bloc_texte, wrap='word', height=25, width=45)
    scroll = tk.Scrollbar(bloc_texte, command=zone_texte_contexte.yview)
    zone_texte_contexte.config(yscrollcommand=scroll.set)

    zone_texte_contexte.pack(side='left', fill='both', expand=True)
    scroll.pack(side='right', fill='y')

    zone_texte_contexte.bind("<MouseWheel>", lambda e: zone_texte_contexte.yview_scroll(int(-1*(e.delta/120)), "units"))

    # Bouton de fermeture bien en dessous
    btn_fermer = tk.Button(contenu_contexte, text=textes_langues["fermer"], font=('arial', 9), fg='green', command=lambda: panneau_contexte.destroy())
    btn_fermer.pack(pady=10)


    # Charger le texte d'aide
    charger_fichier_contexte(zone_texte_contexte)  # On passe la zone en argument à la fonction pour que le chargement du texte soit bien attibué au bon endroit.

    # Affichage
    panneau_contexte.pack(side='right', fill='y', padx=10, pady=10)


def charger_fichier_aide(zone_texte_aide):  # La référence est obligatoirment passée en argument pour que cela fonctionne normalement.
    try:
        aide = "aide.txt"  # Définit le nom ou le chemin du fichier 'Aide'
        with open(aide, "r", encoding="utf-8") as f:  # Le fichier est ouvert en mode 'r' -> read et encodé en UTF-8 (UNICODE) pour tenir compte des accents en français
            contenu = f.read()  # Le contenu du fichier est lu et placé dans une variable afin d'être utilisé.
            zone_texte_aide.delete("1.0", tk.END)  # La zone de texte d'aide est d'abord effacée de la 1ère à la dernière ligne.
            zone_texte_aide.insert(tk.END, contenu)  # Le contenu est inséré dans la zone de texte.
    except FileNotFoundError:  # Lève une execption en l'absence du fichier.
        zone_texte_aide.insert(tk.END, "⚠️ Fichier d'aide introuvable.\n⚠️ File not found.")


def charger_fichier_contexte(zone_texte_contexte):  # La référence est obligatoirment passée en argument pour que cela fonctionne normalement.
    try:
        contexte = "contexte.txt"  # Définit le nom ou le chemin du fichier 'Contexte'
        with open(contexte, "r", encoding="utf-8") as f:
            contenu = f.read()
            zone_texte_contexte.delete("1.0", tk.END)
            zone_texte_contexte.insert(tk.END, contenu)
    except FileNotFoundError:
        zone_texte_contexte.insert(tk.END, "⚠️ Fichier d'aide introuvable.\n⚠️ File not found.")


def convertir():
    entree_valeur = entree.get().strip()
    base_saisie = base_var.get()

    if not entree_valeur:
        erreur_label.config(text=textes_langues["aucune_valeur"], fg="red")
        return

    if entree_valeur.startswith("-"):
        erreur_label.config(text=textes_langues["note_valeur_negative"], fg="red")
        return

    try:
        if base_saisie == textes_langues["texte_decimal"]:
            n = int(entree_valeur)
        elif base_saisie == textes_langues["texte_binaire"]:
            if not all(car in "01" for car in entree_valeur):
                raise ValueError
            n = int(entree_valeur, 2)
        elif base_saisie == textes_langues["texte_octal"]:
            if not all(car in "01234567" for car in entree_valeur):
                raise ValueError
            n = int(entree_valeur, 8)
        elif base_saisie == textes_langues["texte_hexadecimal"]:
            if not all(car in "0123456789abcdefABCDEF" for car in entree_valeur):
                raise ValueError
            n = int(entree_valeur, 16)
        else:
            raise ValueError

        # Affichage des résultats
        resultat_entier.config(text=str(n))
        resultat_octal.config(text=oct(n)[2:])
        resultat_binaire.config(text=bin(n)[2:])
        resultat_hexadecimal.config(text=hex(n)[2:].upper())

        binaire_brut_var.set(bin(n)[2:])
        hexadecimal_brut_var.set(hex(n)[2:].upper())

        appliquer_format_binaire()
        appliquer_format_hexadecimal()

        erreur_label.config(text=textes_langues["message_ok"], fg="green")

    except ValueError:
        erreur_label.config(text=textes_langues["erreur_base"], fg="red")



def effacer():  # Fonction qui efface tous les chmaps des résultats et la case d'entrée de la valeur à convertir.
    entree.delete(0, tk.END)
    erreur_label.config(text=textes_langues["message_effacer"], font=('arial', 10, 'bold'), fg='green', justify='center')
    resultat_entier.config(text="", width=50)
    resultat_binaire.config(text="", width=50)
    resultat_octal.config(text="", width=50)
    resultat_hexadecimal.config(text="", width=50)


def bouton_copier(label):
    texte = label.cget("text")
    if texte:
        message = textes_langues["copie_effectuee"].format(texte)
        erreur_label.config(text=message, fg="blue")
        fenetre.clipboard_clear()
        fenetre.clipboard_append(texte)
    else:
        erreur_label.config(text=textes_langues["copie_vide"], fg="red")



def bouton_coller():  # Fonction qui traite l'appui sur le bouton 'coller' situé à gauche de la case d'entrée de la valeur afin d'y placer une valeur gardée dans le presse-papier.
    try:
        texte = fenetre.clipboard_get()  # Récupère ce qui se trouve dans le clipboard et place-le dans la variable 'texte'.
        entree.delete(0, tk.END)  # Efface le champ d'entrée d'une valeur avant de coller le clipboard.
        entree.insert(0, texte)  # Colle le texte récupéré.
        erreur_label.config(text=textes_langues["coller"], font=('arial', 10, 'bold'), fg="green")
    except tk.TclError:
        erreur_label.config(text=textes_langues["coller_vide"], font=('arial', 10, 'bold'), fg="red")


def grouper_par_blocs(texte, taille_bloc):  # Fonction qui gère la mise en bloc du résultat selon le choix du menu déroulant.
    reste = len(texte) % taille_bloc
    if reste != 0:
        texte = '0' * (taille_bloc - reste) + texte  # Ajoute un ou plusieurs '0' en fonction du nombre de caractères restants à gauche (lecture logique  de bas niveau)
    return ' '.join(texte[i:i+taille_bloc] for i in range(0, len(texte), taille_bloc))  # Retourne une chaîne de caractères séparés par un espace tous les 'x' caractères de droite à gauche. Le 'x' étant donné par la variable 'taille_bloc' en focntion du choix du menu déroulant contextuel.


def appliquer_format_binaire(*args):   # Fonction qui met à jour le label 'resultat_binaire' en fonction du choix dans le menu déroulant - *args sert à ignorer les arguments demandés par le widget 'optionMenu'
    val = format_binaire_var.get()
    texte = binaire_brut_var.get()
    if val == textes_langues["brut"]:
        resultat_binaire.config(text=texte)
    elif val == textes_langues["blocs_4"]:
        resultat_binaire.config(text=grouper_par_blocs(texte, 4))
    elif val == textes_langues["blocs_8"]:
        resultat_binaire.config(text=grouper_par_blocs(texte, 8))
       
    ajuster_label(resultat_binaire, texte)
  


def appliquer_format_hexadecimal(*args):  # Fonction qui met à jour le label 'resultat_hexadecimal' en fonction du choix dans le menu déroulant - *args sert à ignorer les arguments demandés par le widget 'optionMenu'
    val = format_hexadecimal_var.get()
    texte = hexadecimal_brut_var.get()
    if val == textes_langues["brut"]:
        resultat_hexadecimal.config(text=texte)
    elif val == textes_langues["blocs_2"]:
        resultat_hexadecimal.config(text=grouper_par_blocs(texte, 2))
    elif val == textes_langues["blocs_4"]:
        resultat_hexadecimal.config(text=grouper_par_blocs(texte, 4))
    elif val == textes_langues["blocs_8"]:
        resultat_hexadecimal.config(text=grouper_par_blocs(texte, 8))
        
    ajuster_label(resultat_hexadecimal, texte)  # Ajuste le label de résultat en fonction du nombre de caractères qu'il contient. Appelle la fonction 'ajuster_label'.


def ajuster_label(label, texte):  # ajuste le label du résultat en fonction de la longueur de la chaîne qu'il contient.
    texte = label.cget("text").replace(" ", "")  # Récupère le texte réel qui se trouve dans le label avant l'ajustement de celui-ci et enlève les espaces inutiles qui perturbent l'affichage.
    nb_caracteres = len(texte)
    label.config(width=max(50, nb_caracteres))  # Le label garde au minimum 50 caractères et au maximum la longueur du texte.
    fenetre.update_idletasks()  # Scrute la boucle d'affichage de la fenêtre principale.
    fenetre.geometry("")  # Calcule automatiquement la taille de la fenêtre pour s'ajuster aux éléments qu'elle contient.

# PROGRAMME PRINCIPAL

#Variable qui va contenir tout le dictionnaire .json de la langue
textes_langues = charger_traductions("lang_fr.json")  # Charge le fichier .json de la langue choisie et la met dans la variable 'textes_langues_langues' (Français par défaut).

# Fenêtre principale 
fenetre = tk.Tk()
fenetre.title(textes_langues["titre"])

# Charge les images des boutons de langue.
img_fr = PhotoImage(file="fr.png")
img_en = PhotoImage(file="gb.png")
img_de = PhotoImage(file="de.png")
img_es = PhotoImage(file="es.png")

# Conteneur Global pour pouvoir placer les programme principal d'un côté et les affichages d'aides et autres sur le côté droit. Encapsulage obligatoire sino on ne peut pas mettre une frame latérale.
conteneur_global = tk.Frame(fenetre)  # Crée le Frame principal conteneur des deux frames : un pour le programme principal et l'autre pour le latéral (aide).
conteneur_global.pack(fill='both', expand=True)  # Le .pack() doit être sur une ligne en dessous sinon il retourne un 'non' dans le placement.

# Boutons de changement de langue.
zone_drapeaux = tk.Frame(conteneur_global, width=100)
bouton_francais = tk.Button(zone_drapeaux, image=img_fr, command=lambda: changer_langue("fr"))  # Affiche le bouton et exécute la fonction 'changer_langue' avec 'fr' en argument.
bouton_anglais = tk.Button(zone_drapeaux, image=img_en, command=lambda: changer_langue("en"))   # Drapeau pour changer l'interface en anglais.
bouton_allemand = tk.Button(zone_drapeaux, image=img_de, command=lambda: changer_langue("de"))  # Drapeau pour changer l'interface en allemand.
bouton_espagnol = tk.Button(zone_drapeaux, image=img_es, command=lambda: changer_langue("es"))  # Drapeau pour changer l'interface en espagnol.
bouton_francais.grid(row=0, column=0, padx=5, pady=2, sticky=tk.E)
bouton_anglais.grid(row=0, column=1, padx=5, pady=2, sticky=tk.E)
bouton_allemand.grid(row=0, column=2, padx=5, pady=2, sticky=tk.E)
bouton_espagnol.grid(row=0, column=3, padx=5, pady=2, sticky=tk.E)
zone_drapeaux.pack(pady=5)

# Conteneur principal qui va contenir tous les éléments du programme principal (entrée, résultats...)
contenu_principal = tk.Frame(conteneur_global)  # Crée une frame dans le conteneur global qui affichera tous les éléments principaux du programme.
contenu_principal.pack(side='left', fill='both', expand=True)

# Variables en StringVar pour le choix du format d'affichage des label 'Binaire' et 'Hexadécimal'.
binaire_brut_var = tk.StringVar()
hexadecimal_brut_var = tk.StringVar()

format_binaire_var = tk.StringVar()
format_binaire_var.set(textes_langues["brut"])

format_hexadecimal_var = tk.StringVar()
format_hexadecimal_var.set(textes_langues["brut"])

# Appel initial des Menus de la fenêtre principale.
construire_menus()

# Zone du champ de saisie et du choix de la base numérique
entree_labelframe = tk.LabelFrame(fenetre, text=textes_langues["label_saisie"], font=('arial', 9), height=20, width=250, fg='#690F96')
entree = tk.Entry(entree_labelframe, width=80)
coller_valeur = tk.Button(entree_labelframe, text="\U0001F4E5", command=lambda: bouton_coller())
coller_valeur.grid(row=0, column=0, padx=5, sticky=tk.E)
entree.grid(row=0, column=1, pady=10, sticky=tk.W)

# -> Création des boutons radio de choix des Base numériques de départ
# -> Déclaration de la variable pour les boutons radio
base_var = tk.StringVar()
base_var.set(textes_langues["texte_decimal"])  # Valeur par défaut

# -> Création du conteneur des boutons radio
boutons_base_frame = tk.Frame(entree_labelframe,)
boutons_base_frame.grid(row=1, column=1, sticky="w", padx=5, pady=5)

# -> Appel de la fonction qui affiche dynamiquement les bons boutons selon la langue
mettre_a_jour_boutons_radio()

# -> Affichage de la zone d'entrée des valeurs/bases
entree_labelframe.pack(in_=contenu_principal, fill='both', padx=10, pady=10)

# Zone d'affichage des erreurs ou de messages importants
erreur_labelframe = tk.LabelFrame(fenetre, text=textes_langues["titre_message"], font=('arial', 9), fg='red', height=20)
erreur_labelframe.pack(in_=contenu_principal, fill='both', pady=10,padx=10)
erreur_label = tk.Label(erreur_labelframe, text=textes_langues["message_effacer"], font=('arial', 10, 'bold'), fg='green', justify='center')
erreur_label.pack(pady=5, padx=5)


# Zone d’affichage des résultats
resultats_labelframe = tk.LabelFrame(fenetre, text=textes_langues["titre_resultats"], font=('arial', 9), fg='green')

# -> Widgets d'affichage du résultat pour les Entiers
resultat_texte_entier = tk.Label(resultats_labelframe, text=textes_langues["texte_decimal"], fg="#326565", justify='right')
resultat_entier = tk.Label(resultats_labelframe, fg="#326565", bg="#99CCCC", font=('arial', 10, 'bold'), anchor='w', justify='right', relief='groove', width=50) # Les résultats à afficher seront en fonction des conversions
bouton_copier_entier = tk.Button(resultats_labelframe, text="\U0001F4CB", command=lambda: bouton_copier(resultat_entier))

# -> Widgets d'affichage du résulat pour les Binaires.
resultat_texte_binaire = tk.Label(resultats_labelframe, text=textes_langues["texte_binaire"], fg="#A83600", anchor='w', justify='right')
resultat_binaire = tk.Label(resultats_labelframe, fg="#A83600", bg="#FFC5A8", font=('arial', 10, 'bold'), anchor='w', justify='right', relief='groove', width=50)
bouton_copier_binaire = tk.Button(resultats_labelframe, text="\U0001F4CB", command=lambda: bouton_copier(resultat_binaire))
options_bin = [textes_langues["brut"], textes_langues["blocs_2"], textes_langues["blocs_4"], textes_langues["blocs_8"]]  # Options d'affichage pour le label 'resultat_binaire : format brut, en 2, 4 ou 8 bits.
menu_format_binaire = tk.OptionMenu(resultats_labelframe, format_binaire_var, *options_bin, command=appliquer_format_binaire)  # Création du menu déroulant pour le choix du format d'affichage.
menu_format_binaire.config(font=('arial', 9))

# -> Widgets d'affichage du résultat Octal.
resultat_texte_octal = tk.Label(resultats_labelframe, text=textes_langues["texte_octal"], fg="#5900B3", anchor='w', justify='right')
resultat_octal = tk.Label(resultats_labelframe, fg="#5900B3", bg="#D3A8FF", font=('arial', 10, 'bold'), anchor='w', justify='right', relief='groove', width=50)
bouton_copier_octal = tk.Button(resultats_labelframe, text="\U0001F4CB", command=lambda: bouton_copier(resultat_octal))

# -> Widget d'affichage pour le résultat en hexadécimal.
resultat_texte_hexadecimal = tk.Label(resultats_labelframe, text=textes_langues["texte_hexadecimal"], fg="#C80430", anchor='w', justify='right')
resultat_hexadecimal = tk.Label(resultats_labelframe, fg="#C80430", bg="#FDACBE", font=('arial', 10, 'bold'), anchor='w', justify='right',relief='groove', width=50)
bouton_copier_hexadecimal = tk.Button(resultats_labelframe, text="\U0001F4CB", command=lambda: bouton_copier(resultat_hexadecimal))
options_hex = [textes_langues["brut"], textes_langues["blocs_2"], textes_langues["blocs_4"], textes_langues["blocs_8"]]
menu_format_hexadecimal = tk.OptionMenu(resultats_labelframe, format_hexadecimal_var, *options_hex, command=appliquer_format_hexadecimal)
menu_format_hexadecimal.config(font=('arial', 9))

# -> Affichage des widgets 'Entier' selon la méthode .grid().
resultat_texte_entier.grid(row=0, column=0, pady=5, padx=5, sticky=tk.E)
resultat_entier.grid(row=0,column=1, pady=5, padx=5, sticky=tk.W)
bouton_copier_entier.grid(row=0, column=2, padx=5, sticky=tk.W)

# -> Affichage des widgets 'Binaire' selon la méthode .grid().
resultat_texte_binaire.grid(row=1, column=0, pady=5, padx=5, sticky=tk.E)
resultat_binaire.grid(row=1,column=1, pady=5, padx=5, sticky=tk.W)
bouton_copier_binaire.grid(row=1, column=2, padx=5, sticky=tk.W)
menu_format_binaire.grid(row=1, column=3, padx=5, sticky=tk.W)

# -> Affichage des widgets 'Octal' selon la méthode .grid().
resultat_texte_octal.grid(row=2, column=0, pady=5, padx=5, sticky=tk.E)
resultat_octal.grid(row=2,column=1, pady=5, padx=5, sticky=tk.W)
bouton_copier_octal.grid(row=2, column=2, padx=5, sticky=tk.W)

# -> Affichage des widgets 'Hexadecimal' selon la méthode .grid()
resultat_texte_hexadecimal.grid(row=3, column=0, pady=5, padx=5, sticky=tk.E)
resultat_hexadecimal.grid(row=3,column=1, pady=5, padx=5, sticky=tk.W)
bouton_copier_hexadecimal.grid(row=3, column=2, padx=5, sticky=tk.W)
menu_format_hexadecimal.grid(row=3, column=3, padx=5, sticky=tk.W)

resultats_labelframe.pack(in_=contenu_principal, fill='both', pady=10, padx=10)  # Affiche le LabelFrame container des zones d'affichage.

# Boutons
boutons_frame = tk.Frame(fenetre)
bouton_effacer = tk.Button(boutons_frame, text=textes_langues["btn_effacer"], font=('arial', 10, 'bold'), command=effacer, fg='blue')
bouton_convertir = tk.Button(boutons_frame, text=textes_langues["btn_convertir"], font=('arial', 10, 'bold'), fg='green', command=convertir)
bouton_quitter = tk.Button(boutons_frame, text=textes_langues["btn_quitter"], font=('arial', 10, 'bold'), fg='red', command=fenetre.destroy)
bouton_effacer.grid(row=0, column=0, padx=40)
bouton_convertir.grid(row=0, column=1, padx=40)
bouton_quitter.grid(row=0, column=2, padx=40)
boutons_frame.pack(in_=contenu_principal, pady=20)

# Boucle d'affichage de la fenêtre principale.
fenetre.config(menu=menu_principal)
fenetre.update_idletasks()  # Scrute la boucle d'affichage de la fenêtre principale.
fenetre.geometry("")  # Calcule automatiquement la taille de la fenêtre pour s'ajuster aux éléments qu'elle contient.
fenetre.minsize(fenetre.winfo_width(), fenetre.winfo_height())
fenetre.mainloop()
