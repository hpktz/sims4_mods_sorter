# 🎮 Sims4 Mods Sorter

This Python program automatically organizes the `.package` files you download to add extra items to your Sims 4 game.

## 🎈 Why Use It?

If you're a Sims 4 player, you've probably downloaded mods to add new items to your game. However, it's not always easy to find the right place for these files. This program helps you organize your mods more efficiently!

## 🛠️ Prerequisites

- Python 3.6 or higher → [Download Python](https://www.python.org/downloads/)
- Pip → [Download Pip](https://pip.pypa.io/en/stable/installing/)
- Sims 4 installed on your computer
- Windows 10 or higher

## 📦 Installation

1. Clone the repository
   ```bash
   git clone https://github.com/hpktz/sims4_mods_sorter
   ```

2. Install the required packages
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 How to Use

1. Navigate to your mods folder
   Usually, mods are located here:
   ```bash
   cd Documents/Electronic Arts/The Sims 4/Mods/CAS
   ```

2. Create categories for your mods by creating folders with the names of the categories (in your language) you want to use.
   **Example:**
   ```bash
   mkdir Accessories # This will create a folder named Accessories
   ```

3. Update the categories in English in the `main.py` file by changing the `categories` variable on **line 15** with this syntax:
   ```python
   categories = ['<category1>', '<category2>', '<category3>', ...]
   ```

4. Then add the translation of the categories in your language in the `categories_dir` variable on **line 17** with this syntax:
   ```python
   categories_dir = {
       '<category1>': '<category1_in_your_language>',
       '<category2>': '<category2_in_your_language>',
       '<category3>': '<category3_in_your_language>',
       ...
   }
   ```

5. (Optional) If you want to ensure that the program does not move the files to the wrong folder, you can add keywords associated with the categories in the `pre_filters` variable on **line 30** with this syntax:
   ```python
   pre_filters = {
       '<category1>': [
           '<keyword1>',
           '<keyword2>',
           '<keyword3>',
           ...
       ],
       '<category2>': [
           '<keyword1>',
           '<keyword2>',
           '<keyword3>',
           ...
       ],
       '<category3>': [
           '<keyword1>',
           '<keyword2>',
           '<keyword3>',
           ...
       ],
       ...
   }
   ```

6. Download your mods to the `Downloads` folder.

7. Run the program
   ```bash
   python main.py
   ```
