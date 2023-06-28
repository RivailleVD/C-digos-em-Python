#função de cálculo
def area(larg , comp):
    a = larg * comp
    print(f'\33[36;1mA área de um terreno {larg}X{comp} é de {a}m².')

#programa principal
print('\33[32;1;4mControle de Terrenos')
print('-' * 20)
l = float(input('\33[31;4;1mLARGURA (m): '))
c = float(input('\33[33;4;1mCOMPRIMENTO (m):\33[33;4;1m '))
area(l , c)