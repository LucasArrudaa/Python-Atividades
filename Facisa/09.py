#9 Faça um Programa que leia dois números inteiros e mostre o maior deles
lista = [] 
numero1 = float(input('Digite um numero :'))
lista.append(numero1) #nome que vc deu a lista depois append para adicionar depois a variavel q vc quer adicionar
numero2 = float(input('Digite outro numero :'))
lista.append(numero2)
print (f'O maior deles é {max(lista)}') #maxlista é para mostrar o maior