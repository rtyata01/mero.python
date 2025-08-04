import sys
from PIL import Image
import os

# Get the script's directory
script_dir = os.path.dirname(__file__)  

# Construct the full path to names.txt
file_path1 = os.path.join(script_dir, "cartoon1.gif")
file_path2 = os.path.join(script_dir, "cartoon2.gif")
file_path_save = os.path.join(script_dir, "cartoons.gif")

images = []
image1 = Image.open(file_path1)
images.append(image1)
image2 = Image.open(file_path2)
images.append(image2)
    
images[0].save(file_path_save, save_all=True, append_images=[images[1]], duration=200, loop=0)