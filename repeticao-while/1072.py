n = int(input())
c = dentro = fora = 0

while c < n:
    x = int(input())
    if 10 <= x <= 20:
        dentro += 1
    else:
        fora += 1
    c += 1

print(f'{dentro} in')
print(f'{fora} out')
