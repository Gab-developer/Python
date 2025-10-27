print('========== LOJAS GABRIEL ==========')
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/ cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual a opção? '))
din = preco - (preco * 10 / 100)
cartao = preco - (preco * 5 / 100)
xx = preco
if opcao == 1:
    print('À vista do valor de R${} fica R${:.2f} no final'.format(preco, din))
elif opcao == 2:
    print('Á vista no cartão, o valor de R${} sai por R${:.2f}'.format(preco, cartao))
elif opcao == 3:
    parcela = preco / 2
    print('O valor é parcelado em 2x com R${:.2f} cada parcela (SEM JUROS)'.format(parcela))
elif opcao == 4:
    totalpar = int(input('Quantas parcelas? '))
    juros = preco + (preco * 20 / 100)
    tudo = juros / totalpar
    print('Pagando {}x no cartão, cada parcela sai por R${:.2f} (COM JUROS)'.format(totalpar, tudo))
else:
    print('Essa opção não é válida!')
