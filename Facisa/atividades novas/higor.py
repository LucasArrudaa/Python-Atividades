manifestacao = [] #lista de manifestações

while True: #laço de repetição infinito

    #Print da opções válidas
    print(' 1) Listagem de Manifestações;\n 2) Criar uma nova Manifestação;\n 3) Exibir quantidade de manifestações ;\n 4) Pesquisar uma manifestação por código;\n 5) Excluir uma manifestação pelo código;\n 6) Sair do Sistema.')

    opcao = int(input('Selecione uma opção válida: ')) #Variável que armazena a opção escolhida

    if opcao > 0 and opcao < 7: #condicional que limita os caracteres a serem utilizados

        if opcao == 1: #Listagem de Manifestações

            if len(manifestacao) > 0: # Verifica se a lista não está vazia
                print("\nListagem de Manifestações:\n")
                for item in manifestacao:
                    print("-", item) # Imprime cada item precedido por um traço, deixando mais bonitinho
                print('\n')
            else: # Se a lista estiver vazia, informa que não há nada disponível
                print("Não há manifestações disponíveis.")

        elif opcao == 2:#Cria uma nova Manifestação
            novaManifestacoes = str(input("\nAdicionar uma manifestação: "))
            if len(novaManifestacoes) == 0:
                print('\n Valor inválido')
            elif novaManifestacoes in manifestacao:  # condição que indentifica manifestações disponiveis e inpede que se repita
                print('\nEssa manifestação já existe!')

            else:
                manifestacao.append(
                    novaManifestacoes)  # condição que adiciona uma nova manifestação (append serve para adicionar um item na lista)
                print('\nA nova manifestação foi adicionada.\n')


        elif opcao == 3: #Exibir quantidade de manifestações
            quantidadedeManifestacoes = len(manifestacao)
            if quantidadedeManifestacoes >= 1:
                print('\nAtualmente temos', quantidadedeManifestacoes, 'manifestações!\n')
            elif quantidadedeManifestacoes <= 0:
                print('Atualmente não temos manifestações')

        elif opcao == 4:#Pesquisar uma manifestação por código
            codigo = int(input("\nDigite o código que deseja pesquisar: "))

            if codigo > 0 and codigo <= len(manifestacao):  # codigo que o usuario digitar tem que ser maior que zero e menor que a quantidade de filmes
                pesquisarCodigo = manifestacao[codigo - 1]  # se o usuario digitar "1", o codigo ira transformar em 0 para pegar o elemento "0" da lista.
                print(f'\n-{pesquisarCodigo}\n')
            else:
                print("\ncódigo inválido!\n")

        elif opcao == 5:#Excluir uma manifestação pelo código

            ##
            print("Listagem de Manifestações:\n")
            for pos in range(len(manifestacao)):
                print(str(pos+1),'- posição:', manifestacao[pos])
            if len(manifestacao) == 0:
                print('A lista está vázia\n')
            else:
                posicaoRemover = int(input("digite a manifestação a ser removida: \n"))
                if posicaoRemover < len(manifestacao) or posicaoRemover > len(manifestacao):
                    print('Comando invalido')
                else:
                    manifestacao.pop(posicaoRemover - 1)  # necessario colocar "-1" pois sempre temos que levar em consideração o que o cliente digita excluindo a posição 0.
                    print("\nmanifestação removida com sucesso")  # é importante realizar essa "limitação" para evitar erro quando o cliente desejar exluir algo .
                    # Excluir uma manisfestação pelo codigo

        elif opcao == 6:#sair do sistema
            print('\nFim do sitema!\n')
            break

    else:
        print('Digite uma opção válida!')