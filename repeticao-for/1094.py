n = int(input())
coelhos = ratos = sapos = total = 0

for _ in range(n):
    quantia, tipo = input().split()
    quantia = int(quantia)

    if tipo == 'C':
        coelhos += quantia
    if tipo == 'R':
        ratos += quantia
    if tipo == 'S':
        sapos += quantia

    total += quantia

percentual_coelhos = (coelhos / total) * 100
percentual_ratos = (ratos / total) * 100
percentual_sapos = (sapos / total) * 100

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {coelhos}')
print(f'Total de ratos: {ratos}')
print(f'Total de sapos: {sapos}')
print(f'Percentual de coelhos: {percentual_coelhos:.2f} %')
print(f'Percentual de ratos: {percentual_ratos:.2f} %')
print(f'Percentual de sapos: {percentual_sapos:.2f} %')
