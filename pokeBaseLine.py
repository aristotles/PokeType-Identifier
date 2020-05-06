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
    print(theType)
    if theType == "Rock" or theType == "Ground" or theType == "Steel":
        allTypes.append("Type1")

    if theType == "Bug" or theType == "Grass":
        allTypes.append("Type2")
    if theType == "Flying":
        allTypes.append("Type3")
    if theType == "Dark" or theType == "Ghost":
        allTypes.append("Type4")
    if theType == "Normal" or theType == "Fairy" or theType == "Fighting":
        allTypes.append("Type5")
    if theType == "Water" or theType == "Ice":
        allTypes.append("Type6")

    count+=1


print(len(allTypes))

count=0

numberRight=0
numberWrong=0
for x in dataset:

    realType=(df.iloc[count]['type'])
    
    if realType == "Rock" or realType == "Ground" or realType == "Steel":

        guessingType=(random.choice(allTypes))

        if "Type1" == guessingType:
            numberRight+=1
        else:
            numberWrong+=1


    if realType == "Grass" or realType == "Bug":

        guessingType=(random.choice(allTypes))

        if "Type2" == guessingType:
            numberRight+=1
        else:
            numberWrong+=1

    if realType == "Flying":

        guessingType=(random.choice(allTypes))

        if "Type3" == guessingType:
            numberRight+=1
        else:
            numberWrong+=1
    if realType == "Dark" or realType == "Ghost":

        guessingType=(random.choice(allTypes))

        if "Type4" == guessingType:
            numberRight+=1
        else:
            numberWrong+=1
    if realType == "Normal" or realType == "Fairy" or realType == "Fighting":

        guessingType=(random.choice(allTypes))

        if "Type5" == guessingType:
            numberRight+=1
        else:
            numberWrong+=1

    if realType == "Water" or realType == "Ice":

        guessingType=(random.choice(allTypes))

        if "Type6" == guessingType:
            numberRight+=1
        else:
            numberWrong+=1

    count+=1




print("right:")
print(numberRight)
print("wrong:")
print(numberWrong)
print("accuracy:")
print(numberRight/(numberWrong+numberRight))
