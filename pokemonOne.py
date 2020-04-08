
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from skimage.io import imread, imshow


myPanda=pd.read_csv('pokePixCSV.csv')

plt.plot(np.fromstring(myPanda.loc[1]['Feature1']))
plt.show()
print("hello")
