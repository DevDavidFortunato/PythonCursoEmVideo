x = float(input('Qual é o salário do Funcionário? R$'))
y = float(input('Quantos porcento (%) de aumento a aplicar?'))
z = x * (1 + (y / 100))
print('O funcionário que ganhava R${:.2f}, com {:.0f}% de aumento passará a ganhar R${:.2f}'.format(x, y, z))

