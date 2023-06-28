def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\33[0;31mERRO! Digite um número inteiro válido.\33[m')
        if ok:
            break
    return valor


#programa principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')