n = float(input('Digite um Número '))
d = n * 2
t = n * 3
r = pow(n, (1/2))
print('o dobro de \33[32;1m{}\33[m vale \33[33;1m{}\33[m'.format(n , d,))
print('o triplo de \33[32;1m{}\33[m vale \33[33;1m{}\33[m'.format(n, t))
print('a raiz quadrada de \33[32;1m{}\33[m é igual \33[33;1m{:.2f}\33[m'.format(n, r))
