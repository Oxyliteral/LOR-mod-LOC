import os
from krita import *

# Set the desired width and height
target_width = 512
target_height = 768

# Get the current document
application = Krita.instance()
folder_path = r""  # Change this to your folder path
# List all PNG files in the specified folder
images = [f for f in os.listdir(folder_path) if f.lower().endswith('.png')]

for image_name in images:
    # Construct the full path to the image
    image_path = os.path.join(folder_path, image_name)
    
    # Load the image
    doc = application.openDocument(image_path)
    if doc:
        width = doc.width() - target_width
        height = doc.height() - target_height
        doc.resizeImage(width // 2, height // 2, target_width, target_height)
        if doc.save() == False:
            break
        doc.close()
    else:
        print(f"Failed to load document: {image_name}")