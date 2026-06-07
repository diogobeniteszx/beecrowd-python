x = float(input())
n = [0] * 100
n[0] = x

for c in range(1, 100):
    n[c] = n[c - 1] / 2

for c in range(100):
    print(f'N[{c}] = {n[c]:.4f}')
