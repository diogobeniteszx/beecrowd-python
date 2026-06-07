n = int(input())

if n % 2 == 0:
    inicio = n + 1
else:
    inicio = n

c = 0
while c < 6:
    print(inicio + 2 * c)
    c += 1
