from transformers import pipeline
import os
import glob
import re
import logging
import shutil

# Disable all logging messages
logging.disable(logging.CRITICAL)

# Function to move file to the correct destination based on classification
def move_to_correct_dest(file_name):
    """
    Moves a file to the correct destination directory based on its name.
    This function uses a combination of pre-defined keyword filters and a zero-shot classification model to determine the category of the file. The file is then moved to a corresponding directory based on the identified category.
    
    Args:
        file_name (str): The full path of the file to be moved.
    
    Returns:
        str: A message indicating whether the file was moved or if it already exists in the destination directory.
    
    The function performs the following steps:
    1. Initializes a zero-shot classification pipeline using the "valhalla/distilbart-mnli-12-3" model.
    2. Defines a list of categories for classification.
    3. Maps each category to its respective directory.
    4. Defines pre-filters to quickly identify categories based on keywords in the file name.
    5. Extracts the base file name without path and extension, and processes it to be more readable.
    6. Checks if the file name contains any pre-filter keywords to determine the category.
    7. If no pre-filter match is found, uses the classifier to determine the category.
    8. Maps the identified category to the corresponding directory.
    9. Defines the output directory path based on the identified category.
    10. Moves the file to the output directory if it doesn't already exist, otherwise returns a message indicating the file already exists.
    """
    
    # Initialize the zero-shot classification pipeline
    classifier = pipeline("zero-shot-classification", 
                          model="valhalla/distilbart-mnli-12-3", 
                          device=1)

    # Define the categories for classification
    categories = ["bottom", "accessory", "jewelry", "shoes", "hair", "full body", "top", "makeup", "facial features"]

    # Map categories to their respective directories
    categories_dir = {
        "bottom": "Bas",
        "accessory": "Accessoires",
        "jewelry": "Bijoux",
        "shoes": "Chaussures",
        "hair": "Cheveux",
        "full body": "Ensembles",
        "top": "Hauts",
        "makeup": "Maquillage",
        "facial features": "Peau",
        "other": "Autres"
    }

    # Pre-filters to quickly identify categories based on keywords
    pre_filters = {
        "bottom": ["skirt", "jeans", "pants", "leggings", "shorts", "panties"],
        "jewelry": ["earrings", "necklace", "rings", "bracelet", "choker", "watch", "hoops"],
        "shoes": ["boots", "pumps", "strap", "sneakers"],
        "full body": ["dress", "outfit", "body", "body suit"],
        "top": ["blazer", "jacket", "vest", "tank"],
        "makeup": ["blush", "highlighter", "eyeliner", "eyeshadow", "lipstick", "gloss", "contour"],
        "skin": ["eyebrows", "freckles", "cheekmole"]
    }

    # Extract the base file name without path and extension
    file_name_b = file_name.split("\\")[-1]
    file_name_b = file_name_b.rstrip('.package')
    file_name_b = file_name_b.replace('_', ' ')
    file_name_b = re.sub(r'([a-z])([A-Z])', r'\1 \2', file_name_b)
    file_name_b = file_name_b.lower()

    # Check if the file name contains any pre-filter keywords
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

    # If no pre-filter match, use the classifier to determine the category
    if not directory:
        directory = classifier(file_name, categories)
        if directory["scores"][0] > 0.25:
            directory = directory["labels"][0]
        else:
            directory = "other"
    
    # Map the category to the corresponding directory
    directory = categories_dir[directory]

    # Define the output directory path
    output_dir = './Documents/Electronic Arts/Les Sims 4/Mods/CAS/' + directory + '/' + file_name.split("\\")[-1]

    # Move the file to the output directory if it doesn't already exist
    if os.path.exists(output_dir):
        return(f"The file {output_dir} already exists.")
    else:
        shutil.move(file_name, output_dir)
        return(f"The file has been moved to: {directory}")

# Define the input directory containing the files to be processed
input_dir = './Downloads'
# Get a list of all .package files in the input directory
files_pack = glob.glob(os.path.join(input_dir, '*.package'))

# Process each file and move it to the correct destination
for index, file in enumerate(files_pack):
    print(str(index) + "/" + str(len(files_pack)) + ": " + move_to_correct_dest(file))
