#6 Realiza a leitura de 1 float referente ao salário do cidadão e apresenta o salário com reajuste de 10% da inflação.
# ou seja, 10% em cima do salario dele

salario = float(input('Digite um numero :'))
inflação = salario * 0.10
salario_novo = salario + inflação 
print(f'a inflação aumentou em {inflação} o salario, portando ficou de {salario_novo} seu salario')