n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nora: '))
media = (n1 + n2) / 2
print('O aluno que tem {} e {} nas notas tem média de {}'.format(n1, n2, media))
if media < 6.0:
    print('O aluno está de \033[0;31mRECUPERAÇÃO\033[m')
else:
    print('O aluno está \033[0;32mAPROVADO!\033[m')
