numbers = {"Viivi" : "111", "Ahmed" : "222", "Pekka" : "333", "Gerorge": "444"}


numbers['Viivi'] = '938039129123923192301'

nimi = input('Anna kaverin nimi: \t')
if nimi in numbers:
    print(f'{nimi}n numero on {numbers[nimi]}')
else:
    print(f'{nimi} ei löytynyt')


# for i in numbers:
#     print(f'{i}n Numero on: {numbers[i]}')

