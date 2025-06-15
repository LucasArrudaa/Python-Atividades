tabela = ' Botafogo', ' Palmeiras', ' Flamengo', ' Inter',' Fortaleza', 'São paulo', 'Corinthians',' Bahia', ' cruzeiro', 'vasco', 'vitoria', ' gremio', ' juventude', ' atletico mineiro', ' fluminense', ' atletico pararaense' ,' braga', 'crisciuma','atletico go', ' cuiaba'
print (f'{tabela}')
 # TUPLA da tabela do brasileiro 2024 em dezembro

while True:
    print ('\n 1 = os cinco primeiro \n 2 = os quatro ultimos \n 3 = ordem alfabetica   \n 4 = posição do Corinthians \n 5 = sair ')
                       # menu de opções

    resposta = int(input('DIGITE UMA OPÇÃO VALIDA: '))

    if resposta == 1: # 5 primeiros
        for cont in range (0,5):
            print(f'Ná posição {cont+1}:{tabela[cont]}')

    elif resposta == 2: # 4 ultimos
        for cont in range (0 , 4):
            print(f'Os 4 ultimos são: {tabela[cont - 4]}')

    elif resposta == 3: # alfabetico
        print(f'Na ordem alfabetica : {sorted(tabela)}')

    elif resposta == 4: #Corinthinas na tabela
        if cont in range (4):
            print(f'O Corinthinas está na 7 posição da tabela ')

    elif resposta == 5:
        print('Fim do programa')
        break
    elif resposta >5:
        print('Digite apenas entre 1 - 5')
        print ('\n 1 = os cinco primeiro \n 2 = os quatro ultimos \n 3 = ordem alfabetica   \n 4 = posição do Corinthians \n 5 = sair ')
                       
        resposta = int(input('DIGITE UMA OPÇÃO VALIDA: '))






    
        


