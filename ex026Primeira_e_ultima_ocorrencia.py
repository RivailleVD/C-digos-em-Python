nome = str(input('Digite seu nome ')).strip().lower()
print('A letra ¨A¨ aparece {} vezes'.format(nome.count('a')))
print('A letra ¨A¨ aparece pela primeira vez na posição {}'.format(nome.find('a')+1))
print('A ultima letra ¨A¨ apareceu na posição {}'.format(nome.rfind('a')+1))
