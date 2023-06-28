num = list()
while True:
    i = int(input("Adicione um Número: "))
    if i not in num:
        num.append(i)
        print("Adicionado com sucesso!")
    else:
        print("Número duplicado, não adicionado!")
    r = str(input("Quer continuar? [S/N] "))
    if r in "Nn":
        break
print("-="*40)
print(f"Você digitou os números {sorted(num)}")
