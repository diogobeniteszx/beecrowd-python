c = int(input())
t = input()

matriz = []

for _ in range(12):
    linha_temp = []
    for _ in range(12):
        linha_temp.append(float(input()))
    matriz.append(linha_temp)

soma = 0
for linha_temp in range(12):
    soma += matriz[linha_temp][c]

media = soma / 12

if t == 'S':
    print(f'{soma:.1f}')
elif t == 'M':
    print(f'{media:.1f}')
