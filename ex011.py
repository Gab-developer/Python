l = float(input('Qual a largura da sua parede?: '))
a = float(input('Qual a altura da sua parede?: '))
area = l * a
tinta = area / 2
print('Sua parede tem a dimensão de {}X{} e sua área é de {}m'.format(l, a, area))
print('Para pinta-la, será necessário {} litros de tinta.'.format(tinta))
