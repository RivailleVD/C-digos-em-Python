#vogal = ('a' , 'e' , 'i' , 'o' , 'u')
palavras = ('aprender' , 'programar' , 'linguagem' , 'python' ,
            'curso' , 'gratis' , 'estudar' , 'praticar' ,
            'trabalhar' , 'mercado' , 'programador' , 'futuro')
for c in palavras:
    print(f'\nNa palavra {c.upper()} temos ' , end= '')
    for letras in c:
        if letras.lower() in 'aeiou':
          print(letras , end=' ')