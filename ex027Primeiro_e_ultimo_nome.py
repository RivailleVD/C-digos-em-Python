nome = str(input('Digite o seu nome ').strip().lower())

print('Prazer em te conhecer! ')

lista = nome.split()

print('Seu primeiro nome é {}'.format(lista[0]))

print('Seu ultimo nome é {}'.format(lista[len(lista)-1]))
#use len para listar o total de termos no split -1 para desconsiderar o zero