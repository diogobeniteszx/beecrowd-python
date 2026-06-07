n = int(input())

for _ in range(n):
    x = int(input())

    if x == 0:
        print('NULL')
    else:
        if x % 2 == 0:
            paridade = 'EVEN'
        else:
            paridade = 'ODD'

        if x > 0:
            sinal = 'POSITIVE'
        else:
            sinal = 'NEGATIVE'

        print(f'{paridade} {sinal}')
