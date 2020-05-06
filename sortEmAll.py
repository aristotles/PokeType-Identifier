import tensorflow as tf
AUTOTUNE = tf.data.experimental.AUTOTUNE
import IPython.display as display
from PIL import Image
import numpy as np
import os
import pathlib
import pandas as pd


path = "/Users/samuel/Downloads/samCsv.csv"

df = pd.read_csv(path)

dataset = df.values

count=0

for x in dataset:
        type=(df.iloc[count]['primaryType'])
        name=(df.iloc[count]['name'])
        path=(df.iloc[count]['imageUrl'])
        if type == "Normal":
            os.rename(path, "/Users/samuel/GitHub/turbo-guacamole/input/class1/"+name+".png")

        if type == "Grass":
            os.rename(path, "/Users/samuel/GitHub/turbo-guacamole/input/class4/"+name+".png")
        if type == "Water":
            os.rename(path, "/Users/samuel/GitHub/turbo-guacamole/input/class3/"+name+".png")
        if type == "Bug":
            os.rename(path, "/Users/samuel/GitHub/turbo-guacamole/input/class4/"+name+".png")
        if type == "Fairy":
            os.rename(path, "/Users/samuel/GitHub/turbo-guacamole/input/class1/"+name+".png")
        if type == "Dark":
            os.rename(path, "/Users/samuel/GitHub/turbo-guacamole/input/class6/"+name+".png")
        if type == "Fighting":
            os.rename(path, "/Users/samuel/GitHub/turbo-guacamole/input/class1/"+name+".png")
        if type == "Rock":
            os.rename(path, "/Users/samuel/GitHub/turbo-guacamole/input/class5/"+name+".png")
        if type == "Steel":
            os.rename(path, "/Users/samuel/GitHub/turbo-guacamole/input/class5/"+name+".png")
        if type == "Ground":
            os.rename(path, "/Users/samuel/GitHub/turbo-guacamole/input/class5/"+name+".png")
        if type == "Flying":
            os.rename(path, "/Users/samuel/GitHub/turbo-guacamole/input/class2/"+name+".png")

        if type == "Ice":
            os.rename(path, "/Users/samuel/GitHub/turbo-guacamole/input/class3/"+name+".png")

        if type == "Ghost":
            os.rename(path, "/Users/samuel/GitHub/turbo-guacamole/input/class6/"+name+".png")

        count+=1

import split_folders

split_folders.ratio('input', output="of6", seed=44, ratio=(.8, .1, .1))
