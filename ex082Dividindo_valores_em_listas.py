num = list()
pares = list()
ímpares = list()
while True:
    num.append(int(input("Digite um número: ")))
    r = str(input("Deseja continuar? [S/N] "))
    if r in "nN":
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print("-=" *30)
print(f"Você digitou {len(num)} termos")
print(f"A lista completa é {num}")
print(f"A lista de pares é {pares}")
print(f"A lista de ímpares é {ímpares}")


