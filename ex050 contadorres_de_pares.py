cont = 0  #contador de váriavéis
soma = 0  # acumula ou grava os valores já digitados
for c in range(1, 7):
    num = int(input('Digite o {} valor! '.format(c)))
    if num % 2 == 0:
        cont = cont +1  #pode ser escrito com "cont += num"
        soma = soma + num    #pode ser escrito com "soma += 1"
print('você digitou {} números Pares e a soma entre eles foi {}'.format(cont , soma))