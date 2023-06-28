n = int(input("Digite um número para calcular seu Fatorial "))
c = n
f = 1
print("Calculando o Fatorial de {}!".format(n))
while c > 0:
    print("{}".format(c), end="")
    print(" X " if c > 1 else ' = ', end="")
    f *= c
    c -= 1
print("{}".format(f))