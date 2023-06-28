from time import sleep


def contador(i,f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-'*20)
    print(f'contagem de {i} até {f} de {p}.')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print("FIM!")
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ',  end='', flush=True)
            cont -= p
        print("FIM!")



#programa principal
contador(1 , 10 , 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)


