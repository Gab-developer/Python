lista0 = []
lista_impar = []
lista_par = []
while True:
    num = int(input('Digite um valor: '))
    lista0.append(num)
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
    resp = input('Deseja continuar? [S/N]: ')
    if resp == 'n':
        break
lista0.sort()
print('-='*30)
print(f'A lista completa em ordem crescente é {lista0}')
print(f'A lista de números pares é: {lista_par}')
print(f'A lista de números ímpares é: {lista_impar}')