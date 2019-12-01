import os
import matplotlib.pylab as plt
import numpy as np

data= np.loadtxt("Logistic.dat")
X = data[:,0]
Y = data[:,1]

plt.figure(figsize=(12,10)),
plt.scatter(X,Y,s=4,c='gold')
plt.xlabel('Fuerza (N)')
plt.ylabel('$\\Theta$')
plt.title('Mapa Logistico')
plt.grid()
plt.savefig("Logistic.png")