# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 22:49:10 2023

@author: Yunus
"""

from PIL import Image
import os


input_dir = 'code/rice/Bacterialblight'
output_dir = 'code/rice/BacterialblightJPEG'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for file_name in os.listdir(input_dir):
    # Check if the file is an image
    if file_name.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.JPG', '.BMP', '.PNG', 'JPEG')):
        # Open the image
        image_path = os.path.join(input_dir, file_name)
        image = Image.open(image_path)

        # Convert to JPEG format
        if image.mode != 'RGB':
            image = image.convert('RGB')

        # Save the converted image
        output_path = os.path.join(output_dir, file_name.split('.')[0] + '.jpeg')
        image.save(output_path, format='JPEG')