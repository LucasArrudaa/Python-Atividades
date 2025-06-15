#ALISTAMENTO MILITAR
nascimento = int(input('Digite o ano do seu nascimento: '))
idade = 2024 - nascimento
print(f'sua idade é de {idade} anos.')
#INFORMAÇÃO DE ACORDO COM SUA IDADE
if idade == 18:
    print('está na hora de se alistar!')
elif idade < 18:
    tempo = 18 - idade
    print(f'Voce não tem idade para se alistar, falta {tempo} anos para você se alistar')
else:
    tempo = idade - 18
    print(f'Voce não tem idade para se alistar, você ta atrasado em {tempo} anos')


