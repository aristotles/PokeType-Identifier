
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from skimage.io import imread, imshow

image = imread('/Users/samuel/GitHub/turbo-guacamole/torchic.jpg')
imshow(image)
print(image.shape)

feature_matrix = np.zeros((1000,607))
print(feature_matrix.shape)

for i in range(0,image.shape[0]):
    for j in range(0,image.shape[1]):
        feature_matrix[i][j] = ((int(image[i,j,0]) + int(image[i,j,1]) + int(image[i,j,2]))/3)

features = np.reshape(feature_matrix, (1000*607))
print(features.shape)
plt.show(features.shape)
