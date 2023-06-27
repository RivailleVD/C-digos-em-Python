b1 = float(input('Nota '))
b2 = float(input('Nota '))
m = float(b1 + b2)/2


cores ={'amarelo':'\33[33;1m',
        'verde' : '\33[32;1m',
        'vermelho': '\33[31;1m'}


if m >= 6:
    print('A média é {}{}{}'.format(cores['amarelo'], m , '\33[m'))
    print('Parabéns, você {}passou!'.format(cores['verde']))

else:
    print('A média é {}{}{}'.format(cores['amarelo'], m , '\33[m'))
    print('Você foi {}Reprovado!'.format(cores['vermelho']))