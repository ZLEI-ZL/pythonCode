import matplotlib.pyplot as plt
import numpy as np

plt.figure(1)

a = plt.subplot(1,1,1, projection = 'polar')

t = np.linspace(0,2*np.pi,6000)

a.plot(t,1+np.cos(t),'-',c='b')

plt.show()

