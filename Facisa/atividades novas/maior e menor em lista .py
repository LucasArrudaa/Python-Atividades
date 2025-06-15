'''Crie um código que seja capaz de encontrar e exibir a maior e a menor palavra da lista (em número de caracteres).'''

palavras =['pyhthon', 'java', 'kotlin', 'javascript','cu'] #criando uma lista

def maiorEMenor(palavras): #criando uma funcao
    maior = palavras[0]
    menor = palavras[0]
    for palavra in palavras:  # para cada palavra na lista
        if len(palavra) > len(maior): # se a palavra for maior que a maior, ou seja  ele vai de uma em uma até encontrar a maior
            maior = palavra
        if len(palavra) < len(menor): # se a palavra for menor que a menor, ou seja ele vai de uma em uma até encontrar a menor
            menor = palavra
    return maior, menor #retorna a maior e a menor

maior, menor = maiorEMenor(palavras) #chamando a funcao
print(maior, menor)
