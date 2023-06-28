from datetime import date
ano = int(input('Ano de nascimento: '))
hoje = date.today().year
idade = hoje - ano
print('Quem nascem em {} tem {} anos em {}.'.format(ano , idade , hoje))
if idade == 18:
    print('Você deve se alistar imediatamente!')
elif idade < 18:
    saldo = idade - 18
    print('faltam {} anos para o seu alistamento!'.format(saldo))
elif idade > 18:
    saldo = idade - 18
    print('Você deveria ter se alistado a {} anos'.format(saldo))
