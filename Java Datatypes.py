t = int(input('Informe a quantidade de testes que será feito análise: '))
n = int(input('Informe o número a ser analisado: '))
i=0
for i in range(1,t):
    if n >= -128 and n <=127:
        print('O valor {} pode ser armazenado tanto como BYTE, SHORT, INT e LONG'.format(n))