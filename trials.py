import tensorflow as tf
AUTOTUNE = tf.data.experimental.AUTOTUNE
import IPython.display as display
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import pathlib
import pandas as pd
from skimage.io import imread, imshow
from sklearn.model_selection import train_test_split

path = "/Users/samuel/Downloads/pokemen2.csv"

#Load the data from local file into a dataframe
df = pd.read_csv(path)
#select input and output
Y = df['primaryType'].values.reshape(df.shape[0],1) #select the label (correct output)
df = df.drop('primaryType', 1)
df = df.drop('secondaryType', 1)
df = df.drop('name', 1) #remove the label from input
dataset = df.values
count=0

newDataFrame = pd.DataFrame([0], columns=["Feature1"])

for x in dataset:

        image = imread(x[0])
        imshow(image)


        feature_matrix = np.zeros((1000,607))


        for i in range(0,image.shape[0]):
            for j in range(0,image.shape[1]):
                feature_matrix[i][j] = ((int(image[i,j,0]) + int(image[i,j,1]) + int(image[i,j,2]))/3)

        features = np.reshape(feature_matrix, (1000*607))

        newDataFrame.loc[count] = {"Feature1": features.tostring()}
        print(count)
        count+=1

count=0


# plt.show()

dataset = newDataFrame.values
newDataFrame.to_csv("pokePixCSV.csv", encoding='utf-8')

X = dataset[:,0:dataset.shape[1]] #select features (input data)
#splitting the data into training and testing
print(X.shape)
print(Y.shape)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2 ) # training to testing ratio is 0.8:0.2
#Now {X_train, X_test, Y_train, Y_test} can be fed to Keras model
