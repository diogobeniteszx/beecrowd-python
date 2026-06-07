n = float(input())

centavos = int(n * 100 + 0.5)

notas_100 = centavos // 10000
resto = centavos % 10000

notas_50 = resto // 5000
resto %= 5000

notas_20 = resto // 2000
resto %= 2000

notas_10 = resto // 1000
resto %= 1000

notas_5 = resto // 500
resto %= 500

notas_2 = resto // 200
resto %= 200

moedas_1 = resto // 100
resto %= 100

moedas_050 = resto // 50
resto %= 50

moedas_025 = resto // 25
resto %= 25

moedas_010 = resto // 10
resto %= 10

moedas_005 = resto // 5
resto %= 5

moedas_001 = resto

print('NOTAS:')
print(f'{notas_100} nota(s) de R$ 100.00')
print(f'{notas_50} nota(s) de R$ 50.00')
print(f'{notas_20} nota(s) de R$ 20.00')
print(f'{notas_10} nota(s) de R$ 10.00')
print(f'{notas_5} nota(s) de R$ 5.00')
print(f'{notas_2} nota(s) de R$ 2.00')

print('MOEDAS:')
print(f'{moedas_1} moeda(s) de R$ 1.00')
print(f'{moedas_050} moeda(s) de R$ 0.50')
print(f'{moedas_025} moeda(s) de R$ 0.25')
print(f'{moedas_010} moeda(s) de R$ 0.10')
print(f'{moedas_005} moeda(s) de R$ 0.05')
print(f'{moedas_001} moeda(s) de R$ 0.01')
