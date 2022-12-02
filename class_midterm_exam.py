# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 13:07:46 2022

@author: Jacob
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

#exam 1
lstt=[]
for a in range(1, 11):
    lstt.append(a**2)
print('The square of 1 to 10 are {}'.format(lstt))
    
#exam 2
def n_smallest(n, lst):
    print('原本的list為{}'.format(lst))
    print('前 {} 小的數字是 '.format(n) + str(sorted(lst)[0:5]))
    
a = [12, 3, 5 ,6, 1, 2, 45]
n_smallest(5, a)

#exam 3
dataset_fcu = pd.read_csv('C:\\users\\Jacob Kai\\Documents\\Python_UniClass\\Week 4\\FCU.csv')
new_col = {'學年度' : 'year',
          '在學學生數小計' : 'total'}
dataset_fcu = dataset_fcu.rename(columns=new_col)

plt.figure(figsize=(12, 6))
plt.axes().set_facecolor('gray')
x=[106, 107, 108, 109, 110]
y = dataset_fcu.groupby('year')['total'].sum().diff().reset_index()
plt.title('FCU Number of Students Change', fontsize=20)
plt.xlabel('Year', fontsize=15, color='brown')
plt.ylabel('Change', fontsize=15, color='brown')
plt.plot(y['year'], y['total'], color='orange')
plt.show()

#exam 4
dataset_ins = pd.read_csv('C:\\users\\Jacob Kai\\Documents\Python_UniClass\\Week 4\\insurance.csv')
dataset_ins1 = dataset_ins.dropna()
dataset_ins2 = dataset_ins1.drop_duplicates()
dataset_ins_final = dataset_ins2.groupby('sex')['expenses'].mean().reset_index()

a = dataset_ins_final['sex'].values
b = dataset_ins_final['expenses'].values

plt.figure(figsize=(8, 6))
plt.title('Comparison of Average Expense of Different Gender')
plt.xlabel('sex')
plt.ylabel('Average Expese')
plt.bar(a, b, width=0.3, color='purple', align='center')
plt.show()

#exam 5
dataset_onl = pd.read_csv('C:\\Users\\Jacob Kai\\Documents\\Python_UniClass\\Week 4\\Online Retail.csv')

dataset_onl = dataset_onl.dropna()

dataset_onl = dataset_onl.drop_duplicates()

dataset_onl = dataset_onl[dataset_onl['Quantity']>0]

dataset_onl['Revenue'] =  dataset_onl['UnitPrice'] * dataset_onl['Quantity']

dataset_onl['InvoiceDate'] = pd.to_datetime(dataset_onl['InvoiceDate'])
dataset_onl['InvoiceYearMonth'] = dataset_onl['InvoiceDate'].dt.strftime('%Y/%m')

onl_month_change = dataset_onl.groupby('InvoiceYearMonth')['Revenue'].sum().diff().reset_index()
plt.figure(figsize=(12, 6))

x = onl_month_change['InvoiceYearMonth']
y = onl_month_change['Revenue']

lst_color = []
for i in y:
    if i >= 0:
        lst_color.append('green')
    else:
        lst_color.append('red')

plt.title('Monthly Change in Revenue')
plt.xlabel('Month')
plt.ylabel('Change')
plt.xticks(rotation=45)

plt.bar(x, y, width=0.8, color=lst_color)

lstY_val = onl_month_change['Revenue'].values.tolist()
for h, v in enumerate(lstY_val):
    plt.text(h, v + 100, '{:,.2f}'.format(v), color='black', horizontalalignment='center')
    
y_tick=[]
y_seg_size = (y.max() - y.min()) / 5
for k in range(6):
    y_tick.append('{0:,.0f}'.format(y.min() + y_seg_size*(k)))
plt.yticks(np.arange(y.min(), y.max() + y_seg_size, step=y_seg_size), y_tick, size=10, color='brown')
    
plt.show()