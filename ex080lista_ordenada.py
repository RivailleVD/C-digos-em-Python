lista = []
for c in range (0, 5):
    n = int(input("Digite um valor: "))
    if c == 0 or n > lista[-1]:  #se for o primeiro ou se for maior do que o último
        lista.append(n)
        print("Adicionado ao final da lista...")
    else:
        pos = 0
        while pos < len(lista): #enquanto a posição n for menor do que a posição da lista
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f"Adicionado na posição {pos} da lista...")
                break
            pos += 1
print("-="*30)
print(f"os valores digitados em ordem foram {lista}")