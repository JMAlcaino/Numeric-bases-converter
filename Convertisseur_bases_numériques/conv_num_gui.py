"""
############################################################################################################
 
 Filename     : conv_num_gui.py                                                                              
 Description  : A GUI numeric bases converter
 Author       : Alcaïno Jean-Marc                                                                          
 Modification : 2025/04/16                                                                            
 Version      : V 3.51

 GitHub       :     https://github.com/JMAlcaino/Useful_Scripts
 Author GitHub :    https://github.com/JMAlcaino

############################################################################################################
 
"""

# Importation des librairies
import tkinter as tk
import random

# Définition des fonctions

def afficher_a_propos():  # Ouvre une petite fenêtre indépendante appelée par le menu 'aide' 'A propos' - Couleur de fond au hasard parmi 4 possibilités.
    bg_couleurs = ['#99CCCC', '#FFC5A8', '#D3A8FF', '#FDACBE']
    couleur = random.choice(bg_couleurs)
    popup_a_propos = tk.Toplevel(bg=couleur)
    popup_a_propos.title("À propos")
    # Taille de la fenêtre popup
    largeur = 300
    hauteur = 180
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
    tk.Label(popup_a_propos, text="Convertisseur de Bases numériques", font=('arial', 12, 'bold'), fg='blue', bg=couleur).pack(pady=10)
    tk.Label(popup_a_propos, text= "Version 3.51\n Jean-Marc Alcaïno\n© 2025", font=('arial', 10), bg=couleur, justify='center').pack(pady=5)
    tk.Button(popup_a_propos, text="Fermer", fg='green', command=popup_a_propos.destroy).pack(pady=10)


def afficher_aide():
    erreur_label.config(text="Choisissez une base à l'aide des boutons radio, entrez une valeur valide pour cette base\n et cliquez sur 'Convertir'", font=('arial', 9), fg='black')

    # Conteneur principal de l’aide
    panneau_aide = tk.LabelFrame(conteneur_global, text="Aide et fonctionnalités", font=('arial', 9), fg='blue')

    # Conteneur vertical interne
    contenu_aide = tk.Frame(panneau_aide)
    contenu_aide.pack(fill='both', expand=True)

    # Conteneur horizontal pour le texte et la scrollbar
    bloc_texte = tk.Frame(contenu_aide)
    bloc_texte.pack(fill='both', expand=True)

    zone_texte_aide = tk.Text(bloc_texte, wrap='word', height=25, width=40)
    scroll = tk.Scrollbar(bloc_texte, command=zone_texte_aide.yview)
    zone_texte_aide.config(yscrollcommand=scroll.set)

    zone_texte_aide.pack(side='left', fill='both', expand=True)
    scroll.pack(side='right', fill='y')

    zone_texte_aide.bind("<MouseWheel>", lambda e: zone_texte_aide.yview_scroll(int(-1*(e.delta/120)), "units"))

    # Bouton de fermeture bien en dessous
    btn_fermer = tk.Button(contenu_aide, text="Fermer", font=('arial', 9), fg='green', command=panneau_aide.destroy)
    btn_fermer.pack(pady=10)


    # Charger le texte d'aide
    charger_fichier_aide(zone_texte_aide)

    # Affichage
    panneau_aide.pack(side='right', fill='y', padx=10, pady=10)


def charger_fichier_aide(zone_texte_aide):
    try:
        aide = "aide.txt"  # Define the file name or path for the help file
        with open(aide, "r", encoding="utf-8") as f:
            contenu = f.read()
            zone_texte_aide.delete("1.0", tk.END)
            zone_texte_aide.insert(tk.END, contenu)
    except FileNotFoundError:
        zone_texte_aide.insert(tk.END, "⚠️ Fichier d'aide introuvable.")


