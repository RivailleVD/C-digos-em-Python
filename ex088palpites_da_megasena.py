from random import sample
lista = list(range(1,61))
jogos = int(input('Quantos jogos você quer jogar: '))
for j in range(1, jogos + 1):
    bilhete = sample(lista,6)
    print(f'Jogo {j}: {sorted(bilhete)}')



''''from random import randint
lista = list()
jogo = int(input("Qauntos jogos Você quer sortear? "))
for jogo in range(0 , 6):
     lista = lista.append(randint(1 , 60))
print(lista)'''   #Não funciona!!!!