vel = float(input('Qual a velocidade do carro? '))
print(KM/h)
if vel > 80:
    print('MULTADO! Você excedeu o limite de velovidade de 80km/h')
    multa = (vel-80)*7
    print('Você pagará uma multa de {}'.format(multa))

print('Tenha um bom dia, dirija com cuidado!')

#else: print('Parou, Parou! Multado por excesso de velocidade em R${}'.format((vel-80)*7))  ¨¨¨estrutura composta¨¨¨