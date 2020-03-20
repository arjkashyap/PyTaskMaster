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

    df = pd.read_csv(file_path)
    states = df['state'].tolist()
    del states[-1]
    n_groups = len(states)      # Number of groups
    states = tuple(states)

    cnf_in =df['indian_confirmed'].tolist()         # Confirmed Indian cases 
    cnf_fn = df['foreign_confirmed'].tolist()        # Confirmed Foreigners
    cured = df['cured'].tolist()
    death = df['death'].tolist()
    del cnf_in[-1], cnf_fn[-1], cured[-1], death[-1]

    # Creating Plot
    fig, ax = plt.subplots()

    index = np.arange(n_groups)
    bar_width = 0.5
    opacity = 0.8
    leg_1 = plt.bar(index, cnf_in, bar_width,
            alpha=opacity,
            color='#05028f',
            label='Indian Confirmed',
            yerr = None)

    leg_2 = plt.bar(index, cnf_fn, bar_width,
            alpha=opacity,
            color='#6aafdb',
            label='Foreign Confirmed',
            yerr=None
            )

    leg_3 = plt.bar(index, cured, bar_width,
            alpha=opacity,
            color='#00c20f',
            label='Cured',
            yerr=None
            )

    leg_4 = plt.bar(index, death, bar_width,
            alpha=opacity,
            color='#ff3f0f',
            label='Deaths',
            yerr=None
            )

    plt.xlabel('People', fontweight='bold', fontsize='17', horizontalalignment='center')
    plt.ylabel('Number')
    plt.title('COVID-19 Data (statewise)')
    plt.xticks(index, states, rotation = 90)
    plt.legend() 
    plt.savefig("saved_graphs/" + current_date + ".png")
    plt.show()


# Draw graph which shows the progression through each date
def spread_chart():
    data = list(reversed(data_lst))
    x_labels = []

    cnf_in_lst = []
    cnf_fn_lst = []
    cured_lst = []
    death_lst = []

    # Reg ex to extract date
    regex = re.compile(r"\d\d[-]\d\d[-]\d\d\d\d")
    for day in data:
        label = regex.search(day)
        df = pd.read_csv(day)
        x_labels.append(label.group())
        cnf_in = df['indian_confirmed'].tolist()         # Confirmed Indian cases 
        cnf_fn = df['foreign_confirmed'].tolist()      # Confirmed Foreigners
        cured = df['cured'].tolist()
        death = df['death'].tolist()
        del cured[-1], death[-1], cnf_fn[-1], cnf_in[-1]

        cnf_in_lst.append(sum(cnf_in))
        cnf_fn_lst.append(sum(cnf_fn))
        cured_lst.append(sum(cured))
        death_lst.append(sum(death))

    # Plotting categorically
    plt.figure(figsize=(7, 4))
    plt.plot(x_labels, cnf_in_lst, color='#05028f')
    plt.plot(x_labels, cnf_fn_lst, color='#6aafdb')
    plt.plot(x_labels, cured_lst, color='#00c20f')
    plt.plot(x_labels, death_lst, color='#ff3f0f')
    plt.legend()
    plt.savefig("saved_graphs/" + x_labels[-1] + "_progress" + ".png")      # Save Figure
    plt.show()

#bar_chart()
#spread_chart()


