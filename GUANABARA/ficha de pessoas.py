nomes = []
idades = []       #descartaveis
sexos = []
for i in range(1,5): #LEMBRA DE MUDAR PARA 1,5
    print(f'------------- {i} pessoa --------------- ')
    nome = str(input(f'Qual o seu nome? ')) .strip() # .strip() fica tudo sem espaço, junto
    nomes.append(nome)
    idade = int(input(f'Qual a sua idade? ')) 
    idades.append(idade)
    sexo = str(input(f'Qual o seu sexo (f / m ) ? ')) .strip()
    sexos.append(sexo)
print (f'As pessoas na lista são {nomes}') 
print(f'As idades são : {idades}')
print(f'os sexos são : {sexos}')












