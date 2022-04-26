x = float(input('Qual o preço do produto? R$'))
y = float(input('Quantos porcento (%) de desconto gostaria de aplicar?'))
z = x*(1-(y/100))
print('O produto que custava R${:.2f}, na promoção com desconto de {:.0f}% vai custar R${:.2f}'.format(x, y, z))
