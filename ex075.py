num = (int(input('Digite um número: ')),
       int(input('Digite mais um: ')),
       int(input('Digite outro: ')),
       int(input('Digite o último: ')))
print(f'Você digitou o numero 9, {num.count(9)} vez(es).')
if 3 in num:
    print(f'O valor 3 foi digitado na {num.index(3)+1}° posição.')
else:
    print('O valor 3 não foi digitado')
print(f'Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')