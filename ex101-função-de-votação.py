def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'\33[32;1mCom {idade} anos: Não VOTA!'
    elif 16 <= idade < 18 or idade > 65:
        return f'\33[33;1mCom {idade} anos: VOTO OPCIONAL!'
    else:
        return f'\33[31;1mCom {idade} anos: VOTO OBRIGATÓRIO!'


#programa principal
nasc = int(input('Em que ano você nasceu?  '))
print(voto(nasc))