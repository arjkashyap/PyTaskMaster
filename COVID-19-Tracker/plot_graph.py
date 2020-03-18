#!/usr/bin/python3.6

"""
        --- Draw Bar chart and Graph ---
This module take data from the csv files in data folde rand plots two types of graphs.
Daily covid-19 data and progress tracker.

"""

import csv
import numpy as np
import matplotlib.pyplot as plt 
import os
import pandas as pd
from datetime import date
from get_data import current_data, create_csv 
import glob
import re

path = "data/"

# Sort CSV files according to each date
data_lst = glob.glob("data/*.csv")
data_lst.sort(key = os.path.getmtime, reverse = True)

# Draw bar chart based on latest data
def bar_chart():
    today = date.today()
    current_date = today.strftime("%d-%m-%Y")
    file_path = data_lst[0]
    # Getting data
    if len(data_lst) == 0:
        create_csv(current_data())

    print("File path: ", file_path)
    df = pd.read_csv(file_path)
    states = df['state'].tolist()
    del states[-1]
    n_groups = len(states)      # Number of groups
    states = tuple(states)
    print(states)

    cnf_in =df['indian_confirmed'].tolist()         # Confirmed Indian cases 
    cnf_fn = df['foreign_confirmed'].tolist()        # Confirmed Foreigners
    cured = df['cured'].tolist()
    death = df['death'].tolist()
    del cnf_in[-1], cnf_fn[-1], cured[-1], death[-1]
   
    # Creating Plot
    fig, ax = plt.subplots()
    
    index = np.arange(n_groups)
    print(len(index))
    bar_width = 0.5
    opacity = 0.8
    leg_1 = plt.bar(index, cnf_in, bar_width,
            alpha=opacity,
            color='#05028f',
            label='Indian Confirmed',
            )

    leg_2 = plt.bar(index, cnf_fn, bar_width,
            alpha=opacity,
            color='#6aafdb',
            label='Foreign Confirmed')

    leg_3 = plt.bar(index, cured, bar_width,
            alpha=opacity,
            color='#00c20f',
            label='Cured')

    leg_4 = plt.bar(index, death, bar_width,
            alpha=opacity,
            color='#ff3f0f',
            label='Deaths')

    plt.xlabel('People')
    plt.ylabel('Number')
    plt.title('COVID-19 Data (statewise)')
    plt.xticks(index + bar_width, states, rotation = 90)
    plt.legend() 
    plt.savefig("saved_graphs/" + current_date + ".png")
    plt.show()

# Draw graph which shows the progression through each date
def spread_chart():
    data = list(reversed(data_lst))
    x_labels = []
    
    # Reg ex to extract date
    regex = re.compile(r"\d\d[-]\d\d[-]\d\d\d\d")
    for day in data:
        label = regex.search(day)
        df = pd.read_csv(day)
        print(label.group())
        x_labels.append(label.group())
  #  cnf_in =df['indian_confirmed'].tolist()         # Confirmed Indian cases 
  #  cnf_fn = df['foreign_confirmed'].tolist()        # Confirmed Foreigners
  #  cured = df['cured'].tolist()
  #  death = df['death'].tolist()
  #  del cnf_in[-1], cnf_fn[-1], cured[-1], death[-1]

    print(x_labels)
spread_chart()
