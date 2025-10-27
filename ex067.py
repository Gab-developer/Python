print('TABUADA 3.0')
while True:
    n1 = int(input('Qual tabuada você deseja ver?: '))
    if n1 < 0:
        print('O programa acabou!')
        break
    for c in range(1, 11):
        print(f'{n1} X {c} = {n1 * c}')
        