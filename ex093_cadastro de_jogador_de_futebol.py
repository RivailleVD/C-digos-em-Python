jogador = dict()
partidas = list()
jogador['nome'] = str(input("Nome do Jogador: "))
tot = int(input("Quantas partidas jogou? "))
for p in range (0, tot):
    partidas.append(int(input(f'Quantos gols na partida{p+1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('=-'*30)
print(jogador)
print('=-'*30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor de {v}')
print('=-'*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'   => Na partida {i}, fez {v} gols. ')
print(f'Foi um total de {jogador["total"]} gols. ')
