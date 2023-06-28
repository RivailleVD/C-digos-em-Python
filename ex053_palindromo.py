frase =str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

# inverso = junto[::-1]  //  esta única linha tem a mesma função de fatiamento do "for"

for letra in range(len(junto) -1, -1 , -1):
    inverso += junto[letra]
if inverso == junto:
    print(junto , inverso)
    print('temos um palindromo')
else:
    print('{} não é um palindromo'.format(frase))