a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if b > c:
    b, c = c, b

if b + c <= a:
    print('NAO FORMA TRIANGULO')
else:
    if b ** 2 + c ** 2 == a ** 2:
        print('TRIANGULO RETANGULO')
    if b ** 2 + c ** 2 < a ** 2:
        print('TRIANGULO OBTUSANGULO')
    if b ** 2 + c ** 2 > a ** 2:
        print('TRIANGULO ACUTANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or a == c or b == c:
        print('TRIANGULO ISOSCELES')
