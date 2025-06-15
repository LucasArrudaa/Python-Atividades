'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu
salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um
programa que nos dê:
• salário bruto.
• quanto pagou ao INSS.
• quanto pagou ao sindicato.
• o salário líquido.'''
# Descobrir horas e quanto ganha por horas 
ganha = float(input('Digite quanto voce ganha por hora: '))
horas = float(input('Digite quantas horas voce trabalha por por mes: '))
salario_bruto = ganha * horas # multiplicar horas pelo valor das horas 

      # calculo para descobrir os descontos
imposto_de_renda = salario_bruto * 0.11  
inss = salario_bruto * 0.08 
sindicato = salario_bruto * 0.05
desconto_total = salario_bruto * 0.24
salario_liquido = salario_bruto - desconto_total#

print(f'''
Seu salario brtuo: {round(salario_bruto)}
Desconto do imposto de renda: {round(imposto_de_renda)}
Desconto do inss: {round(inss)}
Desconto do sindicato: {round(sindicato)}
Seu salario liquido: {round(salario_liquido)} ''')


