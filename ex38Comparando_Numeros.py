a = float(input('Primeiro número: '))
b = float(input('Segundo número: '))
if a > b:
    print('O primeiro valor (\33[32;1m{}\33[m) é maior do que o segundo valor(\33[34;1m{}\33[m)'.format(a , b))
elif b > a:
    print('O segundo valor(\33[34;1m{}\33[m) é maior do que o primeiro valor(\33[32;1m{}\33[m)'.format(b, a))
else:
    print('Os dois valores são iguais!')