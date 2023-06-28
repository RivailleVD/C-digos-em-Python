matriz = [[0,0,0] , [0,0,0] , [0,0,0]]
par = sumcol = mai = 0              #contadores
for c in range (0,3):
    for l in range (0,3):
        matriz[c][l] = int(input(f"Digite um valor para [{c} , {l}]: ")) # varivel dos valores colunas e linhas


for c in range (0,3):               #repetição para gerar a estrutura da matriz
    for l in range (0,3):
     print(f'[{matriz[c][l]:^5}] ', end='')
     if matriz[c][l] % 2 == 0:      #condição de soma dos valores pares
         par += matriz[c][l]
    print()

for l in range (0,3):               #função para somar os valores da terceira coluna
    sumcol += matriz[l][2]

for c in range (0,3):               #função para escolher o maior numero da segunda linha
    if c ==0:
        mai = matriz[1][c]
    elif matriz[1] [c] > mai:
        mai = matriz[1][c]



print("=~"* 30)
print(f"A soma dos pares é {par}")
print("=~"*30)
print(f"A soma da terceira coluna é {sumcol}")
print("=~"*30)
print(f"O maior numero da segunda linha é {mai}")