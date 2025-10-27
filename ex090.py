aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 6:
    aluno['situação'] = 'APROVADO'
elif 5 <= aluno['media'] < 6:
    aluno['situação'] = 'RECUPERAÇÃO'
else:
    aluno['situação'] = 'REPROVADO'
print('-='*30)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')