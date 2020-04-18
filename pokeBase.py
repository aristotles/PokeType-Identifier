import numpy as np
import os
import pathlib
import pandas as pd
import random


path = "/Users/samuel/Downloads/pokeCsvNew.csv"

df = pd.read_csv(path)

dataset = df.values

count=0
allTypes=[]
for x in dataset:
    theType=(df.iloc[count]['type'])
    allTypes.append(theType)
    count+=1


count=0

numberRight=0
numberWrong=0
for x in dataset:

    realType=(df.iloc[count]['type'])
    name=(df.iloc[count]['name'])
    guessingType=(random.choice(allTypes))

    if realType == guessingType:
        numberRight+=1
    else:
        numberWrong+=1

    count +=1

print("right:")
print(numberRight)
print("wrong:")
print(numberWrong)
print("accuracy:")
print(numberRight/numberWrong)
