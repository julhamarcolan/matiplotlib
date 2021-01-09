import matplotlib.pyplot as plt
plt.style.use('dark_background')

plt.title('Exemplos de uso da Matiplotlib: Função de primeiro grau')
#plt.plot(x,y)
#plt.plot([1,2,3,4], [2,4,6,8])
# f = 2x
plt.xlabel('x')
plt.ylabel('2x')
#plt.show()

#Colocando um grid 
plt.grid(True)
#plt.show()

#Mudando a cor
#plt.plot([1,2,3,4],  [2,4,6,8], color='red')
#plt.show()

#Mudando  a forma 
#plt.scatter([1,2,3,4],  [2,4,6,8], color='red')
#plt.show()

#Duas formas juntas
plt.plot([1,2,3,4],  [2,4,6,8])
plt.scatter([1,2,3,4],  [2,4,6,8])
plt.show()