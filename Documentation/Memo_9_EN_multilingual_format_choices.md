
# Memo — Multilingual Format Handling (Binary & Hexadecimal)

##  Purpose of this memo
To ensure a **clear, stable, bilingual** format‑handling system in the converter (Raw, Blocks of 4, Blocks of 8, etc.) **without unnecessary complexity**, while preserving the selected format when switching languages.

This document explains:

- The original issue  
- How the simplified solution works  
- The utility function `find_format_key()`  
- The final structured functions  
- A clear logic diagram  
- A “Future Jean 🔮” recap section  

---

#  The Original Issue

When switching languages:

- The drop‑down menu options were rebuilt in the new language  
- **But the selected format was identified by its visible text**, which changes between languages  
- Therefore the program could not know that `"Blocs de 4"` (FR) corresponds to `"Blocks of 4"` (EN)

Result:

 - The selected format could be lost  
 - Or the wrong format could be applied  
 - Or the first program launch didn’t apply formatting correctly  

---

#  The Adopted Solution (Simple & Robust)

We chose the **simplest approach** to maintain:

 **Compare translated texts directly**, but  
 **Save the old visible text before switching languages**, then  
 Convert it back into a **logical format key** via a utility function  
 Reapply the same format in the new language

Thus:

 - No extra “internal code system”  
 - No complex callbacks  
 - The program stays readable and intuitive  
 - Format persists correctly across languages  
 - Works correctly on first launch  

---

#  Utility Function: `find_format_key()`

This small helper is the essential piece   
It converts the visible text (old language) into a stable logical key:

```python
def find_format_key(old_text):
    format_keys = ["brut", "blocs_2", "blocs_4", "blocs_8"]
    for key in format_keys:
        if old_translations.get(key) == old_text:
            return key
    return "brut"
```

Inputs:

- `old_text` → the visible text *in the previous language*  
- `old_translations` → the JSON dictionary of that previous language  

Output:

- `"brut"`  
- `"blocs_2"`  
- `"blocs_4"`  
- `"blocs_8"`

Thanks to this, the program knows exactly which logical format the user had selected.

---

#  `changer_langue()` — Final Clean Version

Here is the clean, commented and readable version:

```python
def changer_langue(new_lang):

    global langue_actuelle, textes_langues
    global zone_texte_aide, panneau_aide, bouton_fermer_aide
    global zone_texte_contexte, panneau_contexte, bouton_fermer_contexte

    # Save old language and visible format texts
    old_lang = langue_actuelle
    old_format_bin = format_binaire_var.get()
    old_format_hex = format_hexadecimal_var.get()

    # Load old language dictionary
    old_translations = load_translations(f"./Langues/lang_{old_lang}.json")

    # Utility: text → logical key
    def find_format_key(old_text):
        keys = ["brut", "blocs_2", "blocs_4", "blocs_8"]
        for key in keys:
            if old_translations.get(key) == old_text:
                return key
        return "brut"

    # Recover format keys
    key_bin = find_format_key(old_format_bin)
    key_hex = find_format_key(old_format_hex)

    # Switch language
    langue_actuelle = new_lang
    textes_langues = load_translations(f"./Langues/lang_{langue_actuelle}.json")

    # Retranslate error_label if needed
    current_text = erreur_label.cget("text")
    old_translations = load_translations(f"./Langues/lang_{old_lang}.json")
    for key, txt in old_translations.items():
        if current_text == txt and key in textes_langues:
            erreur_label.config(text=textes_langues[key])
            break

    # Update labels, menus, radiobuttons…
    update_interface()
    update_radio_buttons()
    build_menus()
    fenetre.update_idletasks()
    fenetre.geometry("")

    # Reapply formats in the new language
    format_binaire_var.set(textes_langues[key_bin])
    format_hexadecimal_var.set(textes_langues[key_hex])
    apply_binary_format()
    apply_hexadecimal_format()

    # Aide / Contexte panels (if open)
    if zone_texte_aide is not None:
        load_help_file()
    if panneau_aide is not None:
        panneau_aide.config(text=textes_langues["titre_aide"])
    if bouton_fermer_aide is not None:
        bouton_fermer_aide.config(text=textes_langues["fermer"])

    if zone_texte_contexte is not None:
        load_context_file()
    if panneau_contexte is not None:
        panneau_contexte.config(text=textes_langues["titre_contexte"])
    if bouton_fermer_contexte is not None:
        bouton_fermer_contexte.config(text=textes_langues["fermer"])
```

---

#  Final Format Application Functions

## Binary

```python
def apply_binary_format(*args):
    val = format_binaire_var.get()
    text = binaire_brut_var.get()

    if val == textes_langues["brut"]:
        resultat_binaire.config(text=text)
    elif val == textes_langues["blocs_4"]:
        resultat_binaire.config(text=group_by_blocks(text, 4))
    elif val == textes_langues["blocs_8"]:
        resultat_binaire.config(text=group_by_blocks(text, 8))

    adjust_label(resultat_binaire)
```

## Hexadecimal

```python
def apply_hexadecimal_format(*args):
    val = format_hexadecimal_var.get()
    text = hexadecimal_brut_var.get()

    if val == textes_langues["brut"]:
        resultat_hexadecimal.config(text=text)
    elif val == textes_langues["blocs_2"]:
        resultat_hexadecimal.config(text=group_by_blocks(text, 2))
    elif val == textes_langues["blocs_4"]:
        resultat_hexadecimal.config(text=group_by_blocks(text, 4))
    elif val == textes_langues["blocs_8"]:
        resultat_hexadecimal.config(text=group_by_blocks(text, 8))

    adjust_label(resultat_hexadecimal)
```

---

#  Logic Diagram (Simple View)

```
[Before language switch]
        │
        ▼
Read text: "Blocs de 4"
        │
        ▼
Convert to key: "blocs_4"
        │
        ▼
Load new language
        │
        ▼
Rebuild menus
        │
        ▼
Set format_binaire_var = "Blocks of 4"
        │
        ▼
apply_binary_format()
        │
        ▼
Correct formatted output in new language
```

---

# Reminder

The essential rule is:

 **Visible text changes with language.  
 Logical meaning does NOT.**

So when switching languages:

1. Save the current visible text  
2. Convert it to a logical key  
3. Load new language  
4. Rebuild menus  
5. Set the visible text in the new language  
6. Reapply formatting  

That’s all.  
And it works **every time**, in every language.

---


