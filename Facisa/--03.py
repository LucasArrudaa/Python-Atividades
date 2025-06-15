while True:
  
  nome = input('Digite o seu nome: ')
  if len(nome) <= 4:
    print('Seu nome é curto,tente novamente')
  else:
    print('Nome aceito!')

  idade = int(input('Digite a sua idade: '))
  if idade >= 0 and idade <= 150:
    print('idade aceita')
  else:
    print('idade inválida, tente novamente')
  
  salario = float(input('Digite seu salario: '))
  if salario >0:
    print('Salario aceito')
  else:
    print('Salario invalido, tente novamente')

  sexo = str(input('Digite seu sexo (M/F): ')) .upper
  if sexo == 'M' or sexo == 'F':
    print('Sexo aceito')
  else:
    print('Opção invalida, tente novamente')
    
  estadoCivil = str(input('Digite seu estado civil (S/C/V/D): ')) .upper
  if estadoCivil == 'S' or estadoCivil == 'C' or estadoCivil == 'V' or estadoCivil == 'D':
    print('Estado civil aceito')
  else:
    print('Opção invalida, tente novamente')



