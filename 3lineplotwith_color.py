import numpy as np 
from matplotlib import pyplot as plt

t = np.arange(0., 5., 0.2)  #this is for making array 
# 0. is begining 
# 5. is end value
# 0.2 is increment value

plt.plot(t,t, 'ro',t,t**2,'bs',t,t**3,'g^')
plt.show()
