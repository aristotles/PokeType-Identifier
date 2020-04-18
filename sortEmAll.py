import tensorflow as tf
AUTOTUNE = tf.data.experimental.AUTOTUNE
import IPython.display as display
from PIL import Image
import numpy as np
import os
import pathlib
import pandas as pd


path = "/Users/samuel/Downloads/pokeCsvNew.csv"

df = pd.read_csv(path)

dataset = df.values

count=0

for x in dataset:
        type=(df.iloc[count]['type'])
        name=(df.iloc[count]['name'])
        path=(df.iloc[count]['location'])
        if type == "Normal":
            os.rename(path, "/Users/samuel/GitHub/turbo-guacamole/input/class1/"+name+".png")
        if type == "Fire":
            os.rename(path, "/Users/samuel/GitHub/turbo-guacamole/input/class2/"+name+".png")
        if type == "Grass":
            os.rename(path, "/Users/samuel/GitHub/turbo-guacamole/input/class3/"+name+".png")
        if type == "Water":
            os.rename(path, "/Users/samuel/GitHub/turbo-guacamole/input/class4/"+name+".png")
        if type == "Bug":
            os.rename(path, "/Users/samuel/GitHub/turbo-guacamole/input/class5/"+name+".png")
        if type == "Fairy":
            os.rename(path, "/Users/samuel/GitHub/turbo-guacamole/input/class6/"+name+".png")
        if type == "Dark":
            os.rename(path, "/Users/samuel/GitHub/turbo-guacamole/input/class7/"+name+".png")
        if type == "Psychic":
            os.rename(path, "/Users/samuel/GitHub/turbo-guacamole/input/class8/"+name+".png")
        if type == "Fighting":
            os.rename(path, "/Users/samuel/GitHub/turbo-guacamole/input/class9/"+name+".png")
        if type == "Rock":
            os.rename(path, "/Users/samuel/GitHub/turbo-guacamole/input/class10/"+name+".png")
        if type == "Steel":
            os.rename(path, "/Users/samuel/GitHub/turbo-guacamole/input/class11/"+name+".png")
        if type == "Ground":
            os.rename(path, "/Users/samuel/GitHub/turbo-guacamole/input/class12/"+name+".png")
        if type == "Flying":
            os.rename(path, "/Users/samuel/GitHub/turbo-guacamole/input/class13/"+name+".png")
        if type == "Electric":
            os.rename(path, "/Users/samuel/GitHub/turbo-guacamole/input/class14/"+name+".png")
        if type == "Ice":
            os.rename(path, "/Users/samuel/GitHub/turbo-guacamole/input/class15/"+name+".png")
        if type == "Dragon":
            os.rename(path, "/Users/samuel/GitHub/turbo-guacamole/input/class16/"+name+".png")
        if type == "Ghost":
            os.rename(path, "/Users/samuel/GitHub/turbo-guacamole/input/class17/"+name+".png")
        if type == "Poison":
            os.rename(path, "/Users/samuel/GitHub/turbo-guacamole/input/class18/"+name+".png")

        count+=1

import split_folders

split_folders.ratio('input', output="output", seed=1337, ratio=(.8, .1, .1))
