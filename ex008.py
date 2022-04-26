x = float(input('Digite uma distância em metros: '))
print('A distância de {:.2f} m corresponde a:'.format(x))
print(' {}km \n {}hm \n {}dam \n {}dm \n {}cm \n {}mm'.format(x/1000, x/100, x/10, x*10, x*100, x*1000))
