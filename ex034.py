din = float(input('Digite o salário do funcionário: R$'))
if din > 1250.00:
    salario = din + (din/10)
if din <= 1250.00:
    salario = din + (din*15/100)
print('Com o salário de R${}, com o aumento, fica com R${:.2f}'.format(din, salario))
