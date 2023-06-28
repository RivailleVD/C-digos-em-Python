dias = int(input('quantos dias o carro ficou alugado? '))
km = int(input('Quantos quilometros o carro percorreu? '))
diaria = 60 * dias
pkm = 0.15 * km
print('\33[1mO total a pagar pelo aluguel do carro é igual a \33[40;7;32mR${:.2f}\33[m'.format(diaria + pkm))
