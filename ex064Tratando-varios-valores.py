n = int(input("Digite um número (999 para encerrar): "))
s = n
c = 0
while n != 999:
    s += n
    c = c + 1
    n = int(input("Digite um número (999 para encerrar): "))
print("A soma é igual a {}".format(s-999))
print("você digitou {} termos ".format(c))