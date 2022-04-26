velocidade = float(input('Qual é a velocidade atual do carro?'))
limite = float(input('Qual é o limite da via?'))

if velocidade <= limite:
    print('Tenha um ótimo dia! Dirija com cuidado')
else:
    print('MULTADO! Você excedeu o limite permitido que é de Km {:.0f}/h'.format(limite))
    print('Você deve pagar uma multa de: R${:.2f}'.format((velocidade - limite) * 7))
