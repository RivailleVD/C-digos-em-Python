print('          \33[33;1mCalcule o seu IMC')
peso = float(input('\33[36;1mDigite seu peso: (KG)  '))
alt = float(input('\33[35;1mDigite sua altura: (m) \33[m'))
imc = peso / (alt ** 2)

print('O seu IMC é {:.2f}'.format(imc))

if imc < 18.5:
    print('\33[33;4;1mVocê está abaixo do peso!')

elif imc >=18.5 and imc <= 25:
    print('\33[32;1mVocê está no seu peso ideal!')

elif imc >=25 and imc <= 30:
    print('\33[31;1;43mVocê está com sobrepeso!\33[m')

elif imc >=30 and imc <=40:
    print('\33[31;4;1mVocê está com obesidade!')

elif imc >= 40:
     print('\33[31;4;1mVocê está com obesidade Mórbida!')
