sal = float(input('qual o salário do funcionário? R$'))
aum = sal + (sal *15/100)
print('com o aumento salarial de \33[32;1m15%\33[m o funcionário passa a receber \33[32;40;7mR${:.2f}'.format(aum))