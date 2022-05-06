#Algoritmo estimativa aumento de preço de produto

valor_mes_01 = input(' Insira o valor que o produto estava sendo vendido mês passado:\n R$ ')
valor_mes_02 = input(' Insira o valor que o produto está sendo vendido atualmente:\n R$ ')

maior = valor_mes_02 > valor_mes_01

if(maior == True):
    maior_valor = valor_mes_02
    menor_valor = valor_mes_01
else:
    maior_valor = valor_mes_01
    menor_valor = valor_mes_02

diferenca = (int(maior_valor) - int(menor_valor))
porcentagem = diferenca * 100 / int(menor_valor)
resultado_variacao = (int(valor_mes_02) * porcentagem / 100)
valor_prox_mes = int(valor_mes_02) + int(resultado_variacao)

print(' A variração no preço do produto entre dois meses foi de:', int(porcentagem), '%.','Logo, caso essa variação continue constante, no próximo mês o produto custará:', 'R$', int(valor_prox_mes))
