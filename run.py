#! /usr/bin/env python3

import os
import requests

def submit(dat):
    url = 'http://104.154.31.122/fruits/'
    response = requests.post(url, json=dat)
    response.raise_for_status()
    print(response.status_code)

def process_files():
    review_dir = 'supplier-data/descriptions/'
    keys = ('name', 'weight', 'description', 'image_name')
    fruits = {}
    for file in os.listdir(review_dir):
        with open(review_dir + file) as f:
            file_name = file.split('.')
            for i, line in enumerate(f, start=0):
                #convert weight to int
                if i is 1:
                    weight = line.split()
                    weight = int(weight[0])
                    fruits[keys[i]] = weight
                else:    
                    fruits[keys[i]] = line.strip()
            fruits['image_name'] = file_name[0] + '.jpeg'
        response = submit(fruits)

if __name__ == "__main__":
    process_files()