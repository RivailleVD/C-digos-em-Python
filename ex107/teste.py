from ex107 import moeda

p = float(input("Digite um valor: "))

print(f"O dobro de R${p} é igual a {moeda.dobro(p)}")
print(f"A metade de R${p} é igual a {moeda.metade(p)}")
print(f"R${p} menos 10% é igual a {moeda.diminuir(p, 10)}")
print(f"R${p} mais 10% é igual a {moeda.aumentar(p, 10)}")