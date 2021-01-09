import matplotlib.pyplot as plt 
import numpy as np

#plt.xkcd()
plt.style.use('dark_background')

x1 = [2,3,6,8]
y1  = [1,2,3,4]

x2 = [1,2,3,4]
y2 = [2,4,6,8]

plt.plot(x1, y1, label="x1,y1")
plt.plot(x2, y2, label="x2,y2")
plt.legend()

plt.show()