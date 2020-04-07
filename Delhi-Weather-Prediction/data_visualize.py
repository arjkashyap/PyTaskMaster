#!/usr/bin/python3.6
"""
Data Visualization module.
Plot Data based on Temprature max, humidity,
"""


import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd


def format_date(date):
    y = date[0:4]
    m = date[4:6]
    d = date[6:8]
    return "{}/{}/{}".format(d, m, y)


def plotData():
    data = './data.csv'
    df = pd.read_csv(data)
    y_val = np.array(df[' _tempm'])

    dates = np.array(df['datetime_utc'])
    x_val = [ format_date(d) for d  in dates ]

    n = len(x_val)
    start_index = n % 100000
    print(start_index)
    print(n)
    tmp = {}
    for i in range(start_index, n):
        #print(x_val[i], y_val[i])
        tmp[y_val[i]] = x_val[i]

    # Plotting data
    plt.figure(figsize = (12, 7))
    plt.plot(x_val, y_val, color = '#ff3f0f')
    plt.xticks(rotation='vertical')
    plt.show()


plotData()

