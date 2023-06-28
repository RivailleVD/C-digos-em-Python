def ficha(jog = '<desconhecido>' , gol = 0):
    print(f'o jogador {jog} fez {gol} gol(s) no campeonato. ')


#programa principal
j = str(input('Nome do jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if j.strip() == '':
    ficha(gol=g)
else:
    ficha(j, g)