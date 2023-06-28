from time import sleep
def fatorial(n, show=False):
    f = 1
    for c in range(n,0,-1):
        sleep(0.5)
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='' )
            else:
                print(' = ', end='')
        f *= c
    return  f


#programa principal
num= int(input('Digite o valor: '))
print(fatorial(num,show=True))
