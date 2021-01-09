import matplotlib.pyplot as plt 
import numpy as np

plt.style.use('dark_background')

x1 = np.arange(0.0, 2.0, 0.01)
y1  = np.sin(2*np.pi*x1)

x2 = [1,2,3,4]
y2 = [2,4,6,8]

fig = plt.figure()

plt.subplot(2, 2, 1)
plt.plot(x1, y1)

plt.subplot(2, 2, 2)
plt.plot(x1, y1, color ='red')

plt.subplot(2, 2, 3)
plt.plot(x2, y2)

plt.subplot(2, 2, 4)
plt.plot(x2, y2, color='red')


plt.show()