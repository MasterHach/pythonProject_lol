import matplotlib.pyplot as plt
import numpy as np
import random as rand


def square_gen():
    square = [[0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0]]
    for i in range(5):
        for j in range(3):
            square[i][j] = rand.randint(0, 1)
            if square[i][j] == 1 and j != 2:
                square[i][4 - j] = 1
    return square


def square_show(square):
    res = np.zeros((5, 5, 3))
    for i in range(5):
        for j in range(5):
            if square[i][j] == 1:
                res[i][j] = 255,255,255
    return res


fig, axes = plt.subplots(nrows=10, ncols=10)
for ax in axes.flat:
    ax.imshow(square_show(square_gen()))
    ax.axis('off')
plt.show()


# square_show(square_gen())


