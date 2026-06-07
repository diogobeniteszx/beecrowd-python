grupo = input()
subgrupo = input()
alimentacao = input()

if grupo == 'vertebrado' and subgrupo == 'ave' and alimentacao == 'carnivoro':
    print('aguia')
elif grupo == 'vertebrado' and subgrupo == 'ave' and alimentacao == 'onivoro':
    print('pomba')
elif grupo == 'vertebrado' and subgrupo == 'mamifero' and alimentacao == 'onivoro':
    print('homem')
elif grupo == 'vertebrado' and subgrupo == 'mamifero' and alimentacao == 'herbivoro':
    print('vaca')
elif grupo == 'invertebrado' and subgrupo == 'inseto' and alimentacao == 'hematofago':
    print('pulga')
elif grupo == 'invertebrado' and subgrupo == 'inseto' and alimentacao == 'herbivoro':
    print('lagarta')
elif grupo == 'invertebrado' and subgrupo == 'anelideo' and alimentacao == 'hematofago':
    print('sanguessuga')
else:
    print('minhoca')
