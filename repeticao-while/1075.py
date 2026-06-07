n = int(input())

c = 0
while c < 10000:
    if c % n == 2:
        print(c)
    c += 1
