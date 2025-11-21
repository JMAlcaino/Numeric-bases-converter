# Managing Destroyed Widgets in Tkinter

## Technical Memo --- Numeric Bases Converter (Jean & Pylo)

When creating a Tkinter user interface, it is common for a widget
(window, LabelFrame, Text, etc.) to be **destroyed** by the program ---
for example when closing the Help or Context panels.\
The issue: **the Python variable holding the reference to this widget is
NOT automatically set to `None`.**\
It continues to point to an object that no longer exists in Tk.\
This is known as a *dangling reference*.

------------------------------------------------------------------------

## 🚨 Typical Symptom

When the code does something like:

-   `variable is not None`\
-   then calls `.config()`, `.insert()`, `.delete()` on the widget

Tkinter raises an error:

    _tkinter.TclError: invalid command name ".!frame.!labelframe.!frame.!text"

This means:\
👉 *"The widget you are trying to modify does not exist anymore."*

------------------------------------------------------------------------

## Why This Happens

-   `destroy()` removes the widget from Tk's internal system.\
-   However, the Python variable referencing that widget **is not
    cleared**.

So from Python's point of view:\
➡️ the variable still exists\
➡️ but from Tk's point of view:\
➡️ the widget no longer exists

It's like holding the address of a house that has been demolished...

------------------------------------------------------------------------

## 🧠 The Clean Solution

Always follow **two mandatory steps** when removing a dynamic Tkinter
widget:

1.  **Destroy the widget on the Tk side**
    -   using `.destroy()`
2.  **Clear the Python reference**
    -   by setting the variable to `None`

Then the rest of the program can safely check:

``` python
if widget is not None:
    # the widget still exists on the Python side
```

But if you do:

``` python
widget = None
```

Then:

-   Python knows there is no widget
-   Tkinter will not be called on a destroyed component
-   And you will never see the error "invalid command name" again

------------------------------------------------------------------------

## 🧩 Why This Matters for the Help / Context Panels

In your program:

-   you open a help panel\
-   you close it via `.destroy()`\
-   but the variables `panneau_aide_actif`, `zone_texte_aide`, etc.\
    **still contained the old reference**

So, when switching language:

-   `changer_langue()` sees `zone_texte_aide is not None`\
-   assumes the widget still exists\
-   calls `charger_fichier_aide()`\
-   which calls `zone_texte_aide.config(...)`\
-   BUT the widget no longer exists on the Tk side\
-   → TclError

The proper approach is to use a dedicated `close_help()` function that:

-   destroys the widget\
-   resets all related variables to `None`\
-   recalculates the window's geometry

------------------------------------------------------------------------

## 📝 Key Points to Remember

✔ A Tkinter widget destroyed by `.destroy()` is **not** automatically
cleared in Python\
✔ Always manually reset the reference to `None`\
✔ Always check both `widget is not None` and `widget.winfo_exists()`
before using a widget\
✔ Doing so prevents all `TclError: invalid command name` issues

------------------------------------------------------------------------

This memo serves as a reminder for all Tkinter interfaces involving
dynamic panels or windows.

**Pylo**
