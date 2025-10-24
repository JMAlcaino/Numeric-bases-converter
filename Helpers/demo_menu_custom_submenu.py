# demo_menu_custom_submenu.py
import tkinter as tk

# --- Thème personnalisable ---
BG_BARRE    = "#222831"   # Fond barre principale
FG_TEXTE    = "#EAEAEA"   # Texte items
FG_ACCEL    = "#8FBCBB"   # Couleur des accélérateurs
BG_HOVER    = "#2F3A45"   # Fond au survol
BORDER_POP  = "#3A4750"   # Bordure du sous-menu
BG_POPUP    = "#1F2833"   # Fond du sous-menu

FONT_ITEM   = ("Segoe UI", 10)
FONT_ACCEL  = ("Consolas", 9)

class MenuItem(tk.Frame):
    """Un 'bouton' de menu custom avec libellé + accélérateur (optionnel)."""
    def __init__(self, parent, text, command=None, accelerator=None):
        super().__init__(parent, bg=BG_BARRE)
        self.command = command

        self.lbl_text = tk.Label(self, text=text, bg=BG_BARRE, fg=FG_TEXTE, font=FONT_ITEM)
        self.lbl_text.pack(side="left", padx=(10, 6), pady=4)

        self.lbl_accel = None
        if accelerator:
            self.lbl_accel = tk.Label(self, text=accelerator, bg=BG_BARRE, fg=FG_ACCEL, font=FONT_ACCEL)
            self.lbl_accel.pack(side="left", padx=(0, 10), pady=4)

        for w in (self, self.lbl_text, self.lbl_accel) if self.lbl_accel else (self, self.lbl_text):
            w.bind("<Enter>", self._on_enter)
            w.bind("<Leave>", self._on_leave)
            w.bind("<Button-1>", self._on_click)

    def _on_enter(self, _):
        self.configure(bg=BG_HOVER); self.lbl_text.configure(bg=BG_HOVER)
        if self.lbl_accel: self.lbl_accel.configure(bg=BG_HOVER)

    def _on_leave(self, _):
        self.configure(bg=BG_BARRE); self.lbl_text.configure(bg=BG_BARRE)
        if self.lbl_accel: self.lbl_accel.configure(bg=BG_BARRE)

    def _on_click(self, _):
        if callable(self.command):
            self.command()

class BarreMenu(tk.Frame):
    """Barre horizontale de 'menus' custom."""
    def __init__(self, parent):
        super().__init__(parent, bg=BG_BARRE, height=28)
        self.pack(fill="x")
        self.items = []

    def add_item(self, text, command=None, accelerator=None, side="left"):
        item = MenuItem(self, text=text, command=command, accelerator=accelerator)
        item.pack(side=side)
        self.items.append(item)
        return item

