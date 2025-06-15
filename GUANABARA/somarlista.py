lista =[]
soma = 0
while True:
    numero = int(input('Digite um numero :'))
    lista.append(numero) # add numeros em lista
    if numero == 999:
        soma = sum(lista) - 999 # somar lista
        lista.remove(999) # remover intem de lista
        print(f'Acabou, os numeros digitados foram : {lista} \na soma de todos os numeros digitados foi de {soma}')
        break






