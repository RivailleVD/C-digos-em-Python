from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6),}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #coloca os itens do dicionario em ordem do maior pro menor
print("-="*30)
print(" == RANKING DOS JOGADORES ==")
for i, v in enumerate(ranking):
    print(f'   {i+1} lugar: {v[0]} com {v[1]}.')   #exibe o ranking dos jogares organizado
    sleep(1)