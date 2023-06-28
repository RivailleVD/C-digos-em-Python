list = ('Lápis' , 1.75,
            'Borracha' , 2,
            'Caderno' , 15.90,
            'Estojo' , 4.20,
            'Transferidor' , 4.20,
            'Compasso' , 9.99,
            'Mochila' , 120.30 ,
            'Canetas' , 22.30,
            'Livro' , 34.90)
print("-"*40)
print("Listagem de Preços")
print("-"*40)
for c in range (0 , len(list)):
    if c % 2 == 0:
        print(f'{list[c]:.<30}' , end='')
    else:
        print(f'{list[c]:>7.2f}')
