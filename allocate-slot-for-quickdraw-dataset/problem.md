<hr/>
## 6. <span title="Spicy" style="color: coral">🌶️🌶️</span>

The following is an example of a tricky piece of arithmetic manipulation you might encounter when using Python for visualization.

Suppose we're working with the [QuickDraw dataset](https://www.kaggle.com/google/tinyquickdraw) of doodled sketches and we want to visualize several sketches at once in a grid-like arrangement.

We'd like to reserve 2x2 inches for each image, and we'd like the whole grid to be no wider than 16 inches.

The code below almost works. It does the following:

1. Get a random number of sketches from some category (e.g. bears, stars, hockey sticks...)
2. Create variables `rows`, `cols`, `height`, and `width`, setting them to numbers we pulled out of the air.
3. Calls `plt.subplots()` using the variables from step 2, which creates a grid with the given characteristics.
4. Draws the sketches from step 1 in the grid from step 3.

Try running the cell a few times to see it in action.

```python
import random
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
rows = 3
cols = 5
# The height and width of the whole grid, measured in inches.
height = 5
width = 16

## Step 3: Create the grid
grid = plt.subplots(rows, cols, figsize=(width, height))

## Step 4: Draw the sketches in the grid
draw_images_on_subplots(imgs, grid)
```

You may have noticed a few problems (with accompanying warning messages printed out):

- We wanted each image to be drawn in a square (with width and height of 2 inches), but they're being drawn inside fat rectangles.
- Our grid can only fit at most 15 images. If we sample more than that, only the first 15 are shown.
- If we sample a small number of images, we waste a lot of space.

All these problems stem from our shoddy approach to step 2 in the code. Instead of using the same grid dimensions every time, they should adapt to the number of images we're showing. For example, if `n = 3`,  we should make a 6" x 2" grid with 1 row and 3 columns. If `n = 15`, we should make a 16" x 4" grid with 2 rows and 8 columns. (We'll have one empty space in the grid, but that's okay, as long as we don't have whole rows or columns that are empty.)

Update the code above to fix the values of `rows`, `cols`, `width`, and `height`, so that our grid adapts to the number of images shown and makes efficient use of space. Run your code a few times to make sure it doesn't generate any warnings.

<small>**Note**: I'm intentionally glossing over the details of steps 1, 3, and 4 of the code. If you're curious about how the functions we imported such as `sample_images_of_category`, or `draw_images_on_subplots` work, you can check out their definitions [here](https://github.com/Kaggle/learntools/blob/master/learntools/python/quickdraw.py). The code uses lots of syntax and data structures that we'll cover later, so if it looks like gibberish to you at this point, don't worry. We will *not* be going into the specifics of data visualization using matplotlib or any other library in this course. But fortunately, we have a [course on Kaggle Learn](https://www.kaggle.com/learn/data-visualisation) on just that topic.</small>

**Bonus**: Can you code this in a way the minimizes the number of empty cells (while obeying the original constraints about 2x2 inches per image and no more than 16" total width)? For example, a naive solution for `n = 10` might create an 8x2 grid, meaning the bottom row would have only 2 images, and 4 empty spaces. A more clever solution would set `rows = 2`, and `columns = 5`.