def convertir():  # Fonction de conversion dans les différentes bases en fonction de la base choisie et de la valeur entrée.
    base = base_var.get()  # Récupère la 'Base' sélectionnée par le bouton-radio actif.
    valeur = entree.get()  # Récupère la valeur entrée dans le champ de saisie (widget 'entry').

    if valeur.startswith("-"):
        erreur_label.config(text="Note : Cette application à but informatique\nne traite pas les valeurs de manière mathématique.\nLes valeurs négatives ne sont donc pas prises en charge.", fg="orange" )
        return
    elif valeur == "":
        erreur_label.config(text="Aucune valeur à convertir !", font=('arial', 10, 'bold'), fg="red")
        return
    else:
        try:
            if base == 'Décimal':
                n = int(valeur)  # La valeur est en base décimale -> le texte est converti en Entier.
            elif base == 'Binaire':
                n = int(valeur, 2)  # La valeur est en base binaire -> le texte est converti en Binaire (Base 2).
            elif base == 'Octal':
                n = int(valeur, 8)  # La valeur est en base octale -> le texte est converti en Octal (Base 8).
            elif base == 'Hexadécimal':
                n = int(valeur, 16)  ## La valeur est en base héxadécimale -> le texte est converti en Hexadécimal (Base 16).
        except ValueError:
            erreur_label.config(text="Attention ! Votre entrée est invalide pour la base sélectionnée !\n Cliquez sur 'Effacer' pour recommencer !", font=('arial', 10, 'bold'), fg='red')
            return  # Stoppe ici si la valeur n'est pas convertible (sort de la boucle 'try:').
        
    # Configuration des différents labels pour affichage des résultats.
    # -> Entier   
    resultat_entier.config(text=str(n))  # La valeur est repassée en Type 'str' car le Label de résultat ne peut recevoir que du texte.

    # -> Binaire
    texte_binaire = bin(n)[2:]
    binaire_brut_var.set(texte_binaire)
    appliquer_format_binaire()  # Execute la fonction d'affichage du résultat en Binaire en fonction du choix du menu déroulant.

    # -> Octal
    resultat_octal.config(text=oct(n)[2:])  # L'indice [2:] sert à n'afficher que les chiffres sans le '0o' qui détermine un nombre octal en Python.

    # -> Hexadécimal
    texte_hexadecimal = hex(n)[2:].upper()
    hexadecimal_brut_var.set(texte_hexadecimal)
    appliquer_format_hexadecimal()

    # -> Message
    erreur_label.config(text="Cliquez sur 'Effacer' pour recommencer !", font=('arial', 10, 'bold'), fg='green')


def effacer():  # Fonction qui efface tous les chmaps des résultats et la case d'entrée de la valeur à convertir.
    entree.delete(0, tk.END)
    erreur_label.config(text="Choisissez la Base, entrez votre valeur, et cliquez sur le bouton 'Convertir'\n Ou coller une valeur avec le bouton situé à gauche.", font=('arial', 10, 'bold'), fg='green', justify='center')
    resultat_entier.config(text="", width=50)
    resultat_binaire.config(text="", width=50)
    resultat_octal.config(text="", width=50)
    resultat_hexadecimal.config(text="", width=50)


def bouton_copier(widget):  # Fonction qui traîte l'appui sur un des boutons 'copier' situés à droite de chaque label de résultat pour l'envoyer dans le presse-papier.
    texte = widget.cget("text").replace(" ", "")
    if texte == "":
       erreur_label.config(text="Aucune valeur à coller !", font=('arial', 10, 'bold'), fg="red")
    else:
        fenetre.clipboard_clear()
        fenetre.clipboard_append(texte)
        erreur_label.config(text=f"Valeur copiée : {texte}", fg="blue")


def bouton_coller():  # Fonction qui traite l'appui sur le bouton 'coller' situé à gauche de la case d'entrée de la valeur afin d'y placer une valeur gardée dans le presse-papier.
    try:
        texte = fenetre.clipboard_get()  # Récupère ce qui se trouve dans le clipboard et place-le dans la variable 'texte'.
        entree.delete(0, tk.END)  # Efface le champ d'entrée d'une valeur avant de coller le clipboard.
        entree.insert(0, texte)  # Colle le texte récupéré.
        erreur_label.config(text="Cliquez sur le bouton 'Convertir'", font=('arial', 10, 'bold'), fg="green")
    except tk.TclError:
        erreur_label.config(text="Aucune valeur à coller !", font=('arial', 10, 'bold'), fg="red")


def grouper_par_blocs(texte, taille_bloc):  # Fonction qui gère la mise en bloc du résultat selon le choix du menu déroulant.
    reste = len(texte) % taille_bloc
    if reste != 0:
        texte = '0' * (taille_bloc - reste) + texte  # Ajoute un ou plusieurs '0' en fonction du nombre de caractères restants à gauche (lecture logique  de bas niveau)
    return ' '.join(texte[i:i+taille_bloc] for i in range(0, len(texte), taille_bloc))  # Retourne une chaîne de caractères séparés par un espace tous les 4 caractères de droite à gauche


def appliquer_format_binaire(*args):   # Fonction qui met à jour le label 'resultat_binaire' en fonction du choix dans le menu déroulant - *args sert à ignorer les arguments demandés par le widget 'optionMenu'
    val = format_binaire_var.get()
    texte = binaire_brut_var.get()
    if val == 'Brut':
        resultat_binaire.config(text=texte)
    else:
        resultat_binaire.config(text=grouper_par_blocs(texte, int(val)))
        ajuster_label(resultat_binaire, texte)
    #ajuster_label(resultat_binaire, texte)  # Ajuste le label de résultat en fonction du nombre de caractères qu'il contient. Appelle la fonction 'ajuster_label'.


