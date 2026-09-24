# # while True:
# #     try:
# #         int(input('Anna numero: '))
# #         break
# #     except ValueError:
# #         pass
# # print('Jippii!!')

# s1 = {2, 3, 5, 7, 9}
# d1 = {'a' : 4, 'b' : 6, 'c' : 8}

# for i in d1:
#     print(i)
# print(type(s1))
# print(type(d1)
class Song:
    def __init__(self, laulaja, nimi):
        self.laulaja = laulaja
        self.nimi = nimi


import random

s1 = Song('Laulaja', 'Biisi')
s2 = Song('Joku Mies', 'Jeaaa hyvä biisi')
s3 = Song('Mies', 'Sää')
s4 = Song('artisti', 'laulu')
s5 = Song('singer', 'song')
s6 = Song('Artist', 'single')

l1 = [s1, s2, s3, s4, s5, s6]
for song in l1:
    print(song.nimi, song.laulaja)

class PlayList:
    munlista = []
    def lisaa():
        for i in range(0,5):
            x = random.choice(l1)
            print(f'{x.nimi} by {x.laulaja} lisätty soittolistaan!')
            PlayList.munlista.append(x.nimi)
    def lisaatarkka(y):
        PlayList.munlista.append(y.name)


print(PlayList.munlista)
PlayList.lisaa()
print(PlayList.munlista)
PlayList.lisaatarkka(s6)
print(PlayList.munlista)
