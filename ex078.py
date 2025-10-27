valores = []
posicao_maior = []
posicao_menor = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um número para a posição {c}: ')))
for posicao, valor in enumerate(valores):
    if valor == max(valores):
        posicao_maior.append(posicao)
    if valor == min(valores):
        posicao_menor.append(posicao)
print(valores)
print(f'O maior valor foi {max(valores)} na posição {posicao_maior}')
print(f'O menor valor foi {min(valores)} na posição {posicao_menor}')
