perfil = {}
gols = []
time = []

while True:
    perfil.clear()
    perfil['nome'] = str(input('Digite o nome: '))
    quantidade = int(input(f'Quantas partidas {perfil["nome"]} jogou?: '))
    gols.clear()
    for c in range(0, quantidade):
        perfil['gols'] = int(input(f'Quantos gols {perfil["nome"]} fez na {c+1}° partida?: '))
        gols.append(perfil['gols'])
        perfil['gols'] = gols
    perfil['total'] = sum(perfil['gols'])
    resp = str(input('Deseja continuar? [S/N]: '))
    time.append(perfil.copy())
    if resp in 'nN':
        break
print('-='*30)
print('cod ', end='')
for i in perfil.keys():
    print(f'{i:<15}', end='')
print()
print('_'*40)
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('_'*40)
