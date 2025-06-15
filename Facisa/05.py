# 5 Realiza a leitura de 1 float referente ao valor de um produto e imprime o valor com descontos de 10%, 20% e 50%

valor = float(input('Digite um valor : '))
desconto1 = valor * 0.10 #(10%)
desconto2 = valor * 0.20 # (20%)
desconto3 = valor * 0.50 # (50%)

print(f'Descontos 10% = {valor - desconto1 } 20% = {valor - desconto2} e 50% = {valor - desconto3 }')
# eu coloco ( - desconto1) para mostrar o valor digitado menos o descontado dado corretamente ex 100 - 10% mostra (90)