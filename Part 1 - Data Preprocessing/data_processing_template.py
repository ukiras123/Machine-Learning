#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Importing the libraries
import numpy as np  # Math
import matplotlib.pyplot as plt
import pandas as pd # import and manage data set

 
# importting the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

# Taking care of missing data
from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values = 'NaN', strategy="mean", axis=0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])