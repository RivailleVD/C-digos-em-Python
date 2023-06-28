sal = float(input('Digite seu salário: R$'))
if sal <= 1250:
    aumento = (sal + (sal *15 / 100))
else:
    aumento = (sal + (sal *10 / 100))
print('O novo salário será R${:.2f}'.format(aumento))
