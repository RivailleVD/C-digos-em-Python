from ex109 import moeda

p = float(input("Digite um valor: "))

print(f'O dobro de {moeda.moeda(p)} é igual a {moeda.dobro(p, True)}')
print(f'A metade de {moeda.moeda(p)} é igual a {moeda.metade(p, True)}')
print(f'{moeda.moeda(p)} menos 10% é igual a {moeda.diminuir(p, 10, True)}')
print(f'{moeda.moeda(p)} mais 10% é igual a {moeda.aumentar(p, 10, True)}')