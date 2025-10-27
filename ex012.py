produto = float(input('Qual é o preço do produto? R$'))
desconto = produto - (produto * 5 / 100)
print('O produto com 5% de desconto, sai do valor de {:.2f}R$ para {:.2f}R$.'.format(produto, desconto))
