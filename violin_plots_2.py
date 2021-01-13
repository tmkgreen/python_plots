#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 09:48:59 2020

@author: tmkgreen
"""


# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# =============================================================================
# import seaborn.categorical
# seaborn.categorical._Old_Violin = seaborn.categorical._ViolinPlotter
# 
# class _My_ViolinPlotter(seaborn.categorical._Old_Violin):
# 
#     def __init__(self, *args, **kwargs):
#         super(_My_ViolinPlotter, self).__init__(*args, **kwargs)
#         self.gray='black'
# 
# seaborn.categorical._ViolinPlotter = _My_ViolinPlotter
# =============================================================================

import seaborn as sns
import numpy as np
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

from pylab import savefig
from matplotlib import rcParams
rcParams['font.family'] = 'Times New Roman'
import matplotlib.pyplot as plt

#MX 

excel_file = '/Users/tmkgreen/Documents/ORNL/Summer 2019/Grade 91 Ppt Counting/Manuscript/Python Plots G91 Paper/Violin Plots/d_eq values.xlsx'
df = pd.read_excel(excel_file,sheet_name='MX USE',usecols=[0,1,2])

##Scale the violin width by the number of observations in each bin
a4_dims = (6, 4)
fig, ax = plt.subplots(figsize=a4_dims)
my_pal = {"Build 99/1": "cyan", "Build 95/5": "darkorange"}
g = sns.violinplot(g=ax,x="TYPE", y="D_EQ", hue="BUILD",data=df,linewidth=1, bw='scott',cut=0,palette=my_pal, split=True,scale="count", inner="quartile")

#sns.set_style({"font.family": ["Times New Roman"]})
g.set(ylabel='MX Precipitate Diameter (nm)',xlabel=None)
plt.legend(bbox_to_anchor=(0.5, 1.1), loc='upper center',ncol=2,frameon=False)

l = g.lines[0]
l.set_linestyle('--')
l.set_color('k')
l.set_linewidth(1)

l = g.lines[1]
l.set_linestyle('-')
l.set_color('k')
l.set_linewidth(1.5)

l = g.lines[2]
l.set_linestyle('--')
l.set_color('k')
l.set_linewidth(1)

l = g.lines[3]
l.set_linestyle('--')
l.set_color('k')
l.set_linewidth(1)

l = g.lines[4]
l.set_linestyle('-')
l.set_color('k')
l.set_linewidth(1.5)

l = g.lines[5]
l.set_linestyle('--')
l.set_color('k')
l.set_linewidth(1)

l = g.lines[6]
l.set_linestyle('--')
l.set_color('k')
l.set_linewidth(1)

l = g.lines[7]
l.set_linestyle('-')
l.set_color('k')
l.set_linewidth(1.5)

l = g.lines[8]
l.set_linestyle('--')
l.set_color('k')
l.set_linewidth(1)

l = g.lines[9]
l.set_linestyle('--')
l.set_color('k')
l.set_linewidth(1)

l = g.lines[10]
l.set_linestyle('-')
l.set_color('k')
l.set_linewidth(1.5)

l = g.lines[11]
l.set_linestyle('--')
l.set_color('k')
l.set_linewidth(1)

l = g.lines[12]
l.set_linestyle('--')
l.set_color('k')
l.set_linewidth(1)

l = g.lines[13]
l.set_linestyle('-')
l.set_color('k')
l.set_linewidth(1.5)

l = g.lines[14]
l.set_linestyle('--')
l.set_color('k')
l.set_linewidth(1)

l = g.lines[15]
l.set_linestyle('--')
l.set_color('k')
l.set_linewidth(1)

l = g.lines[16]
l.set_linestyle('-')
l.set_color('k')
l.set_linewidth(1.5)

l = g.lines[17]
l.set_linestyle('--')
l.set_color('k')
l.set_linewidth(1)

g.set_ylim(0,75)
y= [0,10,20,30,40,50,60,70]
g.set_yticks(y)
sns.set_style("whitegrid")

plt.savefig('violin plots.png', format='png', dpi=1200)

