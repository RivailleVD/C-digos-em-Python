list = []
mai = 0
men = 0
for c in range (0,5):
    list.append(int(input(f"Digite um valor para a posição {c}: ")))
    if c == 0:
        mai = men = list[c]
    else:
        if list[c] > mai:
            mai = list[c]
        if list[c] < men:
            men = list[c]
print('=-'*30)
print(f'Você digitou os valores {list}')
print(f'o maior valor digitado foi {mai} nas posições ' , end='')
for i  , v in enumerate (list):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'o menor valor digitado foi {men} nas posições ', end='')
for i , v in enumerate (list):
    if  v == men:
        print(f'{i}...', end="")
print()
