#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

X = [1,2]
#Y = [659.8,301.8,77.1,148.9,183.5]
#e = [146.41,52.36,36.69,69.93,68.48]
#Y = [190.6,756.4,130.9,174.8,357.7]
#e = [66.47,71.13,43.11,69.10,65.78]

#Y = [0.521,0.4790]
#e = [0.013,0.013]

#Y = [0.4953,0.505]
#e = [0.024,0.024]

Y =  [0.479, 0.505]
e = [0.013,0.024]

#Y = [165.6,241.3,141.9,686.9,216.6]
#e = [80.18,41.03,56.70,83.08,67.35]
#Y = [103,257.9,115,131.6,821.8]
#e = [74.51,58.01,33.30,55.90,98.24]

plt.errorbar(X,Y,e,fmt='bo')
plt.bar(X,Y,align="center")

plt.ylim(0.4,0.6)
#plt.xticks(X, ['Left to Right','Right to Left']) # 目盛りを数字から地名に書き換える
plt.xticks(X,['section for LR', 'section for RL'])
plt.xlabel('stimulus')
plt.ylabel('the ratio of fired cells')
#plt.axhline(y=0.5,color='red')

#plt.axvline(x=31100,color='red')

plt.savefig('out2_sub.eps')
plt.show()
