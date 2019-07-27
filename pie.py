# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 19:29:45 2019

@author: HP-PC
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
 
# Data to plot
dataset=pd.read_csv('diseases_details.csv')
print(dataset)
date='19-03-2019'
datee=dataset.columns
for i in range (0,len(datee)):
    if(datee[i]==date):
        index=i
        break;
print(index)        
labels = dataset.iloc[:,0]
print(labels)
sizes = dataset.iloc[:,index]
print(sizes)
 
# Plot
plt.pie(sizes,labels=labels,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()