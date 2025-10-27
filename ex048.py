soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
print('A soma de todos os valores solicitados é {}'.format(soma))
