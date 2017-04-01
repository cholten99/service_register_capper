# Imports
from images2gif import writeGif
from PIL import Image
import os

# Get the names of all the picture files in the "pics" folder into an array
file_names = sorted((file_name for file_name in os.listdir('pics')))

# Create an arrange of binary images from the list of files
image_array = [Image.open("pics/" + file_name) for file_name in file_names]

# Create animated gif from list of binary images
# writeGif("animation.gif", image_array, duration = 1)
