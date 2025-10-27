cont = 0
cont5 = 0
lista = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    resp = input('Deseja continuar? [S/N]: ')
    cont += 1
    if resp == 'n':
        break
if 5 in lista:
    print(f'O valor 5 foi encontrado na lista!')
else:
    print(f'O valor 5 não foi encontrado na lista!')
lista.sort(reverse=True)
print(f'Você digitou {cont} elementos!')
print(f'A ordem decrescente dos números que você digitou é: {lista}')