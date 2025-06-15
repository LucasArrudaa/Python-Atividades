lista =[]
soma = 0
while True:
    numero = int(input('Digite um numero :'))
    lista.append(numero) # add numeros em lista
    if numero == 999:
        soma = sum(lista) - 999 # somar lista - 99 pq quando ele colocar 999 esse numero entra na lista tmb
        lista.remove(999) # remover intem de lista, pq quando ele colocar 999 esse numero entra na lista tmb
        print(f'Acabou, os numeros digitados foram : {lista} \na soma de todos os numeros digitados foi de {soma}')
        break
