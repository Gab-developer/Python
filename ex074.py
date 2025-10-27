from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Eu sorteei os valores {n[0:5]}')
print(f'O maior valor foi o {max(n)}')
print(f'O menor valor foi o {min(n)}')