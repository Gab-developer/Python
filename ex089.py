lista = []
cont = 0
while True:
    lista.append([])
    lista[cont].append(str(input('Nome: ')))
    lista[cont].append(float(input('Nota 1: ')))
    lista[cont].append(float(input('Nota 2: ')))
    media = (lista[cont][1] + lista[cont][2]) / 2
    lista[cont].append(media)
    parar = str(input('Deseja continuar? [S/N] '))
    if parar in 'Nn':
        break
    cont += 1
print('-='*30)
print('Nº Nome          Média')
print('-'*25)
for pos, alun in enumerate(lista):
    print(pos, f'{alun[0]:<15}', alun[3])
while True:
    print('-'*25)
    aluno = int(input('Deseja ver a nota de qual aluno? (999 para parar): '))
    if aluno == 999:
        break
    else:
        print(f'As notas de {lista[aluno][0]} são {lista[aluno][1:3]}')
print('Programa Finalizado\nVolte sempre! :D')