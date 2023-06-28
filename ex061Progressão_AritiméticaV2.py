print("Gerador de PA")
print("-="*20)
n1 = int(input("Primeiro termo: "))
r = int(input("Razão: "))
termo = n1
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print("{} » ".format(termo), end="")
        termo += r
        c += 1
    print("Pausa")
    mais = int(input("Quantos termos você quer mostrar mais? "))
print("Progressão finalizada com {} termos mostrados".format(total))
