print('-'*35)
print('          LOJAS BARATÃO                     ')
print('-'*35)
cont = soma = 0
while True:
    cont += 1
    nome = input('Nome do produto: ')
    preco = float(input('Preço do produto? R$'))
    escolha = input('Deseja continuar? [S/N]: '.upper())
    soma += preco
    if escolha == 'N':
        print(f'Você comprou {cont} produtos')
        print(f'O valor total foi de R${soma:.2f}')
        break
