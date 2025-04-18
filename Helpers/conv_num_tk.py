#!/usr/bin/env python3
"""
############################################################################################################
 
 Filename     : conv_num_tk.py                                                                              
 Description  : A simple but useful GUI numeric bases converter
 Author       : Alcaïno Jean-Marc                                                                          
 Modification : 2025/04/08                                                                            
 Version      : V 1.0

 GitHub       :     https://github.com/JMAlcaino/Useful_Scripts
 Author GitHub :    https://github.com/JMAlcaino

############################################################################################################
"""
# Importation de bibliothèques
import tkinter as tk

# Définition des variables
binaire = ['0', '1']
octal = ['0', '1', '2', '3', '4', '5', '6', '7']
hexadecimal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F' ]

texte_explications = """Voici les différentes Bases numériques concernées dans ce convertisseur :
- Entier      --> Nombre en  Base 10  contenant les chiffres de 0 à 9 : (0 1 2 3 4 5 6 7 8 9).
- Binaire     --> Nombre en Base 2 contenant les chiffres 0 et 1.
- Octal       --> Nombre en Base 8 contenant les chiffres de 0 à 7 : (0 1 2 3 4 5 6 7).
- Hexadécimal --> Nombre en Base 16 contenant les chiffres de 0 à 9 et les lettres de A à F : (0 1 2 3 4 5 6 7 8 9 A B C D E F)."""


# Définition des fonctions
def conv_entier():
    while True:
        try:
            nombre_entier = int(input("\nEntrez un nombre entier -> "))
            break
        except ValueError:
            print("Votre entrée n'est pas un entier, merci de corriger.")

    b = str(bin(nombre_entier))
    o = str(oct(nombre_entier))
    h = str.upper(str(hex(nombre_entier)))
    print(f"\nEntier -> {nombre_entier} - Binaire -> {b[2:]} - Octal -> {o[2:]} - Héxadécimal -> {h[2:]}\n")


def conv_binaire():
    while True:
        try:
            nombre_binaire = input("\nEntrez un nombre en format binaire (exemple : 1110111) -> ")
            for nombre in nombre_binaire:
                if nombre in binaire:
#                    print(nombre)  # Vérification pour debug
                    continue
                else :
                    print("Votre entrée n'est pas un binaire, merci de corriger.")
                    conv_binaire()
            break
        except ValueError:
            print("Votre entrée n'est pas un binaire, merci de corriger.")

    e = int(nombre_binaire, 2)
    o = str(oct(e))
    h = str.upper(str(hex(e)))
    print(f"\nBinaire -> {nombre_binaire} - Entier -> {e} - Octal -> {o[2:]} - Héxadécimal -> {h[2:]}\n")
 

def conv_octal():
    while True:
        try:
            nombre_octal = input("\nEntrez un nombre en format octal (exemple : 457) -> ")
            for nombre in nombre_octal:
                if nombre in octal:
                    continue
                else:
                    print("Votre entrée n'est pas un octal, merci de corriger.")
                    conv_octal()
            break
        except ValueError:
            print("Votre entrée n'est pas un octal, merci de corriger.")

    e = int(nombre_octal, 8)
    b = str(bin(e))
    h = str.upper(str(hex(e)))
    print(f"\nOctal -> {nombre_octal} - Entier -> {e} - Binaire -> {b[2:]} - Héxadécimal -> {h[2:]}\n")


def conv_hexa():
    while True:
        try:
            nombre_hexa = input("\nEntrez un nombre en format hexadécimal (exemple : 12FA8) -> ")
            nombre_hexa = nombre_hexa.upper()
            for caractere in nombre_hexa:
                if caractere in hexadecimal:
                    continue
                else:
                    print("Votre entrée n'est pas un hexadémal, merci de corriger.")
                    conv_hexa()
            break
        except ValueError:
            print("Votre entrée n'est pas un hexadémal, merci de corriger.")

    e = int(nombre_hexa, 16)
    b = str(bin(e))
    o = str(oct(e))
    print(f"\nHéxadécimal -> {nombre_hexa} - Entier -> {e} - Binaire -> {b[2:]} - Octal -> {o[2:]}\n")
 

# Affichage fenêtre principale
fenetre = tk.Tk()                                            # Main window 
fenetre.title("Convertisseur Bases")                               # Main window's title
fenetre.geometry("500x200")                                  # Size of the window
fenetre.configure(bg='#404040')                              # Background color of window in hexadecimal

msgexplications = tk.Message(fenetre,           # Définition du widget Message dans la fenêtre principale.			
                 text=texte_explications,  # Texte à afficher dans le widget.
                 width=600,         # Largeur du widget.
                 relief="groove",   # Style de relief du widget.
                 justify="left",  # Justification tu texte en 'centré'.
                 borderwidth=5)     # Largeur de bordure du widget.
msgexplications.configure(bg='#b9bca0',         # Configuration de la couleur du texte en héxadécimal avec Tinker_code_couleurs
              fg='#745164',         # Configuration de la couleur de fond du widget.
              font=('times', 12))  # Configuration de la font, de la dimension et du style.
#msgexplications.pack()                          # Initialisation du widget Message.

b1=tk.Button(fenetre,                                        # Create the button to chose the color
             text='Effacer',
             bg='#a0a0a9')

b2=tk.Button(fenetre,                                        # Create the 'quit" button
             text='          Quitter          ',          # Text with spaces for the dimension (à revoir avec les dimensions des boutons)
             fg='red',
             bg='#a0a0a9',
             command=fenetre.destroy)                        # The 'destroy' command is called to close the main window

msgexplications.grid(row=1,padx=15,pady=5)
b1.grid(row=2,padx=15,pady=5)                    # Display the buttons with the 'grid' method
b2.grid(row=2,column=1,padx=10,pady=5)


fenetre.mainloop()                                           # Main window loop for the display