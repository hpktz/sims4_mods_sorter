from transformers import pipeline
import os
import glob
import re
import logging
import shutil

logging.disable(logging.CRITICAL)

def mose_to_correct_dest(file_name):
    classifier = pipeline("zero-shot-classification", 
                      model="valhalla/distilbart-mnli-12-3", 
                      device=1)

    categories = ["bottom", "accessory", "jewerly", "shoes", "hair", "full body", "top", "makeup", "facial features"]

    categories_dir = {
        "bottom": "Bas",
        "accessory": "Accessoires",
        "jewerly": "Bijoux",
        "shoes": "Chaussures",
        "hair": "Cheveux",
        "full body": "Ensembles",
        "top": "Hauts",
        "makeup": "Maquillage",
        "facial features": "Peau",
        "other": "Autres"
    }

    pre_filters = {
        "bottom": ["skirt", "jeans", "pants", "leggings", "shorts", "panties"],
        "jewerly": ["earrings", "necklace", "rings", "bracelet", "choker", "watch", "hoops"],
        "shoes": ["boots", "pumps", "strap", "sneakers"],
        "full body": ["dress", "outfit", "body", "body suit"],
        "top": ["blazer", "jacket", "vest", "tank"],
        "makeup": ["blush", "highlighter", "eyeliner", "eyeshadow", "lipstick", "gloss", "contour"],
        "skin": ["eyebrows", "freckles", "cheekmole"]
    }

    file_name_b = file_name.split("\\")[-1]
    file_name_b = file_name_b.rstrip('.package')
    file_name_b = file_name_b.replace('_', ' ')
    file_name_b = re.sub(r'([a-z])([A-Z])', r'\1 \2', file_name_b)
    file_name_b = file_name_b.lower()

    for key_word, words in pre_filters.items():
        for word in words:
            if word in file_name_b:
                directory = key_word
                break
        else:
            continue
        break
    else:
        directory = None
    

    if not directory:
        directory = classifier(file_name, categories)
        if directory["scores"][0] > 0.25:
            directory = directory["labels"][0]
        else:
            directory = "other"
    
    directory = categories_dir[directory]

    output_dir = './Documents/Electronic Arts/Les Sims 4/Mods/CAS/' + directory +'/' + file_name.split("\\")[-1]

    if os.path.exists(output_dir):
        return(f"Le fichier {output_dir} existe déjà.")
    else:
        shutil.move(file_name, output_dir)
        return(f"Le fichier a été déplacé vers : {directory}")




input_dir = './Downloads'
files_pack = glob.glob(os.path.join(input_dir, '*.package'))

for index, file  in enumerate(files_pack):
    print(str(index) + "/" + str(len(files_pack)) + ":" + mose_to_correct_dest(file))
