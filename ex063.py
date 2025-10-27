print('-'*20)
print('SEQUÊNCIA DE FIBONACCI')
print('-'*20)
termo = int(input('Digite quantos termos vocÊ deseja: '))
t1 = 0
t2 = 1
print('~'*20)
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= termo:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end="")
    t1 = t2
    t2 = t3
    cont += 1
print('\nFIM')