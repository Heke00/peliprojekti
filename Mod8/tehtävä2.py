nimet = []


while True:
    x = input('Anna nimi: \t')
    if x != '':
        nimet.append(x)
    else:
        break
    
    if len(nimet) == 1:
        print(f'Uusi nimi: \n{nimet}')
    elif len(nimet) >= 2:
        print('Edelliset nimet:')
        for i in nimet:
            print(f'i')

print('Kaikki nimet:')
for i in nimet:
    print(i)
    
