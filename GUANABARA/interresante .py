idades = []
homens = []
mulheres = []

while True:
    print('----------------------------------------------------')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo [M/F]: ').strip().upper()[0]
    if idade >= 18:
        idades.append(idade)

    while sexo not in 'MF':  # Validação para garantir que o sexo seja M ou F
        print("Opção inválida. Digite 'M' para masculino ou 'F' para feminino.")
        sexo = input('Digite seu sexo [M/F]: ').strip().upper()[0]

    if sexo == 'M':
        homens.append(sexo)
    elif sexo == 'F':
        mulheres.append(sexo)

    continuar = input('Quer continuar? [S/N]: ').strip().upper()[0]

    while continuar not in 'SN': # se o input continuar nao receber s ou n ( pode esvcrever junto)

        print("Opção inválida. Digite 'S' para sim ou 'N' para não.")
        continuar = input('Quer continuar? [S/N]: ').strip().upper()[0]

    if continuar == 'N':
        break
print('----------------------------------------------------')
print(f'idades maiores de 18 anos:{idades}')
print(f'Homens registrados: {len(homens)}')
print(f'Mulheres registradas: {len(mulheres)}')

