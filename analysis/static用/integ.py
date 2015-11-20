#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

X = [1,2,3,4,5]
Y = [659.8,301.8,77.1,148.9,183.5]
e = [146.41,52.36,36.69,69.93,68.48]
#Y = [190.6,756.4,130.9,174.8,357.7]
#e = [66.47,71.13,43.11,69.10,65.78]
#Y = [25.1,74.3,630,88.2,132.8]
#e = [18.54,16.32,71.88,31.71,60.59]
#Y = [165.6,241.3,141.9,686.9,216.6]
#e = [80.18,41.03,56.70,83.08,67.35]
#Y = [103,257.9,115,131.6,821.8]
#e = [74.51,58.01,33.30,55.90,98.24]

plt.errorbar(X,Y,e,fmt='bo',color='k')
plt.bar(X,Y,align="center")

plt.xticks(X, ['ka','ki','ku','ke','ko']) # 目盛りを数字から地名に書き換える
plt.xlabel('pools for response')
plt.ylabel('the number of fired cells')
plt.savefig('out1_1.eps')
plt.show()
