lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar!!')
    resposta = input('Você quer continuar? [S/N]: ')
    if resposta == 'n':
        break
lista.sort()
print(f'A lista que você digitou foi: {lista}')