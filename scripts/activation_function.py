#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 18:13:30 2019

@author: linlin
"""
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
plt.rc('text', usetex=True)
import seaborn as sns
import numpy as np
sns.set()
def sigmoid(x):
    # sigmoid = lambda x: 1/(1+np.exp(-x))
    y = 1/(1+np.exp(-x))
    eq = r'$\sigma(z)=\frac{1}{1 + e^{-z}}$'
    return eq, y
def tanh(x):
#    tanh = lambda x: (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))
    y = (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))
    eq = r'$tanh(z) = \frac{e^z-e^{-z}}{e^z+e^{-z}}$'
    return eq, y
def log(x):
    y = lambda x: -np.log(x)
    eq = r'$-log(z)$'
    return eq, y


def plot_function(x, y, title, filename, ylim=[-0.1,1.1],):
    plt.figure()
    plt.plot(x, y)
    plt.ylim(ylim)
    plt.title(title)
#    plt.margins(0)
    plt.savefig(filename, bbox_inches = 'tight',pad_inches = 0, dpi=300)

x = np.linspace(-10, 10, 100)

eq_sigmoid, y_sigmoid = sigmoid(x)

plot_function(x,y_sigmoid, title=eq_sigmoid, filename="../figures/sigmoid.png")

eq_tanh, y_tanh = tanh(x)
ylim = [-1.1,1.1]
plot_function(x,y_tanh, title = eq_tanh, filename="../figures/tanh.png", ylim=ylim)
#x = np.linspace(0.01, 10, 100)
#y_log = log(x)
#eq2 = r'$-\log(x)$'
#plot_function(x,y_log, title = "- Logarithm", text=eq2, filename="../figures/log.jpg")