# ---------- Sous-menu (popup) ----------
class PopupMenu(tk.Toplevel):
    """Petit menu popup stylé, façon sous-menu."""
    def __init__(self, parent, items):
        super().__init__(parent)
        self.configure(bg=BORDER_POP)
        self.overrideredirect(True)     # pas de bordure ni barre de titre
        self.transient(parent)

        self.body = tk.Frame(self, bg=BG_POPUP)
        self.body.pack(padx=1, pady=1)

        # Construire les lignes (texte + accélérateur aligné à droite)
        for entry in items:
            if entry is None:
                # séparateur
                sep = tk.Frame(self.body, bg=BORDER_POP, height=1)
                sep.pack(fill="x", padx=6, pady=4)
                continue

            text, accel, command = entry
            row = tk.Frame(self.body, bg=BG_POPUP)
            row.pack(fill="x")

            lbl_text = tk.Label(row, text=text, bg=BG_POPUP, fg=FG_TEXTE, font=FONT_ITEM, anchor="w")
            lbl_text.grid(row=0, column=0, sticky="ew", padx=(10, 12), pady=5)

            lbl_acc = tk.Label(row, text=accel or "", bg=BG_POPUP, fg=FG_ACCEL, font=FONT_ACCEL, anchor="e")
            lbl_acc.grid(row=0, column=1, sticky="e", padx=(0, 10))

            # colonnes pour occuper l'espace (texte à gauche, accel à droite)
            row.grid_columnconfigure(0, weight=1)
            row.grid_columnconfigure(1, weight=0)

            def on_enter(_e, r=row, lt=lbl_text, la=lbl_acc):
                r.configure(bg=BG_HOVER); lt.configure(bg=BG_HOVER); la.configure(bg=BG_HOVER)
            def on_leave(_e, r=row, lt=lbl_text, la=lbl_acc):
                r.configure(bg=BG_POPUP); lt.configure(bg=BG_POPUP); la.configure(bg=BG_POPUP)
            def on_click(_e, cmd=command):
                self.withdraw()
                self.destroy()
                if callable(cmd): cmd()

            for w in (row, lbl_text, lbl_acc):
                w.bind("<Enter>", on_enter)
                w.bind("<Leave>", on_leave)
                w.bind("<Button-1>", on_click)

        # fermeture si clic en dehors / perte focus / Esc
        self.bind("<FocusOut>", lambda e: self.safe_close())
        self.bind("<Escape>",   lambda e: self.safe_close())

        # capture clics globaux pour fermer si clic externe
        self._global_binding = self.master.bind_all("<Button-1>", self._global_click, add="+")
        self.focus_set()

    def popup_at_widget_bottom(self, widget):
        # Positionner le popup sous le widget donné
        x = widget.winfo_rootx()
        y = widget.winfo_rooty() + widget.winfo_height()
        self.geometry(f"+{x}+{y}")

    def _global_click(self, event):
        # Fermer si le clic n’est pas dans ce toplevel
        if event.widget is self or str(event.widget).startswith(str(self)):
            return  # clic interne: ne rien faire
        self.safe_close()

    def safe_close(self):
        try:
            if self._global_binding:
                self.master.unbind_all("<Button-1>")
        except Exception:
            pass
        if self.winfo_exists():
            self.withdraw()
            self.destroy()

# ---------- Démo avec sous-menu “Fichier” ----------
def main():
    root = tk.Tk()
    root.title("Démo menu custom + sous-menu")
    root.geometry("760x460")

    # Actions
    def action_nouveau():
        tk.messagebox.showinfo("Nouveau", "Action Nouveau… (à brancher)")

    def action_quitter():
        root.destroy()

    def action_aide():
        tk.messagebox.showinfo("Aide", "Ouvrir le panneau d’aide ici.")

    # Barre principale
    barre = BarreMenu(root)

    # Item "Fichier" avec sous-menu
    item_fichier = barre.add_item("Fichier")  # on clique pour ouvrir le sous-menu

    def open_fichier_submenu(_event=None):
        # Liste des entrées: (label, accel, command) ; None = séparateur
        entries = [
            ("Nouveau",      "Ctrl+N", action_nouveau),
            None,
            ("Quitter",      "Ctrl+Q", action_quitter),
        ]
        pop = PopupMenu(root, entries)
        pop.popup_at_widget_bottom(item_fichier)

    # click pour ouvrir le sous-menu
    for w in (item_fichier, item_fichier.lbl_text):
        w.bind("<Button-1>", open_fichier_submenu)

    # Items simples
    barre.add_item("Aide", action_aide, accelerator="F1")
    barre.add_item("Quitter", action_quitter, accelerator="Ctrl+Q")

    # Raccourcis clavier globaux
    root.bind_all("<Control-q>", lambda e: action_quitter())
    root.bind_all("<Control-n>", lambda e: action_nouveau())
    root.bind_all("<F1>",        lambda e: action_aide())
    root.bind_all("<Escape>",    lambda e: root.focus_set())  # petite sortie d'états

    # Zone de contenu
    zone = tk.Frame(root, bg="#111820")
    zone.pack(fill="both", expand=True)
    tk.Label(zone,
             text="Sous-menu 'Fichier' personnalisé :\n"
                  "- clique 'Fichier' pour voir le popup\n"
                  "- survol/hover\n"
                  "- accélérateurs stylés\n"
                  "- clic externe/ESC pour fermer\n"
                  "- Ctrl+N / Ctrl+Q / F1 actifs",
             fg="#D9E0E6", bg="#111820",
             font=("Segoe UI", 11)).pack(pady=40)

    root.mainloop()

# messagebox dispo si lancé tel quel
if __name__ == "__main__":
    try:
        import tkinter.messagebox as messagebox
        tk.messagebox = messagebox
    except Exception:
        pass
    main()
