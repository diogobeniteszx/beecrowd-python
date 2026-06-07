hora_inicial, hora_final = input().split()
hora_inicial = int(hora_inicial)
hora_final = int(hora_final)

if hora_final > hora_inicial:
    duracao = hora_final - hora_inicial
else:
    duracao = (24 - hora_inicial) + hora_final

print(f'O JOGO DUROU {duracao} HORA(S)')
