from random import randint
from time import sleep
computador = randint(0 , 5)
print('Vou pensar em número entre 0 e 5, tente adivinhar!')
print('(<OwO>)')
jogador = int(input('Que número eu pensei? '))
print ('vamos ver... vamos ver...')
sleep(3)
if jogador == computador:
    print('Err... PARABÉNS! Você conseguiu me vencer!')
    print('(*O_O)')
else:
    print('Wahahaha Eu venci! pensei no número {}'.format(computador))
    print('(*w*)')
