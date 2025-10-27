n1 = int(input('Digite um número: '))
es = str(input('Deseja continuar? [S/N]: ').upper())
cont = 1
soma = 1
maior = 0
menor = 0
while es == 'S':
    n1 = int(input('Digite um número: '))
    es = str(input('Deseja continuar? [S/N]: ').upper())
    soma += n1
    cont += 1
    media = soma / cont
print('Você digitou {} números e a média entre eles é {:.1f}'.format(cont, media))
