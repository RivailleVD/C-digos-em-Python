num = int(input('Digite um número '))
total = 0  #acumulador
for c in range(1 , num + 1):
    if num % c == 0:
        total = total + 1
        print('\33[33m' , end='')

    else:
         print('\33[31m' , end='')
    print('{} '.format(c) , end='')

print('\n\33[mO número {} foi divisível {} vezes'.format(num , total))
if total ==2:
    print('por isso {} é um número primo!'.format(num ))
else:
    print('E por isso ele não é primo!')