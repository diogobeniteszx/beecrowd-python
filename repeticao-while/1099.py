n = int(input())

c = 0
while c < n:
    x, y = map(int, input().split())
    
    menor = x
    maior = y
    if x > y:
        menor, maior = maior, menor
    
    soma = 0
    numero = menor + 1
    
    while numero < maior:
        if numero % 2 != 0:
            soma += numero
        numero += 1
    
    print(soma)
    c += 1
