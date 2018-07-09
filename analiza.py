import os
import pandas as pd

directory = "./gngdata"



for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        print("found: " + filename)
        filename = "gngdata/" + filename

        csv = pd.read_csv(filename)
        print(csv.head())

    else:
        pass

