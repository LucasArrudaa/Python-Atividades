lista = []
soma = 0
while True:
    print('Digite ( -1) para cancelar o programa')
    numeros = int(input('Digete um numero: '))
    if numeros != -1:  # ate ele n encerrar o programas, vamos ta fazendo os calculos dentro do if
        soma += numeros
        lista.append(numeros)
        media = soma / len(lista)
    else:  # a partir do momento que ele encerra o programa, ele mostra tudo que pede
        numeros == -1
        print(
            f'O numero maior foi {max(lista)} e o menor foi {min(lista)}\n a media é de {media} ')
        break 
