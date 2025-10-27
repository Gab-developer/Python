valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salário do comprador? R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = valor / (anos * 12)
print('O valor da prestação vai ser R${:.2f}'.format(prestacao))
maximo = (salario * 30) / 100
if prestacao > maximo:
    print('\033[0;31mO empréstimo NÃO foi aprovado!!!\033[m')
else:
    print('\033[0;32mO empréstimo foi aprovado!!!\033[m')
