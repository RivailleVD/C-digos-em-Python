cont = ("zero" , "um" , "dois" , "três" , "quatro" ,
       "cinco" , "seis" , "sete" , "oito" , "nove" ,
       "dez" , "onze" , "doze" , "treze" , "catorze" ,
       "quinze" , "dezesses" , "dezessete" , "dezoito" ,
       "dezenove" , "vinte")

resp = "Ss"

while resp in "Ss":                             #inicia um loop infinito
       num = int(input("Digite um número entre 0 e 20: "))

       if 0<= num <= 20:                  #se num estiver entre zero e vinte
        print(f"Você digitou o numero {cont[num]}")
        resp = str(input("Continuar? [S/N]: "))
print("Fim do pragrama!")