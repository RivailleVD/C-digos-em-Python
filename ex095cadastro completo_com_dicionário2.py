time = list()
jogador = dict()
partidas = list()

# Analisa os dados dos jogaores

while True:
    jogador.clear()
    jogador['nome'] = str(input("Nome do Jogador: "))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for p in range (0, tot):
        partidas.append(int(input(f'Quantos gols na partida {p+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

# função para continuar ou interromper a aplicação

    while True:
        resp = str(input('Quer continuar[S/N]? ')).upper()[0] #vai jogar a primeira letra para maiúscula
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)

#exibe os cabeçalhos organizados dos dicionários

print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' *40)

#função exibe os dados dos dicionarios organizados formatados dentro dos dicinários

for k, v in enumerate(time):
    print(f'{k+1:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15} ', end='')
    print()
print('-'*40)

#função para buscar dentro do dicionário

while True:
    busca = int(input('Mostrar dados de qual jogador?(999 fecha) '))-1
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não exite jogador com cógico {busca}!')

#exibe o total de gols do jogador escolhido

    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
        print('-'*40)
print('<<< VOLTE SEMPRE! >>>')

