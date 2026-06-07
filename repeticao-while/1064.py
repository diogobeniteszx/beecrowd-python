c = positivos = soma = 0

while c < 6:
    n = float(input())
    
    if n > 0:
        positivos += 1
        soma += n
    c += 1

media = soma / positivos
print(f'{positivos} valores positivos')
print(f'{media:.1f}')
