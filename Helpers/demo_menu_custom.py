# demo_menu_custom.py
import tkinter as tk

# --- Thème minimal personnalisable ---
BG_BARRE   = "#222831"  # fond de la barre
FG_TEXTE   = "#EAEAEA"  # texte principal
FG_ACCEL   = "#8FBCBB"  # couleur des accélérateurs (ex: Ctrl+Q)
BG_HOVER   = "#2F3A45"  # fond au survol
FONT_ITEM  = ("Segoe UI", 10)
FONT_ACCEL = ("Consolas", 9)

class MenuItem(tk.Frame):
    """Un 'bouton' de menu custom avec label + accélérateur stylé."""
    def __init__(self, parent, text, command, accelerator=None):
        super().__init__(parent, bg=BG_BARRE)
        self.command = command

        # Label principal
        self.lbl_text = tk.Label(self, text=text, bg=BG_BARRE, fg=FG_TEXTE, font=FONT_ITEM)
        self.lbl_text.pack(side="left", padx=(10, 6), pady=4)

        # Accélérateur stylé (facultatif)
        if accelerator:
            self.lbl_accel = tk.Label(self, text=accelerator, bg=BG_BARRE, fg=FG_ACCEL, font=FONT_ACCEL)
            self.lbl_accel.pack(side="left", padx=(0, 10), pady=4)
        else:
            self.lbl_accel = None

        # Interactions (survol + clic)
        for w in (self, self.lbl_text, self.lbl_accel) if self.lbl_accel else (self, self.lbl_text):
            w.bind("<Enter>", self._on_enter)
            w.bind("<Leave>", self._on_leave)
            w.bind("<Button-1>", self._on_click)

    def _on_enter(self, _):
        self.configure(bg=BG_HOVER)
        self.lbl_text.configure(bg=BG_HOVER)
        if self.lbl_accel:
            self.lbl_accel.configure(bg=BG_HOVER)

    def _on_leave(self, _):
        self.configure(bg=BG_BARRE)
        self.lbl_text.configure(bg=BG_BARRE)
        if self.lbl_accel:
            self.lbl_accel.configure(bg=BG_BARRE)

    def _on_click(self, _):
        if callable(self.command):
            self.command()

class BarreMenu(tk.Frame):
    """Barre horizontale de 'menus' custom (labels cliquables stylés)."""
    def __init__(self, parent):
        super().__init__(parent, bg=BG_BARRE, height=28)
        self.pack(fill="x")
        self.items = []

    def add_item(self, text, command, accelerator=None, side="left"):
        item = MenuItem(self, text=text, command=command, accelerator=accelerator)
        item.pack(side=side)  # left pour empiler horizontalement des items
        self.items.append(item)
        return item

# -------------------------------------------------------------------

def main():
    root = tk.Tk()
    root.title("Démo menu custom Tkinter")
    root.geometry("720x420")

    # Fonctions des items
    def action_aide():
        tk.messagebox.showinfo("Aide", "Ici, tu peux ouvrir ton panneau d'aide.")

    def action_quitter():
        root.destroy()

    # Barre de menu custom
    barre = BarreMenu(root)
    # Quelques items d'exemple
    barre.add_item("Fichier", lambda: None)  # un faux item "titre" de section
    barre.add_item("Aide", action_aide, accelerator="F1")
    barre.add_item("Quitter", action_quitter, accelerator="Ctrl+Q")

    # Raccourcis clavier (globaux)
    root.bind_all("<Control-q>", lambda e: action_quitter())
    root.bind_all("<F1>",        lambda e: action_aide())

    # Contenu de démo
    zone = tk.Frame(root, bg="#111820")
    zone.pack(fill="both", expand=True)
    tk.Label(zone,
             text="Barre de menus personnalisée : accélérateurs stylés, survol, clic, raccourcis.\n"
                  "Essaie F1 et Ctrl+Q.\n\n"
                  "À intégrer plus tard si tu veux moderniser ton app 😉",
             fg="#D9E0E6", bg="#111820",
             font=("Segoe UI", 11)).pack(pady=40)

    root.mainloop()

# Nécessaire pour messagebox si tu lances tel quel
if __name__ == "__main__":
    try:
        import tkinter.messagebox as messagebox  # alias pour compat
        tk.messagebox = messagebox
    except Exception:
        pass
    main()
