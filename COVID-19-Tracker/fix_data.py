#!/usr/bin/python3.6
import pandas as pd
import csv
import os

path='data'
files = os.listdir(path)
print(files)
def format_data(csv_file):
    df = pd.read_csv(csv_file)
    df = df[['label', 'state', 'confirmed', 'cured', 'death']]
    print(df.head())
    df.to_csv(csv_file, index=False)

for f in files:
    format_data(os.path.join(path, f))
