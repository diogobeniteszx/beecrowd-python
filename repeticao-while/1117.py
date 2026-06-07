notas_validas = 0
soma_notas = 0.0

while notas_validas < 2:
    nota = float(input())

    if 0 <= nota <= 10:
        soma_notas += nota
        notas_validas += 1
    else:
        print('nota invalida')

media = soma_notas / 2
print(f'media = {media:.2f}')
