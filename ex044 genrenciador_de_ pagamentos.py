print('\33[32;1m{:=^40}'.format ('\33[32;1mLojas Elfie'))

preço = float(input('Qual o preço das compras? R$'))

print ('''FORMAS DE PAGAMENTO
[ 1 ] á vista dinheiro / cheque
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opção = int(input('Qual é a opção? '))

if opção == 1:
    total = preço - (preço * 10 /100)

elif opção == 2:
    total = preço - (preço * 5 / 100)

elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} Sem Juros!'.format(parcela))

elif opção == 4:
     total = preço + (preço * 20 / 100)
     totalparc = int(input('Quantas parcelas? '))
     parcela = total / totalparc
     print('Sua compra será divida em {}x de R${:.2f} com juros!'.format(totalparc , parcela))

else:
    total = preço
    print('\33[31mOpção Inválida, Tente novamente!')

print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço , total))