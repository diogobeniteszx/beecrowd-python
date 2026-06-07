t = int(input())
n = []

for c in range(1000):
    resto = c % t
    n.append(resto)

for c in range(1000):
    print(f'N[{c}] = {n[c]}')
