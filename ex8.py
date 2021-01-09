#Exemplo de como fazer um gráfico em barras usando a matplolib  (grupos de barras)
#Os dados foram extraídos de votações feitas no twitter 

import matplotlib.pyplot as plt 
import numpy as np
plt.style.use('dark_background')

#acertos = [questão 1, questão 2, questão 3]
acertos =[52, 2, 47]
erros = [38, 65, 17]

#Definindo o tamanho de cada barra
tamanho = 0.25
#plt.figure(figsize = (10,5))

#Posições das barras 
#colocamos uma barra ao lado da outra de forma incremental pela referencia da largura da anterior
b1 = np.arange(len(acertos))
b2 = [x + tamanho for x in b1]

#Obs: não esquecer  de colocar o tamanho 
plt.bar(b1, acertos, width=tamanho, label='acertos')
plt.bar(b2, erros, width=tamanho, label='erros')

#Titulo do gráfico 
plt.title("ENEM")  
#Definindo os títulos dos eixos x-> opções e y-> número de pessoas que votaram na opção
plt.xlabel("Questões")
plt.ylabel("Número de acertos ou erros")
#preciso mudar a legenda manualmente
#plt.xticks([ r + tamanho for r in range(len(acertos))], ['Questão 1', 'Questão 2', 'Questão 3'])

#para aparecer o label
plt.legend()
plt.show()
