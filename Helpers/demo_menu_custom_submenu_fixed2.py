# demo_menu_custom_submenu_fixed2.py
import tkinter as tk

# --- Thème personnalisable ---
BG_BARRE    = "#222831"
FG_TEXTE    = "#EAEAEA"
FG_ACCEL    = "#8FBCBB"
BG_HOVER    = "#2F3A45"
BORDER_POP  = "#3A4750"
BG_POPUP    = "#1F2833"

FONT_ITEM   = ("Segoe UI", 10)
FONT_ACCEL  = ("Consolas", 9)

class MenuItem(tk.Frame):
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
            w.bind("<ButtonRelease-1>", self._on_click)
    def _on_enter(self, _): 
        self.configure(bg=BG_HOVER); self.lbl_text.configure(bg=BG_HOVER)
        if self.lbl_accel: self.lbl_accel.configure(bg=BG_HOVER)
    def _on_leave(self, _):
        self.configure(bg=BG_BARRE); self.lbl_text.configure(bg=BG_BARRE)
        if self.lbl_accel: self.lbl_accel.configure(bg=BG_BARRE)
    def _on_click(self, _):
        if callable(self.command): self.command()

class BarreMenu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=BG_BARRE, height=28)
        self.pack(fill="x")
        self.items = []
    def add_item(self, text, command=None, accelerator=None, side="left"):
        item = MenuItem(self, text=text, command=command, accelerator=accelerator)
        item.pack(side=side)
        self.items.append(item)
        return item

class PopupMenu(tk.Toplevel):
    def __init__(self, parent, items):
        super().__init__(parent)
        self.configure(bg=BORDER_POP)
        self.overrideredirect(True)
        self.transient(parent)
        self._grab_active = False
        self.body = tk.Frame(self, bg=BG_POPUP); self.body.pack(padx=1, pady=1)

        for entry in items:
            if entry is None:
                sep = tk.Frame(self.body, bg=BORDER_POP, height=1); sep.pack(fill="x", padx=6, pady=4); continue
            text, accel, command = entry
            row = tk.Frame(self.body, bg=BG_POPUP); row.pack(fill="x", anchor="w")
            lt = tk.Label(row, text=text, bg=BG_POPUP, fg=FG_TEXTE, font=FONT_ITEM, anchor="w")
            lt.grid(row=0, column=0, sticky="ew", padx=(10, 12), pady=5)
            la = tk.Label(row, text=accel or "", bg=BG_POPUP, fg=FG_ACCEL, font=FONT_ACCEL, anchor="e")
            la.grid(row=0, column=1, sticky="e", padx=(0, 10))
            row.grid_columnconfigure(0, weight=1); row.grid_columnconfigure(1, weight=0)
            def on_enter(_e, r=row, a=la, t=lt): r.configure(bg=BG_HOVER); a.configure(bg=BG_HOVER); t.configure(bg=BG_HOVER)
            def on_leave(_e, r=row, a=la, t=lt): r.configure(bg=BG_POPUP); a.configure(bg=BG_POPUP); t.configure(bg=BG_POPUP)
            def on_click(_e, cmd=command): self.safe_close(); cmd and cmd()
            for w in (row, lt, la):
                w.bind("<Enter>", on_enter); w.bind("<Leave>", on_leave); w.bind("<ButtonRelease-1>", on_click)

        self.bind("<Escape>",   lambda e: self.safe_close())
        self.after(1, self._ensure_focus_and_bind)

    def _ensure_focus_and_bind(self):
        try: self.focus_force()
        except Exception: pass
        self.after(150, self._bind_global_clicks)
        try: self.grab_set(); self._grab_active = True
        except Exception: self._grab_active = False

    def _bind_global_clicks(self):
        # Écouter clic gauche et droit
        self.master.bind_all("<Button-1>", self._global_click_outside, add="+")
        self.master.bind_all("<Button-3>", self._global_click_outside, add="+")

    def popup_at_widget_bottom(self, widget):
        x = widget.winfo_rootx(); y = widget.winfo_rooty() + widget.winfo_height()
        self.geometry(f"+{x}+{y}"); self.deiconify(); self.lift()

    def _global_click_outside(self, event):
        # Quelle que soit la destination du clic (grab actif), on compare les coordonnées écran
        px, py = event.x_root, event.y_root
        x0, y0 = self.winfo_rootx(), self.winfo_rooty()
        x1, y1 = x0 + self.winfo_width(), y0 + self.winfo_height()
        inside = (x0 <= px <= x1) and (y0 <= py <= y1)
        if not inside:
            self.safe_close()

    def safe_close(self):
        try:
            self.master.unbind_all("<Button-1>")
            self.master.unbind_all("<Button-3>")
        except Exception: pass
        if self._grab_active:
            try: self.grab_release()
            except Exception: pass
        if self.winfo_exists():
            self.withdraw(); self.destroy()

def main():
    root = tk.Tk(); root.title("Sous-menu robuste — clic externe OK"); root.geometry("760x460")
    def action_nouveau(): tk.messagebox.showinfo("Nouveau", "Action Nouveau… (à brancher)")
    def action_quitter(): root.destroy()
    def action_aide(): tk.messagebox.showinfo("Aide", "Ouvrir le panneau d’aide ici.")
    barre = BarreMenu(root)
    item_fichier = barre.add_item("Fichier")
    def open_fichier_submenu(_event=None):
        entries = [("Nouveau","Ctrl+N",action_nouveau), None, ("Quitter","Ctrl+Q",action_quitter)]
        def _open():
            pop = PopupMenu(root, entries); root._last_popup = pop; pop.popup_at_widget_bottom(item_fichier)
        root.after(1, _open)
    for w in (item_fichier, item_fichier.lbl_text):
        w.bind("<ButtonRelease-1>", open_fichier_submenu)
    barre.add_item("Aide", action_aide, accelerator="F1")
    barre.add_item("Quitter", action_quitter, accelerator="Ctrl+Q")
    root.bind_all("<Control-q>", lambda e: action_quitter())
    root.bind_all("<Control-n>", lambda e: action_nouveau())
    root.bind_all("<F1>",        lambda e: action_aide())
    root.bind_all("<Escape>",    lambda e: root.focus_set())
    zone = tk.Frame(root, bg="#111820"); zone.pack(fill="both", expand=True)
    tk.Label(zone, text="Test :\n- Clique 'Fichier' → sous-menu\n- Échap ferme\n- Clic EXTERNE ferme aussi (gauche & droit)",
             fg="#D9E0E6", bg="#111820", font=("Segoe UI", 11)).pack(pady=40)
    root.mainloop()

if __name__ == "__main__":
    try:
        import tkinter.messagebox as messagebox
        tk.messagebox = messagebox
    except Exception: pass
    main()
