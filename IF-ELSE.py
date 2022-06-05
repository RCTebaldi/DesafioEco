n = int(input('Informe o seu número aqui: '))
if (n % 2) == 0:
    if n >= 2 and n <= 5 or n > 20:
        print('The number {} is NOT WEIRD'.format(n))
    else:
        print('The number {} is WEIRD'.format(n))
else:
    print('The number {} is WEIRD'.format(n))


