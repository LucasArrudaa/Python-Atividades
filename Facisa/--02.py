'''• Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagemde
erro e voltando a pedir as informações.'''
while True:
  usuario = input('Digite o seu nome para o usuario: ')
  senha = input('Digite a sua senha: ')
  if senha == usuario:
    print('não podemos aceitar essa senha, tente novamente')
  else:
    print('senha aceita')
    break