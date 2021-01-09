#Exemplo de como fazer um gráfico em barras (barras na horizontal) usando a matplolib 
#Os dados foram extraídos de votações feitas no twitter 

import matplotlib.pyplot as plt 
import numpy as np
#plt.style.use('dark_background')

resposta = [ 'a', 'b', 'c', 'd', 'e']
pessoas = [4, 38, 20,2,3]

#Titulo do gráfico 
plt.title("ENEM")  

#Definindo os títulos dos eixos x-> opções e y-> número de pessoas que votaram na opção
plt.xlabel("Número de pessoas que votaram")
plt.ylabel("Opções")

plt.barh(resposta, pessoas, color ="red")
#plt.barh(resposta, pessoas)
plt.show()

