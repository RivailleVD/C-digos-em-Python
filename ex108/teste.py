from ex108 import moeda

p = float(input("Digite um valor: "))

print(f"O dobro de {moeda.moeda(p)} é igual a {moeda.moeda(moeda.dobro(p))}")
print(f"A metade de {moeda.moeda(p)} é igual a {moeda.moeda(moeda.metade(p))}")
print(f"{moeda.moeda(p)} menos 10% é igual a {moeda.moeda(moeda.diminuir(p, 10))}")
print(f"{moeda.moeda(p)} mais 10% é igual a {moeda.moeda(moeda.aumentar(p, 10))}")