def appliquer_format_hexadecimal(*args):  # Fonction qui met à jour le label 'resultat_hexadecimal' en fonction du choix dans le menu déroulant - *args sert à ignorer les arguments demandés par le widget 'optionMenu'
    val = format_hexadecimal_var.get()
    texte = hexadecimal_brut_var.get()
    if val == 'Brut':
        resultat_hexadecimal.config(text=texte)
    else:
        resultat_hexadecimal.config(text=grouper_par_blocs(texte, int(val)))
        ajuster_label(resultat_hexadecimal, texte)  # Ajuste le label de résultat en fonction du nombre de caractères qu'il contient. Appelle la fonction 'ajuster_label'.


def ajuster_label(label, texte):  # ajuste le label du résultat en fonction de la longueur de la chaîne qu'il contient.
    texte = label.cget("text").replace(" ", "")  # Récupère le texte réel qui se trouve dans le label avant l'ajustement de celui-ci et enlève les espaces inutiles qui perturbent l'affichage.
    nb_caracteres = len(texte)
    label.config(width=max(50, nb_caracteres))  # Le label garde au minimum 50 caractères et au maximum la longueur du texte.
    fenetre.update_idletasks()  # Scrute la boucle d'affichage de la fenêtre principale.
    fenetre.geometry("")  # Calcule automatiquement la taille de la fenêtre pour s'ajuster aux éléments qu'elle contient.

# PROGRAMME PRINCIPAL

# Fenêtre principale 
fenetre = tk.Tk()
fenetre.title("Convertisseur de bases numériques")
fenetre.geometry("620x520")


# Conteneur Global pour pouvoir placer les programme principal d'un côté et les affichages d'aides et autres sur le côté droit. Encapsulage obligatoire sino on ne peut pas mettre une frame latérale.
conteneur_global = tk.Frame(fenetre)  # Crée le Frame principal conteneur des deux frames : un pour le programme principal et l'autre pour le latéral (aide).
conteneur_global.pack(fill='both', expand=True)  # Le .pack() doit être sur une ligne en dessous sinon il retourne un 'non' dans le placement.

# Conteneur principal qui va contenir tous les éléments du programme principal (entrée, résultats...)
contenu_principal = tk.Frame(conteneur_global)  # Crée une frame dans le conteneur global qui affichera tous les éléments principaux du programme.
contenu_principal.pack(side='left', fill='both', expand=True)

# Variables en StringVar pour le choix du format d'affichage des label 'Binaire' et 'Hexadécimal'.
format_binaire_var = tk.StringVar(value=4)  # Valeur par défaut pour un affichage par bloc de 4 bits.
binaire_brut_var = tk.StringVar()  # Création d'une valeur brute qui servira de base au choix de l'affichage du résultat Binaire via le menu déroulant.
format_hexadecimal_var = tk.StringVar(value=4)  # Valeur par défaut pour un affichage par bloc de 4 digits héxadécimaux.
hexadecimal_brut_var = tk.StringVar()  # Création d'une valeur brute qui servira de base au choix de l'affichage du résultat Binaire via le menu déroulant.

# Menus
menu_principal = tk.Menu(fenetre) # Implémente un menu pour la fenêtre principale.

# -> Menu 'Fichier'
menu_fichier = tk.Menu(menu_principal, tearoff=0)
menu_fichier.add_command(label="Quitter", command=fenetre.destroy)
menu_principal.add_cascade(label="Fichier", menu=menu_fichier)


# -> Menu 'Aide'
menu_aide = tk.Menu(menu_principal, tearoff=0)
menu_aide.add_command(label="Aide", command=afficher_aide)
menu_aide.add_command(label="À propos", command=afficher_a_propos)
menu_principal.add_cascade(label="Aide", menu=menu_aide)


# Zone du champ de saisie et du choix de la base numérique
entree_labelframe = tk.LabelFrame(fenetre, text="Entrez valeur à convertir et la base numérique de départ.", font=('arial', 9), height=20, width=250, fg='#690F96')
entree = tk.Entry(entree_labelframe, width=80)
entree.grid(row=0, column=1, pady=10, sticky=tk.W)
coller_valeur = tk.Button(entree_labelframe, text="\U0001F4E5", command=lambda: bouton_coller())
coller_valeur.grid(row=0, column=0, padx=5, sticky=tk.E)


# Boutons radio pour choisir la base
base_var = tk.StringVar(value="Décimal")  # valeur par défaut

bases = ["Décimal", "Binaire", "Octal", "Hexadécimal"]
for b in bases:
    if b == 'Décimal':
        couleur = '#326565'
        rangee = 1
    elif b == 'Binaire':
        couleur = '#A83600'
        rangee = 2
    elif b == 'Octal':
        couleur = '#5900B3'
        rangee = 3
    elif b == 'Hexadécimal':
        couleur = '#C80430'
        rangee = 4
    tk.Radiobutton(entree_labelframe, text=b, fg=couleur, variable=base_var, value=b, padx=5).grid(row=rangee, column=1, sticky=tk.W)

