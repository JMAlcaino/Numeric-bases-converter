#!/usr/bin/env python3
"""
############################################################################################################
 
 Filename     : conv_num_bases.py                                                                              
 Description  : A simple but useful numeric bases converter
 Author       : Alcaïno Jean-Marc                                                                          
 Modification : 2025/04/08                                                                            
 Version      : V 2.1

 GitHub       :     https://github.com/JMAlcaino/Useful_Scripts
 Author GitHub :    https://github.com/JMAlcaino

############################################################################################################
"""

# Définition des variables
binaire = ['0', '1']
octal = ['0', '1', '2', '3', '4', '5', '6', '7']
hexadecimal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F' ]


# Définition des fonctions
def generique(titre):  # Fonction qui affiche le titre du script quelque-soit sa longueur
    lg = len(titre) + 8  # 3 espaces avant et après le titre + 2 pour le '#' du début et la fin du tableau de titre.
    print(lg * "#")
    print("#" + (lg - 2) * " " + "#")
    print("#   " + titre + "   #")
    print("#" + (lg - 2) * " " + "#")
    print(lg * "#")


def choix():
    while True:
        print("\n * Conversion d'un entier        -> Entrez 1")
        print(" * Conversion d'un binaire       -> Entrez 2")
        print(" * Conversion d'un octal         -> Entrez 3")
        print(" * Conversion d'un hexadécimal   -> Entrez 4")
        print(" * Quitter le programme          -> Entrez 5\n")
        choix = int(input("Quel est votre choix de conversion ? -> "))
        if choix == 1:
            conv_entier()
        elif choix == 2:
            conv_binaire()
        elif choix == 3:
            conv_octal()
        elif choix == 4:
            conv_hexa()
        elif choix == 5:
            print("\nMerci d'avoir utilisé le convertisseur !\n")
            exit()
        else:
            print("\nChoix incorrect, veuillez rééssayer... \n\n")


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
    encore()


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
    encore()


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
    encore()


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
    encore()


def encore():
    while True:
        encore = input("\nRecommencer o/n ? ")
        if encore == 'o':
            choix()
        elif encore == 'n':
            print("\nMerci d'avoir utilisé le convertisseur !\n")
            exit()
        else:
            print("\nVeuillez entrer 'o' ou 'n'...\n")


# Programme principal
if __name__ == '__main__':

    generique("Convertisseur de bases")

    print("\nCe script permet de convertir un nombre suivant les différentes bases numériques.\n")
    print("Voici les différentes Bases numériques concernées dans ce convertisseur : ")
    print(" - Entier      --> Nombre en  Base 10  contenant les chiffres de 0 à 9 : (0 1 2 3 4 5 6 7 8 9).")
    print(" - Binaire     --> Nombre en Base 2 contenant les chiffres 0 et 1.")
    print(" - Octal       --> Nombre en Base 8 contenant les chiffres de 0 à 7 : (0 1 2 3 4 5 6 7).")
    print(" - Hexadécimal --> Nombre en Base 16 contenant les chiffres de 0 à 9 et les lettres de A à F : (0 1 2 3 4 5 6 7 8 9 A B C D E F).\n")

    choix()








"""
Ce morceau de programme n'est pas utilisé ici mais il permet l'affichage des conversions pour un entier.
Exemple tiré du manuel en ligne de Python 3.13 -> https://docs.python.org/fr/3.13/library/string.html#formatspec

# conversions
nombre_binaire = bin(nombre_entier)
nombre_octal = oct(nombre_entier)
nombre_hexadecimal = hex(nombre_entier)

# Affichage formaté simple
print(f"\nL'entier {nombre_entier} donne :  en binaire -> {nombre_binaire} - en octal -> {nombre_octal} - en hexadéciaml -> {nombre_hexadecimal}\n")

# Affichage formaté spécial ne fonctionne qui si on entre un entier
print("\n Résultats format traditionnel :")
print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}\n".format(nombre))
print("\n Résultats format Python :")
print("int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}\n".format(nombre))
"""
