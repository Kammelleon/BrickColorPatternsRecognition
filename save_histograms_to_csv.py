import csv
import os
import numpy as np
import cv2

# label numbers:
# muszlowy - 0
# gothic - 1
# york - 2
# light - 3
# barwy_jesieni - 4


name = "gothic"
label_number = 1

folder = os.listdir(name)
folder_name = name
with open(f'{name}.csv', 'w+', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for item in folder:
        if item.endswith(".jpg") or item.endswith(".png"):
            image = item
            print(f"Processing: {image}")
            img = cv2.imread(f'{folder_name}/{image}')
            vals = img.mean(axis=2).flatten() # calculate mean value from RGB channels and flatten to 1D array
            data_points, bins = np.histogram(vals, range(257))
            data_points = list(data_points)
            data_points.append(label_number)
            writer.writerow(data_points)
