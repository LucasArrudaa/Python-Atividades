pesos = [] #DESCARTAVEL
for i in range(1,7): # COMEÇAR COM 1 E TERMINAR COM 6
                     #achei interessante usar a variante i dentro do input
                     #para se referir a numeração da pessoa informada
                     #ex 1 pessoa, 2 pessoa
    peso = float(input(f"Digite o peso da {i}ª pessoa (em kg): "))
    pesos.append(peso) # 'append é uma lista vazia, que vai receber a resposta do input na DESCARTAVEL POREM
    #colocar descartavel + .append( )                          # tem que criar uma descartavel la em cima para SER A LISTA
    #dentro do parentes, a variavel q vai entrar

maior_peso = max(pesos)
menor_peso = min(pesos)
print(f'{maior_peso} Kg maior \n{menor_peso} Kg menor ')


