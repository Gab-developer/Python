print('Gerador de PA')
print('=-'*10)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{}'.format(termo),end='')
    print(' -> ' if cont < 10 else '', end='')
    termo = termo + razao
    cont += 1
print(' FIM')