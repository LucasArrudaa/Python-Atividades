numeros = [] # descartavel
resultado = 0

for n in range(2):  #gerar dois input
    valor = int(input('Digite um valor: '))
    numeros.append(valor)

while True:

    print ('\n 1 = somar \n 2 = multiplicar  \n 3 = maior  \n 4 = novos numeros  \n 5 = sair do programa \n ')
    resposta = int(input('DIGITE UMA OPÇÃO VALIDA: '))

    if resposta == 1: # somar numeros
        resultado = sum(numeros)
        print(f'Resposta = {resultado} ')
        break
    elif resposta == 2: # multiplicar numeros
        resultado = numeros[0] * numeros[1] # o primeiro numero da lista sempre sera contado como 0
        print(f'Resposta  = {resultado}')
        break
    elif resposta == 3: # maior numero
        resultado = max(numeros)
        print(f'Resposta  = {resultado}')
        break
    elif resposta == 4: #troca de numeros
        for n in range(2):
            valor = int(input('Digite um valor: '))
            numeros.append(valor)
            break
    elif resposta == 5:
        print('FIM')
        break
    else:
        print('OPÇÃO INVALIDA!\nDigite apenas entre 1 - 5')