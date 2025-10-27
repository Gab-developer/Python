s = float(input('Qual o salário do funcionjário? R$'))
porcen = s + (s * 15 / 100)
print('Um funcionário que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}'.format(s, porcen))
