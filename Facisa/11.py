''' Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
• salários até R$ 280,00 (incluindo) : aumento de 20%
• salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
• salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
• salários de R$ 1500,00 em diante : aumento de 5%
• Após o aumento ser realizado, informe na tela:
• o salário antes do reajuste;
• o percentual de aumento aplicado;
• o valor do aumento;
• o novo salário, após o aumento.'''

salario = float(input('Digite seu salario: ')) # salario atual do cliente
if salario <= 280 and salario >= 0: # de 0 ate 280 desconto de 20%
    vintePorcento = salario * 0.20  # descobrindo quanto é 20% 
    salario = salario + vintePorcento  # aumentando o salario com os %
    print(f'Voce recebeu o aumento de 20%, no caso {round(vintePorcento)} seu novo salario é de {round(salario)}')
elif salario >= 281 and salario <= 700 : # de 281 ate 700 desconto de 15%  AND SIGNIFCA ' E '
    quinzePorcento = salario * 0.15 # descobrindo quanto é 15%
    salario = salario + quinzePorcento # aumentando o salario com os %
    print(f'Voce recebeu o aumento de 15%, no caso {round(quinzePorcento)} seu novo salario é de {round(salario)}')
elif salario >= 701 and salario <= 1500 :
    dezPorcento = salario + 0.10# descobrindo quanto é 10%
    salario = salario + dezPorcento # aumentando o salario com os %
    print(f'Voce recebeu o aumento de 10%, no caso {round(dezPorcento)} seu novo salario é de {round(salario)}')
else:
    cincoPorcento = salario * 0.05 # descobrindo quanto é 5%   ( DE 1 A 10 SE USA % ASSIM  ' 0.01  0.02  0.03)
    salario = cincoPorcento + salario # aumentando o salario com os %
    print(f'Voce recebeu o aumento de 5%, no caso {round(cincoPorcento)} seu novo salario é de {round(salario)}') 


