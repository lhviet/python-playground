import random
from math import sqrt
from matplotlib import pyplot as plt
from learntools.python.quickdraw import random_category, sample_images_of_category, draw_images_on_subplots

## Step 1: Sample some sketches
# How many sketches to view - a random number from 2 to 20
n = random.randint(2, 20)
# Choose a random quickdraw category. (Check out https://quickdraw.withgoogle.com/data for an overview of categories)
category = random_category()
imgs = sample_images_of_category(n, category)

## Step 2: Choose the grid properties
######## Your changes should go here ###############
cols = 8
if n < 8 or n == 8:
    cols = n
else:
    list = []
    for i in range(1, 8):
        list.append(n % i)
    list.append(n % (int(sqrt(n)) + 1))
    list.reverse()
    index = list.index(min(list))
    if index == 0:
        cols = int(sqrt(n)) + 1
    else:
        cols = 8 - index
rows = int(n / cols) + int(bool(n % cols))
# The height and width of the whole grid, measured in inches.
height = rows * 2
width = cols * 2

print(f'{n} images')
print(f'{rows} rows x {cols} cols')
print(f'{width} x {height} inches')

## Step 3: Create the grid
grid = plt.subplots(rows, cols, figsize=(width, height))

## Step 4: Draw the sketches in the grid
draw_images_on_subplots(imgs, grid)