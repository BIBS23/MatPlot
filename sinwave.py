import math
import matplotlib.pyplot as plt 
import numpy as np

x = np.arange(0,math.pi*6,0.05)
a = np.sin(x)
y = np.cos(x)
z = -np.cos(x)
plt.plot(x,a)
plt.plot(x,y)
plt.plot(x,z)
plt.grid()


plt.show()
