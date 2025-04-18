import tkinter as tk

def afficher_aide_avec_animation():
    # Crée le panneau à droite avec largeur 0
    panneau = tk.Frame(fenetre, bg='lightblue', width=0)
    panneau.pack(side='right', fill='y')

    # Fonction récursive pour simuler l'effet déroulant
    def derouler(larg=0):
        if larg <= 200:
            panneau.config(width=larg)
            fenetre.after(10, lambda: derouler(larg + 10))

    derouler()

# Fenêtre principale
fenetre = tk.Tk()
fenetre.geometry("600x300")
fenetre.title("Démo animation panneau d’aide")

# Contenu fictif
contenu = tk.Label(fenetre, text="Contenu principal", font=('Arial', 14))
contenu.pack(padx=20, pady=20)

# Bouton pour déclencher l'affichage animé
btn = tk.Button(fenetre, text="Afficher l'aide", command=afficher_aide_avec_animation)
btn.pack(pady=10)

fenetre.mainloop()
