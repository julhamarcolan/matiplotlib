#Exemplo de como fazer um gráfico em barras usando a matplolib 
#Os dados foram extraídos de votações feitas no twitter 

import matplotlib.pyplot as plt 
import numpy as np
#plt.style.use('dark_background')

resposta = [ 'a', 'b', 'c', 'd', 'e']
pessoas = [18, 1, 7, 12, 52]

#Titulo do gráfico 
plt.title("ENEM")  

#Definindo os títulos dos eixos x-> opções e y-> número de pessoas que votaram na opção
plt.ylabel("Número de pessoas que votaram")
plt.xlabel("Opções")

plt.bar(resposta, pessoas, color ="red")
#plt.bar(resposta, pessoas)
plt.show()

