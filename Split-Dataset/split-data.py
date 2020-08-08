#!/usr/bin/env python
# coding: utf-8
"""
A Helper program to automate the process of splitting the dataset 
into train, test and validation data.
To use this, enter the name of the label classes in the classes list
Make sure these label classes match the name of the subdirs in the 
dataset root folder.
"""


import numpy as np
import os
import shutil
import random
import glob




classes = []




PATH = 'data'


def count_data():
    t = 0
    for c in classes:
        path = os.path.join(PATH, c)
        n = len(os.listdir(path))
        t += n
        print(c, n)
        data_cout[c] = n
    return t, data_cout


def split_data():
    # Creating dirs
    train_path = os.path.join(PATH, 'train')         
    valid_path = os.path.join(PATH, 'valid')
    test_path = os.path.join(PATH, 'test')
    if (os.path.isdir(train_path)) or (os.path.isdir(valid_path)) or (os.path.isdir(test_path)):
        raise Exception("Something Went wrong !! Make sure the data is not already split and the data folder contains only the label classes image folders")
    else:   
        p_age = [0.7, 0.2, 0.1]
        os.makedirs(train_path)          # Create train, valid, test dir 
        os.makedirs(valid_path)
        os.makedirs(test_path)
        for c in classes:
            path = os.path.join(PATH, c)
            c_train = os.path.join(train_path, c)
            c_valid = os.path.join(valid_path, c)
            c_test = os.path.join(test_path, c)
            os.makedirs(c_train)       # Create Image dirs for each label class
            os.makedirs(c_valid)
            os.makedirs(c_test)
            train_count = int(data_cout[c] * 0.7)    # Number of images to take move
            valid_count = int(data_cout[c] * 0.2)
            test_count = int(data_cout[c] * 0.1)
            print(train_count, valid_count, test_count)

            # Move files
            for img in random.sample(glob.glob(os.path.join(path, '*')), train_count):
                shutil.move(img, c_train)
            for img in random.sample(glob.glob(os.path.join(path, '*')), valid_count):
                shutil.move(img, c_valid)
            for img in random.sample(glob.glob(os.path.join(path, '*')), test_count):
                shutil.move(img, c_test)
            shutil.rmtree(path)         # Remove the old dir
           
    

if __name__ == '__main__':
        
    data_cout = {}            # Dictonary stores the number of images of each class
    total, data_cout = count_data()
    split_data()



