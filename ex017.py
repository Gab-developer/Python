co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('Com o cateto oposto medindo {} e o cateto adjacente medindo {}, pode-se afirmar que a hipotenusa mede {:.2f}'. format(co, ca, hi))
