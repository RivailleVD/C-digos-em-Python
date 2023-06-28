a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
#Verificando o menor valor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#Verificando o maior valor
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
#resposta
print('O maior valor será {}'.format(maior))
print('O menor valor será {}'.format(menor))

