pares = 0

for _ in range(5):
    n = float(input())
    if n % 2 == 0:
        pares += 1

print(f'{pares} valores pares')
