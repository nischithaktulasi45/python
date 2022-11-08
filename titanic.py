# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 11:22:02 2022

@author: SPTINT-13
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv('C:/Users/SPTINT-13/chirag/tested.csv')
print(data.shape)
print(data.info())
print(data.isnull().sum())
print(len(data))
print(data.head(10))
print(data['Survived'].value_counts().plot(kind='bar'))
plt.scatter(data['Fare'],data['Pclass'])
print(data[data['Sex']=='female']['Survived'].value_counts().plot(kind='bar'))
print(data[data['Pclass']==3]['Survived'].value_counts().plot(kind='bar'))
print(data[data['Sex']=='female']['Survived'].value_counts().plot(kind='pie'))


import seaborn as sns
plt.scatter(x=data['Age'],y=data['Fare'])
plt.hist(data['Fare'])
sns.barplot(x='Pclass',y='Survived',data=data)
