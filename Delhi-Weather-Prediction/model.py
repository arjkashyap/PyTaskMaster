#!/usr/bin/python3.6

"""
Predicting Delhi Weather using Linear Regression.
"""

import pandas as pd
import csv 
import math
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import svm

data = "./data.csv"

# Read csv file data
df = pd.read_csv(data)
#print(df.head())

# Data Filter

# _conds: conditions (haze/smoke)
# _dewptm: dewpoint temperature
# _hum: humidity
# _tempm: temperature max
df = df[[ 'datetime_utc' ,' _dewptm', ' _hum', ' _tempm']]

# Remove nan values
df.fillna(-99999, inplace=True)

total = len(df)


# Removing dates
"""
Date Time format: 
    YYYY/mm/dd-Time
"""
dates = df['datetime_utc']
df.drop('datetime_utc', axis=1, inplace=True)


# Extracting year, month, and date
y = dates.map( lambda y : y[0:4] )      # Year
m = dates.map( lambda m : m[4: 6] )     # Month
d = dates.map( lambda day: day[6: 8] )     # Date

#df.insert(0, 'year', y)
#df.insert(0, 'month', m)
#df.insert(0, 'day', d)

print("Data Frame")
print(df)

# Features
X = np.array(df.drop(' _tempm', axis=1))
print("Features")
print(X)

# Labels
y = np.array(df[' _tempm'])
print("Labels: ")
print(y)


# Splitting Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

# Classifier
clf = LinearRegression()

# Training
clf.fit(X_train, y_train)

# Training
confidence = clf.score(X_test, y_test)

print("Accuracy: " + str(confidence))


# Testing other kernels
"""
for k in ['poly', 'rbf', 'sigmoid']:
    print('current kernel: ', k)
    clf = svm.SVR(kernel=k)
    clf.fit(X_train, y_train)
    confidence = clf.score(X_test, y_test)
    print(k, confidence)
"""


