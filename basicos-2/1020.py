total_dias = int(input())

anos = total_dias // 365
resto_dias = total_dias % 365

meses = resto_dias // 30
dias = resto_dias % 30

print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')
