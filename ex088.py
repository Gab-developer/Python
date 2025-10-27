import random
for x in range(int(input('Quantos jogos você deseja?: '))):
    print(f'JOGO {x+1}: {random.sample(range(1, 61), 6)}')