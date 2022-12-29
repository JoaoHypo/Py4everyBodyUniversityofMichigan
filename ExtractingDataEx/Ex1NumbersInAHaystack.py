"""
Finding Numbers in a Haystack

In this assignment you will read through and parse a file with text and numbers. 
You will extract all the numbers in the file and compute the sum of the numbers.

"""
import re

filename = input("Digite o nome do arquivo: ") # Pede o nome do arquivo

handle = open(filename) # Cria um 'link' entre o arquivo e o programa

soma = [0] # Inicia a soma dos valores encontrados no arquivo

for line in handle: # Loop para iterar entre as linhas do texto

    findall = re.findall('[0-9]+',line) # Porcura por todo e qualquer numero sem espaço na linha e adiciona a uma lista

    # print(findall) Print para ver o que cada linha encontrou de numero (teste)

    for i in findall: # Loop par atualizar a soma

        soma = [soma[0] + int(findall[findall.index(i)])] # Atualiza á soma com os termos da lista Findall ja somados

    # print(soma) Print teste para acompanhar a Soma

print(soma[0]) # Resultado final 😁
