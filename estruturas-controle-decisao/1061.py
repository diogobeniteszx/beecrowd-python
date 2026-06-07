linha_inicio = input().split()
dia_inicio = int(linha_inicio[1])

hora_inicio, minuto_inicio, segundo_inicio = input().split(' : ')
hora_inicio = int(hora_inicio)
minuto_inicio = int(minuto_inicio)
segundo_inicio = int(segundo_inicio)

linha_termino = input().split()
dia_termino = int(linha_termino[1])

hora_termino, minuto_termino, segundo_termino = input().split(' : ')
hora_termino = int(hora_termino)
minuto_termino = int(minuto_termino)
segundo_termino = int(segundo_termino)

total_inicio = (
    dia_inicio * 24 * 60 * 60 +
    hora_inicio * 60 * 60 +
    minuto_inicio * 60 +
    segundo_inicio
)

total_termino = (
    dia_termino * 24 * 60 * 60 +
    hora_termino * 60 * 60 +
    minuto_termino * 60 +
    segundo_termino
)

diferenca = total_termino - total_inicio

dias = diferenca // (24 * 60 * 60)
resto = diferenca % (24 * 60 * 60)

horas = resto // (60 * 60)
resto %= (60 * 60)

minutos = resto // 60
segundos = resto % 60

print(f'{dias} dia(s)')
print(f'{horas} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{segundos} segundo(s)')
