import numpy as np 
import matplotlib.pyplot as plt
plt.style.use('dark_background')


forma = np.loadtxt('exemplo.txt')
plt.plot(forma)
plt.savefig('teste.png', format='png')
plt.show()
