# 🎮 Sims4 Mods Sorter

Ce programme Python organise automatiquement les fichiers `.package` que vous téléchargez pour ajouter des éléments supplémentaires dans votre jeu Sims 4.

## 🎈 Pourquoi l'utiliser ?

Si vous êtes un joueur de Sims 4, vous avez probablement téléchargé des mods pour ajouter de nouveaux objets à votre jeu. Cependant, il n'est pas toujours facile de trouver le bon emplacement pour ces fichiers. Ce programme vous aide à organiser vos mods de manière plus efficace !

## 🛠️ Prérequis

- Python 3.6 ou supérieur → [Télécharger Python](https://www.python.org/downloads/)
- Pip → [Télécharger Pip](https://pip.pypa.io/en/stable/installing/)
- Sims 4 installé sur votre ordinateur
- Windows 10 ou supérieur

## 📦 Installation

1. Clonez le dépôt
   ```bash
   git clone https://github.com/hpktz/sims4_mods_sorter
   ```

2. Installez les packages requis
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Comment l'utiliser

1. Accédez au dossier de vos mods
   Habituellement, les mods se trouvent ici :
   ```bash
   cd Documents/Electronic Arts/The Sims 4/Mods/CAS
   ```

2. Créez des catégories pour vos mods en créant des dossiers avec les noms des catégories (dans votre langue) que vous souhaitez utiliser.
   **Exemple :**
   ```bash
   mkdir Accessoires # Cela créera un dossier appelé Accessoires
   ```

3. Mettez à jour les catégories en anglais dans le fichier `main.py` en modifiant la variable `categories` à la **ligne 15** avec cette syntaxe :
   ```python
   categories = ['<categorie1>', '<categorie2>', '<categorie3>', ...]
   ```

4. Ajoutez ensuite la traduction des catégories dans votre langue dans la variable `categories_dir` à la **ligne 17** avec cette syntaxe :
   ```python
   categories_dir = {
       '<categorie1>': '<categorie1_in_your_langage>',
       '<categorie2>': '<categorie2_in_your_langage>',
       '<categorie3>': '<categorie3_in_your_langage>',
       ...
   }
   ```

5. (Optionnel) Si vous souhaitez vous assurer que le programme ne déplace pas les fichiers dans le mauvais dossier, vous pouvez ajouter des mots-clés associés aux catégories dans la variable `pre_filters` à la **ligne 30** avec cette syntaxe :
   ```python
   pre_filters = {
       '<categorie1>': [
           '<keyword1>',
           '<keyword2>',
           '<keyword3>',
           ...
       ],
       '<categorie2>': [
           '<keyword1>',
           '<keyword2>',
           '<keyword3>',
           ...
       ],
       '<categorie3>': [
           '<keyword1>',
           '<keyword2>',
           '<keyword3>',
           ...
       ],
       ...
   }
   ```

6. Téléchargez vos mods dans le dossier `Downloads`.

7. Exécutez le programme
   ```bash
   python main.py
   ```