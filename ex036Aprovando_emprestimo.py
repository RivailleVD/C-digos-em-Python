valor = float(input('Qual o valor da casa? '))
sal = float(input('Digite sua renda mensal: '))
temp = int(input('quantos anos de financiamento? '))
parcela = valor / (12 * temp)
if parcela > (sal*30/100):
    print('Infelizmente o valor de \33[33;1m{:.2f}\33[m da parcela é muito alto para o seu rendimento de \33[4m{:.2f}\33[m!'.format(parcela , sal))
    print('portanto seu crédito foi \33[1;31mnegado!')
else:
    print('A percela de \33[33;1m{:.2f}\33[m não execede os 30% do seu rendimento!'.format(parcela))
    print('seu cédito foi \33[32;1maprovado\33[m!')

#print('{:.2f}'.format(parcela))