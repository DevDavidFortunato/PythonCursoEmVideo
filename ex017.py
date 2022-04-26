from math import hypot
ca = float(input('Digite o comprimento do Cateto Adjacente: '))
co = float(input('Digite o comprimento do Cateto Oposto: '))

hi = hypot(ca, co)

print('O valor da HIPOTENUSA é: {0:.2f}'.format(hi))
