from ex115.lib import cabeçalho, menu, leiaint
from time import sleep
from ex115.lib.arquivo import arquivoexiste, criararquivo, lerarquivo,cadastrar

arq = 'Cadastro Pessoas.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerarquivo(arq)
    elif resposta == 2:
        #Opção de cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        #saindo do sistema
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        #digitou uma opção errada no menu.
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
