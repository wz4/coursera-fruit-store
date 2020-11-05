#!/usr/bin/env python3

import os
from PIL import Image

def convert_image(image):
    try:
        im = Image.open('supplier-data/images/' + image)
        new = im.resize((600, 400)).convert('RGB')
        name = image.split('.')
        path = 'supplier-data/images/' + name[0] + '.jpeg'
        print(path)
        new.save(path, 'jpeg')
        print('SAVED!')

    except IOError as e:
        print(e)

def process_images():
    for file in os.listdir('supplier-data/images'):
        convert_image(file)

if __name__ == "__main__":
    process_images()