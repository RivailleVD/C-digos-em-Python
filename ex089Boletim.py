lista = list()
while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Digite a Nota1: "))
    nota2 = float(input("Digite a Nota2: "))
    media = (nota1+nota2)/2
    lista.append([nome, [nota1 , nota2], media])
    resp = str(input("Deseja continuar[S/N]?: "))
    if resp in "Nn":       #Se a resposta for igual a "Nn" pare
        break
print("="*30)

print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')   #exibe os termos devidamente formatados a esquerda ou direita
print('-'*30)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
    #i mostra a enumeração dos termos
    #a[0] vai exibir os nomes em colunas
    #a[2] vai exibir as médias em colunas
while True:
    print("-"*30)
    opc = int(input("Mostrar nota do aluno?[00 interrompe] "))
    if opc == 00:
        print("FINALIZANDO")
        break
    if opc <= len(lista) -1:  #vai selecionar o aluno da lista de acordo com a opção digitada -1
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]}') #vai exibir os termos da lista em suas posições
    print("<<< VOLTE SEMPRE >>>")
