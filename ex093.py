perfil = {}
gols = []
perfil['nome'] = str(input('Digite o nome: '))
quantidade = int(input(f'Quantas partidas {perfil["nome"]} jogou?: '))
for c in range(0, quantidade):
    perfil['gols'] = int(input(f'Quantos gols {perfil["nome"]} fez na {c+1}° partida?: '))
    gols.append(perfil['gols'])
    perfil['gols'] = gols
perfil['total'] = sum(perfil['gols'])
print('-='*30)
print(perfil)
print('-='*30)
for k, v in perfil.items():
    print(f'O campo {k} tem valor {v}')
print('-='*30)
print(f'O jogador {perfil["nome"]} jogou {quantidade} partidas')
for i, v in enumerate(perfil['gols']):
    print(f'           =>Na partida {i+1}, fez {v} gols')
print(f'Foi um total de {perfil["total"]} gols')