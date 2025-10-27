def ficha(nome='<desconhecido>', gols=0):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato!'


nome = str(input('Digite o nome: '))
gols = input('Quantos gols fez?: ')
if gols == '' and nome:
    msg = ficha(nome)
elif nome == '' and gols:
    msg = ficha(gols=gols)
else:
    msg = ficha()
print(msg)