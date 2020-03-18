#!/usr/bin/python3.6

"""
        --- Draw Bar chart and Graph ---
This module take data from the csv files in data folde rand plots two types of graphs.
Daily covid-19 data and progress tracker.

"""

import csv
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt 
import os
import pandas as pd
from datetime import date
from get_data import current_data, create_csv 
import glob

path = "data/"
data_lst = glob.glob("./data/*.csv")
data_lst.sort(key = os.path.getmtime, reverse = True)

def bar_chart():
    today = date.today()
    current_date = today.strftime("%d-%m-%Y")
    file_path = path + current_date + ".csv"
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
   
    # Converting all parameters to tuples
    cnf_in = tuple([int(x) for x in cnf_in])
    cnf_fn = tuple([int(x) for x in cnf_fn])
    cured = tuple([int(x) for x in cured])
    death = tuple([int(x) for x in death])

    # Creating Plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    print(len(index))
    bar_width = 0.25
    opacity = 0.8
    leg_1 = plt.bar(index, cnf_in, bar_width,
            alpha=opacity,
            color='#117391',
            label='Indian Confirmed')

    leg_2 = plt.bar(index, cnf_fn, bar_width,
            alpha=opacity,
            color='#6aafdb',
            label='Foreign Confirmed')

    leg_3 = plt.bar(index, cured, bar_width,
            alpha=opacity,
            color='#5cdb9b',
            label='Cured')

    leg_4 = plt.bar(index, death, bar_width,
            alpha=opacity,
            color='#ff3f0f',
            label='Deaths')

    plt.xlabel('People')
    plt.ylabel('Number')
    plt.title('COVID-19 Data (statewise)')
    plt.xticks(index + bar_width, states)
    plt.legend()

    plt.tight_layout()
    plt.show()


bar_chart()




