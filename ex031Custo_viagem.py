from time import sleep
distancia = float(input('Qual a distância da viagem? '))
print('Você irá fazer uma viagem de {} quilômetros'.format(distancia))
print('Calculando o valor...')
sleep(4)
if distancia <= 200:
    valor = distancia *0.50
    print('O valor da sua viagem custará R${:.2f}'.format(valor))
else:
    valor = distancia * 0.40
    print('O valor da viagem custará R${:.2f}'.format(valor))
print('boa viagem!')
print('>==>==>==>'*5)