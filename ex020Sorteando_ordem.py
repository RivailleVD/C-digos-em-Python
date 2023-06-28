import random
n1 = str(input('Primeiro Aluno '))
n2 = str(input('Segundo Aluno '))
n3 = str(input('Terceiro Aluno '))
n4 = str(input('Quarto Aluno '))
ls = [n1 , n2 , n3 , n4]
random.shuffle (ls)
print('A ordem de apresentação dos trabalhos será')
print(ls)

