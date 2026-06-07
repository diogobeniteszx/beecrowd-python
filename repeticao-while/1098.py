i = 0.0
while i <= 2.0:
    c = 1
    while c <= 3:
        j = i + c
        print(f'I={i} J={j}')
        c += 1
    i = round(i + 0.2, 1)
