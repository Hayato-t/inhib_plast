import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("plot.dat")
x=data[:,0]
y=data[:,1]
counter1_0=0
counter1_1=0
counter2_0=0
counter2_1=0

for i in range(0,len(x)-1):
    if x[i]>=80500 and x[i]<82500:
        if y[i]>=912 and y[i]<932:
            counter1_0 = counter1_0 + 1
        elif y[i]>=932 and y[i]<952:
            counter2_0 = counter2_0 + 1

    elif x[i]>=82500 and x[i]<84500:
        if y[i]>=912 and y[i]<932:
            counter1_1 = counter1_1 + 1
        elif y[i]>=932 and y[i]<952:
            counter2_1 = counter2_1 + 1


print counter1_0
print counter1_1
print counter2_0
print counter2_1
#plt.xlim(30500,33500)
#plt.xlim(0,33500)
plt.xlim(80500,84500)
plt.ylim(912,931)
#plt.ylim(512,831)
#plt.ylim(832,911)
#plt.axhline(y=575,color='red')
#plt.axhline(y=639,color='red')
#plt.axhline(y=703,color='red')
#plt.axhline(y=767,color='red')

#plt.axhline(y=848,color='red')
#plt.axhline(y=864,color='red')
#plt.axhline(y=880,color='red')
#plt.axhline(y=896,color='red')

#plt.axvline(x=31100,color='red')
#plt.axvline(x=31700,color='red')
#plt.axvline(x=32300,color='red')
#plt.axvline(x=32900,color='red')

#plt.xlabel('time [ms]')
#plt.ylabel('cell number')
#plt.plot(x,y,'.')
#plt.savefig('raster.eps')
#plt.show()
