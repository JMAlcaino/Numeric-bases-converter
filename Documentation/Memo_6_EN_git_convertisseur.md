# Git Memo – “Numeric Bases Converter” Project

This memo summarizes the most useful Git commands for your project, following your usual workflow:

- **main** branch → stable, published version on GitHub  
- **dev** branch → work area, tests, new features

---

## 1. Update the `main` branch from `dev`

### 1.1. Simple method via GitHub (Pull Request)

1. Go to your GitHub repository → **Pull requests** tab  
2. Click **New pull request**  
3. Choose:
   - **base** = `main`
   - **compare** = `dev`
4. Review the differences  
5. Click **Create pull request**  
6. Add a title (e.g., `Merge dev → main`)  
7. Click **Merge pull request**  
8. Confirm with **Confirm merge**

> Result: `main` now contains everything from `dev`.

---

### 1.2. Same operation via command line

```bash
git checkout main
git pull origin main
git merge dev
git push origin main
```

---

## 2. Update **a single file** from `dev` into `main`

### 2.1. GitHub method (copy/paste)

1. On GitHub, switch to the **dev** branch  
2. Open the file you want to transfer  
3. Click the **Edit** icon (pencil)  
4. Copy the entire file content  
5. Switch to **main**  
6. Open the same file  
7. Click **Edit**, paste the content  
8. Commit (e.g., `Updated file from dev`)

> Useful for correcting one file without merging the entire branch.

---

### 2.2. Command-line method: checkout a specific file

```bash
git checkout main
git checkout dev -- path/to/file.py
git add path/to/file.py
git commit -m "Updated file from dev"
git push origin main
```

Example for your project:

```bash
git checkout main
git checkout dev -- src/convertisseur_bases.py
git add src/convertisseur_bases.py
git commit -m "Update convertisseur_bases from dev"
git push origin main
```

---

## 3. Update your `dev` branch from `main`

```bash
git checkout dev

git checkout main
git pull origin main

git checkout dev
git merge main

git push origin dev   # optional
```

> Do this when you have released a stable version on `main` and want to continue development from a clean base.

---

## 4. Recommended workflow for your project

1. Develop and test in **dev**  
2. When stable:
   - Create a Pull Request `dev → main`  
   - OR merge locally and push  
3. For a small isolated fix:
   - Update a **single file** (Section 2)  
4. Keep **main** clean and stable for:
   - Public GitHub  
   - Future releases  
   - Documentation reference  

---

## 5. Useful Git commands (quick reference)

```bash
git branch              # Show current branch
git branch -a           # List all branches
git checkout -b new     # Create new branch
git status              # Show file changes
git log --oneline --graph --all   # History with graph
```

---

*Memo written with your copilote Pylo – Per Scientiam, ad Caelum ✈️*
