maior = posicao = 0

c = 1
while c <= 100:
    valor = int(input())

    if valor > maior:
        maior = valor
        posicao = c
    c += 1

print(maior)
print(posicao)
