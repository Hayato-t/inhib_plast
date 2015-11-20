import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("plot.dat")
x=data[:,0]
y=data[:,1]
counter=np.zeros(25)

for i in range(0,len(x)):
    for j in range(0,5):
        if x[i]>=30500+600*j and x[i]<31100+600*j:
            for k in range(0,5):
                if y[i]>=(512+k*64) and y[i]<(576+k*64):
                    counter[k+5*j] = counter[k+5*j] + 1
                elif y[i]>=(832+k*16) and y[i]<(848+k*16):
                    counter[k+5*j] = counter[k+5*j] + 1



for i in range(0,25):
    print counter[i]

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
