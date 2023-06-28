def leiadinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',' , '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\33[0;31mERRO: \"{entrada}\" é um preço invalido!\33[m')
        else:
            válido = True
            return float(entrada)