entree_labelframe.pack(in_=contenu_principal, fill='both', pady=10, padx=10)

# Zone d'affichage des erreurs ou de messages importants
erreur_labelframe = tk.LabelFrame(fenetre, text='Message important !', font=('arial', 9), fg='red', height=20)
erreur_labelframe.pack(in_=contenu_principal, fill='both', pady=10,padx=10)
erreur_label = tk.Label(erreur_labelframe, text="Entrez votre valeur, choisissez la Base et cliquez sur le bouton 'Convertir'\n Ou coller une valeur avec le bouton situé à gauche.", font=('arial', 10, 'bold'), fg='green', justify='center')
erreur_label.pack(pady=5, padx=5)


# Zone d’affichage des résultats
resultats_labelframe = tk.LabelFrame(fenetre, text='Résultats', font=('arial', 9), fg='green')

# -> Widgets d'affichage du résultat pour les Entiers
resultat_texte_entier = tk.Label(resultats_labelframe, text="Décimal", fg="#326565", justify='right')
resultat_entier = tk.Label(resultats_labelframe, fg="#326565", bg="#99CCCC", font=('arial', 10, 'bold'), anchor='w', justify='right', relief='groove', width=50) # Les résultats à afficher seront en fonction des conversions
bouton_copier_entier = tk.Button(resultats_labelframe, text="\U0001F4CB", command=lambda: bouton_copier(resultat_entier))

# -> Widgets d'affichage du résulat pour les Binaires.
resultat_texte_binaire = tk.Label(resultats_labelframe, text="Binaire", fg="#A83600", anchor='w', justify='right')
resultat_binaire = tk.Label(resultats_labelframe, fg="#A83600", bg="#FFC5A8", font=('arial', 10, 'bold'), anchor='w', justify='right', relief='groove', width=50)
bouton_copier_binaire = tk.Button(resultats_labelframe, text="\U0001F4CB", command=lambda: bouton_copier(resultat_binaire))
options_bin = ["Brut", "2", "4", "8"]  # Options d'affichage pour le label 'resultat_binaire : format brut, en 2, 4 ou 8 bits.
menu_format_binaire = tk.OptionMenu(resultats_labelframe, format_binaire_var, *options_bin, command=appliquer_format_binaire)  # Création du menu déroulant pour le choix du format d'affichage.
menu_format_binaire.config(font=('arial', 9))

# -> Widgets d'affichage du résultat Octal.
resultat_texte_octal = tk.Label(resultats_labelframe, text="Octal", fg="#5900B3", anchor='w', justify='right')
resultat_octal = tk.Label(resultats_labelframe, fg="#5900B3", bg="#D3A8FF", font=('arial', 10, 'bold'), anchor='w', justify='right', relief='groove', width=50)
bouton_copier_octal = tk.Button(resultats_labelframe, text="\U0001F4CB", command=lambda: bouton_copier(resultat_octal))

# -> Widget d'affichage pour le résultat en hexadécimal.
resultat_texte_hexadecimal = tk.Label(resultats_labelframe, text="Hexadécimal", fg="#C80430", anchor='w', justify='right')
resultat_hexadecimal = tk.Label(resultats_labelframe, fg="#C80430", bg="#FDACBE", font=('arial', 10, 'bold'), anchor='w', justify='right',relief='groove', width=50)
bouton_copier_hexadecimal = tk.Button(resultats_labelframe, text="\U0001F4CB", command=lambda: bouton_copier(resultat_hexadecimal))
options_hex = ["Brut", "2", "4", "8"]
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
effacer_bouton = tk.Button(boutons_frame, text='Effacer', font=('arial', 10, 'bold'), command=effacer, fg='blue').grid(row=0, column=0, padx=40)
convertir_bouton = tk.Button(boutons_frame, text="Convertir", font=('arial', 10, 'bold'), fg='green', command=convertir).grid(row=0, column=1, padx=40)
quitter_bouton = tk.Button(boutons_frame, text='Quitter', font=('arial', 10, 'bold'), fg='red', command=fenetre.destroy).grid(row=0, column=2, padx=40)
boutons_frame.pack(in_=contenu_principal, pady=20)


# Boucle d'affichage de la fenêtre principale.
fenetre.config(menu=menu_principal)
fenetre.update_idletasks()  # Scrute la boucle d'affichage de la fenêtre principale.
fenetre.geometry("")  # Calcule automatiquement la taille de la fenêtre pour s'ajuster aux éléments qu'elle contient.
fenetre.mainloop()
