valdia = float(input('Digite valor da diária do veículo locado: R$'))
dia = int(input('Digite quantos dias o veículo foi locado: '))
valkm = float(input('Digite valor do Km rodado: R$'))
km = float(input('Digite quantos Km o veículo locado rodou: '))

print('O valor total a pagar é de: R${:.2f}'.format(valdia * dia + valkm * km))
