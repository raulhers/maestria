import matplotlib.pyplot as plt 
import numpy as np 
x = np.arange(8)
plt.plot(x,[xi**2 for xi in x])
print(plt.axis())
plt.axis([1,8,-3,8])
plt.axis(ymin=4,ymax=10)
plt.show()
