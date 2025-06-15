for n in range(6): #gerar 6 repetição
    nascimento = int(input('seu ano de nascimento :')) # o input vai ser gerado 6x
    idade = 2024 - nascimento # para saber a idade da pessoa
    if idade >= 18: #se for maior ou igual a 18
        print(f'Você nasceu em {nascimento}, voce tem {idade} de idade, vc é de maior')
    else: #se for menor
     print(f'{nascimento} sua idade é de {idade}, vc é de menor de idade')




