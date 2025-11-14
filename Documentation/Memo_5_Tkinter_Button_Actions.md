#  Memo – Multiple Actions with a Single Tkinter Button

##  Context
A Tkinter button (`tk.Button`) can only have **one `command=`** parameter.  
If you write it twice, the second one overwrites the first.

Incorrect example:
```python
button = tk.Button(root, text="Test",
                   command=lambda: func1(),
                   command=lambda: func2())  # ❌ only the last one works
```

---

##  Simple solution using a single `lambda`
You can call several functions **inside the same lambda**:

```python
button = tk.Button(root, text="Test",
                   command=lambda: (func1(), func2()))
```

Both functions will be executed **in order** when the button is clicked.

---

##  Practical example (language selection)
```python
def button_action(lang):
    change_language(lang)
    load_help(lang)

button_french = tk.Button(flags_zone, image=img_fr,
                          command=lambda: button_action("fr"))
button_english = tk.Button(flags_zone, image=img_en,
                           command=lambda: button_action("en"))
```

Only one function (`button_action`) handles all languages,
and each button simply passes its language code to it.

---

##  Bonus tip
You can also write it directly in one line:
```python
command=lambda: (change_language("fr"), load_help("fr"))
```
but using a dedicated function keeps your code cleaner.

---

##  Key points
- Only one `command=` per button.  
- To run multiple actions → group them inside a `lambda` or a function.  
- To pass parameters → `lambda: my_function(param)`.

---

> Memo for the *Numeric Bases Converter* project  
> Jean-Marc Alcaïno – 2025
