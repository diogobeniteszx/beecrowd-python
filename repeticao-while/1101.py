while True:
    m, n = map(int, input().split())

    if m <= 0 or n <= 0:
        break

    if m > n:
        m, n = n, m

    atual = m
    soma = 0

    while atual <= n:
        print(atual, end=' ')
        soma += atual
        atual += 1

    print(f'Sum={soma}')
