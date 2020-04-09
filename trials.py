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
import seaborn as sns

from sklearn.linear_model import LogisticRegressionCV

from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Flatten
from tensorflow.keras.utils import to_categorical

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
        if count < 1000:
            image = imread(x[0])
            imshow(image)


            feature_matrix = np.zeros((140,140))


            for i in range(0,image.shape[0]):
                for j in range(0,image.shape[1]):
                    feature_matrix[i][j] = ((int(image[i,j,0]) + int(image[i,j,1]) + int(image[i,j,2]))/3)

            # features = np.reshape(feature_matrix, (1000*607))

            newDataFrame.loc[count] = {"Feature1": feature_matrix}

            # print(features.tostring())

        count+=1

count=0


# plt.show()
# print(newDataFrame)
# newString=newDataFrame.loc[2]["Feature1"]
# plt.imshow(newString,aspect="auto")
# plt.show()
# newString=newDataFrame.loc[6]["Feature1"]
# plt.imshow(newString,aspect="auto")
# plt.show()
# newString=newDataFrame.loc[7]["Feature1"]
# print(len(newString))
# newString.replace('[','')
# newString.replace(']','')
# print(len(newDataFrame.loc[2]["Feature1"]))
# print(len(newString))
# print(newString)
# print(newDataFrame.loc[2]["Feature1"])
# print(newString)
# print(newString.shape)

# random = np.random.normal(0,1,size=[100,100])
# plt.imshow(newString,aspect="auto")
# plt.show()

dataset = newDataFrame.values
# newDataFrame.to_csv("pokePixCSV.csv", encoding='utf-8')

X = dataset[:,0:dataset.shape[1]] #select features (input data)

nb_classes = 18

print(X.shape)
print(Y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2 )

for i in range(9):
    plt.subplot(3,3,i+1)
    plt.xticks([])
    plt.yticks([])
    newString=X_train[i][0]
    # plt.imshow(newString, cmap='gray', interpolation='none')
    # plt.show()
    print("Class {}".format(y_train[i]))
    print(i)
    plt.title("Class {}".format(y_train[i]))

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

X_train /= 255
X_test /= 255

y_train = to_categorical(y_train,nb_classes)
y_test = to_categorical(y_test,nb_classes)

print(y_test)

model = Sequential([ Flatten(input_shape=(28,28)), Dense(512, activation='relu'), Dense(512,activation='relu'), Dense(10,activation='softmax')])

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X_train, y_train, batch_size=128, epochs=4, verbose=1,)

loss,accuracy = model.evaluate(X_test, y_test, verbose=1)
print('Test score (loss):', loss)
print('Test accuracy:', accuracy)
