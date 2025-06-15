numeros = []
resultado = 0              # variante descartavel
maior = 0
numero1= int(input('Digite um valor: '))
numero2= int(input('Digite um valor: '))

while True:
    print ('\n 1 = somar \n 2 = multiplicar  \n 3 = maior  \n 4 = novos numeros  \n 5 = sair do programa \n ') # painel 

    resposta = int(input('DIGITE UMA OPÇÃO VALIDA: ')) #respota

    if resposta == 1: # somar numeros
        resultado = numero1 + numero2
        print(f'\n Resposta = {resultado} ')

    elif resposta == 2: # multiplicar numeros
        resultado = numero1 * numero2
        print(f'\n Resposta  = {resultado}')

    elif resposta == 3: # maior numero
        if numero1 >= numero2: #caso n1 seja maior
            maior = numero1
        else: #caso seja o n2 o maior
            maior = numero2
        print(f'\n O maior valor digitado foi {maior}')
        
    elif resposta == 4: # troca de numeros
        numero1 = int(input('Digite um valor: '))
        numero2 = int(input('Digite um valor: '))
    elif resposta == 5: #encerrar programa
        print('Fim do programa')
        break












